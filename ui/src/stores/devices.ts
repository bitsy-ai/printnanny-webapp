import { defineStore, acceptHMRUpdate } from "pinia";
import * as api from "printnanny-api-client";
import type * as apiTypes from "printnanny-api-client";
import { useAlertStore } from "./alerts";
import type { Device } from "@/types";

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
    /** @type { Device[] } */
    devices: [],
  }),
  actions: {
    async create(hostname) {
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
    async fetch() {
      try {
        const res = await devicesApi.devicesList();
        console.log("Fetched devices: ", res.data.results);
        return this.$patch({
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
  import.meta.hot.accept(acceptHMRUpdate(useDeviceStore, import.meta.hot));
}
