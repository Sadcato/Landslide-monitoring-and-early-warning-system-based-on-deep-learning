{
  /*预警组件 */
}

{
  /*导入 GPS 组件 */
}
import GPS from "./GPS/GPS";
{
  /*导入 折线图 组件 */
}
import Chart from "./chart/Chart";

export default function Forewarning() {
  return (
    <div className="w-screen h-hit bg-white overflow-y-auto">
      {/*插入 GPS 组件 */}
      <div className="mt-10 px-8">
        <GPS />
      </div>
      {/*插入 折线图 组件 */}
      <Chart />
    </div>
  );
}
