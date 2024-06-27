{
  /*导入 Outlet组件 插槽 */
}
import { Outlet } from "react-router-dom";
{
  /*导入 app.scss全局样式 和 index.css Tailwindcss */
}
import "./styles/app.css";
import "./styles/index.css";
{
  /*导入 菜单 组件 */
}
import Menu from "./views/menus/Menus";

import { useAutoFetchData } from "./api/api";

{
  /*示波器顶级组件 */
}
const App = () => {
  {
    /*请求接口 */
  }
  useAutoFetchData();
  return (
    <div className="relative box-border flex bg-[#f6f6f6]">
      {/*子路由组件插槽 */}
      <div className="sticky top-0 left-0">
        <Menu />
      </div>
      <Outlet />
    </div>
  );
};
export default App;
