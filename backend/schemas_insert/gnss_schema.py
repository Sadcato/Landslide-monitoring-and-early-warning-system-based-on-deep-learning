# from datetime import datetime
# from processor.gnss import GNSSData
# from utils.db_utils import execute_query

# async def store_gnss_data(data: GNSSData):
#     if data:
#         # 插入GGA数据
#         if data.get("Message Type") == "GGA":
#             query_gga = """
#                 INSERT INTO gnss_data_GGA (
#                     message_type, 
#                     utctime, 
#                     latitude, 
#                     longitude, 
#                     fix_quality, 
#                     num_of_satellites, 
#                     hdop, 
#                     altitude, 
#                     height_of_geoid
#                 ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
#             """
#             utc_time = data.get("UTC Time")
#             if utc_time:
#                 try:
#                     utc_time = datetime.strptime(utc_time, '%H:%M:%S').strftime('%H:%M:%S')
#                 except ValueError:
#                     utc_time = None  # 或者设为默认时间
#             args_gga = (
#                 data.get("Message Type"),
#                 utc_time,
#                 data.get("Latitude"),
#                 data.get("Longitude"),
#                 data.get("Fix Quality"),
#                 data.get("Number of Satellites"),
#                 data.get("HDOP"),
#                 data.get("Altitude"),
#                 data.get("Height of Geoid")
#             )
#             await execute_query(query_gga, args_gga)

#         # 插入RMC数据
#         elif data.get("Message Type") == "RMC":
#             query_rmc = """
#             INSERT INTO gnss_data_RMC (
#                 message_type, 
#                 speed_over_ground, 
#                 course_over_ground, 
#                 date
#             ) VALUES (%s, %s, %s, %s)
#             """
#             date = data.get("Date")
#             if date:
#                 date = datetime.strptime(date, '%Y-%m-%d').strftime('%Y-%m-%d')

#             args_rmc = (
#                 data.get("Message Type"),
#                 data.get("Speed Over Ground"),
#                 data.get("Course Over Ground"),
#                 date
#             )
#             await execute_query(query_rmc, args_rmc)
#     print("b")