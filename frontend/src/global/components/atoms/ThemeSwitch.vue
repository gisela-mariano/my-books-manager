<template>
  <div class="theme-switch">
    <i
      v-tooltip.top="{
        value: tooltipMessage,
        class: 'default-tooltip',
      }"
      class="pi"
      :class="systemMetaInfo.theme === Themes.LIGHT ? 'pi-moon' : 'pi-sun'"
      @click="switchTheme"
    />
  </div>
</template>

<script setup lang="ts">
import { I18nKeys } from "@common/types";
import { useTheme } from "@global/composables";
import { useSystemStore } from "@global/store";
import { LocalStorageKeys, Themes } from "@global/types";
import { storeToRefs } from "pinia";
import { computed } from "vue";
import { useI18n } from "vue-i18n";

const systemStore = useSystemStore();
const { systemMetaInfo } = storeToRefs(systemStore);

const { t } = useI18n();
const { setTheme } = useTheme();

const tooltipMessage = computed(() =>
  systemMetaInfo.value.theme === Themes.LIGHT
    ? t(`${I18nKeys.GLOBAL}.components.themeSwitch.switchLabel.dark`)
    : t(`${I18nKeys.GLOBAL}.components.themeSwitch.switchLabel.light`),
);

const switchTheme = () => {
  const newTheme = systemMetaInfo.value.theme === Themes.LIGHT ? Themes.DARK : Themes.LIGHT;

  systemStore.setTheme(newTheme);
  localStorage.setItem(LocalStorageKeys.THEME, newTheme);

  setTheme();
};
</script>

<style scoped lang="scss">
.theme-switch {
  i {
    font-size: 1.5rem;
    cursor: pointer;
  }
}
</style>
