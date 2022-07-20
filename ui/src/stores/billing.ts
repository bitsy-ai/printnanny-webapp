import { defineStore, acceptHMRUpdate } from "pinia";
import * as api from "printnanny-api-client";
import { useAlertStore } from "./alerts";
import type { UiAlert } from "@/types";
import { ApiConfig, handleApiError } from "@/utils/api";
const billingApi = api.BillingApiFactory(ApiConfig);

export const useBillingStore = defineStore({
  id: "billing",
  state: () => ({
    summary: undefined as api.BillingSummary | undefined,
  }),
  getters: {
    billingFormReady: (state) => state.summary !== undefined,
  },
  actions: {
    async fetch() {
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
