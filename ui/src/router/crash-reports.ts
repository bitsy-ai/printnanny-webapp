import type { RouteRecordRaw } from "vue-router";

import DashboardLayout from "@/layouts/DashboardLayout.vue";
import PageTitle from "@/components/nav/PageTitle.vue";
import CrashReportList from "@/components/devices/CrashReportList.vue";
import DeviceTopRight from "@/components/devices/DeviceTopRight.vue";

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
          default: CrashReportList,
          TopRight: DeviceTopRight,
          TopBar: PageTitle,
        },
        meta: { title: "Crash Reports", requiresAuth: true },
      },
    ],
  },
] as Array<RouteRecordRaw>;
