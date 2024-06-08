from fastapi import FastAPI, HTTPException, WebSocket,WebSocketDisconnect
from services_extract.gnss_service import retrieve_gnss_data
from services_extract.sensor_service import retrieve_sensor_data
from reader.data_reader import ReadSerial
import asyncio
from services_extract.db_service import *


app = FastAPI()

data_source = ReadSerial()


@app.on_event("startup")
async def start_reading():
    """ 在应用启动时以异步方式开始串口数据读取和处理 """
    asyncio.create_task(data_source.process_and_store_data())




    ''' GNSS数据端点 '''

@app.websocket("/ws/gnss/Message_Type")
async def websocket_gnss_message_type(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            # 获取最新的GNSS消息类型数据
            Message_Type = await get_latest_gnss_Message_Type()
            if Message_Type is None:
                await websocket.send_json({"err": "No Message Type data available"})
            else:
                await websocket.send_json({"Message Type": Message_Type})
            await asyncio.sleep(1)  # 设置适当的间隔以避免过载
    except WebSocketDisconnect:
        print("Client disconnected")
    except Exception as e:
        print(f"Error: {str(e)}")
        await websocket.close(code=1011)  # 发送适当的WebSocket关闭码
    

@app.websocket("/ws/gnss/UTC_Time")
async def websocket_gnss_utc_time(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            # 获取最新的GNSS UTC时间数据
            UTC_Time = await get_latest_gnss_UTC_Time()
            if UTC_Time is None:
                await websocket.send_json({"err": "No UTC Time data available"})
            else:
                await websocket.send_json({"UTC Time": UTC_Time})
            await asyncio.sleep(1)  # 设置适当的间隔以避免过载
    except WebSocketDisconnect:
        print("Client disconnected")
    except Exception as e:
        print(f"Error: {str(e)}")
        await websocket.close(code=1011)  # 发送适当的WebSocket关闭码




@app.websocket("/ws/gnss/Latitude")
async def websocket_gnss_latitude(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            # 获取最新的GNSS纬度数据
            Latitude = await get_latest_gnss_Latitude()
            if Latitude is None:
                await websocket.send_json({"err": "No Latitude data available"})
            else:
                await websocket.send_json({"Latitude": Latitude})
            await asyncio.sleep(1)  # 调整此值以控制发送频率
    except WebSocketDisconnect:
        print("Client disconnected")
    except Exception as e:
        print(f"Error: {str(e)}")
        await websocket.close(code=1011)  # 发送适当的WebSocket关闭码


@app.websocket("/ws/gnss/Longitude")
async def websocket_gnss_longitude(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            Longitude = await get_latest_gnss_Longitude()
            if Longitude is None:
                await websocket.send_json({"err": "No Longitude data available"})
            else:
                await websocket.send_json({"Longitude": Longitude})
            await asyncio.sleep(1)  # Update interval
    except WebSocketDisconnect:
        print("WebSocket disconnected")
    except Exception as e:
        print(f"Error: {str(e)}")
        await websocket.close(code=1011)  # Internal server error


from fastapi import WebSocket, WebSocketDisconnect

@app.websocket("/ws/gnss/Fix_Quality")
async def websocket_gnss_fix_quality(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            # 获取最新的GNSS Fix Quality数据
            Fix_Quality = await get_latest_gnss_Fix_Quality()
            if Fix_Quality is None:
                await websocket.send_json({"err": "No Fix Quality data available"})
            else:
                await websocket.send_json({"Fix Quality": Fix_Quality})
            await asyncio.sleep(1)  # 控制发送数据的频率
    except WebSocketDisconnect:
        print("Client disconnected")
    except Exception as e:
        print(f"Error: {str(e)}")
        await websocket.close(code=1011)  # 使用适当的WebSocket关闭码


@app.websocket("/ws/gnss/Number_of_Satellites")
async def websocket_gnss_number_of_satellites(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            # 获取最新的GNSS卫星数量数据
            Number_of_Satellites = await get_latest_gnss_Number_of_Satellites()
            if Number_of_Satellites is None:
                await websocket.send_json({"err": "No Number of Satellites data available"})
            else:
                await websocket.send_json({"Number of Satellites": Number_of_Satellites})
            await asyncio.sleep(1)  # 根据需要调整更新频率
    except WebSocketDisconnect:
        print("Client disconnected")
    except Exception as e:
        print(f"Error: {str(e)}")
        await websocket.close(code=1011)  # 发送适当的WebSocket关闭码

@app.websocket("/ws/gnss/HDOP")
async def websocket_gnss_hdop(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            hdop = await get_latest_gnss_HDOP()
            if hdop is None:
                await websocket.send_json({"err": "No HDOP data available"})
            else:
                await websocket.send_json({"HDOP": hdop})
            await asyncio.sleep(1)  # Update interval
    except WebSocketDisconnect:
        print("WebSocket disconnected")
    except Exception as e:
        print(f"Error: {str(e)}")
        await websocket.close(code=1011)  # Internal server error


@app.websocket("/ws/gnss/altitude")
async def websocket_gnss_altitude(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            Altitude = await get_latest_gnss_Altitude()
            if Altitude is None:
                await websocket.send_json({"err": "No Altitude data available"})
            else:
                await websocket.send_json({"Altitude": Altitude})
            await asyncio.sleep(1)  # Adjust frequency based on requirements
    except WebSocketDisconnect:
        print("Client disconnected - Altitude stream")
    except Exception as e:
        print(f"Error in Altitude stream: {str(e)}")
        await websocket.close(code=1011)


@app.websocket("/ws/gnss/height_of_geoid")
async def websocket_gnss_height_of_geoid(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            Height_of_Geoid = await get_latest_gnss_Height_of_Geoid()
            if Height_of_Geoid is None:
                await websocket.send_json({"err": "No Height of Geoid data available"})
            else:
                await websocket.send_json({"Height_of_Geoid": Height_of_Geoid})
            await asyncio.sleep(1)  # Adjust frequency based on requirements
    except WebSocketDisconnect:
        print("Client disconnected - Height of Geoid stream")
    except Exception as e:
        print(f"Error in Height of Geoid stream: {str(e)}")
        await websocket.close(code=1011)



@app.websocket("/ws/gnss/Speed_Over_Ground")
async def websocket_gnss_speed_over_ground(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            speed_over_ground = await get_latest_gnss_Speed_Over_Ground()
            if speed_over_ground is None:
                await websocket.send_json({"err": "No Speed Over Ground data available"})
            else:
                await websocket.send_json({"Speed Over Ground": speed_over_ground})
            await asyncio.sleep(1)
    except WebSocketDisconnect:
        print("Client disconnected")
    except Exception as e:
        print(f"WebSocket error: {str(e)}")
        await websocket.close()


@app.websocket("/ws/gnss/Course_Over_Ground")
async def websocket_gnss_course_over_ground(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            course_over_ground = await get_latest_gnss_Course_Over_Ground()
            if course_over_ground is None:
                await websocket.send_json({"err": "No Course Over Ground data available"})
            else:
                await websocket.send_json({"Course Over Ground": course_over_ground})
            await asyncio.sleep(1)
    except WebSocketDisconnect:
        print("Client disconnected")
    except Exception as e:
        print(f"WebSocket error: {str(e)}")
        await websocket.close()


from datetime import datetime

@app.websocket("/ws/gnss/Date")
async def websocket_gnss_date(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            date_obj = await get_latest_gnss_Date()  # 假设返回的是 datetime.date 对象或 None
            if date_obj is None:
                await websocket.send_json({"error": "No Date data available"})
            else:
                date_str = date_obj.strftime('%Y-%m-%d')  # 将 date 对象转换为字符串
                await websocket.send_json({"Date": date_str})
            await asyncio.sleep(1)  # Update interval
    except WebSocketDisconnect:
        print("WebSocket disconnected")
    except Exception as e:
        print(f"Error: {str(e)}")
        await websocket.close(code=1011)







# 传感器数据端点

@app.websocket("/ws/sensor/Temperature")
async def websocket_sensor_temperature(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            temperature = await get_latest_Temperature()
            if temperature is None:
                await websocket.send_json({"error": "No temperature data available"})
            else:
                await websocket.send_json({"Temperature": temperature})
            await asyncio.sleep(1)  # Update interval
    except WebSocketDisconnect:
        print("WebSocket disconnected")
    except Exception as e:
        print(f"Error: {str(e)}")
        await websocket.close(code=1011)  # Internal server error


@app.websocket("/ws/sensor/humidity")
async def websocket_sensor_humidity(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            # 获取最新的湿度数据
            Humidity = await get_latest_Humidity()
            if Humidity is None:
                await websocket.send_json({"error": "No Humidity data available"})
            else:
                await websocket.send_json({"Humidity": Humidity})
            await asyncio.sleep(1)  # 控制数据发送频率
    except WebSocketDisconnect:
        print("Client disconnected")
    except Exception as e:
        print(f"Error: {str(e)}")
        await websocket.close(code=1011)  # 发送适当的WebSocket关闭码

@app.websocket("/ws/sensor/Soil_Humidity")
async def websocket_soil_humidity(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            # 获取最新的土壤湿度数据
            Soil_Humidity = await get_latest_Soil_Humidity()
            if Soil_Humidity is None:
                await websocket.send_json({"error": "No Soil_Humidity data available"})
            else:
                await websocket.send_json({"Soil_Humidity": Soil_Humidity})
            await asyncio.sleep(1)  # 控制更新频率
    except WebSocketDisconnect:
        print("Client disconnected from soil humidity stream")
    except Exception as e:
        print(f"Error in soil humidity stream: {str(e)}")
        await websocket.close(code=1011)


# from services_extract.gnss_service import retrieve_gnss_data
# from services_extract.sensor_service import retrieve_sensor_data

# @app.websocket("/ws/gnss/history")
# async def websocket_gnss_history(websocket: WebSocket):
#     await websocket.accept()  # 接受WebSocket连接
#     try:
#         # 这里假设 retrieve_gnss_data() 是异步的，并且返回历史GNSS数据
#         data = await retrieve_gnss_data()
#         if data:
#             await websocket.send_json({"data": data})
#         else:
#             await websocket.send_json({"error": "No GNSS history data available"})
#     except Exception as e:
#         # 使用 WebSocket 发送错误消息
#         await websocket.send_json({"error": str(e)})
#     finally:
#         await websocket.close(code=1011) 

# from fastapi import WebSocket

# @app.websocket("/ws/sensor/history")
# async def websocket_sensor_history(websocket: WebSocket):
#     await websocket.accept()  # 接受WebSocket连接
#     try:
#         # 这里假设 retrieve_sensor_data() 是异步的，并且返回历史传感器数据
#         data = await retrieve_sensor_data()
#         if data:
#             await websocket.send_json({"data": data})
#         else:
#             await websocket.send_json({"error": "No sensor history data available"})
#     except Exception as e:
#         # 使用 WebSocket 发送错误消息
#         await websocket.send_json({"error": str(e)})
#     finally:
#         await websocket.close(code=1011)  # 适当的关闭代码

# @app.get("/api/sensor/history")
# async def get_sensor_history():
#     """ 获取历史传感器数据 """
#     try:
#         data = await retrieve_sensor_data()
#         return {"data": data}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

# @app.get("/api/gnss/Message_Type")
# async def get_gnss_Message_Type():
#     try:
#         Message_Type = await get_latest_gnss_Message_Type()
#         if Message_Type is None:
#             return {"err": "No Message Type data available"}
#         return {"Message Type": Message_Type}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))