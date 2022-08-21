import DashboardLayout from "@/layouts/DashboardLayout.vue";
import SettingsView from "@/views/SettingsView.vue";

export default [
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

]