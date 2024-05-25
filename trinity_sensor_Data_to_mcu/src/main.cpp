#include <Arduino.h>

#include "init.hpp"
#include "gnss.hpp"

typedef struct
{
  char gnss_msg_gga[GNSS_SENTENCE_BUFFER_SIZE];
  char gnss_msg_rmc[GNSS_SENTENCE_BUFFER_SIZE];
  float dht_temp[10];
  float dht_humd[10];
  uint8_t soil_humd[10];
} mcu_state_t;

void send_data(mcu_state_t *state)
{
  // Send GNSS data
  Serial.println(state->gnss_msg_gga);
  Serial.println(state->gnss_msg_rmc);

  // Send DHT11 sensor data
  Serial.print("$TEMP,");
  for (int i = 0; i < 10; i++)
  {
    Serial.print(state->dht_temp[i], 1);
    if (i < 9)
    {
      Serial.print(",");
    }
  }
  Serial.println();

  Serial.print("$HUMIDITY,");
  for (int i = 0; i < 10; i++)
  {
    Serial.print(state->dht_humd[i], 1);
    if (i < 9)
    {
      Serial.print(",");
    }
  }
  Serial.println();

  // Send soil sensor data
  Serial.print("$SOILHUM,");
  for (int i = 0; i < 10; i++)
  {
    Serial.print(state->soil_humd[i], 1);
    if (i < 9)
    {
      Serial.print(",");
    }
  }
  Serial.println();
}

void setup()
{
  gnss_init(true);
  serial_init();
  sensor_init();
}

void loop()
{
  mcu_state_t state;

  // Get DHT11 sensor data
  for (uint8_t i = 0; i < sizeof(state.dht_temp) / sizeof(state.dht_temp[0]);)
  {
    float temp = DhtSensor.readTemperature();
    if (isnan(temp))
    {
      continue;
    }
    state.dht_temp[i++] = temp;
    delay(10);
  }
  for (uint8_t i = 0; i < sizeof(state.dht_humd) / sizeof(state.dht_humd[0]);)
  {
    float humd = DhtSensor.readHumidity();
    if (isnan(humd))
    {
      continue;
    }
    state.dht_humd[i++] = humd;
    delay(10);
  }

  // Get soil sensor data
  for (uint8_t i = 0; i < sizeof(state.soil_humd) / sizeof(state.soil_humd[0]); i++)
  {
    state.soil_humd[i] = analogRead(SOIL_PIN);
    delay(10);
  }

  // Get GNSS message
  while (!gnss_get_message(state.gnss_msg_gga, "GGA"))
  {
    ;
  }
  while (!gnss_get_message(state.gnss_msg_rmc, "RMC"))
  {
    ;
  }

  // Send final data
  send_data(&state);
}
