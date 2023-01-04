import { defineStore, acceptHMRUpdate } from "pinia";
import type * as api from "printnanny-api-client";
import type { CrashReport } from "printnanny-api-client";
import { handleApiError } from "@/utils/api";
import { useAccountStore } from "./account";

export const useCrashReportStore = defineStore({
  id: "crashReports",
  state: () => ({
    crashReports: [] as Array<CrashReport>,
    loading: false,
  }),
  getters: {
    showEmpty: (state) =>
      state.loading == false && Object.keys(state.crashReports).length == 0,
  },
  actions: {
    async delete(id: number) {
      const accountStore = useAccountStore();
      const res = await accountStore.devicesApi
        .pisDestroy(id)
        .catch(handleApiError);
      console.debug("devicesDestroy response: ", res);
    },
    async fetchCrashReports(): Promise<Array<Pi> | undefined> {
      this.$patch({ loading: true });
      const accountStore = useAccountStore();
      const res = await accountStore.crashReportsApi.crashReportsList().catch(handleApiError);
      console.debug("pisList response ", res);
      if (res?.data?.results) {
        this.$patch({
          loading: false,
          crashReports: res.data.results
        });
        return res.data.results;
      } else {
        this.$patch({ loading: false });
      }
    },
  },
});

if (import.meta.hot) {
  import.meta.hot.accept(acceptHMRUpdate(useCrashReportStore, import.meta.hot));
}
