import * as Vue from "vue";
import { createRouter, createWebHistory } from "vue-router";
import { useAccountStore } from "@/stores/account";
import { posthogPageview } from "@/utils/posthog";

import crashReportRoutes from "./crash-reports";
import deviceRoutes from "./devices";
import swagRoutes from "./swag";
import settingsRoutes from "./settings";
import homeRoutes from "./home";
import shopRoutes from "./shop";
import videoRoutes from "./videos";
import workspaceRoutes from "./workspaces";

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
    ...workspaceRoutes,
  ],
});

// set page title
const DEFAULT_TITLE =
  "PrintNanny: monitoring + workflow automation for 3D printers";
router.afterEach((to, from) => {
  // Use next tick to handle router history correctly
  // see: https://github.com/vuejs/vue-router/issues/914#issuecomment-384477609
  // ref: https://stackoverflow.com/questions/51639850/how-to-change-page-titles-when-using-vue-router
  Vue.nextTick(() => {
    document.title = (to.meta.title as string) || DEFAULT_TITLE;
  });
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
  if (to.meta.requiresAuth === true) {
    const account = useAccountStore();
    if (!account.isAuthenticated) {
      // attempt to refresh login using session cookie, enables django-loginas for debugging
      await account.fetchUser();
      if (!account.isAuthenticated) {
        // redirect the user to the login page
        return { name: "login" };
      }
    }
  }
});

export default router;
