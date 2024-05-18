import serial
import time

class ReadSerial:
    def __init__(self, port='/dev/ttyS3', baudrate=9600):
        self.ser = serial.Serial(port, baudrate)

    def read_data(self):
        while True:
            if self.ser.in_waiting > 0:
                line = self.ser.readline().decode('utf-8').strip()
                yield line
                time.sleep(1)
