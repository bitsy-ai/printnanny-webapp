import { defineStore, acceptHMRUpdate } from "pinia";
import * as api from "printnanny-api-client";
import { ApiConfig, handleApiError } from "@/utils/api";

const devicesApi = api.DevicesApiFactory(ApiConfig);

export const useWizardStore = defineStore({
  id: "wizard",
  state: () => ({
    pi: undefined as api.Pi | undefined,
    loading: false,
    downloadUrl: undefined as string | undefined,
  }),
  actions: {
    async loadPi(piId: number) {
      if (this.pi === undefined) {
        const res = await devicesApi.pisRetrieve(piId);
        console.log("loadPi response", res);
        this.$patch({ pi: res.data });
        return res.data;
      }
      return this.pi;
    },
    async downloadLicenseZip(piId: number) {
      this.$patch({ loading: true });

      const res = await devicesApi.pisLicenseZipRetrieve(piId);

      if (res.data) {
        const blob = new Blob([res.data], {
          type: res.headers["content-type"],
        });
        console.log("downloadLicenseZip response:", res);
        // try to initiate download as object blob

        const pi = await this.loadPi(piId);
        const link = document.createElement("a");
        link.href = URL.createObjectURL(blob);
        link.download = `PrintNanny-${pi?.hostname}.zip`;
        link.click();
        URL.revokeObjectURL(link.href);

        this.$patch({ loading: false, downloadUrl: res.config.url });
      }
    },
    async createPi(req: api.PiRequest) {
      // Wireguard TODO: allow user to specify fqdn
      this.$patch({ loading: true });
      const res = await devicesApi.pisCreate(req).catch(handleApiError);
      console.debug("pisCreate response", res);

      this.$patch({ loading: false, pi: res.data });
      return res.data;
    },
  },
});

if (import.meta.hot) {
  import.meta.hot.accept(acceptHMRUpdate(useWizardStore, import.meta.hot));
}
