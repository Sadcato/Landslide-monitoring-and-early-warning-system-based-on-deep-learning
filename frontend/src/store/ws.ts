{
  /*WebSocket的状态管理 */
}
import { proxy } from "valtio";

interface WsStore {
  receive: boolean;
  isDisconnect: boolean;
}

export const wsStore = proxy<WsStore>({
  receive: false,
  isDisconnect: false,
});
