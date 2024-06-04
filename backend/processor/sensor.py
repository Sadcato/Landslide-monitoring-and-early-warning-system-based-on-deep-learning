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
            self.temp = values
        elif sensor_type == "$HUMIDITY":
            self.humidity = values
        elif sensor_type == "$SOILHUM":
            self.soil_humidity = values

    def get_latest_temp(self):
        return self.temp[-1] if self.temp else None

    def get_latest_humidity(self):
        return self.humidity[-1] if self.humidity else None

    def get_latest_soil_humidity(self):
        return self.soil_humidity[-1] if self.soil_humidity else None
