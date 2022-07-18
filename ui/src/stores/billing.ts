import { defineStore, acceptHMRUpdate } from "pinia";
import * as api from "printnanny-api-client";
import { useAlertStore } from "./alerts";
import type { UiAlert, UiError } from "@/types";
import { useRouter } from "vue-router";

const apiConfig = new api.Configuration({
  basePath: window.location.origin,
  baseOptions: {
    xsrfCookieName: "csrftoken",
    xsrfHeaderName: "X-CSRFTOKEN",
    withCredentials: true,
  },
});
const billingApi = api.BillingApiFactory(apiConfig);

export const useBillingStore = defineStore({
  id: "billing",
  state: () => ({
    summary: undefined as api.BillingSummary | undefined
  }),
  getters: {
    billingFormReady: (state) => state.summary !== undefined,
  },
  actions: {
    async cancel() {
      const alerts = useAlertStore();
      const router = useRouter();
      if (this.summary == undefined) { return }
      try {
        const res = await billingApi.billingCancelCreate(
          parseInt(this.summary.subscription.id)
        );
        console.log(
          "Cancelled subscription, updated billing summary: ",
          res.data
        );
        const alert: UiAlert = {
          header: "Subscription was cancelled",
          message:
            "Sorry to see you go! Email support@printnanny.ai if you need any further assistance.",
        };
        alerts.push(alert);
        this.$patch({ summary: res.data });
        router.push({ name: "billing" });
      } catch (e: any) {
        if (e.isAxiosError) {
          const alerts = useAlertStore();
          let msg;
          if (
            e.response.data.non_field_errors &&
            e.response.data.non_field_errors.length > 0
          ) {
            msg = e.response.data.non_field_errors.join("\n");
          } else if (e.response.data.detail) {
            msg = e.response.data.detail;
          } else if (e.response.data.error) {
            msg = e.response.data.error;
          } else {
            msg = e.response.data;
          }
          const alert: UiError = {
            header: e.response.statusText,
            message: msg,
            error: e,
          };
          alerts.push(alert);
          console.error(e.response);
        } else {
          throw e;
        }
      }
    },
    async reactivate() {
      const alerts = useAlertStore();
      const router = useRouter();
      if (this.summary === undefined) {
        return
      } else {
        try {
          const res = await billingApi.billingReactivateCreate(
            this.summary.subscription.id
          );
          console.log(
            "Reactivated subscription, updated billing summary: ",
            res.data
          );
          const alert: UiAlert = {
            header: "Subscription reactivated",
            message:
              "Welcome back! Email support@printnanny.ai if you need any further assistance.",
          };
          alerts.push(alert);
          this.$patch({ summary: res.data });
          router.push({ name: "billing" });
        } catch (e: any) {
          if (e.isAxiosError) {
            const alerts = useAlertStore();
            let msg;
            if (
              e.response.data.non_field_errors &&
              e.response.data.non_field_errors.length > 0
            ) {
              msg = e.response.data.non_field_errors.join("\n");
            } else if (e.response.data.detail) {
              msg = e.response.data.detail;
            } else if (e.response.data.error) {
              msg = e.response.data.error;
            } else {
              msg = e.response.data;
            }
            const alert: UiError = {
              header: e.response.statusText,
              message: msg,
              error: e,
            };
            alerts.push(alert);
            console.error(e.response);
          } else {
            throw e;
          }
        }
      }
    },
    async fetch() {
      try {
        const res = await billingApi.billingSummaryRetrieve();
        console.log("Fetched billing summary: ", res.data);
        return this.$patch({ summary: res.data });
      } catch (e: any) {
        if (e.isAxiosError) {
          const alerts = useAlertStore();
          let msg;
          if (
            e.response.data.non_field_errors &&
            e.response.data.non_field_errors.length > 0
          ) {
            msg = e.response.data.non_field_errors.join("\n");
          } else if (e.response.data.detail) {
            msg = e.response.data.detail;
          } else if (e.response.data.error) {
            msg = e.response.data.error;
          } else {
            msg = e.response.data;
          }
          const alert: UiError = {
            header: e.response.statusText,
            message: msg,
            error: e,
          };
          alerts.push(alert);
          console.error(e.response);
        } else {
          throw e;
        }
      }
    },
  },
});

if (import.meta.hot) {
  import.meta.hot.accept(acceptHMRUpdate(useBillingStore, import.meta.hot));
}
