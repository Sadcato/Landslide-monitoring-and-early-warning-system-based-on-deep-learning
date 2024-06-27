import { useEffect } from "react";
import { useWebSocket } from "ahooks";
import { message } from "antd";
import { useSnapshot } from "valtio";
import { chartStore } from "../store/charts";
import { wsStore } from "../store/ws";
import { baseUrlConfig } from "../config/baseUrl";

const connectionStatusMap = {
  0: "正在连接",
  1: "已连接",
  2: "正在关闭",
  3: "已关闭",
};

const useWebSocketHandler = () => {
  const wsSnapshot = useSnapshot(wsStore);
  const { readyState, sendMessage, latestMessage, disconnect, connect } =
    useWebSocket(`${baseUrlConfig.webSocketUrl}`, {
      reconnectLimit: 0, // 禁止自动重连
      reconnectInterval: 0, // 禁止自动重连
    });

  useEffect(() => {
    const connectionStatus = connectionStatusMap[readyState];
    console.log(`WebSocket connection status: ${connectionStatus}`);
    if (connectionStatus === "已连接") {
      message.success(`WebSocket ${connectionStatus}`, 3);
    }
    if (connectionStatus === "已关闭") {
      message.warning(`WebSocket ${connectionStatus}`, 3);
    }
  }, [readyState]);

  useEffect(() => {
    if (readyState === 1 && latestMessage) {
      try {
        const parsedMessage = JSON.parse(latestMessage.data);
        console.log(latestMessage.data);
        const data = parsedMessage.risk_status;

        if (data.type === "ping") {
          sendMessage(JSON.stringify({ type: "pong" }));
          console.log("Received ping, sent pong.");
        }

        if (Array.isArray(data)) {
          chartStore.chartData = data.map((item) => ({
            x: item.x,
            y: item.y,
          }));
        }
      } catch (error) {
        console.error("Error parsing message:", error);
      }
    }
  }, [latestMessage, sendMessage, wsSnapshot.receive, readyState]);

  return {
    readyState,
    sendMessage,
    disconnect,
    connect,
  };
};

export default useWebSocketHandler;
