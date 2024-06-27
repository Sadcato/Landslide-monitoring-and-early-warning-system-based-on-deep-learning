{
  /*信息监控组件 */
}
{
  /*导入环境信息组件 */
}
import Environment from "./environment/Environment";
{
  /*导入 气候信息 组件 */
}
import Climate from "./climate/Climate";
{
  /*导入 卫星信息与风险检测 组件 */
}
import NavigationRisk from "./navigationRisk/NavigationRisk";

export default function Forewarning() {
  return (
    <div className="w-screen h-hit bg-white overflow-y-auto">
      {/*插入 环境信息 组件 */}
      <Environment />
      {/*插入 气候信息 组件 */}
      <Climate />
      {/*插入 卫星信息与风险检测 组件 */}
      <NavigationRisk />
    </div>
  );
}
