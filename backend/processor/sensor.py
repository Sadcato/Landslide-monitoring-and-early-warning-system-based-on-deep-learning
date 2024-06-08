import datetime
from utils.db_utils import execute_query



class SensorData:
    def __init__(self):
        self.temp = []
        self.humidity = []
        self.soil_humidity = []
        self.error = False

    def update_sensor_data(self, data_str):
        parts = data_str.split(',')
        sensor_type = parts[0]
        try:
            values = [float(val) if '.' in val else int(val) for val in parts[1:] if val.replace('.', '').isdigit()]
        except ValueError as e:
            print(f"Error processing sensor data: {data_str} -> {e}")
            return None

        if sensor_type == "$TEMP":
            self.temp = values
        elif sensor_type == "$HUMIDITY":
            self.humidity = values
        elif sensor_type == "$SOILHUM":
            self.soil_humidity = values

        return {
            "Temperature": self.get_latest_temp(),
            "Humidity": self.get_latest_humidity(),
            "Soil Humidity": self.get_latest_soil_humidity()
        }

    def get_latest_temp(self):
        return self.temp[-1] if self.temp else None

    def get_latest_humidity(self):
        return self.humidity[-1] if self.humidity else None

    def get_latest_soil_humidity(self):
        return self.soil_humidity[-1] if self.soil_humidity else None
    
    """插入sensor数据"""
    async def store_sensor_data(self,sensor_data):
        timestamp = datetime.datetime.now()
        query = """
        INSERT INTO sensor_data (timestamp, temperature, humidity, soil_humidity)
        VALUES (%s, %s, %s, %s)
        """
        await execute_query(query, (timestamp, sensor_data['Temperature'], sensor_data['Humidity'], sensor_data['Soil Humidity']))

