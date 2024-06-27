import json from "@rollup/plugin-json";

export default {
  // 其他配置...
  plugins: [
    json(), // 添加此行
    // 其他插件...
  ],
};
