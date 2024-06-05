from fastapi import FastAPI, HTTPException
from services.gnss_service import retrieve_gnss_data
from services.sensor_service import retrieve_sensor_data
from reader.data_reader import ReadSerial
import asyncio
from services.db_service import *
from reader import data_reader
app = FastAPI()

data_source = ReadSerial()


@app.on_event("startup")
async def start_reading():
    """ 在应用启动时以异步方式开始串口数据读取和处理 """
    asyncio.create_task(data_source.process_and_store_data())




# GNSS数据端点

@app.get("/api/gnss/Message_Type")
async def get_gnss_Message_Type():
    try:
        Message_Type = await get_latest_gnss_Message_Type()
        if Message_Type is None:
            return {"err": "No Message Type data available"}
        return {"Message Type": Message_Type}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@app.get("/api/gnss/UTC_Time")
async def get_gnss_UTC_Time():
    try:
        UTC_Time = await get_latest_gnss_UTC_Time()
        if UTC_Time is None:
            return {"err": "No UTC Time data available"}
        return {"UTC Time": UTC_Time}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/gnss/Magnetic_Variation")
async def get_gnss_Magnetic_Variation():
    try:
        Magnetic_Variation = await get_latest_gnss_Magnetic_Variation()
        if Magnetic_Variation is None:
            return {"err": "No Magnetic Variation data available"}
        return {"Magnetic Variation": Magnetic_Variation}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/gnss/Latitude")
async def get_gnss_Latitude():
    try:
        Latitude = await get_latest_gnss_Latitude()
        if Latitude is None:
            return {"err": "No Latitude data available"}
        return {"Latitude": Latitude}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/gnss/Longitude")
async def get_gnss_Longitude():
    try:
        Longitude = await get_latest_gnss_Longitude()
        if Longitude is None:
            return {"err": "No Longitude data available"}
        return {"Longitude": Longitude}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/gnss/Fix_Quality")
async def get_gnss_Fix_Quality():
    try:
        Fix_Quality = await get_latest_gnss_Fix_Quality()
        if Fix_Quality is None:
            return {"err": "No Fix Quality data available"}
        return {"Fix Quality": Fix_Quality}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/gnss/Number_of_Satellites")
async def get_gnss_Number_of_Satellites():
    try:
        Number_of_Satellites = await get_latest_gnss_Number_of_Satellites()
        if Number_of_Satellites is None:
            return {"err": "No Number of Satellites data available"}
        return {"Number of Satellites": Number_of_Satellites}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/gnss/HDOP")
async def get_gnss_hdop():
    """ 从数据库中获取最新的HDOP值 """
    try:
        hdop = await get_latest_gnss_HDOP()
        if hdop is None:
            return {"err": "No HDOP data available"}
        return {"HDOP": hdop}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/gnss/Altitude")
async def get_gnss_Altitude():
    try:
        Altitude = await get_latest_gnss_Altitude()
        if Altitude is None:
            return {"err": "No Altitude data available"}
        return {"Altitude": Altitude}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/gnss/Height_of_Geoid")
async def get_gnss_Height_of_Geoid():
    try:
        Height_of_Geoid = await get_latest_gnss_Height_of_Geoid()
        if Height_of_Geoid is None:
            return {"err": "No Height_of_Geoid data available"}
        return {"Height_of_Geoid": Height_of_Geoid}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/gnss/Status")
async def get_gnss_Status():
    try:
        Status = await get_latest_gnss_Status()
        if Status is None:
            return {"err": "No Status data available"}
        return {"Status": Status}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/gnss/Speed_Over_Ground")
async def get_gnss_Speed_Over_Ground():
    try:
        Speed_Over_Ground = await get_latest_gnss_Speed_Over_Ground()
        if Speed_Over_Ground is None:
            return {"err": "No Speed_Over_Ground data available"}
        return {"Speed_Over_Ground": Speed_Over_Ground}
    except Exception as e:
        raise HTTPException(Speed_Over_Ground_code=500, detail=str(e))

@app.get("/api/gnss/Course_Over_Ground")
async def get_gnss_Course_Over_Ground():
    try:
        Course_Over_Ground = await get_latest_gnss_Course_Over_Ground()
        if Course_Over_Ground is None:
            return {"err": "No Course_Over_Ground data available"}
        return {"Course_Over_Ground": Course_Over_Ground}
    except Exception as e:
        raise HTTPException(Course_Over_Ground_code=500, detail=str(e))

@app.get("/api/gnss/Date")
async def get_gnss_Date():
    try:
        Date = await get_latest_gnss_Date()
        if Date is None:
            return {"err": "No Date data available"}
        return {"Date": Date}
    except Exception as e:
        raise HTTPException(Date_code=500, detail=str(e))






# 传感器数据端点

@app.get("/api/sensor/Temperature")
async def get_sensor_Temperature():
    """ 从数据库中获取最新的温度值 """
    try:
        temperature = await get_latest_Temperature()
        if temperature is None:
            return {"error": "No temperature data available"}
        return {"Temperature": temperature}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/sensor/Humidity")
async def get_sensor_Humidity():
    try:
        Humidity = await get_latest_Humidity()
        if Humidity is None:
            return {"error": "No Humidity data available"}
        return {"Humidity": Humidity}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/sensor/Soil_Humidity")
async def get_sensor_Soil_Humidity():
    try:
        Soil_Humidity = await get_latest_Soil_Humidity()
        if Soil_Humidity is None:
            return {"error": "No Soil_Humidity data available"}
        return {"Soil_Humidity": Soil_Humidity}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


from services.gnss_service import retrieve_gnss_data
from services.sensor_service import retrieve_sensor_data

@app.get("/api/gnss/history")
async def get_gnss_history():
    """ 获取历史GNSS数据 """
    try:
        data = await retrieve_gnss_data()
        return {"data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/sensor/history")
async def get_sensor_history():
    """ 获取历史传感器数据 """
    try:
        data = await retrieve_sensor_data()
        return {"data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))