import uuid4 from "uuid4";
import moment from "moment";

import * as api from "printnanny-api-client";
import { defineStore, acceptHMRUpdate } from "pinia";
import { ExclamationTriangleIcon } from "@heroicons/vue/24/outline";
import Janode from "janode";
import StreamingPlugin from "janode/plugins/streaming";

import type { UiAlert, AlertAction } from "@/types";
import { handleApiError } from "@/utils/api";
import type { WebrtcStream } from "printnanny-api-client";
import { useEventStore } from "./events";
import { useAlertStore } from "./alerts";
import { useAccountStore } from "./account";

const RTCPeerConnection = window.RTCPeerConnection.bind(window);

export const useWebrtcStore = defineStore({
  id: "webrtc",
  state: () => ({
    stream: undefined as undefined | api.WebrtcStream,
    connection: undefined as undefined | any,
    session: undefined as undefined | any,
    streamingHandle: undefined as undefined | any,
    pc: undefined as undefined | RTCPeerConnection,
    loading: true,
  }),

  actions: {
    async getStream(piId: number): Promise<undefined | api.WebrtcStream> {
      const stream = await this.getOrCreateCloudStream(piId);
      if (stream === undefined) {
        console.warn("Failed to initialize Webrtc stream");
        return;
      }
      this.$patch({ stream: stream });
      return stream;
    },

    async getOrCreateCloudStream(
      piId: number
    ): Promise<undefined | api.WebrtcStream> {
      const account = useAccountStore();
      const req = {
        active: true,
        config_type: api.JanusConfigType.Cloud,
      } as api.WebrtcStreamRequest;
      const res = await account.devicesApi
        .webrtcStreamUpdateOrCreate(piId, req)
        .catch(handleApiError);
      if (res) {
        this.$patch({ stream: res.data });
        return res.data;
      }
    },

    async stopAllStreams() {
      const videoEl = document.getElementById(
        "janus-video"
      ) as HTMLVideoElement;
      if (videoEl == null) {
        console.warn("Failed to get #janus-video element");
      }
      if (videoEl?.srcObject) {
        console.log("Stopping stream");
        (<MediaStream>videoEl.srcObject)
          .getTracks()
          .forEach((stream) => stream.stop());
        videoEl.srcObject = null;
      }
      if (this.stream !== undefined) {
        const eventsStore = useEventStore();
        const req = {
          id: uuid4(),
          created_dt: moment.utc().toISOString(),
          subject_pattern: api.PiCamCommandSubjectPatternEnum.PiPiIdCommandCam,
          event_type: api.PiCamCommandType.CamStop,
          pi: this.stream.pi,
        } as api.PiCamCommandRequest;

        await eventsStore.publish_command(req);
      }
    },

    async closePC() {
      if (this.pc !== undefined) {
        console.log("stopping PeerConnection");
        this.pc.close();
        this.$patch({ pc: undefined });
      }
    },

    async trickle(event: any) {
      const { candidate } = event;
      if (candidate === undefined) {
        this.streamingHandle.trickleComplete().catch((e: any) => {
          console.error("trickleComplete error", e);
        });
      } else {
        this.streamingHandle.trickle(candidate).catch((e: any) => {
          console.error("trickle error", e);
        });
      }
    },

    async setVideoElement(mediaStream: any) {
      if (!mediaStream) {
        return;
      }
      const videoEl = document.getElementById(
        "janus-video"
      ) as HTMLVideoElement;
      if (videoEl == null) {
        console.warn("Failed to get #janus-video element");
      }
      videoEl.srcObject = mediaStream;
      console.log("Setting videoEl mediastream", videoEl, mediaStream);
      videoEl?.play();
      this.$patch({ loading: false });
    },

    async doAnswer(offer: any) {
      const pc = new RTCPeerConnection({
        iceServers: [
          {
            urls: "stun:stun.l.google.com:19302",
          },
        ],
      });
      pc.onnegotiationneeded = (event) =>
        console.log("pc.onnegotiationneeded", event);
      pc.onicecandidate = (event) =>
        this.trickle({ candidate: event.candidate });
      pc.oniceconnectionstatechange = () => {
        console.log(
          "pc.oniceconnectionstatechange => " + pc.iceConnectionState
        );
        if (
          pc.iceConnectionState === "failed" ||
          pc.iceConnectionState === "closed"
        ) {
          console.warn("Stopping all streams and closing peer connection");
          this.stopAllStreams();
          this.closePC();
        }
      };
      pc.ontrack = (event) => {
        console.log("pc.ontrack", event);

        event.track.onunmute = (evt) => {
          console.log("track.onunmute", evt);
          /* TODO set srcObject in this callback */
        };
        event.track.onmute = (evt) => {
          console.log("track.onmute", evt);
        };
        event.track.onended = (evt) => {
          console.log("track.onended", evt);
        };

        const remoteStream = event.streams[0];
        this.setVideoElement(remoteStream);
      };

      this.$patch({ pc });
      await pc.setRemoteDescription(offer);
      console.log("set remote sdp OK");
      const answer = await pc.createAnswer();
      console.log("create answer OK");
      pc.setLocalDescription(answer);
      console.log("set local sdp OK");
      return answer;
    },

    async startStream(jsep: any) {
      const { status, id } = await this.streamingHandle.start({ jsep });
      console.log(`start ${id} response sent with status ${status}`);
    },

    async watchStream(stream: WebrtcStream, streamingHandle: any) {
      const watchdata = {
        id: stream.id,
        pin: stream.stream_pin,
        media: stream.info["data"]["info"]["media"],
      };
      console.log("Sending watchdata", watchdata);
      const { jsep, _restart = false } = await streamingHandle.watch(watchdata);
      console.log(`Received offer`, jsep);

      const answer = await this.doAnswer(jsep);
      await this.startStream(answer);
    },

    async initWebrtcStream(stream: api.WebrtcStream) {
      const alertStore = useAlertStore();
      const connectOpts = {
        is_admin: false,
        address: {
          url: import.meta.env.VITE_PRINTNANNY_JANUS_CLOUD_WS_URL,
          token: stream.api_token,
        },
      };
      if (stream.is_admin) {
        connectOpts["is_admin"] = true;
      }

      const connection = await Janode.connect(connectOpts);
      this.$patch({ connection });
      const session = await connection.create();
      this.$patch({ session });
      console.log("Janus session established", session);

      session.once(Janode.EVENT.SESSION_DESTROYED, () => {
        console.log(`Janus session destroyed`, session);
      });

      const streamingHandle = await session.attach(StreamingPlugin);
      this.$patch({ streamingHandle });
      console.log(`Attached StreamingPlugin handle`, streamingHandle);
      streamingHandle.once(Janode.EVENT.HANDLE_DETACHED, () => {
        console.log(`${streamingHandle} manager handle detached`);
      });

      // Janode exports "EVENT" property with core events
      streamingHandle.on(Janode.EVENT.HANDLE_WEBRTCUP, (_data: any) =>
        console.log("webrtcup event")
      );
      streamingHandle.on(Janode.EVENT.HANDLE_MEDIA, (evtdata: any) =>
        console.log("media event", evtdata)
      );
      streamingHandle.on(Janode.EVENT.HANDLE_SLOWLINK, (evtdata: any) => {
        console.log("slowlink event", evtdata);
        const actions = [
          {
            color: "amber",
            text: "Refresh Page",
            onClick: () => {
              window.location.reload();
            },
          },
        ] as Array<AlertAction>;
        const alert = {
          message:
            "Connection to PrintNanny Cloud is slow. Video may appear choppy.",
          header: "Slow connection detected",
          icon: ExclamationTriangleIcon,
          actions: actions,
        } as UiAlert;
        alertStore.push(alert);
      });
      streamingHandle.on(Janode.EVENT.HANDLE_HANGUP, (evtdata: any) =>
        console.log("hangup event", evtdata)
      );
      streamingHandle.on(Janode.EVENT.HANDLE_DETACHED, (evtdata: any) =>
        console.log("detached event", evtdata)
      );

      connection.on(Janode.EVENT.CONNECTION_CLOSED, () => {
        console.log(`Connection with ${stream.ws_url} closed`);
      });

      connection.on(
        Janode.EVENT.CONNECTION_ERROR,
        ({ message }: { message: any }) => {
          console.log(`Connection with Janus error (${message})`);

          // TODO notify clients via alert

          // TODO reconnect
          // notify clients
        }
      );

      streamingHandle.on(
        StreamingPlugin.EVENT.STREAMING_STATUS,
        (evtdata: any) => {
          console.log(
            `${
              streamingHandle.name
            } streaming handle event status ${JSON.stringify(evtdata)}`
          );
        }
      );
      streamingHandle.on(Janode.EVENT.HANDLE_TRICKLE, (evtdata: any) =>
        console.log(
          `${streamingHandle.name} trickle event ${JSON.stringify(evtdata)}`
        )
      );

      await this.watchStream(stream, streamingHandle);
    },
  },
});

if (import.meta.hot) {
  import.meta.hot.accept(acceptHMRUpdate(useWebrtcStore, import.meta.hot));
}
