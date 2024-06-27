import { proxy } from "valtio";

export const dataStore = proxy({
  // 海拔
  altitude: null,
  // 经度
  longitude: null,
  // 纬度
  latitude: null,
  // 温度
  temperature: null,
  // 湿度
  humidity: null,
  // 土壤湿度
  soilHumidity: null,
  // 危险等级
  dangerClass: null,
  // 地面速度
  speedOverGround: null,
  // 地面角度（航向角）
  courseOverGround: null,
  // 能获取的卫星数量
  satelliteCount: null,
});
