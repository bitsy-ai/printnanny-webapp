import type { RouteRecordRaw } from "vue-router";

import VideoList from "@/components/video/VideoList.vue";
import DashboardLayout from "@/layouts/DashboardLayout.vue";
import PageTitle from "@/components/nav/PageTitle.vue";

export default [
  // DashboardLayout views
  // default: main content area
  // TopRight: action buttons in upper-right
  {
    path: "/videos",
    components: {
      default: DashboardLayout,
      TopBar: PageTitle,
    },
    children: [
      {
        path: "",
        name: "videos",
        components: {
          default: VideoList,
          TopBar: PageTitle,
        },
        meta: { title: "Manage Network" },
      },
    ],
  },
] as Array<RouteRecordRaw>;
