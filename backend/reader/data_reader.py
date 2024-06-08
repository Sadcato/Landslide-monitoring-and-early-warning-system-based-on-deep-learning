import serial
from concurrent.futures import ThreadPoolExecutor
import asyncio
from processor.gnss import GNSSData
from processor.sensor import SensorData
from assessment.calculate import calculate_risk_level
from store_data.risk_data import store_risk_data
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

            # Assuming both GNSS and Sensor data are processed in the same cycle
            elif gnss_data and sensor_data:
                # Calculate risk level based on the latest GNSS and Sensor data
                risk_level = calculate_risk_level(
                    gnss_data.get('Speed Over Ground'), 
                    gnss_data.get('Course Over Ground'), 
                    gnss_data.get('Altitude'), 
                    sensor_data.get('Temperature'), 
                    sensor_data.get('Soil Humidity'), 
                    sensor_data.get('Humidity')
                )
                # Store the risk assessment into the database
                await store_risk_data(gnss_data, sensor_data, risk_level)

            await asyncio.sleep(0.1)  # Sleep to prevent high CPU usage