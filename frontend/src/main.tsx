{
  /*山体滑坡监控预警系统前端 */
}
{
  /*导入 React、ReactDOM、Route路由 */
}
import ReactDOM from "react-dom/client";
import { HashRouter, BrowserRouter } from "react-router-dom";
{
  /*导入 路由 组件*/
}
import Router from "./config/router";
{
  /*导入 滚动到顶部 组件*/
}
import ScrollToTop from "./components/ScrollToTop";

{
  /*
  获取根元素，并确保其为HTMLElement类型
  */
}
const rootElement = document.getElementById("root") as HTMLElement | null;
{
  /*定义 路由 类型*/
}
const mode = "hash";

if (rootElement) {
  ReactDOM.createRoot(rootElement).render(
    mode === "hash" ? (
      <HashRouter>
        <ScrollToTop>
          <Router />
        </ScrollToTop>
      </HashRouter>
    ) : (
      <BrowserRouter>
        <ScrollToTop>
          <Router />
        </ScrollToTop>
      </BrowserRouter>
    )
  );
} else {
  console.error("未能找到ID为'root'的元素！");
}
