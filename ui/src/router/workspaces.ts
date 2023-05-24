import DashboardLayout from "@/layouts/DashboardLayout.vue";
import PageTitle from "@/components/nav/PageTitle.vue";

export default [
  {
    path: "/workspace/",
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
          TopBar: PageTitle,
        },
        meta: { title: "Workspace & Team Members" },
      },
      {
        path: "new/",
        name: "workspaceCreate",
        components: {
          default: () =>
            import("@/components/workspaces/WorkspaceCreateForm.vue"),
          TopBar: PageTitle,
        },
        meta: { title: "Create Shared Workspace" },
      },
      {
        path: "invite/",
        name: "workspaceInvite",
        components: {
          default: () =>
            import("@/components/workspaces/WorkspaceInviteForm.vue"),
          TopBar: PageTitle,
        },
        meta: { title: "Invite Team Member" },
      },
    ],
  },
];
