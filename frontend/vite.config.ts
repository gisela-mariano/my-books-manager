import { fileURLToPath, URL } from "node:url";

import vue from "@vitejs/plugin-vue";
import { defineConfig } from "vite";
import vueDevTools from "vite-plugin-vue-devtools";

// https://vite.dev/config/
export default defineConfig({
  plugins: [vue(), vueDevTools()],
  resolve: {
    alias: {
      "@": fileURLToPath(new URL("./src", import.meta.url)),
      "@modules": fileURLToPath(new URL("./src/modules", import.meta.url)),
      "@core": fileURLToPath(new URL("./src/core", import.meta.url)),
      "@common": fileURLToPath(new URL("./src/common", import.meta.url)),
      "@global": fileURLToPath(new URL("./src/global", import.meta.url)),
    },
  },
  css: {
    preprocessorOptions: {
      scss: {
        additionalData: `@use "@/common/sass/main.scss" as *;`,
      },
    },
  },
});
