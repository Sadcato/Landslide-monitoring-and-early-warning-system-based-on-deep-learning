# import datetime
# from utils.db_utils import execute_query

# async def store_sensor_data(sensor_data):
#         timestamp = datetime.datetime.now()
#         query = """
#         INSERT INTO sensor_data (timestamp, temperature, humidity, soil_humidity)
#         VALUES (%s, %s, %s, %s)
#         """
#         await execute_query(query, (timestamp, sensor_data['Temperature'], sensor_data['Humidity'], sensor_data['Soil Humidity']))
