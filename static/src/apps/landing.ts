import "vite/modulepreload-polyfill";

import { createApp } from "vue";
import { createPinia } from "pinia";

import Landing from "@/components/landing/Landing.vue";
import "@/index.css";
const app = createApp(Landing);

app.use(createPinia());

app.mount("#landing");
