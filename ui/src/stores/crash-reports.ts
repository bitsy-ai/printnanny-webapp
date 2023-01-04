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
    showReport: false,
    viewReport: undefined as undefined | CrashReport
  }),
  getters: {
    showEmpty: (state) =>
      state.loading == false && Object.keys(state.crashReports).length == 0,
  },
  actions: {
    openReport(report: CrashReport) {
      this.$patch({ viewReport: report, showReport: true });

    },
    closeReport() {
      this.$patch({ showReport: false })
    },
    async fetchCrashReports(): Promise<Array<CrashReport> | undefined> {
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
