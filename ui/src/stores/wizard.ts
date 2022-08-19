import uuid4 from "uuid4";
import { defineStore, acceptHMRUpdate } from "pinia";
import * as api from "printnanny-api-client";
import { ApiConfig, handleApiError } from "@/utils/api";
import { useEventStore } from "./events";
import { JSONCodec } from "nats.ws";
import type { Subscription, NatsConnection } from "nats.ws";
import { ConnectTestStatus, ConnectTestStep } from "@/types";
import moment from "moment";

const devicesApi = api.DevicesApiFactory(ApiConfig);

export const useWizardStore = defineStore({
  id: "wizard",
  // persist option provided by: https://github.com/prazdevs/pinia-plugin-persistedstate
  // persist: {
  //   storage: sessionStorage,
  // },
  state: () => ({
    pi: undefined as api.Pi | undefined,
    loading: false,
    downloadUrl: undefined as string | undefined,
    // connectTestSteps: [
    //   new ConnectTestStep(
    //     "Turn on Raspberry Pi",

    //     api.PiBootStatusType.BootStarted,
    //     "Connect Raspberry Pi to power source. Test will begin automatically.",
    //     api.PiBootStatusType.BootSuccess,
    //     api.PiBootStatusType.BootDegraded
    //   ),
    //   new ConnectTestStep(
    //     "Sync Settings",
    //     api.PiBootStatusType.SyncSettingsStarted,
    //     "Waiting for Raspberry Pi to finish powering up.",
    //     api.PiBootStatusType.SyncSettingsSuccess,
    //     api.PiBootStatusType.SyncSettingsError
    //   ),
    //   // new ConnectTestStep(
    //   //   "Test Remote Command"
    //   //   api.PiBootCommandType
    //   // ),
    //   new ConnectTestStep(
    //     "Test Camera",
    //     api.PiCamStatusType.CamStarted,
    //     "Waiting for Raspberry Pi settings sync to finish",

    //     api.PiCamStatusType.CamStartSuccess,
    //     api.PiCamStatusType.CamError
    //   ),
    connectTestSteps: [] as Array<ConnectTestStep>,
    natsClient: undefined as undefined | NatsConnection
  }),
  actions: {
    async connectNats(piId: number) {
      const eventStore = useEventStore();
      await this.loadPi(piId);
      const natsClient = await eventStore.connect();
      if (natsClient === undefined) {
        return;
      }
      this.$patch({ natsClient })
      return natsClient
      // subscribe to Pi events
      // const sub = natsClient.subscribe(`pi.${piId}.>`);
      // (async (sub: Subscription) => {
      //   console.log(`Subscribed to ${sub.getSubject()} events...`);
      //   for await (const msg of sub) {
      //     console.log("Received msg", msg)

      //     const event: api.PolymorphicPiEventRequest = jsonCodec.decode(
      //       msg.data
      //     );
      //     console.debug("PolymorphicPiEventRequest", event);
      //     this.handlePiEvent(event);
      //   }
      // })(sub);
    },
    handlePiEvent(event: api.PolymorphicPiEventRequest) {
      const connectTestSteps = this.connectTestSteps.map((step) => {
        if (step.pendingEventType == event.event_type) {
          step.start();
        }
        if (step.successEventType == event.event_type) {
          step.success();
        }
        if (step.errrorEventType == event.event_type) {
          step.error();
        }
        console.log("Returning step: ", step);
        return step;
      });
      this.$patch({ connectTestSteps });
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

    async initConnectTestSteps(pi: api.Pi) {
      const natsClient = await this.connectNats(pi.id);
      const statusCommand = {
        id: uuid4(),
        created_dt: moment.utc().toISOString(),
        subject_pattern: api.PiBootCommandSubjectPatternEnum.PiPiIdCommandBoot,
        event_type: api.PiBootCommandType.SystemctlShow,
        pi: pi.id
      } as api.PiBootCommandRequest;

      const settingsCommand = {
        id: uuid4(),
        created_dt: moment.utc().toISOString(),
        subject_pattern: api.PiBootCommandSubjectPatternEnum.PiPiIdCommandBoot,
        event_type: api.PiBootCommandType.SyncSettings,
        pi: pi.id
      } as api.PiBootCommandRequest;


      const camCommand = {
        id: uuid4(),
        created_dt: moment.utc().toISOString(),
        subject_pattern: api.PiCamCommandSubjectPatternEnum.PiPiIdCommandCam,
        event_type: api.PiCamCommandType.CamStart,
        pi: pi.id
      } as api.PiCamCommandRequest;

      const connectTestSteps = [
        new ConnectTestStep("Turn on Raspberry Pi", "Connect Raspberry Pi to power source. Test will begin automatically.", pi.id, statusCommand, natsClient),
        new ConnectTestStep("Sync PrintNanny Settings", "Your settings will be sync'd with PrintNanny Cloud.", pi.id, settingsCommand, natsClient),
        new ConnectTestStep("Test Camera", "Test web camera connection", pi.id, camCommand, natsClient)
      ]
      this.$patch({ connectTestSteps })
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
  },
});

if (import.meta.hot) {
  import.meta.hot.accept(acceptHMRUpdate(useWizardStore, import.meta.hot));
}
