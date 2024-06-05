from utils.db_utils import execute_query

async def store_gnss_data(gnss_data):
    if gnss_data:
        query = """
        INSERT INTO gnss_data (message_type, utctime, latitude, longitude, fix_quality, num_of_satellites,
                               hdop, altitude, height_of_geoid, speed_over_ground, course_over_ground, date, magnetic_variation)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        await execute_query(query, (
            gnss_data['Message Type'], gnss_data['UTC Time'], gnss_data['Latitude'],
            gnss_data['Longitude'], gnss_data['Fix Quality'], gnss_data['Number of Satellites'],
            gnss_data['HDOP'], gnss_data['Altitude'], gnss_data['Height of Geoid'],
            gnss_data['Speed Over Ground'], gnss_data['Course Over Ground'], gnss_data['Date'],
            gnss_data['Magnetic Variation']
        ))

async def store_sensor_data(sensor_data):
    if sensor_data:
        query = """
        INSERT INTO sensor_data (temperature, humidity, soil_humidity)
        VALUES (%s, %s, %s)
        """
        await execute_query(query, (sensor_data.get('Temperature'), sensor_data.get('Humidity'), sensor_data.get('Soil Humidity')))



async def get_latest_gnss_Message_Type():
    query = "SELECT message_type FROM gnss_data ORDER BY id DESC LIMIT 1"
    result = await execute_query(query)
    return result[0][0] if result else None

async def get_latest_gnss_UTC_Time():
    query = "SELECT utcime FROM gnss_data ORDER BY id DESC LIMIT 1"
    result = await execute_query(query)
    return result[0][0] if result else None

async def get_latest_gnss_Magnetic_Variation():
    query = "SELECT magnetic_variation FROM gnss_data ORDER BY id DESC LIMIT 1"
    result = await execute_query(query)
    return result[0][0] if result else None

async def get_latest_gnss_Latitude():
    query = "SELECT latitude FROM gnss_data ORDER BY id DESC LIMIT 1"
    result = await execute_query(query)
    return result[0][0] if result else None

async def get_latest_gnss_Longitude():
    query = "SELECT longitude FROM gnss_data ORDER BY id DESC LIMIT 1"
    result = await execute_query(query)
    return result[0][0] if result else None

async def get_latest_gnss_Fix_Quality():
    query = "SELECT fix_quality FROM gnss_data ORDER BY id DESC LIMIT 1"
    result = await execute_query(query)
    return result[0][0] if result else None

async def get_latest_gnss_Number_of_Satellites():
    query = "SELECT number_of_satellites FROM gnss_data ORDER BY id DESC LIMIT 1"
    result = await execute_query(query)
    return result[0][0] if result else None

async def get_latest_gnss_HDOP():
    query = "SELECT hdop FROM gnss_data ORDER BY id DESC LIMIT 1"
    result = await execute_query(query)
    return result[0][0] if result else None

async def get_latest_gnss_Altitude():
    query = "SELECT altitude FROM gnss_data ORDER BY id DESC LIMIT 1"
    result = await execute_query(query)
    return result[0][0] if result else None

async def get_latest_gnss_Height_of_Geoid():
    query = "SELECT height_of_geoid FROM gnss_data ORDER BY id DESC LIMIT 1"
    result = await execute_query(query)
    return result[0][0] if result else None

async def get_latest_gnss_Status():
    query = "SELECT status FROM gnss_data ORDER BY id DESC LIMIT 1"
    result = await execute_query(query)
    return result[0][0] if result else None

async def get_latest_gnss_Speed_Over_Ground():
    query = "SELECT speed_over_ground FROM gnss_data ORDER BY id DESC LIMIT 1"
    result = await execute_query(query)
    return result[0][0] if result else None

async def get_latest_gnss_Course_Over_Ground():
    query = "SELECT course_over_ground FROM gnss_data ORDER BY id DESC LIMIT 1"
    result = await execute_query(query)
    return result[0][0] if result else None

async def get_latest_gnss_Date():
    query = "SELECT date FROM gnss_data ORDER BY id DESC LIMIT 1"
    result = await execute_query(query)
    return result[0][0] if result else None

async def get_latest_Temperature():
    query = "SELECT temperature FROM sensor_data ORDER BY id DESC LIMIT 1"
    result = await execute_query(query)
    return result[0][0] if result else None

async def get_latest_Humidity():
    query = "SELECT humidity FROM sensor_data ORDER BY id DESC LIMIT 1"
    result = await execute_query(query)
    return result[0][0] if result else None

async def get_latest_Soil_Humidity():
    query = "SELECT soil_humidity FROM sensor_data ORDER BY id DESC LIMIT 1"
    result = await execute_query(query)
    return result[0][0] if result else None