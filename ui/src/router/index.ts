import { createRouter, createWebHistory } from "vue-router";
import HomeView from "@/views/HomeView.vue";
import DashboardView from "@/views/DashboardView.vue";
import { useAccountStore } from "@/stores/account";

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,
    },
    {
      path: "/devices/",
      name: "devices",
      component: DashboardView,
    },
    {
      path: "/login/",
      name: "login",
      component: () => import("@/views/LoginView.vue"),
    },
    // clear account store data and direct to home
    {
      path: "/logout/",
      name: "logout",
      redirect: { name: "home" },
      beforeEnter: async (_to, _from) => {
        const account = useAccountStore();
        await account.logout();
      },
    },
    {
      path: "/about/",
      name: "about",
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import("@/views/AboutView.vue"),
    },
    // begin device routes
    {
      path: "/device/connect/",
      name: "device-connect",
      component: () => import("@/views/DeviceCreateView.vue"),
    },
    // end device routes

    // begin profile/settings/billings routers
    {
      path: "/settings/",
      name: "settings",
      component: () => import("@/views/SettingsView.vue"),
    },
    {
      path: "/settings/billing/",
      name: "billing",
      component: () => import("@/views/SettingsView.vue"),
    },
    {
      path: "/privacy/",
      name: "privacy",
      component: () => import("@/views/PrivacyView.vue"),
    },
    {
      path: "/terms/",
      name: "terms",
      component: () => import("@/views/TermsOfServiceView.vue"),
    },
    {
      path: "/notifications/settings/",
      name: "alertSettings",
      component: () => import("@/views/SettingsView.vue"),
    },
  ],
});

router.beforeEach(async (to, _from) => {
  const account = useAccountStore();
  await account.fetchUser();
  if (
    // make sure the user is authenticated
    !account.isAuthenticated &&
    // ❗️ Avoid an infinite redirect
    to.name !== "login" &&
    // ❗️ Login is not required for home view
    to.name !== "home"
  ) {
    // redirect the user to the login page
    return { name: "login" };
  }
});

export default router;
