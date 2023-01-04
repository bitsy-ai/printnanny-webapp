import type { RouteRecordRaw } from "vue-router";

import DashboardLayout from "@/layouts/DashboardLayout.vue";
import PageTitle from "@/components/nav/PageTitle.vue";
import DeviceDelete from "@/components/devices/DeviceDelete.vue";
import DeviceList from "@/components/devices/DeviceList.vue";
import DeviceTopRight from "@/components/devices/DeviceTopRight.vue";

import wizardRoutes from "./wizard";

export default [
  // DashboardLayout views
  // default: main content area
  // TopRight: action buttons in upper-right
  {
    path: "/crash-reports/",
    components: {
      default: DashboardLayout,
      TopBar: PageTitle,
    },
    children: [
      {
        path: "",
        name: "crash-reports",
        components: {
          default: DeviceList,
          TopRight: DeviceTopRight,
          TopBar: PageTitle,
        },
        meta: { title: "Crash Reports" },
      },
    ],
  },
] as Array<RouteRecordRaw>;
