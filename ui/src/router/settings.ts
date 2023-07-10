import type { RouteRecordRaw } from "vue-router";

import DashboardLayout from "@/layouts/DashboardLayout.vue";
import SettingsView from "@/views/SettingsView.vue";

export default [
  {
    path: "/settings/",
    component: DashboardLayout,
    name: "settings",
    children: [
      {
        path: "billing/",
        name: "billing",
        component: SettingsView,
        meta: { title: "Manage Subscription", requiresAuth: true },
      },
      {
        path: "notifications/",
        name: "alertSettings",
        component: SettingsView,
        meta: { title: "Notification Settings", requiresAuth: true },
      },
      {
        path: "network/",
        name: "networkSettings",
        component: SettingsView,
        meta: { title: "Network", requiresAuth: true },
      },
    ],
  },
] as Array<RouteRecordRaw>;
