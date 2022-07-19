import { createApp, markRaw } from "vue";
import { createPinia } from "pinia";
import router from "./router";
import piniaPluginPersistedstate from "pinia-plugin-persistedstate";

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

app.mount("#app");
