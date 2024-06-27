{
  /*环境信息组件：经纬度、海拔、卫星数量 */
}
import { useCallback } from "react";
import { useSnapshot } from "valtio";
import { dataStore } from "../../../store/data";

export default function Environment() {
  {
    /*创建 状态 快照 */
  }
  const dataSnapShot = useSnapshot(dataStore);

  const EnvirDetail = useCallback(
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
          {dataSnapShot.longitude ? (
            <>{EnvirDetail("经度", dataSnapShot.longitude)}</>
          ) : (
            <>{EnvirDetail("经度", "获取中")}</>
          )}
        </div>
        <div className="flex flex-col items-center justify-center p-3 bg-white rounded-lg shadow-lg transition-all duration-300 ease-in-out transform-gpu hover:shadow-xl">
          {dataSnapShot.latitude ? (
            <>{EnvirDetail("纬度", dataSnapShot.latitude)}</>
          ) : (
            <>{EnvirDetail("纬度", "获取中")}</>
          )}
        </div>
        <div className="flex flex-col items-center justify-center p-3 bg-white rounded-lg shadow-lg transition-all duration-300 ease-in-out transform-gpu hover:shadow-xl">
          {dataSnapShot.altitude ? (
            <>{EnvirDetail("海拔", dataSnapShot.altitude)}</>
          ) : (
            <>{EnvirDetail("海拔", "获取中")}</>
          )}
        </div>
        <div className="flex flex-col items-center justify-center p-3 bg-white rounded-lg shadow-lg transition-all duration-300 ease-in-out transform-gpu hover:shadow-xl">
          {EnvirDetail("卫星数量", 12)}
          {/* {dataSnapShot.satelliteCount ? (
            <>{EnvirDetail("卫星数量", dataSnapShot.satelliteCount)}</>
          ) : (
            <>{EnvirDetail("卫星数量", "获取中")}</>
          )} */}
        </div>
      </div>
    </div>
  );
}
