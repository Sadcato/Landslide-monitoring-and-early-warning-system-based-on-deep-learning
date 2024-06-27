import { proxy } from "valtio";

export const isOpenMenuState = proxy({
  // state
  fold: false,
  // action
  isOpen: () => {
    isOpenMenuState.fold = !isOpenMenuState.fold;
  },
});
