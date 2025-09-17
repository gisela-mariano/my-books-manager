import { createPinia } from "pinia";
import PrimeVue from "primevue/config";
import Skeleton from "primevue/skeleton";
import Toast from "primevue/toast";
import ToastService from "primevue/toastservice";
import Tooltip from "primevue/tooltip";
import { createApp } from "vue";

import App from "@/App.vue";
import router from "@/router";
import { i18n } from "@core/i18n";
import vCustomTooltip from "@global/directives/v-custom-tooltip";
import Aura from "@primeuix/themes/aura";

const app = createApp(App);

app.use(createPinia());
app.use(router);
app.use(PrimeVue, {
  theme: {
    preset: Aura,
    options: {
      prefix: "p",
      darkModeSelector: ".theme-dark",
    },
  },
});
app.use(ToastService);
app.use(i18n);

app.component("Toast", Toast);
app.component("Skeleton", Skeleton);

app.directive("tooltip", Tooltip);
app.directive("custom-tooltip", vCustomTooltip);

app.mount("#app");
