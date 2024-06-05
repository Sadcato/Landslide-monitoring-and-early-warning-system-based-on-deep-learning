from fastapi import FastAPI
from reader.data_reader import ReadSerial
from processor.gnss import GNSSData
from processor.sensor import SensorData
import threading
import logging
app = FastAPI()

# 初始化数据解析对象
gnss_data = GNSSData()
sensor_data = SensorData()

# 创建ReadSerial实例
data_source = ReadSerial()

@app.on_event("startup")
def start_reading():
    threading.Thread(target=stream_sensor_data, daemon=True).start()

def stream_sensor_data():
    for data in data_source.read_data():
        process_data(data)

def process_data(data):
    try:
        if data.startswith("$GNGGA"):
            gnss_data.parse_gngga_sentence(data)
        elif data.startswith("$GNRMC"):
            gnss_data.parse_gnrmc_sentence(data)
        elif data.startswith("$TEMP"):
            sensor_data.update_sensor_data(data)
        elif data.startswith("$HUMIDITY"):
            sensor_data.update_sensor_data(data)
        elif data.startswith("$SOILHUM"):
            sensor_data.update_sensor_data(data)
    except Exception as e:
        logging.error(f"Error processing data: {e}")
        gnss_data.error = True
        sensor_data.error = True



# GNSS数据端点

# @app.get("/api/gnss/Message Type")
# def get_gnss_message_type():
#     return {"Message Type": gnss_data.gngga_data.get("Message Type") or gnss_data.gnrmc_data.get("Message Type")}
@app.get("/api/gnss/Message Type")
def get_gnss_message_type():
    if gnss_data.error:
        gnss_data.error = False  
        return {"err": "err"}
    return {"Message Type": gnss_data.gngga_data.get("Message Type")}
    

# @app.get("/api/gnss/UTC Time")
# def get_gnss_utc_time():
#     return {"UTC Time": gnss_data.gngga_data.get("UTC Time") or gnss_data.gnrmc_data.get("UTC Time")}
@app.get("/api/gnss/UTC Time")
def get_gnss_utc_time():
    if gnss_data.error:
        gnss_data.error = False  
        return {"err": "err"}
    return {"UTC Time": gnss_data.gngga_data.get("UTC Time")}

@app.get("/api/gnss/Magnetic Variation")
def get_gnss_magnetic_variation():
    if gnss_data.error:
        gnss_data.error = False  
        return {"err": "err"}
    return {"Magnetic Variation": gnss_data.gnrmc_data.get("Magnetic Variation")}

# @app.get("/api/gnss/Latitude")
# def get_gnss_latitude():
#     return {"Latitude": gnss_data.gngga_data.get("Latitude") or gnss_data.gnrmc_data.get("Latitude")}
@app.get("/api/gnss/Latitude")
def get_gnss_latitude():
    if gnss_data.error:
        gnss_data.error = False  
        return {"err": "err"}
    return {"Latitude": gnss_data.gngga_data.get("Latitude")}

# @app.get("/api/gnss/Longitude")
# def get_gnss_longitude():
#     return {"Longitude": gnss_data.gngga_data.get("Longitude") or gnss_data.gnrmc_data.get("Longitude")}
@app.get("/api/gnss/Longitude")
def get_gnss_longitude():
    if gnss_data.error:
        gnss_data.error = False 
        return {"err": "err"}
    return {"Longitude": gnss_data.gngga_data.get("Longitude")}

@app.get("/api/gnss/Fix Quality")
def get_gnss_fix_quality():
    if gnss_data.error:
        gnss_data.error = False  
        return {"err": "err"}
    return {"Fix Quality": gnss_data.gngga_data.get("Fix Quality")}

@app.get("/api/gnss/Number of Satellites")
def get_gnss_number_of_satellites():
    if gnss_data.error:
        gnss_data.error = False 
        return {"err": "err"}
    return {"Number of Satellites": gnss_data.gngga_data.get("Number of Satellites")}

@app.get("/api/gnss/HDOP")
def get_gnss_hdop():
    if gnss_data.error:
        gnss_data.error = False  
        return {"err": "err"}
    return {"HDOP": gnss_data.gngga_data.get("HDOP")}

@app.get("/api/gnss/Altitude")
def get_gnss_altitude():
    if gnss_data.error:
        gnss_data.error = False  
        return {"err": "err"}
    return {"Altitude": gnss_data.gngga_data.get("Altitude")}

@app.get("/api/gnss/Height of Geoid")
def get_gnss_height_of_geoid():
    if gnss_data.error:
        gnss_data.error = False 
        return {"err": "err"}
    return {"Height of Geoid": gnss_data.gngga_data.get("Height of Geoid")}

@app.get("/api/gnss/Status")
def get_gnss_status():
    if gnss_data.error:
        gnss_data.error = False  
        return {"err": "err"}
    return {"Status": gnss_data.gnrmc_data.get("Status")}

@app.get("/api/gnss/Speed Over Ground")
def get_gnss_speed_over_ground():
    if gnss_data.error:
        gnss_data.error = False  
        return {"err": "err"}
    return {"Speed Over Ground": gnss_data.gnrmc_data.get("Speed Over Ground")}

@app.get("/api/gnss/Course Over Ground")
def get_gnss_course_over_ground():
    if gnss_data.error:
        gnss_data.error = False  
        return {"err": "err"}
    return {"Course Over Ground": gnss_data.gnrmc_data.get("Course Over Ground")}

@app.get("/api/gnss/Date")
def get_gnss_date():
    if gnss_data.error:
        gnss_data.error = False  
        return {"err": "err"}
    return {"Date": gnss_data.gnrmc_data.get("Date")}






# 传感器数据端点

@app.get("/api/sensor/Temperature")
def get_sensor_temperature():
    if sensor_data.error:
        sensor_data.error = False  # 重置错误标志
        return {"err": "err"}
    return {"Temperature": sensor_data.get_latest_temp()}

@app.get("/api/sensor/Humidity")
def get_sensor_humidity():
    if sensor_data.error:
        sensor_data.error = False  # 重置错误标志
        return {"err": "err"}
    return {"Humidity": sensor_data.get_latest_humidity()}

@app.get("/api/sensor/Soil Humidity")
def get_sensor_soil_humidity():
    if sensor_data.error:
        sensor_data.error = False  # 重置错误标志
        return {"err": "err"}
    return {"Soil Humidity": sensor_data.get_latest_soil_humidity()}