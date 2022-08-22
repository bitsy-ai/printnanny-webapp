import * as api from "printnanny-api-client";
import { defineStore, acceptHMRUpdate } from "pinia";

import Janode from "janode";
import StreamingPlugin from "janode/plugins/streaming";

import { ApiConfig, handleApiError } from "@/utils/api";
import type { WebrtcStream } from "printnanny-api-client";

const devicesApi = api.DevicesApiFactory(ApiConfig);

export const useWebrtcStore = defineStore({
  id: "webrtc",
  state: () => ({
    stream: undefined as undefined | api.WebrtcStream,
    connection: undefined as undefined | any,
    session: undefined as undefined | any,
    streamingHandle: undefined as undefined | any,
    pc: undefined as undefined | RTCPeerConnection,
  }),

  actions: {
    async getStream(piId: number): Promise<undefined | api.WebrtcStream> {
      const stream = await this.getOrCreateCloudStream(piId);
      if (stream === undefined) {
        console.warn("Failed to initialize Webrtc stream");
        return;
      }
      const videoEl = document.getElementById(
        "janus-video"
      ) as HTMLVideoElement;
      this.$patch({ stream: stream });
      return stream;
    },

    async getOrCreateCloudStream(
      piId: number
    ): Promise<undefined | api.WebrtcStream> {
      const req = {
        active: true,
        config_type: api.JanusConfigType.Cloud,
      } as api.WebrtcStreamRequest;
      const res = await devicesApi
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
      if (videoEl?.srcObject) {
        console.log("Stopping stream");
        (<MediaStream>videoEl.srcObject)
          .getTracks()
          .forEach((stream) => stream.stop());
        videoEl.srcObject = null;
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
      const videoEl = document.getElementById(
        "janus-video"
      ) as HTMLVideoElement;
      videoEl.srcObject = mediaStream;
      videoEl?.play();
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
      console.log(`Received offer ${jsep}`);

      const answer = await this.doAnswer(jsep);
      await this.startStream(answer);
    },

    async initWebrtcStream(stream: api.WebrtcStream) {
      const connectOpts = {
        is_admin: false,
        address: {
          url: stream.ws_url,
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
      console.log(`Session established ${session}`);

      session.once(Janode.EVENT.SESSION_DESTROYED, () => {
        console.log(`${session} session destryed`);
      });

      const streamingHandle = await session.attach(StreamingPlugin);
      this.$patch({ streamingHandle });
      console.log(`Attached StreamingPlugin handle ${streamingHandle}`);
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
      streamingHandle.on(Janode.EVENT.HANDLE_SLOWLINK, (evtdata: any) =>
        console.log("slowlink event", evtdata)
      );
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
            `${streamingHandle.name
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
