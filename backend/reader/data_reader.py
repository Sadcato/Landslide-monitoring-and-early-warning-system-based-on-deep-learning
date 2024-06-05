import serial
import time
from services.db_service import store_gnss_data, store_sensor_data
from processor.gnss import GNSSData
from processor.sensor import SensorData
from concurrent.futures import ThreadPoolExecutor
import serial
import asyncio

class ReadSerial:
    def __init__(self, port='/dev/ttyS3', baudrate=115200):
        self.ser = serial.Serial(port, baudrate)
        self.gnss_data_processor = GNSSData()
        self.sensor_data_processor = SensorData()
        self.executor = ThreadPoolExecutor(1)
    async def process_and_store_data(self):
        while True:
            line = await asyncio.get_running_loop().run_in_executor(
                self.executor, self.ser.readline)
            line = line.decode('utf-8').strip()

        # Process GNSS data
            if line.startswith("$GNGGA") or line.startswith("$GNRMC"):
                gnss_data = self.gnss_data_processor.parse_gngga_sentence(line) if line.startswith("$GNGGA") else self.gnss_data_processor.parse_gnrmc_sentence(line)
                if gnss_data:
                    await self.gnss_data_processor.store_gnss_data(gnss_data) 

            # Process sensor data
                elif line.startswith("$TEMP") or line.startswith("$HUMIDITY") or line.startswith("$SOILHUM"):
                    sensor_data = self.sensor_data_processor.update_sensor_data(line)
                    if sensor_data:
                        await self.sensor_data_processor.store_sensor_data(sensor_data)

                await asyncio.sleep(0.1) 
