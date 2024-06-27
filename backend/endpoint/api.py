from fastapi import FastAPI, Response, WebSocket, WebSocketDisconnect, HTTPException
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
import asyncio
import logging
from reader.data_reader import ReadSerial
from services_extract.db_service import *

# Initialize logging
logging.basicConfig(filename='gnss_data.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

app = FastAPI()
data_source = ReadSerial()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
    logging.info("Starting data reading process")
    data_source.start_task()

@app.on_event("shutdown")
async def shutdown_event():
    logging.info("Shutting down: cancelling background tasks...")
    data_source.cancel_task()
    logging.info("All background tasks cancelled.")

def sse_format(data: dict) -> str:
    """Format the dictionary data into SSE format."""
    return f"data: {data}\n\n"

async def fetch_latest_data(data_fetcher):
    while True:
        try:
            data = await data_fetcher()
            if data is None:
                yield sse_format({"error": "No data available"})
            else:
                yield sse_format(data)
        except Exception as e:
            logging.error(f"Error fetching data: {e}")
            yield sse_format({"error": str(e)})
        await asyncio.sleep(1)  # Refresh rate

@app.get("/api/gnss/message_type", response_class=Response)
async def sse_gnss_message_type():
    return StreamingResponse(fetch_latest_data(get_latest_gnss_Message_Type), media_type="text/event-stream")

@app.get("/api/gnss/latitude", response_class=Response)
async def sse_gnss_latitude():
    return StreamingResponse(fetch_latest_data(get_latest_gnss_Latitude), media_type="text/event-stream")

@app.get("/api/gnss/longitude", response_class=Response)
async def sse_gnss_longitude():
    return StreamingResponse(fetch_latest_data(get_latest_gnss_Longitude), media_type="text/event-stream")

@app.get("/api/gnss/fix_quality", response_class=Response)
async def sse_gnss_fix_quality():
    return StreamingResponse(fetch_latest_data(get_latest_gnss_Fix_Quality), media_type="text/event-stream")

@app.get("/api/gnss/number_of_satellites", response_class=Response)
async def sse_gnss_number_of_satellites():
    logging.info("Handling /api/gnss/number_of_satellites request")
    try:
        response = StreamingResponse(fetch_latest_data(get_latest_gnss_Number_of_Satellites), media_type="text/event-stream")
        logging.info("Successfully set up StreamingResponse for /api/gnss/number_of_satellites")
        return response
    except Exception as e:
        logging.error(f"Error setting up StreamingResponse for /api/gnss/number_of_satellites: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.get("/api/gnss/hdop", response_class=Response)
async def sse_gnss_hdop():
    return StreamingResponse(fetch_latest_data(get_latest_gnss_HDOP), media_type="text/event-stream")

@app.get("/api/gnss/altitude", response_class=Response)
async def sse_gnss_altitude():
    return StreamingResponse(fetch_latest_data(get_latest_gnss_Altitude), media_type="text/event-stream")

@app.get("/api/gnss/height_of_geoid", response_class=Response)
async def sse_gnss_height_of_geoid():
    return StreamingResponse(fetch_latest_data(get_latest_gnss_Height_of_Geoid), media_type="text/event-stream")

@app.get("/api/gnss/speed_over_ground", response_class=Response)
async def sse_gnss_speed_over_ground():
    return StreamingResponse(fetch_latest_data(get_latest_gnss_Speed_Over_Ground), media_type="text/event-stream")

@app.get("/api/gnss/course_over_ground", response_class=Response)
async def sse_gnss_course_over_ground():
    return StreamingResponse(fetch_latest_data(get_latest_gnss_Course_Over_Ground), media_type="text/event-stream")

@app.get("/api/sensor/temperature", response_class=Response)
async def sse_sensor_temperature():
    return StreamingResponse(fetch_latest_data(get_latest_Temperature), media_type="text/event-stream")

@app.get("/api/sensor/humidity", response_class=Response)
async def sse_sensor_humidity():
    return StreamingResponse(fetch_latest_data(get_latest_Humidity), media_type="text/event-stream")

@app.get("/api/sensor/soil_humidity", response_class=Response)
async def sse_sensor_soil_humidity():
    return StreamingResponse(fetch_latest_data(get_latest_Soil_Humidity), media_type="text/event-stream")

@app.get("/api/risk", response_class=Response)
async def sse_risk_status():
    return StreamingResponse(fetch_latest_data(get_latest_risk_status), media_type="text/event-stream")

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
            await asyncio.sleep(1)  # Adjust the sleep time as necessary
    except WebSocketDisconnect:
        logging.info("Client disconnected from risk_status stream")
    except Exception as e:
        logging.error(f"Error in risk_status stream: {str(e)}")
        await websocket.close(code=1011)
