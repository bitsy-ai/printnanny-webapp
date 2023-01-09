import { ref, h } from "vue";
import { defineStore, acceptHMRUpdate } from "pinia";
import type * as api from "printnanny-api-client";
import type { Pi } from "printnanny-api-client";
import { handleApiError } from "@/utils/api";
import { useAccountStore } from "./account";
import type { TableActionLink } from "@/types";
import { ExternalLinkIcon, TrashIcon } from "@heroicons/vue/solid";

export function buildDeviceActions(
  pi: Pi,
  index: number
): Array<Array<TableActionLink>> {
  const externalLinks = [
    {
      href: pi.urls.mission_control,
      name: "PrintNanny OS",
      icon: ExternalLinkIcon,
    },
    {
      href: pi.urls.octoprint,
      name: "OctoPrint",
      icon: ExternalLinkIcon,
    },
    {
      href: pi.urls.syncthing,
      name: "Syncthing",
      icon: ExternalLinkIcon,
    },
    {
      href: pi.urls.swupdate,
      name: "Software Update",
      icon: ExternalLinkIcon,
    },
  ];

  const footerActions = [
    {
      name: "Delete",
      routerLink: {
        name: "device-delete",
        params: { id: pi.id },
        query: { hostname: pi.hostname },
      },
      icon: TrashIcon,
    },
  ];

  // const favoriteAction = defineComponent({
  //   extends: defineComponent({ ...DeviceFavoriteMenuItem }), data: () => ({ pi: pi, index: index })
  // });

  // const favoriteAction = DeviceFavoriteMenuItem.setup({ pi, index })

  return [externalLinks, footerActions];
}

export const useDeviceStore = defineStore({
  id: "devices",
  state: () => ({
    networkSettings: undefined as undefined | api.NetworkSettings,
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
    async fetchNetworkSettings(): Promise<undefined | api.NetworkSettings> {
      this.$patch({ loading: true });
      const accountStore = useAccountStore();

      const res = await accountStore.devicesApi
        .networkSettingsRetrieve()
        .catch(handleApiError);
      console.debug("networkSettingsList response", res);
      const networkSettings = res?.data;
      this.$patch({
        loading: false,
        networkSettings: networkSettings,
      });
      return networkSettings;
    },
    async saveNetworkSettings(
      request: api.PatchedNetworkSettingsRequest
    ): Promise<undefined | api.NetworkSettings> {
      const accountStore = useAccountStore();
      if (this.networkSettings) {
        const res = await accountStore.devicesApi.networkSettingsPartialUpdate(
          this.networkSettings.id,
          request
        );
        const networkSettings = res?.data;
        return networkSettings;
      }
    },
  },
});

if (import.meta.hot) {
  import.meta.hot.accept(acceptHMRUpdate(useDeviceStore, import.meta.hot));
}
