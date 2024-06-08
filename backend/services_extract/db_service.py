from utils.db_utils import execute_query





async def get_latest_gnss_Message_Type():
    query = "SELECT message_type FROM gnss_data_GGA ORDER BY id DESC LIMIT 1"
    result = await execute_query(query)
    return result[0][0] if result else None

async def get_latest_gnss_Latitude():
    query = "SELECT latitude FROM gnss_data_GGA ORDER BY id DESC LIMIT 1"
    result = await execute_query(query)
    return result[0][0] if result and result[0][0] is not None else 0.0

async def get_latest_gnss_Longitude():
    query = "SELECT longitude FROM gnss_data_GGA ORDER BY id DESC LIMIT 1"
    result = await execute_query(query)
    return result[0][0] if result and result[0][0] is not None else 0.0

async def get_latest_gnss_Fix_Quality():
    query = "SELECT fix_quality FROM gnss_data_GGA ORDER BY id DESC LIMIT 1"
    result = await execute_query(query)
    return result[0][0] if result else None

async def get_latest_gnss_Number_of_Satellites():
    query = "SELECT num_of_satellites FROM gnss_data_GGA ORDER BY id DESC LIMIT 1"
    result = await execute_query(query)
    return result[0][0] if result else None

async def get_latest_gnss_HDOP():
    query = "SELECT hdop FROM gnss_data_GGA ORDER BY id DESC LIMIT 1"
    result = await execute_query(query)
    return result[0][0] if result and result[0][0] is not None else 0.0

async def get_latest_gnss_Altitude():
    query = "SELECT altitude FROM gnss_data_GGA ORDER BY id DESC LIMIT 1"
    result = await execute_query(query)
    return result[0][0] if result and result[0][0] is not None else 0.0

async def get_latest_gnss_Height_of_Geoid():
    query = "SELECT height_of_geoid FROM gnss_data_GGA ORDER BY id DESC LIMIT 1"
    result = await execute_query(query)
    return result[0][0] if result and result[0][0] is not None else 0.0

async def get_latest_gnss_Speed_Over_Ground():
    query = "SELECT speed_over_ground FROM gnss_data_RMC ORDER BY id DESC LIMIT 1"
    result = await execute_query(query)
    return result[0][0] if result and result[0][0] is not None else 0.0

async def get_latest_gnss_Course_Over_Ground():
    query = "SELECT course_over_ground FROM gnss_data_RMC ORDER BY id DESC LIMIT 1"
    result = await execute_query(query)
    return result[0][0] if result and result[0][0] is not None else 0.0

async def get_latest_Temperature():
    query = "SELECT temperature FROM sensor_data ORDER BY id DESC LIMIT 1"
    result = await execute_query(query)
    return result[0][0] if result and result[0][0] is not None else 0.0

async def get_latest_Humidity():
    query = "SELECT humidity FROM sensor_data ORDER BY id DESC LIMIT 1"
    result = await execute_query(query)
    return result[0][0] if result else None

async def get_latest_Soil_Humidity():
    query = "SELECT soil_humidity FROM sensor_data ORDER BY id DESC LIMIT 1"
    result = await execute_query(query)
    return result[0][0] if result else None

async def get_latest_risk_status():
    query = "SELECT * FROM landslide_risk_status"
    result = await execute_query(query)
    return result[0][0] if result else None