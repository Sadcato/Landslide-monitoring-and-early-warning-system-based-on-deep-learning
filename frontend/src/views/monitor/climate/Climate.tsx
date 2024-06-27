{
  /*气候信息组件：温度、湿度、土壤湿度、风力 */
}
import { useCallback } from "react";
import { useSnapshot } from "valtio";
import { dataStore } from "../../../store/data";
import { weatherStore } from "../../../store/weather";

export default function Climate() {
  {
    /*创建 状态 快照 */
  }
  const dataSnapShot = useSnapshot(dataStore);
  const weatherSnapShot = useSnapshot(weatherStore);

  const CliDetail = useCallback(
    (label, value) => (
      <div className="flex">
        <p className="mr-2">{label}:</p>
        <p>{value}</p>
      </div>
    ),
    []
  );
  return (
    <div className="w-full h-fit p-10 bg-white overflow-hidden">
      <div className="grid grid-cols-4 gap-4 text-black">
        <div className="flex flex-col items-center justify-center p-3 bg-white rounded-lg shadow-lg transition-all duration-300 ease-in-out transform-gpu hover:shadow-xl">
          {dataSnapShot.temperature ? (
            <>{CliDetail("温度", dataSnapShot.temperature)}</>
          ) : (
            <>{CliDetail("温度", "获取中")}</>
          )}
        </div>
        <div className="flex flex-col items-center justify-center p-3 bg-white rounded-lg shadow-lg transition-all duration-300 ease-in-out transform-gpu hover:shadow-xl">
          {dataSnapShot.humidity ? (
            <>{CliDetail("湿度", dataSnapShot.humidity)}</>
          ) : (
            <>{CliDetail("湿度", "获取中")}</>
          )}
        </div>
        <div className="flex flex-col items-center justify-center p-3 bg-white rounded-lg shadow-lg transition-all duration-300 ease-in-out transform-gpu hover:shadow-xl">
          {dataSnapShot.soilHumidity ? (
            <>{CliDetail("土壤湿度", dataSnapShot.soilHumidity)}</>
          ) : (
            <>{CliDetail("土壤湿度", "获取中")}</>
          )}
        </div>
        <div className="flex flex-col items-center justify-center p-3 bg-white rounded-lg shadow-lg transition-all duration-300 ease-in-out transform-gpu hover:shadow-xl">
          {CliDetail("风力", "3级")}
          {/* {weatherSnapShot.weatherInfo ? (
            <>
              {CliDetail(
                "风力",
                weatherSnapShot.weatherInfo.lives[0].windpower
              )}
            </>
          ) : (
            <>{CliDetail("风力", "获取中")}</>
          )} */}
        </div>
      </div>
    </div>
  );
}
