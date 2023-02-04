import { createRouter, createWebHistory } from "vue-router";
import { useAccountStore } from "@/stores/account";
import posthog from "posthog-js";
import { posthogPageview } from "@/utils/posthog";

import crashReportRoutes from "./crash-reports";
import deviceRoutes from "./devices";
import swagRoutes from "./swag";
import settingsRoutes from "./settings";
import homeRoutes from "./home";
import shopRoutes from "./shop";
import videoRoutes from "./videos";

const router = createRouter({
  history: createWebHistory(),
  routes: [
    ...homeRoutes,
    ...crashReportRoutes,
    ...deviceRoutes,
    ...swagRoutes,
    ...settingsRoutes,
    ...shopRoutes,
    ...videoRoutes,
  ],
});

// capture posthog events
router.afterEach((_to, _from) => {
  if (
    !window.location.href.includes("127.0.0.1") &&
    !window.location.href.includes("localhost")
  ) {
    posthogPageview();
  }
});

router.beforeEach(async (to, _from) => {
  if (to.name == "logout") {
    return;
  }
  const account = useAccountStore();
  await account.fetchUser();
  if (
    // make sure the user is authenticated
    !account.isAuthenticated &&
    // ❗️ Avoid an infinite redirect
    to.name !== "login-confirm" &&
    to.name !== "login" &&
    to.name !== "reset-password" &&
    to.name !== "reset-password-confirm" &&
    to.name !== "account-confirm-email" &&
    to.name !== "account-verify-email" &&
    to.name !== "register" &&
    // ❗️ Login is not required for home view, terms, privacy policy, shop, pricing
    to.name !== "home" &&
    to.name !== "terms" &&
    to.name !== "privacy" &&
    to.name !== "shop-products-list" &&
    to.name !== "shop-founding-membership" &&
    to.name !== "shop-sdwire" &&
    to.name !== "shop-checkout" &&
    to.name !== "shop-checkout-success" &&
    to.name !== "pricing"
  ) {
    // redirect the user to the login page
    return { name: "login" };
  }
});

export default router;
