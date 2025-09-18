import { useSystemStore } from "@global/store";
import { LocalStorageKeys, Themes } from "@global/types";

import { storeToRefs } from "pinia";

export const useTheme = () => {
  const systemStore = useSystemStore();
  const { systemMetaInfo } = storeToRefs(systemStore);

  const setTheme = () => {
    const theme = localStorage.getItem(LocalStorageKeys.THEME) || systemMetaInfo.value.theme;

    document.body.setAttribute("components-mode", theme);

    theme === Themes.DARK
      ? document.documentElement.classList.add("theme-dark")
      : document.documentElement.classList.remove("theme-dark");
  };

  return { setTheme };
};
