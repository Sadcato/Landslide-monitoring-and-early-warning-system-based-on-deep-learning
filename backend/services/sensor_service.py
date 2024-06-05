from utils.db_utils import execute_query



async def retrieve_sensor_data():
    query = "SELECT * FROM sensor_data"
    return await execute_query(query)
