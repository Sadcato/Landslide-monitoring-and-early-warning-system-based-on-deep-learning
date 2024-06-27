{
  /*菜单 组件 */
}

{
  /*导入React */
}
import React, { useState, useMemo, useCallback } from "react";
{
  /*导入第三方库 */
}
import { useNavigate } from "react-router-dom";
import { MenuFoldOutlined, MenuUnfoldOutlined } from "@ant-design/icons";
import { Affix, Button, Menu, Layout } from "antd";
{
  /*导入 全局 状态管理 */
}
import { useSnapshot } from "valtio";
import { isOpenMenuState } from "../../store/isOpenMenu";
{
  /*导入数据 */
}
import menuLink, { iconMapping } from "../../data/menuLink";

const { Sider } = Layout;

const Menus: React.FC = () => {
  const isOpenMenuSnap = useSnapshot(isOpenMenuState);

  {
    /*创建 菜单组件 固定状态 */
  }
  const [top] = useState<number>(0);
  {
    /*获取 useNavigate 钩子函数，用于路由跳转 */
  }
  const navigate = useNavigate();
  const handleNavigate = useCallback(
    (url: string) => {
      navigate(url);
    },
    [navigate]
  );

  const items = useMemo(
    () =>
      menuLink.map((item) => ({
        key: item.id,
        icon: React.createElement(iconMapping[item.icon]),
        label: item.label,
        onClick: () => handleNavigate(item.url),
      })),
    [handleNavigate]
  );

  return (
    <Affix offsetTop={top}>
      <div className="max-w-[200px] h-screen bg-white overflow-hidden">
        <div
          className={`flex flex-col justify-between h-full py-4 border-r border-gray-20 ${
            isOpenMenuSnap.fold ? "w-16" : ""
          }`}
        >
          <div>
            <Sider trigger={null} collapsible collapsed={isOpenMenuSnap.fold}>
              <div className="flex pl-5 mb-6 ">
                <span className="text-xl text-black font-bold">
                  {isOpenMenuSnap.fold ? "🦺" : "🦺山体滑坡预警"}
                </span>
              </div>
              <Menu
                defaultSelectedKeys={["1"]}
                mode="inline"
                inlineCollapsed={isOpenMenuSnap.fold}
                items={items}
                className={`px-2 ${isOpenMenuSnap.fold ? "w-16" : ""}`}
              />
            </Sider>
          </div>
          <div className="flex justify-end pr-2">
            <Button
              onClick={isOpenMenuSnap.isOpen}
              style={{ marginBottom: 16 }}
            >
              <div className="flex justify-center items-center text-sky-500">
                {isOpenMenuSnap.fold ? (
                  <MenuUnfoldOutlined />
                ) : (
                  <MenuFoldOutlined />
                )}
              </div>
            </Button>
          </div>
        </div>
      </div>
    </Affix>
  );
};
export default Menus;
