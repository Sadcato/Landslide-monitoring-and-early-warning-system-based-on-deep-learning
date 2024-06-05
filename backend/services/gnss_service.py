# services/gnss_service.py
from utils.db_utils import execute_query



async def retrieve_gnss_data():
    query = "SELECT * FROM gnss_data"
    return await execute_query(query)
