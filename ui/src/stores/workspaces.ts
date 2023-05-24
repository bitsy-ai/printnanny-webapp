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
      const req = { name, is_active: "true", slug: name };
      const res = await account.workspaceApi
        .workspacesCreate(req)
        .catch(handleApiError);
      if (res) {
        return res.data;
      }
    },
  },
});

if (import.meta.hot) {
  import.meta.hot.accept(acceptHMRUpdate(useWorkspaceStore, import.meta.hot));
}
