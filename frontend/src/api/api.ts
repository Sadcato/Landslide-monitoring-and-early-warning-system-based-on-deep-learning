import { useEffect } from "react";
import { dataStore } from "../store/data";
import { baseUrlConfig } from "../config/baseUrl";

const baseUrl = baseUrlConfig.baseUrl;

const createRequestHook = (url, key) => {
  return () => {
    useEffect(() => {
      console.log(`Connecting to ${url}`);
      const eventSource = new EventSource(url);

      const handleMessage = (event) => {
        const data = JSON.parse(event.data);
        dataStore[key] = data;
        console.log(`Received data for ${key}:`, data);
      };

      const handleError = (event) => {
        const es = event.target;
        if (es.readyState === EventSource.CLOSED) {
          dataStore[key] = null;
          console.log(`Connection to ${url} closed.`);
        } else {
          console.error(`Error in connection to ${url}:`, event);
        }
      };

      eventSource.addEventListener("message", handleMessage);
      eventSource.addEventListener("error", handleError);

      return () => {
        eventSource.removeEventListener("message", handleMessage);
        eventSource.removeEventListener("error", handleError);
        eventSource.close();
        console.log(`Disconnected from ${url}`);
      };
    }, [url]);
  };
};

// 海拔请求
export const useGetDataAltitude = createRequestHook(
  `${baseUrl}/api/gnss/altitude`,
  "altitude"
);
// 经度请求
export const useGetDataLongitude = createRequestHook(
  `${baseUrl}/api/gnss/longitude`,
  "longitude"
);
// 纬度请求
export const useGetDataLatitude = createRequestHook(
  `${baseUrl}/api/gnss/latitude`,
  "latitude"
);
// 温度请求
export const useGetDataTemperature = createRequestHook(
  `${baseUrl}/api/sensor/temperature`,
  "temperature"
);
// 湿度请求
export const useGetDataHumidity = createRequestHook(
  `${baseUrl}/api/sensor/humidity`,
  "humidity"
);
// 土壤湿度请求
export const useGetDataSoilHumidity = createRequestHook(
  `${baseUrl}/api/sensor/soil_humidity`,
  "soilHumidity"
);
// 危险等级请求
export const useGetDataDangerClass = createRequestHook(
  `${baseUrl}/api/risk`,
  "dangerClass"
);
// 地面速度请求
export const useGetDataSpeedOverGround = createRequestHook(
  `${baseUrl}/api/gnss/speed_over_ground`,
  "speedOverGround"
);
// 地面角度（航向角）请求
export const useGetDataCourseOverGround = createRequestHook(
  `${baseUrl}/api/gnss/course_over_ground`,
  "courseOverGround"
);
// 可获取到的卫星数量请求
export const useGetDataSatelliteCount = createRequestHook(
  `${baseUrl}/api/gnss/number_of_satellites`,
  "satelliteCount"
);

export const useAutoFetchData = () => {
  useGetDataAltitude();
  useGetDataLongitude();
  useGetDataLatitude();
  useGetDataTemperature();
  useGetDataHumidity();
  useGetDataSoilHumidity();
  useGetDataDangerClass();
  useGetDataSpeedOverGround();
  useGetDataCourseOverGround();
  useGetDataSatelliteCount();
  console.log("All data fetch hooks have been invoked.");
};
