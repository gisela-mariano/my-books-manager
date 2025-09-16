import "@/assets/main.css"

import { createPinia } from "pinia"
import PrimeVue from "primevue/config"
import Skeleton from "primevue/skeleton"
import Toast from "primevue/toast"
import ToastService from "primevue/toastservice"
import Tooltip from "primevue/tooltip"
import { createApp } from "vue"

import App from "@/App.vue"
import router from "@/router"

const app = createApp(App)

app.use(createPinia())
app.use(router)
app.use(PrimeVue)
app.use(ToastService)

app.component("Toast", Toast)

app.directive("tooltip", Tooltip)
app.component("Skeleton", Skeleton)

app.mount("#app")
