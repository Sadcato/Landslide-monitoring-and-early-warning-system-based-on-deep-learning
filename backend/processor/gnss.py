from pynmeagps import NMEAReader
from io import BytesIO
import datetime
from utils.db_utils import execute_query
import logging

class GNSSData:
    def __init__(self):
        self.error = False

 

    from datetime import datetime
   
    def parse_gngga_sentence(self, nmea_sentence):
        if not nmea_sentence.startswith("$GNGGA"):
            return None
        nmea_stream = BytesIO((nmea_sentence + '\r\n').encode('ascii'))
        nmr = NMEAReader(nmea_stream)
      
        try:
            raw_data = next(nmr)
            msg = raw_data[1]
            return {
            "Message Type": msg.msgID,
            "UTC Time": msg.time.strftime('%H:%M:%S') if msg.time else None,
            "Latitude": float(msg.lat) if msg.lat else None,
            "Longitude": float(msg.lon) if msg.lon else None,
            "Fix Quality": int(msg.quality) if msg.quality else None,
            "Number of Satellites": int(msg.numSV) if msg.numSV else None,
            "HDOP": float(msg.HDOP) if msg.HDOP else None,
            "Altitude": float(msg.alt) if msg.alt else None,
            "Height of Geoid": float(msg.sep) if msg.sep else None
        }
                
        except StopIteration:
            return None
        except Exception as e:
            return None
 
    def parse_gnrmc_sentence(self, nmea_sentence):
        if not nmea_sentence.startswith("$GNRMC"):
            return None
        nmea_stream = BytesIO((nmea_sentence + '\r\n').encode('ascii'))
        nmr = NMEAReader(nmea_stream)
        try:
            raw_data = next(nmr)
            msg = raw_data[1]
            speed_over_ground_knots = getattr(msg, 'spd', None)
            """转换节为米每秒,1节 = 0.51444 米每秒"""
            speed_over_ground_mps = float(speed_over_ground_knots) * 0.51444 if speed_over_ground_knots is not None else None
            return {
            "Message Type": msg.msgID,
            "Speed Over Ground": speed_over_ground_mps,
            "Course Over Ground": float(msg.cog) if msg.cog else None,
            "Date": msg.date.strftime('%Y-%m-%d') if msg.date else None
        }
        except StopIteration:
            return None
        except Exception as e:
            return None
 
    async def store_gnss_data(self,data):
        if data:
            hdop = data.get("HDOP")
            '''检查HDOP值,当其大于10时则不继续执行插入数据库的操作'''
            if hdop is not None and hdop > 10:
                logging.info(f'Skipped data with high HDOP value: {hdop}')
                return  
            
            timestamp = datetime.datetime.now()
            '''插入GGA数据'''

            if data.get("Message Type") == "GGA":
                
                query_gga = """
                INSERT INTO gnss_data_GGA (
                    timestamp,
                    message_type, 
                    latitude, 
                    longitude, 
                    fix_quality, 
                    num_of_satellites, 
                    hdop, 
                    altitude, 
                    height_of_geoid
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """

                args_gga = (
                timestamp,
                data.get("Message Type"),
                data.get("Latitude"),
                data.get("Longitude"),
                data.get("Fix Quality"),
                data.get("Number of Satellites"),
                data.get("HDOP"),
                data.get("Altitude"),
                data.get("Height of Geoid")
                )
                await execute_query(query_gga, args_gga)

                """插入RMC数据"""
                
            elif data.get("Message Type") == "RMC":
                query_rmc = """
            INSERT INTO gnss_data_RMC (
                timestamp,
                message_type, 
                speed_over_ground, 
                course_over_ground
            ) VALUES (%s, %s, %s, %s)
            """
                
                args_rmc = (
                timestamp,
                data.get("Message Type"),
                data.get("Speed Over Ground"),
                data.get("Course Over Ground")
                
            )
                await execute_query(query_rmc, args_rmc)
