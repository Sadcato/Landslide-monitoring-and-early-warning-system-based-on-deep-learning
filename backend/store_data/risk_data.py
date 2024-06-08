from utils.db_utils import execute_query
from datetime import datetime

async def store_risk_data(gnss_data, sensor_data, risk_level):
    timestamp = datetime.now()
    query = """
    INSERT INTO landslide_risk_status (
        timestamp,
        risk_level,
        latitude,
        longitude,
        fix_quality,
        num_of_satellites,
        hdop,
        altitude,
        height_of_geoid,
        speed_over_ground,
        course_over_ground,
        temperature,
        humidity,
        soil_humidity
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    args = (
        timestamp,
        risk_level,
        gnss_data.get('Latitude'),
        gnss_data.get('Longitude'),
        gnss_data.get('Fix Quality'),
        gnss_data.get('Number of Satellites'),
        gnss_data.get('HDOP'),
        gnss_data.get('Altitude'),
        gnss_data.get('Height of Geoid'),
        gnss_data.get('Speed Over Ground'),
        gnss_data.get('Course Over Ground'),
        sensor_data.get('Temperature'),
        sensor_data.get('Humidity'),
        sensor_data.get('Soil Humidity')
    )
    await execute_query(query, args)
