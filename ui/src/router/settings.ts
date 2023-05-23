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
        meta: { title: "Manage Subscription" },
      },
      {
        path: "notifications/",
        name: "alertSettings",
        component: SettingsView,
        meta: { title: "Notification Settings" },
      },
      {
        path: "network/",
        name: "networkSettings",
        component: SettingsView,
        meta: { title: "Network" },
      },
      {
        path: "workspace/",
        name: "workspaceSettings",
        component: SettingsView,
        meta: { title: "Workspace & Team Members" },
      },
    ],
  },
] as Array<RouteRecordRaw>;
