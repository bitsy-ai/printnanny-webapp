import type { RouteRecordRaw } from "vue-router";

import DashboardLayout from "@/layouts/DashboardLayout.vue";
import PageTitle from "@/components/nav/PageTitle.vue";
import DeviceDelete from "@/components/devices/DeviceDelete.vue";
import DeviceList from "@/components/devices/DeviceList.vue";
import DeviceTopRight from "@/components/devices/DeviceTopRight.vue";
export default [
  // DashboardLayout views
  // default: main content area
  // TopRight: action buttons in upper-right
  {
    path: "/devices/",
    components: {
      default: DashboardLayout,
      TopBar: PageTitle,
    },
    children: [
      {
        path: "",
        name: "devices",
        components: {
          default: DeviceList,
          TopRight: DeviceTopRight,
          TopBar: PageTitle,
        },
        meta: { title: "Manage Network", requiresAuth: true },
      },
      {
        path: "delete/:id/",
        name: "device-delete",
        components: {
          default: DeviceDelete,
        },
        props: { default: true },
        meta: { title: "Delete Connection", requiresAuth: true },
      },
    ],
  },
] as Array<RouteRecordRaw>;
