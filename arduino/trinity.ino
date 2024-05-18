
#include <SoftwareSerial.h> // GPS模块
#include <DHT.h> // 温湿度传感器
#include <TinyGPS++.h> // GPS库

#define Moisture A0 //土壤湿度传感器 AO 引脚
#define DO 7        //土壤湿度传感器 DO 引脚
#define GPS_RX_PIN 3 // GPS模块RX引脚
#define GPS_TX_PIN 4 // GPS模块TX引脚
#define DHTPIN 8     // 温湿度传感器引脚
#define DHTTYPE DHT11 // 温湿度传感器类型
#define PACKET_LEN 10 // 数据包长度
#define SEND_INTERVAL 500 // 推送间隔

SoftwareSerial gpsSerial(GPS_RX_PIN, GPS_TX_PIN); // GPS模块软串口对象
DHT dht(DHTPIN, DHTTYPE); // 温湿度传感器对象
TinyGPSPlus gps; // 创建 TinyGPS++ 对象

void setup() {
  Serial.begin(9600); // 初始化串口通信
  gpsSerial.begin(9600); // 初始化GPS模块的串口通信
  dht.begin(); // 初始化温湿度传感器
  pinMode(Moisture, INPUT); // 设置土壤湿度传感器引脚为输入模式
  pinMode(DO, INPUT); // 设置土壤湿度传感器引脚为输入模式
  Serial.println("Setup complete");
}

void loop() {
  // 读取GPS数据
  while (gpsSerial.available() > 0) {
    if (gps.encode(gpsSerial.read())) {
      // 经度、纬度
      Serial.print("Latitude: ");
      Serial.print(gps.location.lat(), 6);
      Serial.println(gps.location.rawLat().negative ? "S" : "N");
      Serial.print("Longitude: ");
      Serial.print(gps.location.lng(), 6);
      Serial.println(gps.location.rawLng().negative ? "W" : "E");
      
      // 北京时间
      Serial.print("Time: ");
      Serial.print(gps.time.hour());
      Serial.print(":");
      Serial.print(gps.time.minute());
      Serial.print(":");
      Serial.print(gps.time.second());
      Serial.print(" ");
      Serial.print(gps.date.year());
      Serial.print("/");
      Serial.print(gps.date.month());
      Serial.print("/");
      Serial.println(gps.date.day());
      
      // 海拔
      Serial.print("Altitude: ");
      Serial.println(gps.altitude.meters());

      // 水平精度
      Serial.print("Horizontal Accuracy: ");
      Serial.println(gps.hdop.value());

      // 正在使用的卫星数量
      Serial.print("Satellites: ");
      Serial.println(gps.satellites.value());

      // 地面速率
      Serial.print("Ground Speed: ");
      Serial.println(gps.speed.mps());

      // 偏向角
      Serial.print("Course: ");
      Serial.println(gps.course.deg());
    }
  }

  // 读取温湿度数据
  Serial.print("$AIRHUM,");
  for (uint8_t i = 0; i < PACKET_LEN; i++) {
    float humidity = dht.readHumidity();
    if (!isnan(humidity)) {
      Serial.print(humidity);
      Serial.print(i == PACKET_LEN-1 ? "\r\n" : ",");
    }
  }

  Serial.print("$TEMP,");
  for (uint8_t i = 0; i < PACKET_LEN; i++) {
    float temperature = dht.readTemperature();
    if (!isnan(temperature)) {
      Serial.print(temperature);
      Serial.print(i == PACKET_LEN-1 ? "\r\n" : ",");
    }
  }

  // 读取土壤湿度数据
  Serial.print("$SOILHUM,");
  for (uint8_t i = 0; i < PACKET_LEN; i++) {
    int soilHumidity = analogRead(Moisture);
    Serial.print(soilHumidity);
    Serial.print(i == PACKET_LEN-1 ? "\r\n" : ",");
  }

  delay(SEND_INTERVAL); // 推送间隔
}
