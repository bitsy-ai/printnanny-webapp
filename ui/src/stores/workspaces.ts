import { defineStore, acceptHMRUpdate } from "pinia";
import { useAccountStore } from "./account";
import type * as api from "printnanny-api-client";

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
  },
});

if (import.meta.hot) {
  import.meta.hot.accept(acceptHMRUpdate(useWorkspaceStore, import.meta.hot));
}
