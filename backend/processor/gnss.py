from pynmeagps import NMEAReader
from io import BytesIO
from utils.db_utils import execute_query

class GNSSData:
    def __init__(self):
        self.error = False

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
                "UTC Time": msg.time,
                "Latitude": msg.lat,
                "Longitude": msg.lon,
                "Fix Quality": msg.quality,
                "Number of Satellites": msg.numSV,
                "HDOP": msg.HDOP,
                "Altitude": msg.alt,
                "Height of Geoid": msg.sep
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
                "UTC Time": msg.time,
                "Latitude": msg.lat,
                "Longitude": msg.lon,
                "Speed Over Ground": getattr(msg, 'spd', None),
                "Course Over Ground": getattr(msg, 'cog', None),
                "Date": getattr(msg, 'date', None),
                "Magnetic Variation": getattr(msg, 'magvar', None)
            }
        except StopIteration:
            return None
        except Exception as e:
            return None
        
    async def store_gnss_data(self, data):
        if data:
            query = """
            INSERT INTO gnss_data (
                message_type, 
                utctime, 
                latitude, 
                longitude, 
                fix_quality, 
                num_of_satellites, 
                hdop, 
                altitude, 
                height_of_geoid,
                speed_over_ground, 
                course_over_ground, 
                date, 
                magnetic_variation
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            args = (
                data.get("Message Type"), 
                data.get("UTC Time"), 
                data.get("Latitude"), 
                data.get("Longitude"), 
                data.get("Fix Quality"),  
                data.get("Number of Satellites"), 
                data.get("HDOP"), 
                data.get("Altitude"), 
                data.get("Height of Geoid"),
                data.get("Speed Over Ground"), 
                data.get("Course Over Ground"), 
                data.get("Date"), 
                data.get("Magnetic Variation")
            )
            await execute_query(query, args)
