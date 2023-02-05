import { defineStore, acceptHMRUpdate } from "pinia";
import type * as api from "printnanny-api-client";
import { handleApiError } from "@/utils/api";
import { useAccountStore } from "./account";

export const useShopStore = defineStore({
  id: "shop",
  state: () => ({
    loading: false,
    products: [] as Array<api.Product>,
    cloudPlans: [] as Array<api.Product>,
    order: undefined as undefined | api.Order,
  }),
  getters: {
    starterPlan: (state) => { state.cloudPlans.find((p) => p.sku === "cloud-starter-plan") },
    scalerPlan: (state) => { state.cloudPlans.find((p) => p.sku === "cloud-starter-plan") },
  },
  actions: {
    // older shop view
    getCloudPlanBySku(sku: string) {
      return this.cloudPlans.find(v => v.sku === sku)
    },
    async fetchProducts() {
      const account = useAccountStore();
      const res = await account.shopApi.shopProductsList();
      console.debug("Fetched products", res.data);
      if (res.data) {
        this.$patch({ products: res.data.results });
        return res.data.results;
      }
    },
    // newer pricing table
    async fetchCloudPlans() {
      const account = useAccountStore();
      const res = await account.shopApi.cloudPlansRetrieve();
      console.debug("Fetched cloud plans", res.data);
      if (res.data) {
        this.$patch({ cloudPlans: res.data.results });
        return res.data.results;
      }
    },
    async createCheckoutSession(email: string, products: Array<string>) {
      const account = useAccountStore();
      this.$patch({ loading: true });
      const req = {
        products: products,
        email: email,
      } as api.OrderCheckoutRequest;

      const res = await account.shopApi
        .shopOrdersCreate(req)
        .catch(handleApiError);
      if (res) {
        this.$patch({ loading: false });
        console.debug(`Got checkout data`, res.data);
        window.location.href = res.data.stripe_checkout_redirect_url;
      }
    },
    async fetchCheckoutSession(sessionId: string) {
      this.$patch({ loading: true });
      const account = useAccountStore();

      const res = await account.shopApi
        .shopCheckoutSuccessRetrieve(sessionId)
        .catch(handleApiError);

      if (res) {
        this.$patch({ loading: false, order: res.data });
        console.debug(res.data);
        return res.data;
      }
    },
  },
});

if (import.meta.hot) {
  import.meta.hot.accept(acceptHMRUpdate(useShopStore, import.meta.hot));
}
