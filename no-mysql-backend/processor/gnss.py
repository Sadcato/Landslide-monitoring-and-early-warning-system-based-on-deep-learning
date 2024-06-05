from pynmeagps import NMEAReader
from io import BytesIO

class GNSSData:
    def __init__(self):
        self.gngga_data = {}
        self.gnrmc_data = {}
        self.error = False

    def parse_gngga_sentence(self, nmea_sentence):
        if not nmea_sentence.startswith("$GNGGA"):
            return "Not a GNGGA sentence"

        nmea_stream = BytesIO((nmea_sentence + '\r\n').encode('ascii'))
        nmr = NMEAReader(nmea_stream)
        
        try:
            raw_data = next(nmr)
            msg = raw_data[1]
            self.gngga_data = {
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
            return "No valid NMEA sentence found"
        except Exception as e:
            return str(e)

    def parse_gnrmc_sentence(self, nmea_sentence):
        if not nmea_sentence.startswith("$GNRMC"):
            return "Not a GNRMC sentence"

        nmea_stream = BytesIO((nmea_sentence + '\r\n').encode('ascii'))
        nmr = NMEAReader(nmea_stream)
        
        try:
            raw_data = next(nmr)
            msg = raw_data[1]
            self.gnrmc_data = {
                "Message Type": msg.msgID,
                "UTC Time": msg.time,
                "Status": getattr(msg, 'status', None),
                "Latitude": msg.lat,
                "Longitude": msg.lon,
                "Speed Over Ground": getattr(msg, 'spd', None),
                "Course Over Ground": getattr(msg, 'cog', None),
                "Date": getattr(msg, 'date', None),
                "Magnetic Variation": getattr(msg, 'magvar', None)
            }
        except StopIteration:
            return "No valid NMEA sentence found"
        except Exception as e:
            return str(e)
