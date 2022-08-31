import type { CheckoutProduct } from "@/types/checkout";
import { defineStore } from "pinia";

export const useCheckoutStore = defineStore({
    id: "store",
    persist: {
        storage: sessionStorage
    },
    state: () => ({
        product: undefined as undefined | CheckoutProduct

    }),
    actions: {
        checkout(product: CheckoutProduct) {
            this.$patch({ product: product });
            this.$router.push({
                name: "checkout",
                query: {
                    product: product
                }
            })
        }
    }
})