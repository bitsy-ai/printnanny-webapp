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
          default: () => import("@/components/workspaces/WorkspaceListView.vue"),
          TopBar: PageTitle,

        },
        meta: { title: "Workspace & Team Members" },
      },
      // {
      //   path: "workspace/invite/",
      //   name: "workspaceInvite",
      //   component: SettingsView,
      //   meta: { title: "Invite Team Member" },
      // }
    ]
  }
]