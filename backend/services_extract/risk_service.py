import logging
from utils.db_utils import execute_query

logging.basicConfig(level=logging.DEBUG)

async def get_latest_data(timestamp):
    query = """
SELECT
    r.speed_over_ground AS speed, 
    r.course_over_ground AS course,
    g.altitude,
    s.soil_humidity AS soil_hum,
    g.latitude, 
    g.longitude,
    g.hdop
FROM gnss_data_RMC r
INNER JOIN gnss_data_GGA g ON g.timestamp BETWEEN DATE_SUB(r.timestamp, INTERVAL 3 SECOND) AND DATE_ADD(r.timestamp, INTERVAL 3 SECOND)
INNER JOIN sensor_data s ON s.timestamp BETWEEN DATE_SUB(g.timestamp, INTERVAL 3 SECOND) AND DATE_ADD(g.timestamp, INTERVAL 3 SECOND)
WHERE r.timestamp <= %s
ORDER BY r.timestamp DESC
LIMIT 1;
"""
    params = (timestamp,)
    try:
        result = await execute_query(query, params)
        if result:
            # logging.debug(f"Data fetched successfully: {result}")
            return dict(zip(["speed", "course", "altitude", "soil_hum", "latitude", "longitude", "hdop"], result[0]))
        else:
            logging.warning("No data fetched. Query executed: " + query)
            return None
    except Exception as e:
        logging.error(f"Error retrieving data: {str(e)}")
        return None
