from pynmeagps import NMEAReader
from io import BytesIO
from datetime import datetime
from utils.db_utils import execute_query


class GNSSData:
    def __init__(self):
        self.error = False

 

    from datetime import datetime

    def parse_gngga_sentence(self, nmea_sentence):
        if not nmea_sentence.startswith("$GNGGA"):
            return None
        nmea_stream = BytesIO((nmea_sentence + '\r\n').encode('ascii'))
        nmr = NMEAReader(nmea_stream)
        print("a")
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
            return {
            "Message Type": msg.msgID,
            "Speed Over Ground": float(msg.spd) if msg.spd else None,
            "Course Over Ground": float(msg.cog) if msg.cog else None,
            "Date": msg.date.strftime('%Y-%m-%d') if msg.date else None
        }
        except StopIteration:
            return None
        except Exception as e:
            return None

    async def store_gnss_data(self,data):
        if data:
        # 插入GGA数据
            if data.get("Message Type") == "GGA":
                query_gga = """
                INSERT INTO gnss_data_GGA (
                    message_type, 
                    utctime, 
                    latitude, 
                    longitude, 
                    fix_quality, 
                    num_of_satellites, 
                    hdop, 
                    altitude, 
                    height_of_geoid
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
                utc_time = data.get("UTC Time")
                if utc_time:
                    try:
                        utc_time = datetime.strptime(utc_time, '%H:%M:%S').strftime('%H:%M:%S')
                    except ValueError:
                        utc_time = None  # 或者设为默认时间
                args_gga = (
                data.get("Message Type"),
                utc_time,
                data.get("Latitude"),
                data.get("Longitude"),
                data.get("Fix Quality"),
                data.get("Number of Satellites"),
                data.get("HDOP"),
                data.get("Altitude"),
                data.get("Height of Geoid")
                )
                await execute_query(query_gga, args_gga)

        # 插入RMC数据
            elif data.get("Message Type") == "RMC":
                query_rmc = """
            INSERT INTO gnss_data_RMC (
                message_type, 
                speed_over_ground, 
                course_over_ground, 
                date
            ) VALUES (%s, %s, %s, %s)
            """
                date = data.get("Date")
                if date:
                    date = datetime.strptime(date, '%Y-%m-%d').strftime('%Y-%m-%d')

                args_rmc = (
                data.get("Message Type"),
                data.get("Speed Over Ground"),
                data.get("Course Over Ground"),
                date
            )
                await execute_query(query_rmc, args_rmc)
        print("b")
