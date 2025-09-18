import { SystemMetaInfo, Themes } from "@global/types";
import { defineStore } from "pinia";
import { ref, Ref } from "vue";

export const useSystemStore = defineStore("system", () => {
  const systemMetaInfo: Ref<SystemMetaInfo> = ref({
    theme: Themes.LIGHT,
    isDark: false,
  });

  const setTheme = (theme: Themes) => {
    systemMetaInfo.value.theme = theme;
    systemMetaInfo.value.isDark = theme === Themes.DARK;
  };

  return { systemMetaInfo, setTheme };
});
