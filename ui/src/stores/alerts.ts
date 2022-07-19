import { defineStore, acceptHMRUpdate } from "pinia";
import * as api from "printnanny-api-client";
import type * as apiTypes from "printnanny-api-client";
import type { UiAlert } from "@/types";
import { ApiConfig } from "@/utils/api";
const alertSettingsApi = api.AlertSettingsApiFactory(ApiConfig);

export const useAlertStore = defineStore({
  id: "alerts",
  state: () => ({
    alerts: [] as Array<UiAlert | UiAlert>,
    settings: undefined as apiTypes.AlertSettings | undefined,
    loading: false,
  }),
  getters: {
    showEmpty: (state) => state.loading == false && state.alerts.length == 0,
    settingsFormReady: (state) => state.settings !== undefined,
  },
  actions: {
    async fetchSettings() {
      this.$patch({ loading: true });

      try {
        const alertsSettingsData = await alertSettingsApi.alertSettingsList();
        console.log("Fetched AlertSettings data: ", alertsSettingsData.data);
        this.$patch({ settings: alertsSettingsData.data });
      } catch (e: any) {
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
          const alert: UiAlert = {
            header: e.response.statusText,
            message: msg,
            error: e,
            actions: [],
          };
          this.alerts.push(alert);
          console.error(e.response);
        } else {
          throw e;
        }
      }
      this.$patch({ loading: false });
    },
    push(alert: UiAlert | UiAlert) {
      this.alerts.push(alert);
    },
  },
});

if (import.meta.hot) {
  import.meta.hot.accept(acceptHMRUpdate(useAlertStore, import.meta.hot));
}
