import { defineStore, acceptHMRUpdate } from "pinia";
import * as api from "printnanny-api-client";
import { ApiConfig, handleApiError } from "@/utils/api"
import { useEventStore } from "./nats";
import type { ConnectTestStep } from "@/types";
import { JSONCodec } from "nats.ws";

const devicesApi = api.DevicesApiFactory(ApiConfig);

export const useWizardStore = defineStore({
  id: "wizard",
  state: () => ({
    pi: undefined as api.Pi | undefined,
    loading: false,
    downloadUrl: undefined as string | undefined,
    connectTestSteps: [] as Array<ConnectTestStep>
  }),
  actions: {

    async connectNats(piId: number) {
      const eventStore = useEventStore();
      const pi = await this.loadPi(piId);
      const natsClient = await eventStore.connect();
      if (natsClient === undefined) { return }
      // create a JSON codec/decoder
      const jsonCodec = JSONCodec<api.PolymorphicPiEventRequest>();
      // subscribe to Pi events
      const sub = natsClient.subscribe(`pi.${piId}`);
      (async (sub: Subscription) => {
        console.log(`Subscribed to ${sub.getSubject()} events...`);
        for await (const msg of sub) {
          const event: api.PolymorphicPiEventRequest = jsonCodec.decode(
            msg.data
          );
          console.log("Deserialized event", event);
          this.handlePiEvent(event);
        }
      })(sub)
    },
    handlePiEvent(event: api.PolymorphicPiEventRequest) {

    },
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
      // responseType: "arraybuffer" is needed to correctly serialize application/zip data
      const res = await devicesApi.pisLicenseZipRetrieve(piId, {
        responseType: "arraybuffer",
      });

      if (res.data) {
        const blob = new Blob([res.data], {
          type: res.headers["content-type"],
        });
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
      if (res) {
        this.$patch({ loading: false, pi: res.data });
        return res.data;
      }
    },

    startTest() {
      this.connectTestSteps[0].start(undefined);
    }
  },
});

if (import.meta.hot) {
  import.meta.hot.accept(acceptHMRUpdate(useWizardStore, import.meta.hot));
}
