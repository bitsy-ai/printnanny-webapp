import { createRouter, createWebHistory } from "vue-router";
import HomeView from "@/views/HomeView.vue";
import DashboardLayout from "@/layouts/DashboardLayout.vue";
import { useAccountStore } from "@/stores/account";
import DeviceList from "@/components/devices/DeviceList.vue";
import DeviceTopRight from "@/components/devices/DeviceTopRight.vue";
import DeviceCreate from "@/components/devices/DeviceCreate.vue";
import DeviceDelete from "@/components/devices/DeviceDelete.vue";
import PiCreateWizard from "@/components/devices/PiCreateWizard.vue";
import PiCreateWizardV2 from "@/components/devices/PiCreateWizardV2.vue";

import SettingsView from "@/views/SettingsView.vue";
import SwagView from "@/views/SwagView.vue";

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,
    },
    {
      path: "/login/",
      name: "login",
      component: () => import("@/views/LoginView.vue"),
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
    // DashboardLayout views
    // default: main content area
    // TopRight: action buttons in upper-right
    {
      path: "/devices/",
      components: {
        default: DashboardLayout,
      },
      children: [
        {
          path: "",
          name: "devices",
          components: {
            default: DeviceList,
            TopRight: DeviceTopRight,
          },
          meta: { title: "Manage Network" },
        },
        {
          path: "connect/:step?/:piId?",
          name: "device-connect",
          components: {
            default: PiCreateWizardV2,
          },
          props: { default: true },
          meta: { title: "Connect New Device" },
        },
        {
          path: "delete/:id/",
          name: "device-delete",
          components: {
            default: DeviceDelete,
          },
          props: { default: true },
          meta: { title: "Delete Connection" },
        },
      ],
    },
    {
      path: "/settings/",
      component: DashboardLayout,
      children: [
        {
          path: "billing/",
          name: "billing",
          component: SettingsView,
          meta: { title: "Manage Subscription" },
        },
        {
          path: "notifications/",
          name: "alertSettings",
          component: SettingsView,
          meta: { title: "Configure Notifications" },
        },
      ],
    },
    {
      path: "/swag/",
      component: DashboardLayout,
      children: [
        {
          path: "",
          name: "swag",
          component: SwagView,
          meta: { title: "Founding Member Swag" },
        },
      ],
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
