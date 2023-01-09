import uuid4 from "uuid4";
import { defineStore, acceptHMRUpdate } from "pinia";
import * as api from "printnanny-api-client";
import { handleApiError } from "@/utils/api";
import { useEventStore } from "./events";
import type { NatsConnection } from "nats.ws";
import { ConnectTestStep } from "@/types";
import moment from "moment";
import { useAccountStore } from "./account";

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
        const account = useAccountStore();
        const res = await account.devicesApi.pisRetrieve(piId);
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
      const account = useAccountStore();

      this.$patch({ loading: true });
      // responseType: "arraybuffer" is needed to correctly serialize application/zip data
      const res = await account.devicesApi.pisLicenseZipRetrieve(piId, {
        responseType: "arraybuffer",
      });

      if (res.data) {
        this.$patch({ loading: false, downloadUrl: res.config.url });
      }
    },
    async createPi(req: api.PiRequest) {
      this.$patch({ loading: true });
      const account = useAccountStore();

      const res = await account.devicesApi.pisCreate(req).catch(handleApiError);
      console.debug("pisCreate response", res);
      if (res) {
        this.$patch({ loading: false, pi: res.data });
        return res.data;
      }
    },

    async finishSetup(piId: number) {
      const req = { setup_finished: true } as api.PatchedPiRequest;
      const account = useAccountStore();

      const res = await account.devicesApi
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
