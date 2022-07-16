import { defineStore, acceptHMRUpdate } from "pinia";
import * as api from "printnanny-api-client";
import type * as apiTypes from "printnanny-api-client";
import type { Alert } from "@/types";

const apiConfig = new api.Configuration({
  basePath: window.location.origin,
  baseOptions: {
    xsrfCookieName: "csrftoken",
    xsrfHeaderName: "X-CSRFTOKEN",
    withCredentials: true,
  },
});

const alertsApi = api.AlertsApiFactory(apiConfig);

export const useAlertStore = defineStore({
  id: "alerts",
  state: () => ({
    /** @type { Alert[] } */
    alerts: [],
    /** @type { apiTypes.AlertSettings } */
    settings: null,
    loading: false
  }),
  getters: {
    showEmpty: (state) => state.loading == false && state.alerts.length == 0
  },
  actions: {
    async fetchSettings() {
      this.$patch({ loading: true });
      try {
        const alertsSettingsData = await alertsApi.alertsSettingsList();
        console.log("Fetched AlertSettings data: ", alertsSettingsData.data);
        this.$patch({ settings: alertsSettingsData.data });
      }
      catch (e: any) {
        if (e.isAxiosError) {
          let msg;
          if (
            e.response.data.non_field_errors &&
            e.response.data.non_field_errors.length > 0
          ) {
            msg = e.response.data.non_field_errors.join("\n");
          } else if (e.response.data.detail) {
            msg = e.response.data.detail;
          } else {
            msg = e.response.data;
          }
          const alert: UiError = {
            header: e.response.statusText,
            message: msg,
            error: e,
          };
          this.alerts.push(alert);
          console.error(e.response);
        } else {
          throw e;
        }
      }
      this.$patch({ loading: false });
    },
    push(alert: Alert) {
      this.alerts.push(alert);
    },
    dismiss(alert: Alert) {
      this.$patch({ alerts: this.alerts.filter((a) => a !== alert) });
    },
  },
});

if (import.meta.hot) {
  import.meta.hot.accept(acceptHMRUpdate(useAlertStore, import.meta.hot));
}
