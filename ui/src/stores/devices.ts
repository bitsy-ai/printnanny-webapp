import { defineStore, acceptHMRUpdate } from "pinia";
import * as api from "printnanny-api-client";
import { ApiConfig, handleApiError } from "@/utils/api";

const devicesApi = api.DevicesApiFactory(ApiConfig);
export const useDeviceStore = defineStore({
  id: "devices",
  state: () => ({
    devices: [] as Array<apiTypes.Device>,
    loading: false,
  }),
  getters: {
    favorites: (state) => state.devices.filter(d => d.favorite),
    showEmpty: (state) =>
      state.loading == false && Object.keys(state.devices).length == 0,
  },
  actions: {
    async delete(id: number) {
      const res = await devicesApi.devicesDestroy(id).catch(handleApiError);
      console.debug("devicesDestroy response: ", res);
    },
    async partialUpdate(
      id: number,
      index: number,
      request: api.PatchedDeviceRequest
    ) {
      this.$patch({ loading: true });
      const res = await devicesApi
        .devicesPartialUpdate(id, request)
        .catch(handleApiError);
      this.$patch({ loading: false });
      if (res?.data) {
        this.devices.splice(index, 1, res.data);
      }
      console.debug("devicesPartialUpdate response", res);
    },

    async create(hostname: string) {
      // Wireguard TODO: allow user to specify fqdn
      const req: apiTypes.DeviceRequest = {
        hostname,
        fqdn: `${hostname}.local`,
      };
      this.$patch({ loading: true });
      const res = await devicesApi.devicesCreate(req).catch(handleApiError);
      this.$patch({ loading: true });
      console.debug("devicesCreate response", res);
    },
    async fetch() {
      this.$patch({ loading: true });
      const res = await devicesApi.devicesList().catch(handleApiError);
      console.debug("devicesList response ", res);
      if (res?.data?.results) {
        this.$patch({
          loading: false,
          devices: res.data.results,
        });
      } else {
        this.$patch({ loading: false });
      }
    },
  },
});

if (import.meta.hot) {
  import.meta.hot.accept(acceptHMRUpdate(useDeviceStore, import.meta.hot));
}
