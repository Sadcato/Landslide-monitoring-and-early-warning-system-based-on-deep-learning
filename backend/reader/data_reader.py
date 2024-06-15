import serial
from concurrent.futures import ThreadPoolExecutor
import asyncio
from processor.gnss import GNSSData
from processor.sensor import SensorData
from services_extract.risk_service import get_latest_data
from assessment.calculate import calculate_risk_level
from store_data.risk_data import store_risk_data
from datetime import datetime, timedelta

class ReadSerial:
    def __init__(self, port='/dev/ttyS3', baudrate=115200):
        self.ser = serial.Serial(port, baudrate)
        self.gnss_data_processor = GNSSData()
        self.sensor_data_processor = SensorData()
        self.executor = ThreadPoolExecutor(1)
        self.last_stored_data = None  # To store the last written data to avoid duplicates

    async def process_and_store_data(self):
        while True:
            now_utc = datetime.utcnow()  # Get current UTC time
            timestamp = now_utc + timedelta(hours=8)  # Convert to Beijing time

            line = await asyncio.get_running_loop().run_in_executor(
                self.executor, self.ser.readline)
            line = line.decode('utf-8').strip()

            # Process GNSS data
            if line.startswith("$GNGGA") or line.startswith("$GNRMC"):
                gnss_data = self.gnss_data_processor.parse_gngga_sentence(line) if line.startswith("$GNGGA") else self.gnss_data_processor.parse_gnrmc_sentence(line)
                if gnss_data:
                    gnss_data['timestamp'] = timestamp
                    if not self.is_duplicate(gnss_data):
                        await self.gnss_data_processor.store_gnss_data(gnss_data, timestamp)

            # Process sensor data
            if line.startswith("$TEMP") or line.startswith("$HUMIDITY") or line.startswith("$SOILHUM"):
                sensor_data = self.sensor_data_processor.update_sensor_data(line)
                if sensor_data:
                    sensor_data['timestamp'] = timestamp
                    if not self.is_duplicate(sensor_data):
                        await self.sensor_data_processor.store_sensor_data(sensor_data, timestamp)

            # Fetch the latest data and calculate risk if both GNSS and Sensor data are processed
            data = await get_latest_data(timestamp)
            if data:
                risk_level, updated_data, risk_score = calculate_risk_level(data)
                updated_data['timestamp'] = timestamp
                if not self.is_duplicate(updated_data):
                    await store_risk_data(
                        timestamp,
                        risk_level,
                        updated_data['latitude'],
                        updated_data['longitude'],
                        updated_data['hdop'],
                        updated_data['altitude'],
                        updated_data['speed'],
                        updated_data['course'],
                        updated_data['soil_hum'],
                        risk_score
                    )
                    self.last_stored_data = updated_data

            await asyncio.sleep(1)  # Sleep to prevent high CPU usage

    def is_duplicate(self, data):
        if self.last_stored_data and all(self.last_stored_data.get(k) == data.get(k) for k in data if k != 'timestamp'):
            return True
        return False
