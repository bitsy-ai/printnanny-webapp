import type { RouteRecordRaw } from "vue-router";

import DashboardLayout from "@/layouts/DashboardLayout.vue";
import SwagView from "@/views/SwagView.vue";

export default [
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
] as Array<RouteRecordRaw>;
