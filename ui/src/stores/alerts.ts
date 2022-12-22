import { defineStore, acceptHMRUpdate } from "pinia";
import * as api from "printnanny-api-client";
import { CheckIcon, ExclamationCircleIcon } from "@heroicons/vue/solid";

import type {
  EmailAlertSettings,
  EmailAlertSettingsRequest,
} from "printnanny-api-client";
import { ApiConfig, handleApiError } from "@/utils/api";
import type { UiAlert } from "@/types";

export const useAlertStore = defineStore({
  id: "alerts",
  state: () => ({
    alerts: [] as Array<UiAlert | UiAlert>,
    emailAlertSettings: undefined as EmailAlertSettings | undefined,
    loading: false,
  }),
  getters: {
    showEmpty: (state) => state.loading == false && state.alerts.length == 0,
    emailAlertSettingsFormReady: (state) =>
      state.emailAlertSettings !== undefined,
  },
  actions: {
    async updateEmailAlertSettings(req: EmailAlertSettingsRequest) {
      const alertSettingsApi = api.SettingsApiFactory(ApiConfig);

      console.log("updateEmailAlertSetting called", req);
      this.$patch({ loading: true });
      if (this.emailAlertSettings) {
        const alertsSettingsData = await alertSettingsApi
          .alertSettingsEmailUpdate(this.emailAlertSettings.id, req)
          .catch(handleApiError);
        if (alertsSettingsData) {
          this.$patch({
            emailAlertSettings: alertsSettingsData.data,
            loading: false,
          });
        }
      }
    },
    async fetchEmailAlertSettings(): Promise<EmailAlertSettings | undefined> {
      const alertSettingsApi = api.SettingsApiFactory(ApiConfig);

      this.$patch({ loading: true });
      const alertsSettingsData = await alertSettingsApi
        .alertSettingsEmailList()
        .catch(handleApiError);
      if (alertsSettingsData && alertsSettingsData.data.results) {
        const emailAlertSettings = alertsSettingsData.data.results[0];
        console.log("Setting emailAlertSettings", emailAlertSettings);
        this.$patch({
          emailAlertSettings: emailAlertSettings,
          loading: false,
        });
        return emailAlertSettings;
      }
    },
    push(uialert: UiAlert) {
      // show at most 1 alert message with the same header
      const alreadyShown = this.alerts.filter(
        (a) => a.header == uialert.header
      );
      if (alreadyShown.length === 0) {
        this.alerts.push(uialert);
      }
    },
  },
});

export function success(header: string, message: string) {
  const store = useAlertStore();
  const alert = {
    header,
    message,
    icon: CheckIcon,
    iconClass: "text-emerald-500",
    actions: [],
  };
  store.push(alert);
}

export function warning(header: string, message: string) {
  const store = useAlertStore();
  const alert = {
    header,
    message,
    icon: ExclamationCircleIcon,
    iconClass: "text-amber-500",
    actions: [],
  };
  store.push(alert);
}

export function error(header: string, message: string) {
  const store = useAlertStore();
  const alert = {
    header,
    message,
    icon: ExclamationCircleIcon,
    iconClass: "text-red-500",
    actions: [],
  };
  store.push(alert);
}

if (import.meta.hot) {
  import.meta.hot.accept(acceptHMRUpdate(useAlertStore, import.meta.hot));
}
