{
  /*路由组件 */
}
{
  /*导入 React */
}
import { Suspense, lazy } from "react";
{
  /*导入 ReactDOM、Route 路由 */
}
import { Route, Routes } from "react-router-dom";

{
  /*导入组件*/
}
{
  /*导入 导航栏 组件*/
}
import App from "../App";
{
  /*导入 预警 组件 */
}
import Forewarning from "../views/foreWarning/Forewarning";
{
  /*导入 监控 组件 */
}
const Monitor = lazy(() => import("../views/monitor/Monitor"));
{
  /*导入 设备管理 组件 */
}
const Device = lazy(() => import("../views/device/Device"));
{
  /*导入 NotFound 组件
  import Notfound from "../views/notFound/Notfound";*/
}
const Notfound = lazy(() => import("../views/notFound/Notfound"));

const Router = () => {
  return (
    <Routes>
      <Route path="/" element={<App />}>
        <Route path="/" element={<Forewarning />} />
        <Route
          path="/monitor"
          element={
            <Suspense>
              <Monitor />
            </Suspense>
          }
        />
        <Route
          path="/device"
          element={
            <Suspense>
              <Device />
            </Suspense>
          }
        />
        <Route
          path="*"
          element={
            <Suspense>
              <Notfound />
            </Suspense>
          }
        />
      </Route>
    </Routes>
  );
};

export default Router;
