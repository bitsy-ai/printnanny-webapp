import DashboardLayout from "@/layouts/DashboardLayout.vue";
import PageTitle from "@/components/nav/PageTitle.vue";

export default [
  {
    path: "/workspaces/",
    components: {
      default: DashboardLayout,
      TopBar: PageTitle,
    },
    children: [
      {
        path: "",
        name: "workspaceList",
        components: {
          default: () =>
            import("@/components/workspaces/WorkspaceListView.vue"),
          TopBar: () => import("@/components/nav/PageTitle.vue"),
          TopRight: () => import("@/components/workspaces/NewWorkspaceButton.vue")
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
];
