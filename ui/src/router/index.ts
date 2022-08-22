import { createRouter, createWebHistory } from "vue-router";
import { useAccountStore } from "@/stores/account";

import deviceRoutes from "./devices";
import swagRoutes from "./swag";
import settingsRoutes from "./settings";
import homeRoutes from "./home";

const router = createRouter({
  history: createWebHistory(),
  routes: [...homeRoutes, ...deviceRoutes, ...swagRoutes, ...settingsRoutes],
});

router.beforeEach(async (to, _from) => {
  const account = useAccountStore();
  await account.fetchUser();
  if (
    // make sure the user is authenticated
    !account.isAuthenticated &&
    // ❗️ Avoid an infinite redirect
    to.name !== "login" &&
    // ❗️ Login is not required for home view, terms, or privacy policy
    to.name !== "home" &&
    to.name !== "terms" &&
    to.name !== "privacy"
  ) {
    // redirect the user to the login page
    return { name: "login" };
  }
});

export default router;
