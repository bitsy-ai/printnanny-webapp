import { defineStore, acceptHMRUpdate } from "pinia";
import * as api from "printnanny-api-client";
import type * as apiTypes from "printnanny-api-client";
import { useAlertStore } from "./alerts";
import type { UiAlert } from "@/types";

const apiConfig = new api.Configuration({
  basePath: window.location.origin,
  baseOptions: {
    xsrfCookieName: "csrftoken",
    xsrfHeaderName: "X-CSRFTOKEN",
    withCredentials: true,
  },
});
const devicesApi = api.DevicesApiFactory(apiConfig);

export const useDeviceStore = defineStore({
  id: "devices",
  state: () => ({
    devices: [] as Array<apiTypes.Device>,
    loading: false,
  }),
  getters: {
    showEmpty: (state) => state.loading == false && state.devices.length == 0,
  },
  actions: {
    async create(hostname: string) {
      try {
        // Wireguard TODO: allow user to specify fqdn
        const req: apiTypes.DeviceRequest = {
          hostname,
          fqdn: `${hostname}.local`,
        };
        const res = devicesApi.devicesCreate(req);
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
          const alert: UiAlert = {
            header: e.response.statusText,
            message: msg,
            error: e,
            actions: []

          };
          alerts.push(alert);
          console.error(e.response);
        } else {
          throw e;
        }
      }
    },
    async fetch() {
      this.$patch({ loading: true });
      try {
        const res = await devicesApi.devicesList();
        console.log("Fetched devices: ", res.data.results);
        this.$patch({
          devices: res.data.results,
        });
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
          const alert: UiAlert = {
            header: e.response.statusText,
            message: msg,
            error: e,
            actions: []
          };
          alerts.push(alert);
          console.error(e.response);
        } else {
          throw e;
        }
      }
      this.$patch({ loading: false });
    },
  },
});

if (import.meta.hot) {
  import.meta.hot.accept(acceptHMRUpdate(useDeviceStore, import.meta.hot));
}
