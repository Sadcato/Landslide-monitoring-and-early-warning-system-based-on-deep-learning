{
  /*全局路由监听组件 */
}
{
  /*导入 React、useEffect、useLocation路由 */
}
import React, { useEffect } from "react";
import { useLocation } from "react-router-dom";
{
  /*需要在所有路由变化都回到顶部，所以在一个顶层组件中监听路由的变化 */
}
const ScrollToTop: React.FC<{ children?: React.ReactNode }> = ({
  children,
}) => {
  const location = useLocation();
  useEffect(() => {
    window.scrollTo(0, 0);
  }, [location]); // 每当location发生变化时，都会执行scrollTo方法

  return children;
};
export default ScrollToTop;
