import { defineStore, acceptHMRUpdate } from "pinia";
import * as api from "printnanny-api-client";
import type * as apiTypes from "printnanny-api-client";
import type { UiAlert } from "@/types";
import { ApiConfig } from "@/utils/api";

const alertSettingsApi = api.SettingsApiFactory(ApiConfig);

export const useAlertStore = defineStore({
  id: "alerts",
  state: () => ({
    alerts: [] as Array<UiAlert | UiAlert>,
    emailAlertSettings: undefined as apiTypes.EmailAlertSettings | undefined,
    loading: false,
  }),
  getters: {
    showEmpty: (state) => state.loading == false && state.alerts.length == 0,
    emailAlertSettingsFormReady: (state) => state.emailAlertSettings !== undefined,
  },
  actions: {
    async updateEmailAlertSettings(req: api.EmailAlertSettingsRequest) {
      console.log("updateEmailAlertSetting called", req)
      this.$patch({ loading: true })
      const alertsSettingsData = await alertSettingsApi.alertSettingsEmailUpdate(this.emailAlertSettings.id, req);
      if (alertsSettingsData) {
        this.$patch({ emailAlertSettings: alertsSettingsData.data, loading: false });
      }


    },
    async fetchSettings() {
      this.$patch({ loading: true });

      try {
        const alertsSettingsData = await alertSettingsApi.alertSettingsEmailList();
        console.log("Fetched AlertSettings data: ", alertsSettingsData.data);
        if (alertsSettingsData.data.results) {
          this.$patch({ emailAlertSettings: alertsSettingsData.data.results[0], loading: false });
        }
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
          this.$patch({ loading: false })
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
