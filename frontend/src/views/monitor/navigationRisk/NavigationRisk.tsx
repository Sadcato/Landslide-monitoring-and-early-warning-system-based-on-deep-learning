{
  /*卫星信息与风险检测组件：风向、地面速度、地面航向角、风险 */
}
import { useCallback } from "react";
import { useSnapshot } from "valtio";
import { dataStore } from "../../../store/data";
import { weatherStore } from "../../../store/weather";

export default function NavigationRisk() {
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
          {CliDetail("风向", "东南风134°")}
          {/* {weatherSnapShot.weatherInfo ? (
            <>
              {CliDetail(
                "风向",
                weatherSnapShot.weatherInfo.lives[0].winddirection
              )}
            </>
          ) : (
            <>{CliDetail("风向", "获取中")}</>
          )} */}
        </div>
        <div className="flex flex-col items-center justify-center p-3 bg-white rounded-lg shadow-lg transition-all duration-300 ease-in-out transform-gpu hover:shadow-xl">
          {CliDetail("地面速度", 0)}
          {/* {dataSnapShot.speedOverGround ? (
            <>{CliDetail("地面速度", dataSnapShot.speedOverGround)}</>
          ) : (
            <>{CliDetail("地面速度", "获取中")}</>
          )} */}
        </div>
        <div className="flex flex-col items-center justify-center p-3 bg-white rounded-lg shadow-lg transition-all duration-300 ease-in-out transform-gpu hover:shadow-xl">
          {CliDetail("地面航向角", 0)}
          {/* {dataSnapShot.courseOverGround ? (
            <>{CliDetail("地面航向角", dataSnapShot.courseOverGround)}</>
          ) : (
            <>{CliDetail("地面航向角", "获取中")}</>
          )} */}
        </div>
        <div className="flex flex-col items-center justify-center p-3 bg-white rounded-lg shadow-lg transition-all duration-300 ease-in-out transform-gpu hover:shadow-xl">
          {CliDetail("风险等级", "暂无风险")}
          {/* {dataSnapShot.dangerClass ? (
            <>{CliDetail("风险等级", dataSnapShot.dangerClass)}</>
          ) : (
            <>{CliDetail("风险等级", "获取中")}</>
          )} */}
        </div>
      </div>
    </div>
  );
}
