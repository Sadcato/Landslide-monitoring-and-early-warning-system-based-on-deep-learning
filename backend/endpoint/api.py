from fastapi import FastAPI,WebSocket,WebSocketDisconnect
from reader.data_reader import ReadSerial
import asyncio
from services_extract.db_service import *


app = FastAPI()

data_source = ReadSerial()


@app.on_event("startup")
async def start_reading():
    """ 在应用启动时以异步方式开始串口数据读取和处理 """
    asyncio.create_task(data_source.process_and_store_data())

    """ 优雅关闭任务确保所有后台任务都能正常关闭"""
@app.on_event("shutdown")
async def shutdown_event():
    print("Shutting down: cancelling background tasks...")
    # task.cancel()
    print("All background tasks cancelled.")



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
    





@app.websocket("/ws/gnss/Latitude")
async def websocket_gnss_latitude(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            Latitude = await get_latest_gnss_Latitude()
            if Latitude is None:
                await websocket.send_json({"err": "No Latitude data available"})
            else:
                await websocket.send_json({"Latitude": Latitude})
            await asyncio.sleep(1) 
    except WebSocketDisconnect:
        print("Client disconnected")
    except Exception as e:
        print(f"Error: {str(e)}")
        await websocket.close(code=1011) 

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
            await asyncio.sleep(1) 
    except WebSocketDisconnect:
        print("WebSocket disconnected")
    except Exception as e:
        print(f"Error: {str(e)}")
        await websocket.close(code=1011) 


from fastapi import WebSocket, WebSocketDisconnect

@app.websocket("/ws/gnss/Fix_Quality")
async def websocket_gnss_fix_quality(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            Fix_Quality = await get_latest_gnss_Fix_Quality()
            if Fix_Quality is None:
                await websocket.send_json({"err": "No Fix Quality data available"})
            else:
                await websocket.send_json({"Fix Quality": Fix_Quality})
            await asyncio.sleep(1) 
    except WebSocketDisconnect:
        print("Client disconnected")
    except Exception as e:
        print(f"Error: {str(e)}")
        await websocket.close(code=1011)  


@app.websocket("/ws/gnss/Number_of_Satellites")
async def websocket_gnss_number_of_satellites(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            Number_of_Satellites = await get_latest_gnss_Number_of_Satellites()
            if Number_of_Satellites is None:
                await websocket.send_json({"err": "No Number of Satellites data available"})
            else:
                await websocket.send_json({"Number of Satellites": Number_of_Satellites})
            await asyncio.sleep(1)  
    except WebSocketDisconnect:
        print("Client disconnected")
    except Exception as e:
        print(f"Error: {str(e)}")
        await websocket.close(code=1011)  


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
            await asyncio.sleep(1)  
    except WebSocketDisconnect:
        print("WebSocket disconnected")
    except Exception as e:
        print(f"Error: {str(e)}")
        await websocket.close(code=1011) 


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
            await asyncio.sleep(1) 
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
            await asyncio.sleep(1) 
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


    ''' 传感器数据端点 '''

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
            await asyncio.sleep(1)  
    except WebSocketDisconnect:
        print("WebSocket disconnected")
    except Exception as e:
        print(f"Error: {str(e)}")
        await websocket.close(code=1011) 


@app.websocket("/ws/sensor/humidity")
async def websocket_sensor_humidity(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            Humidity = await get_latest_Humidity()
            if Humidity is None:
                await websocket.send_json({"error": "No Humidity data available"})
            else:
                await websocket.send_json({"Humidity": Humidity})
            await asyncio.sleep(1) 
    except WebSocketDisconnect:
        print("Client disconnected")
    except Exception as e:
        print(f"Error: {str(e)}")
        await websocket.close(code=1011) 

@app.websocket("/ws/sensor/Soil_Humidity")
async def websocket_soil_humidity(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            Soil_Humidity = await get_latest_Soil_Humidity()
            if Soil_Humidity is None:
                await websocket.send_json({"error": "No Soil_Humidity data available"})
            else:
                await websocket.send_json({"Soil_Humidity": Soil_Humidity})
            await asyncio.sleep(1)  
    except WebSocketDisconnect:
        print("Client disconnected from soil humidity stream")
    except Exception as e:
        print(f"Error in soil humidity stream: {str(e)}")
        await websocket.close(code=1011)


@app.websocket("/ws/risk")
async def websocket_risk_status(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            risk_status = await get_latest_risk_status()
            if risk_status is None:
                await websocket.send_json({"error": "No risk_status data available"})
            else:
                await websocket.send_json({"risk_status": risk_status})
            await asyncio.sleep(1)  
    except WebSocketDisconnect:
        print("Client disconnected from risk_status stream")
    except Exception as e:
        print(f"Error in risk_status stream: {str(e)}")
        await websocket.close(code=1011)