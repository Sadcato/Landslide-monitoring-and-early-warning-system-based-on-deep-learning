#include "init.hpp"

SoftwareSerial GnssSerial(GNSS_RXD, GNSS_TXD);
DHT DhtSensor(DHT_PIN, DHT11);

void gnss_init(bool use_baudrate_38400)
{
  const uint8_t cmd_gnss_use_38400[] = {0xF1, 0xD9, 0x06, 0x00, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x96, 0x00, 0x00, 0xA4, 0x5A};
  const uint8_t cmd_gnss_use_9600[] = {0xF1, 0xD9, 0x06, 0x00, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x80, 0x25, 0x00, 0x00, 0xB3, 0x07};
  const uint32_t baudrates[] = {115200, 57600, 38400, 19200, 9600};

  for (uint8_t i = 0; i < sizeof(baudrates) / sizeof(baudrates[0]); i++)
  {
    GnssSerial.begin(baudrates[i]);
    if (use_baudrate_38400)
    {
      for (uint8_t j = 0; j < sizeof(cmd_gnss_use_38400); j++)
      {
        GnssSerial.write(cmd_gnss_use_38400[j]);
      }
    }
    else
    {
      for (uint8_t j = 0; j < sizeof(cmd_gnss_use_9600); j++)
      {
        GnssSerial.write(cmd_gnss_use_9600[j]);
      }
    }

    GnssSerial.flush();
    GnssSerial.end();
    delay(10);
  }

  GnssSerial.begin(use_baudrate_38400 ? 38400 : 9600);
}

void serial_init()
{
  Serial.begin(MCU_BAUDRATE);
}

void sensor_init()
{
  pinMode(SOIL_PIN, INPUT);
  DhtSensor.begin();
}
