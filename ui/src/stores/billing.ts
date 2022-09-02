import { defineStore, acceptHMRUpdate } from "pinia";
import * as api from "printnanny-api-client";
import { ApiConfig, handleApiError } from "@/utils/api";
const billingApi = api.BillingApiFactory(ApiConfig);

export const useBillingStore = defineStore({
  id: "billing",
  state: () => ({
    summary: undefined as api.BillingSummary | undefined,
    loading: false,
  }),
  getters: {
    billingFormReady: (state) => state.summary !== undefined,
  },
  actions: {
    async fetchSummary() {
      const res = await billingApi
        .billingSummaryRetrieve()
        .catch(handleApiError);
      console.log("billingSummaryRetrieve response", res);
      if (res && res.data) {
        this.$patch({ summary: res.data });
      }
    },
  },
});

if (import.meta.hot) {
  import.meta.hot.accept(acceptHMRUpdate(useBillingStore, import.meta.hot));
}
