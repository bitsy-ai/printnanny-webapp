// Add this at the beginning of your app entry.
import "vite/modulepreload-polyfill";
import { createApp, markRaw } from "vue";
import { createPinia } from "pinia";
import router from "./router";
import piniaPluginPersistedstate from "pinia-plugin-persistedstate";
import posthog from "posthog-js";

import App from "./App.vue";
import "./index.css";
const app = createApp(App);
app.use(router);
const pinia = createPinia();
// hydrate pinia from local storage
pinia.use(piniaPluginPersistedstate);
// attach router to pinia store, so navigation/history may be accessed from store actions
pinia.use(({ store }) => {
  store.$router = markRaw(router);
});
app.use(pinia);

// initialize posthog in production only
if (window.location.href.includes("printnanny.ai")) {
  console.log("Initializing Posthog");
  posthog.init(import.meta.env.VITE_POSTHOG_CLIENT_KEY, {
    api_host: import.meta.env.VITE_POSTHOG_API_URL,
  });
}

app.mount("#app");
