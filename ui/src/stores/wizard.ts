import uuid4 from "uuid4";
import { defineStore, acceptHMRUpdate } from "pinia";
import * as api from "printnanny-api-client";
import { ApiConfig, handleApiError } from "@/utils/api";
import { useEventStore } from "./events";
import type { NatsConnection } from "nats.ws";
import { ConnectTestStep } from "@/types";
import moment from "moment";
import type { Pi } from "printnanny-api-client";

const devicesApi = api.DevicesApiFactory(ApiConfig);

export const useWizardStore = defineStore({
  id: "wizard",
  state: () => ({
    pi: undefined as api.Pi | undefined,
    loading: false,
    downloadUrl: undefined as string | undefined,
    connectTestSteps: [] as Array<ConnectTestStep>,
    natsClient: undefined as undefined | NatsConnection,
  }),
  actions: {
    async connectNats(piId: number) {
      const eventStore = useEventStore();
      await this.loadPi(piId);
      const natsClient = await eventStore.connect();
      if (natsClient === undefined) {
        return;
      }
      this.$patch({ natsClient });
      return natsClient;
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

    async initConnectTestSteps() {
      if (this.pi === undefined) {
        return;
      }
      const pi = this.pi;
      const natsClient = await this.connectNats(pi.id);
      if (natsClient == undefined) {
        return;
      }
      const statusCommand = {
        id: uuid4(),
        created_dt: moment.utc().toISOString(),
        subject_pattern: api.PiBootCommandSubjectPatternEnum.PiPiIdCommandBoot,
        event_type: api.PiBootCommandType.SystemctlShow,
        pi: pi.id,
      } as api.PiBootCommandRequest;

      const settingsCommand = {
        id: uuid4(),
        created_dt: moment.utc().toISOString(),
        subject_pattern: api.PiBootCommandSubjectPatternEnum.PiPiIdCommandBoot,
        event_type: api.PiBootCommandType.SyncSettings,
        pi: pi.id,
      } as api.PiBootCommandRequest;

      const camCommand = {
        id: uuid4(),
        created_dt: moment.utc().toISOString(),
        subject_pattern: api.PiCamCommandSubjectPatternEnum.PiPiIdCommandCam,
        event_type: api.PiCamCommandType.CamStart,
        pi: pi.id,
      } as api.PiCamCommandRequest;

      const connectTestSteps = [
        new ConnectTestStep(
          "Turn on Raspberry Pi",
          "Connect Raspberry Pi to power source. Test will begin automatically.",
          pi.id,
          statusCommand,
          natsClient
        ),
        new ConnectTestStep(
          "Sync PrintNanny Settings",
          "Your settings will be sync'd with PrintNanny Cloud.",
          pi.id,
          settingsCommand,
          natsClient
        ),
        new ConnectTestStep(
          "Turn on Camera",
          "Test web camera connection.",
          pi.id,
          camCommand,
          natsClient
        ),
      ];
      this.$patch({ connectTestSteps });
      return connectTestSteps;
    },
    async downloadLicenseZip(piId: number) {
      this.$patch({ loading: true });
      // responseType: "arraybuffer" is needed to correctly serialize application/zip data
      const res = await devicesApi.pisLicenseZipRetrieve(piId, {
        responseType: "arraybuffer",
      });

      if (res.data) {
        // const blob = new Blob([res.data], {
        //   type: res.headers["content-type"],
        // });
        // const pi = await this.loadPi(piId);
        // const link = document.createElement("a");
        // link.href = URL.createObjectURL(blob);
        // link.download = `PrintNanny-${pi?.hostname}.zip`;
        // link.click();
        // URL.revokeObjectURL(link.href);

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

    async finishSetup(piId: number) {
      const req = { setup_finished: true } as api.PatchedPiRequest;
      const res = await devicesApi
        .pisPartialUpdate(piId, req)
        .catch(handleApiError);
      if (res) {
        this.$patch({ pi: res.data });
      }
    },
  },
});

if (import.meta.hot) {
  import.meta.hot.accept(acceptHMRUpdate(useWizardStore, import.meta.hot));
}
