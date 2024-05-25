#include <Arduino.h>
#include <SoftwareSerial.h>

#define GNSS_USE_BAUDRATE_38400

#ifdef GNSS_USE_BAUDRATE_38400
const uint8_t GNSS_SET_BAUDRATE_CMD[] = {
    0xF1,
    0xD9,
    0x06,
    0x00,
    0x08,
    0x00,
    0x00,
    0x00,
    0x00,
    0x00,
    0x00,
    0x96,
    0x00,
    0x00,
    0xA4,
    0x5A,
};
#else
const uint8_t GNSS_SET_BAUDRATE_CMD[] = {
    0xF1,
    0xD9,
    0x06,
    0x00,
    0x08,
    0x00,
    0x00,
    0x00,
    0x00,
    0x00,
    0x80,
    0x25,
    0x00,
    0x00,
    0xB3,
    0x07,
};
#endif

SoftwareSerial GnssSerial(10, 11);

void gnss_init()
{
  GnssSerial.begin(115200);

  for (uint8_t j = 0; j < sizeof(GNSS_SET_BAUDRATE_CMD); j++)
  {
    GnssSerial.write(GNSS_SET_BAUDRATE_CMD[j]);
  }

  GnssSerial.flush();
  GnssSerial.end();
  delay(100);

#ifdef GNSS_USE_BAUDRATE_38400
  GnssSerial.begin(38400);
#else
  GnssSerial.begin(9600);
#endif
}

void setup()
{
  gnss_init();
  Serial.begin(115200);
}

void loop()
{
  if (GnssSerial.available())
  {
    uint8_t ch = GnssSerial.read();
    Serial.write(ch);
  }
}

