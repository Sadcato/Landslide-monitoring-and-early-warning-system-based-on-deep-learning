from utils.db_utils import execute_query
import datetime


class SensorData:
    def __init__(self):
        self.temp = []
        self.humidity = []
        self.soil_humidity = []
        self.error = False

    def update_sensor_data(self, data_str):
        parts = data_str.split(',')
        sensor_type = parts[0]
        values = [float(val) if '.' in val else int(val) for val in parts[1:]]
        if sensor_type == "$TEMP":
            return {"Temperature": values[-1] if values else None}
        elif sensor_type == "$HUMIDITY":
            return {"Humidity": values[-1] if values else None}
        elif sensor_type == "$SOILHUM":
            return {"Soil Humidity": values[-1] if values else None}
        return None

    def get_latest_temp(self):
        return self.temp[-1] if self.temp else None

    def get_latest_humidity(self):
        return self.humidity[-1] if self.humidity else None

    def get_latest_soil_humidity(self):
        return self.soil_humidity[-1] if self.soil_humidity else None
    
    async def store_sensor_data(sensor_data):
        timestamp = datetime.datetime.now()
        query = """
        INSERT INTO sensor_data (timestamp, temperature, humidity, soil_humidity)
        VALUES (%s, %s, %s, %s)
        """
        await execute_query(query, (timestamp, sensor_data['Temperature'], sensor_data['Humidity'], sensor_data['Soil Humidity']))
