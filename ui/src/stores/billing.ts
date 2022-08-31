import { defineStore, acceptHMRUpdate } from "pinia";
import * as api from "printnanny-api-client";
import { ApiConfig, handleApiError } from "@/utils/api";
const billingApi = api.BillingApiFactory(ApiConfig);

export const useBillingStore = defineStore({
  id: "billing",
  state: () => ({
    summary: undefined as api.BillingSummary | undefined,
    products: [] as Array<api.BillingProduct>,
    loading: false,
    stripeCheckoutSessionUrl: undefined as undefined | string

  }),
  getters: {
    billingFormReady: (state) => state.summary !== undefined,
    getProductByName: (state) => {
      return (name: string) => state.products.find((product) => product.name == name)
    },
  },
  actions: {
    async fetchCheckoutSession(stripePriceLookupKey) {
      this.$patch({ loading: true });
      const req = {
        stripe_price_lookup_key: stripePriceLookupKey
      } as api.BillingCheckoutSession
      const res = await billingApi.billingCheckoutCreate(req).catch(handleApiError);
      if (res) {
        this.$patch({ loading: false, stripeCheckoutSessionUrl: res.data.url });
        console.log(`Redirecting to ${res.data.url}`);
        window.location = res.data.url;

      }

    },
    async fetchProducts() {
      const res = billingApi.billingProductsList();
      console.log("Fetched products", res.data)
      if (res.data) {
        this.$patch({ products: res.data })
      }
    },
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
