#ifndef INIT_HPP
#define INIT_HPP

#include <stdbool.h>
#include <stdint.h>

#include <Arduino.h>
#include <Adafruit_Sensor.h>
#include <DHT.h>
#include <SoftwareSerial.h>

#define MCU_BAUDRATE 115200

#define DHT_PIN 8
#define SOIL_PIN 23

#define GNSS_TXD 11
#define GNSS_RXD 10

extern SoftwareSerial GnssSerial;
extern DHT DhtSensor;

void gnss_init(bool use_baudrate_38400);
void serial_init();
void sensor_init();

#endif
