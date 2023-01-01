import { defineStore, acceptHMRUpdate } from "pinia";
import type * as api from "printnanny-api-client";
import type { Pi } from "printnanny-api-client";
import { handleApiError } from "@/utils/api";
import { useAccountStore } from "./account";

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
      const accountStore = useAccountStore();
      const res = await accountStore.devicesApi
        .pisDestroy(id)
        .catch(handleApiError);
      console.debug("devicesDestroy response: ", res);
    },
    async partialUpdate(
      id: number,
      index: number,
      request: api.PatchedPiRequest
    ) {
      this.$patch({ loading: true });
      const accountStore = useAccountStore();

      const res = await accountStore.devicesApi
        .pisPartialUpdate(id, request)
        .catch(handleApiError);
      this.$patch({ loading: false });
      if (res?.data) {
        this.pis.splice(index, 1, res.data);
      }
      console.debug("piPartialUpdate response", res);
    },
    async fetchDevices(): Promise<Array<Pi> | undefined> {
      this.$patch({ loading: true });
      const accountStore = useAccountStore();
      const res = await accountStore.devicesApi.pisList().catch(handleApiError);
      console.debug("pisList response ", res);
      if (res?.data?.results) {
        this.$patch({
          loading: false,
          pis: res.data.results,
        });
        return res.data.results;
      } else {
        this.$patch({ loading: false });
      }
    },
  },
});

if (import.meta.hot) {
  import.meta.hot.accept(acceptHMRUpdate(useDeviceStore, import.meta.hot));
}
