import * as api from "printnanny-api-client";
import type { StateTree } from "pinia";
import { defineStore, acceptHMRUpdate } from "pinia";
import Janode from 'janode';
import StreamingPlugin from 'janode/plugins/streaming';
import { ApiConfig, handleApiError } from "@/utils/api";


const { Logger } = Janode;
const devicesApi = api.DevicesApiFactory(ApiConfig);

export const useWebrtcStore = defineStore({
  id: "webrtc",
  state: () => ({
    streams: [] as Array<api.WebrtcStream>,
    connection: undefined as undefined | Janode.Connection
  }),

  actions: {
    async init(piId: number): Promise<undefined | api.WebrtcStream> {
      const stream = await this.getOrCreateCloudStream(piId);
      if (stream === undefined) {
        console.warn("Failed to initialize Webrtc stream");
        return
      }
      await this.initWebrtcStream(stream);
    },

    async getOrCreateCloudStream(piId: number): Promise<undefined | api.WebrtcStream> {
      const req = { active: true, config_type: api.JanusConfigType.Cloud } as api.WebrtcStreamRequest;
      const res = await devicesApi.webrtcStreamUpdateOrCreate(piId, req).catch(handleApiError);
      if (res) {
        this.$patch((state: StateTree) => {
          state.push(res.data)
          state.hasChanged = true;
        })
        return res.data
      }

    },

    async initWebrtcStream(stream: api.WebrtcStream) {

      let connectOpts = {
        is_admin: false,
        address: {
          url: stream.ws_url,
          token: stream.api_token
        }
      }
      if (stream.is_admin) {
        connectOpts["is_admin"] = true;
      }

      const connection = await Janode.connect(connectOpts);
      const session = await connection.create();
      Logger.info(`Session established ${session}`);

      session.once(Janode.EVENT.SESSION_DESTROYED, () => {
        Logger.info(`${session} session destryed`);
      });

      const streamingHandle = await session.attach(StreamingPlugin);
      Logger.info(`Attached StreamingPlugin handle ${streamingHandle}`);
      streamingHandle.once(Janode.EVENT.HANDLE_DETACHED, () => {
        Logger.info(`${streamingHandle} manager handle detached`);
      });


      // Janode exports "EVENT" property with core events
      streamingHandle.on(Janode.EVENT.HANDLE_WEBRTCUP, (_data: any) => Logger.info('webrtcup event'));
      streamingHandle.on(Janode.EVENT.HANDLE_MEDIA, (evtdata: any) => Logger.info('media event', evtdata));
      streamingHandle.on(Janode.EVENT.HANDLE_SLOWLINK, (evtdata: any) => Logger.info('slowlink event', evtdata));
      streamingHandle.on(Janode.EVENT.HANDLE_HANGUP, (evtdata: any) => Logger.info('hangup event', evtdata));
      streamingHandle.on(Janode.EVENT.HANDLE_DETACHED, (evtdata: any) => Logger.info('detached event', evtdata));

      connection.on(Janode.EVENT.CONNECTION_CLOSED, () => {
        Logger.info(`Connection with ${stream.ws_url} closed`);
      });

      connection.on(Janode.EVENT.CONNECTION_ERROR, ({ message }: { message: any }) => {
        Logger.info(`Connection with Janus error (${message})`);


        // TODO notify clients via alert

        // TODO reconnect
        // notify clients
      });

      streamingHandle.on(StreamingPlugin.EVENT.STREAMING_STATUS, (evtdata: any) => {
        Logger.info(`${streamingHandle.name} streaming handle event status ${JSON.stringify(evtdata)}`);
        // replyEvent(socket, evtdata.status, { id: evtdata.id });
      });

    }

  }
});

if (import.meta.hot) {
  import.meta.hot.accept(acceptHMRUpdate(useWebrtcStore, import.meta.hot));
}
