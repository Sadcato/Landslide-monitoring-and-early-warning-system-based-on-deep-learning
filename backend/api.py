from fastapi import FastAPI
from fastapi.responses import JSONResponse
from reader.data_reader import ReadSerial
import threading

app = FastAPI()

data_source = ReadSerial()

latest_values = {}

@app.on_event("startup")
def start_reading():
    threading.Thread(target=stream_sensor_data, daemon=True).start()

def stream_sensor_data():
    for data in data_source.read_data():
        process_data(data)

def process_data(data):
    global latest_values
    if data.startswith('$'):
        key, value = data.split(',')
        latest_values[key] = value.strip()

@app.get("/reading")
def get_readings():
    return JSONResponse(content=latest_values)
