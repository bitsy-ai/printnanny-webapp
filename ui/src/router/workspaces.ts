import type { RouteRecordRaw } from "vue-router";

export default [
  {
    path: "/workspaces/",
    components: {
      default: () => import("@/layouts/DashboardLayout.vue"),
      TopBar: () => import("@/components/nav/PageTitle.vue"),
    },
    children: [
      {
        path: "",
        name: "workspaceList",
        components: {
          default: () =>
            import("@/components/workspaces/WorkspaceListView.vue"),
          TopBar: () => import("@/components/nav/PageTitle.vue"),
          TopRight: () =>
            import("@/components/workspaces/NewWorkspaceButton.vue"),
        },
        meta: { title: "Workspaces & Team Members" },
      },
      {
        path: "new/",
        name: "workspaceCreate",
        components: {
          default: () =>
            import("@/components/workspaces/WorkspaceCreateForm.vue"),
          TopBar: () => import("@/components/nav/PageTitle.vue"),
        },
        meta: { title: "Create a Shared Workspace" },
      },
      {
        path: "invite/:slug",
        name: "workspaceInvite",
        components: {
          default: () =>
            import("@/components/workspaces/WorkspaceInviteForm.vue"),
          TopBar: () => import("@/components/nav/PageTitle.vue"),
        },
        props: { default: true },
        meta: { title: "Invite Team Members" },
      },
    ],
  },
] as Array<RouteRecordRaw>;
