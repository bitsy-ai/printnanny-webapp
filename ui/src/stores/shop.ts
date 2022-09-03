import { defineStore, acceptHMRUpdate } from "pinia";
import * as api from "printnanny-api-client";
import { ApiConfig, handleApiError } from "@/utils/api";

const shopApi = api.ShopApiFactory(ApiConfig);

export const useShopStore = defineStore({
  id: "shop",
  state: () => ({
    loading: false,
    products: [] as Array<api.Product>,
    order: undefined as undefined | api.Order,
  }),
  actions: {
    async fetchProducts() {
      const res = await shopApi.shopProductsList();
      console.debug("Fetched products", res.data);
      if (res.data) {
        this.$patch({ products: res.data.results });
        return res.data.results;
      }
    },
    async createCheckoutSession(email: string, products: Array<string>) {
      this.$patch({ loading: true });
      const req = {
        products: products,
        email: email,
      } as api.OrderCheckoutRequest;

      const res = await shopApi.shopOrdersCreate(req).catch(handleApiError);
      if (res) {
        this.$patch({ loading: false });
        console.debug(
          `Redirecting to ${res.data.stripe_checkout_redirect_url}`
        );
        window.location.href = res.data.stripe_checkout_redirect_url;
      }
    },
    async fetchCheckoutSession(sessionId: string) {
      this.$patch({ loading: true });

      const res = await shopApi
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