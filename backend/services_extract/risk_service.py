from utils.db_utils import execute_query

async def get_latest_data():
    query_rmc = "SELECT speed_over_ground, course_over_ground FROM gnss_data_RMC ORDER BY timestamp DESC LIMIT 1"
    query_gga = "SELECT altitude FROM gnss_data_GGA ORDER BY timestamp DESC LIMIT 1"
    query_sensor = "SELECT temperature, soil_humidity, humidity FROM sensor_data ORDER BY timestamp DESC LIMIT 1"

    # 获取RMC数据
    rmc_result = await execute_query(query_rmc)
    speed, course = rmc_result[0] if rmc_result else (None, None)

    # 获取GGA数据
    gga_result = await execute_query(query_gga)
    altitude = gga_result[0] if gga_result else (None)

    # 获取传感器数据
    sensor_result = await execute_query(query_sensor)
    temp, soil_hum, hum = sensor_result[0] if sensor_result else (None, None, None)

    return speed, course, altitude, temp, soil_hum, hum
