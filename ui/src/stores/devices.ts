import { defineStore, acceptHMRUpdate } from "pinia";
import * as api from "printnanny-api-client";
import type { Pi, WebrtcStream } from "printnanny-api-client";
import { ApiConfig, handleApiError } from "@/utils/api";

const devicesApi = api.DevicesApiFactory(ApiConfig);
export const useDeviceStore = defineStore({
  id: "devices",
  state: () => ({
    pis: [] as Array<Pi>,
    loading: false,
  }),
  getters: {
    favorites: (state) => state.pis.filter((d) => d.favorite),
    showEmpty: (state) =>
      state.loading == false && Object.keys(state.pis).length == 0,
  },
  actions: {
    async delete(id: number) {
      const res = await devicesApi.pisDestroy(id).catch(handleApiError);
      console.debug("devicesDestroy response: ", res);
    },
    async partialUpdate(
      id: number,
      index: number,
      request: api.PatchedPiRequest
    ) {
      this.$patch({ loading: true });
      const res = await devicesApi
        .pisPartialUpdate(id, request)
        .catch(handleApiError);
      this.$patch({ loading: false });
      if (res?.data) {
        this.pis.splice(index, 1, res.data);
      }
      console.debug("piPartialUpdate response", res);
    },

    async create(hostname: string) {
      // Wireguard TODO: allow user to specify fqdn
      const req: api.PiRequest = {
        hostname,
        fqdn: `${hostname}.local`,
      };
      this.$patch({ loading: true });
      const res = await devicesApi.pisCreate(req).catch(handleApiError);
      this.$patch({ loading: true });
      console.debug("pisCreate response", res);
    },
    async fetchDevices() {
      this.$patch({ loading: true });
      const res = await devicesApi.pisList().catch(handleApiError);
      console.debug("pisList response ", res);
      if (res?.data?.results) {
        this.$patch({
          loading: false,
          pis: res.data.results,
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
