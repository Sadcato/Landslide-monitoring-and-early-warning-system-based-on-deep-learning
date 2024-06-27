{
  /*菜单数据 */
}
import {
  MenuUnfoldOutlined,
  MenuFoldOutlined,
  WarningOutlined,
  FundOutlined,
  DeploymentUnitOutlined,
} from "@ant-design/icons";

// 定义图标映射
export const iconMapping: { [key: string]: React.ComponentType<any> } = {
  MenuUnfoldOutlined: MenuUnfoldOutlined,
  MenuFoldOutlined: MenuFoldOutlined,
  DeploymentUnitOutlined: DeploymentUnitOutlined,
  WarningOutlined: WarningOutlined,
  FundOutlined: FundOutlined,
};

// 定义菜单项的类型
export interface MenuLinkItem {
  id: number;
  label: string;
  icon: keyof typeof iconMapping; // 使用 iconMapping 的键作为类型
  url?: string;
}

// 定义菜单项数据
const menuLink: MenuLinkItem[] = [
  {
    id: 1,
    label: "预警",
    icon: "WarningOutlined",
    url: "/",
  },
  {
    id: 2,
    label: "监控",
    icon: "FundOutlined",
    url: "/monitor",
  },
  {
    id: 3,
    label: "设备管理",
    icon: "DeploymentUnitOutlined",
    url: "/device",
  },
];

export default menuLink;
