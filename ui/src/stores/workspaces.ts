import { defineStore, acceptHMRUpdate } from "pinia";
import { useAccountStore } from "./account";
import type * as api from "printnanny-api-client";
import { handleApiError } from "@/utils/api";

import { success } from "./alerts";

export const useWorkspaceStore = defineStore({
  id: "workspaces",
  state: () => ({
    workspaces: [] as Array<api.Workspace>,
  }),
  actions: {
    async fetchWorkspaces(): Promise<Array<api.Workspace>> {
      const account = useAccountStore();
      const res = await account.workspaceApi.workspacesList();
      console.log("workspaceList", res);
      if (res && res.data && res.data.results) {
        this.$patch({ workspaces: res.data.results });
        return res.data.results;
      }
      return [];
    },

    async createWorkspace(name: string): Promise<undefined | api.Workspace> {
      const account = useAccountStore();
      const req = {
        name,
        is_active: "true",
        slug: name.match(/[a-zA-Z]|\d|-|_+/g)?.join(""),
      };
      const res = await account.workspaceApi
        .workspacesCreate(req)
        .catch(handleApiError);
      if (res) {
        console.log("Created workspace", res.data);
        return res.data;
      }
    },
    async inviteToWorkspace(
      email: string,
      workspace: api.Workspace
    ): Promise<undefined | api.WorkspaceInvite> {
      const account = useAccountStore();
      const req = { email, workspace: workspace.id } as api.WorkspaceInviteCreateRequest;
      const res = await account.workspaceApi
        .workspacesCreateInvite(req)
        .catch(handleApiError);
      if (res) {
        console.log("Sent invite", res.data);
        const invite = res.data as api.WorkspaceInvite;
        success(
          `Sent invitation to ${invite.invitee_identifier}`,
          `${invite.invitee_identifier} was invited to your shared workspace: ${workspace.name}`
        );
        return invite;
      }
    },
    async resendInvite(workspace_invite: number): Promise<undefined | api.WorkspaceInvite> {
      const account = useAccountStore();
      const req = { workspace_invite } as api.WorkspaceInviteRemindRequest;
      const res = await account.workspaceApi.workspacesRemindInvite(req).catch(handleApiError);
      if (res) {
        console.log("Send invite reminder", res.data);
        const invite = res.data as api.WorkspaceInvite;
        success(`Sent reminder to ${invite.invitee_identifier}`, "Let your team-mate know they should double-check their spam inbox if they're not receiving emails.")
        return invite;
      }
    }
  },
});

if (import.meta.hot) {
  import.meta.hot.accept(acceptHMRUpdate(useWorkspaceStore, import.meta.hot));
}
