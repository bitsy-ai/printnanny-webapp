<script lang="ts" >
import Vue from "vue";
import { mapState, mapActions } from "vuex";
import * as api from "printnanny-api-client";
import adapter from "webrtc-adapter";
import Janus from "janus-gateway-js";

import {
  DEVICE_MODULE,
  DEVICE,
  GET_DEVICE,
  JANUS_STREAM,
  SETUP_JANUS_CLOUD,
  GET_JANUS_STREAM,
} from "@/store/devices";
import { EVENTS_MODULE, STREAM_START, STREAM_STOP } from "@/store/events";
import {
  JanusVideoStats,
  JanusStreamComponentData,
} from "@/models/janus.interfaces";

function initialData(): JanusStreamComponentData {
  return {
    loading: false,
    active: false,
    error: null,
    timer: null,
    videoStats: null,
  };
}

const JanusStream = Vue.extend({
  props: {
    configType: {
      type: String,
      required: true,
    },
    deviceId: {
      type: String,
      required: true,
    },
    offlineImage: {
      type: String,
      required: true,
    },
  },
  data: function () {
    return initialData();
  },
  computed: {
    ...mapState(DEVICE_MODULE, {
      device: DEVICE,
      janusStream: JANUS_STREAM,
    }),
    showVideo: function () {
      return this.loading === false && this.active === true;
    },
    videoStreamEl: function () {
      return `janus-stream-${this.configType}-${this.deviceId}`;
    },
  },
  async created() {
    // fetch device data
    if (this.deviceId) {
      await this.getDevice(this.deviceId);
    }
  },
  methods: {
    ...mapActions(DEVICE_MODULE, {
      getDevice: GET_DEVICE,
      setupJanusCloud: SETUP_JANUS_CLOUD,
      getJanusStream: GET_JANUS_STREAM,
    }),
    ...mapActions(EVENTS_MODULE, {
      streamStart: STREAM_START,
      streamStop: STREAM_STOP,
    }),
    async connectStream(janusStream: api.JanusStream) {
      const janus = new Janus.Client(janusStream.ws_url, {
        token: janusStream.auth.api_token,
        keepalive: "true",
      });

      console.log(
        "Browser details detected",
        adapter.browserDetails.browser,
        adapter.browserDetails.version
      );
      const connection = await janus.createConnection(this.videoStreamEl);
      this.connection = connection;
      console.log("Created janus connection", connection);

      try {
        const session = await connection.createSession();
        this.session = session;

        console.log("Created janus session", session);

        const plugin = await session.attachPlugin(Janus.StreamingPlugin.NAME);
        this.plugin = plugin;

        this.timer = setInterval(this.getVideoStats, 200);
        this.setupRemoteTrack(plugin, this.videoStreamEl);
        console.log("Plugin attached", plugin);
        plugin.on("message", (message: any, jesp: any) => {
          console.log("plugin.on message", message, jesp);
        });

        const streamInfo = await this.getOrCreateStreamMountpoint(plugin);
        console.log("got streamInfo", streamInfo);
      } catch (error) {
        return await this.handleError(error);
      }
    },
    async getVideoStats() {
      const _self = this;
      const peer = this.plugin.getPeerConnection();
      if (peer) {
        const stats = await peer.getStats();
        stats.forEach((stat: any) => {
          switch (stat.type) {
            case "inbound-rtp":
              _self.parseInboundRtpStat(stat);
              break;
            default:
              break;
          }
        });
      }
    },
    async handleError(error: any) {
      console.error(error);
      this.error = error;
      await this.stopMonitoring();
      this.loading = false;
    },
    async setupJanusStream(): Promise<
      api.JanusCloudStream | api.JanusEdgeStream
    > {
      switch (this.configType) {
        case api.JanusConfigType.Cloud:
          return await this.setupJanusCloud(this.deviceId);
        case api.JanusConfigType.Edge:
          return await this.getJanusStream({
            device: this.deviceId,
            configType: this.configType,
          });
      }
    },
    async startMonitoring() {
      this.loading = true;
      this.active = true;

      this.error = null;
      const janusStream = await this.setupJanusStream();
      console.log("Calling this.streamStart with janusStream", janusStream);
      await this.streamStart({
        device: janusStream.device,
        stream: janusStream.id,
      });
      await this.connectStream(janusStream);
    },
    async stopMonitoring() {
      this.loading = false;
      if (this.janusStream) {
        await this.streamStop({
          device: this.deviceId,
          stream: this.janusStream.id,
        });
      }
      await this.reset();
    },
    async reset() {
      await this.resetJanus();
      this.data = initialData();
    },
    async resetJanus() {
      if (this.plugin) {
        await this.plugin.detach();
        console.info("Detatched plugin", this.plugin);
        await this.plugin.cleanup();
        console.info("Cleaned up all streaming resources");
      }
    },

    async getOrCreateStreamMountpoint(plugin: any) {
      try {
        const res = await plugin.connect(this.janusStream.id, {
          type: "rtp",
          secret: this.janusStream.secret,
          pin: this.janusStream.pin,
          is_private: true,
          audio: false,
          video: true,
          data: false,
          videoport: this.janusStream.rtp_port,
          videopt: 96,
          videortpmap: "H264/90000",
          videofmtp: "profile-level-id=42e028;packetization-mode=1",
        });
        console.log("plugin.connect response", res);
        return await plugin.start();
      } catch (error) {
        console.log(
          "plugin.connect returned error, attempting to create mountpoint",
          error
        );
        const res = await plugin.create(this.janusStream.id, {
          type: "rtp",
          secret: this.janusStream.secret,
          pin: this.janusStream.pin,
          is_private: true,
          audio: false,
          video: true,
          data: false,
          videoport: this.janusStream.rtp_port,
          videortpmap: "H264/90000",
          videopt: 96,
          videofmtp: "profile-level-id=42e028;packetization-mode=1",
        });
        console.log("plugin.create response", res);
        return await this.getOrCreateStreamMountpoint(plugin);
      }
    },
    monitoringActive() {
      return this.device.monitoring_active === true;
    },
    parseInboundRtpStat(stat: any) {
      const prevStat = this.videoStats;
      const nextStat: JanusVideoStats = {
        bsnow: stat.bytesReceived,
        tsnow: stat.timestamp,
        fps: stat.framesPerSecond,
        packetsLost: stat.packetsLost,
        height: stat.frameHeight,
        width: stat.frameWidth,
        decoderImplementation: stat.decoderImplementation,
      };
      if (prevStat == null) {
        nextStat.bsbefore = nextStat.bsnow;
        nextStat.tsbefore = nextStat.tsnow;
      } else {
        nextStat.bsbefore = prevStat.bsbefore;
        nextStat.tsbefore = prevStat.tsbefore;
        let timePassed = nextStat.tsnow - nextStat.tsbefore;
        // timestamp is in microseconds in Safari, otherwise miliseconds
        if (adapter.browserDetails.browser === "safari") {
          timePassed = timePassed / 1000;
        }
        let bitRate = Math.round(
          ((nextStat.bsnow - nextStat.bsbefore) * 8) / timePassed
        );
        if (adapter.browserDetails.browser === "safari") {
          bitRate = Math.round(bitRate / 1000);
        }
        let bitRateStr = bitRate + " kbits/sec";

        nextStat.bsbefore = nextStat.bsnow;
        nextStat.tsbefore = nextStat.tsnow;
        nextStat.bitrate = bitRateStr;
      }
      this.videoStats = nextStat;
    },
    setupRemoteTrack(plugin: any, el: any) {
      const videoReady = this.videoReady;
      plugin.on("pc:track:remote", function (event: any) {
        console.log("plugin.on pc:track:remote", event);
        if (event.type === "track") {
          const video = document.getElementById(el) as HTMLMediaElement;
          // video.onloadeddata = function (e) {
          //   console.log('loadeddata event called')
          //   video.play()
          //   return videoReady()
          // }
          // video.onloadedmetadata = function (e) {
          //   console.log('onloadedmetadata event called')
          //   video.play()
          //   return videoReady()
          // }
          const mediaStream = event.streams[0];
          console.log(
            "Attaching stream",
            mediaStream,
            "to video element",
            video
          );
          if ("srcObject" in video) {
            console.log("Attaching video.srcObject = medisStream");
            video.srcObject = mediaStream;
          } else {
            console.log(
              "Attaching video.src = URL.createObjectURL(mediaStream)"
            );
            video.src = URL.createObjectURL(mediaStream);
          }
          video.play();
          videoReady();
        }
      });
    },
    videoReady() {
      this.loading = false;
    },
  },
});

export default JanusStream;
</script>
<template>
  <div class="card">
    <div class="card-header">
      <h3 class="card-title text-center">
        <span v-show="loading" class="text-center mt-3">
          Waiting for {{ device.hostname }} camera
        </span>
        <span v-show="showVideo" class="text-center mt-3">
          {{ device.hostname }} Live
        </span>
        <span v-show="!showVideo && !loading" class="text-center mt-3">
          {{ device.hostname }} Offline
        </span>
      </h3>
    </div>
    <div class="card-body">
      <div v-show="!showVideo">
        <img class="img-responsive w-25 d-block mx-auto" :src="offlineImage" />
      </div>
      <div v-show="loading" class="text-center mt-3">
        <span
          class="spinner-border spinner-border-sm"
          role="status"
          aria-hidden="true"
        ></span>
        Waiting for {{ device.hostname }} camera
      </div>
      <div v-show="showVideo">
        <video
          v-show="showVideo"
          class="rounded centered"
          :id="videoStreamEl"
          width="100%"
          height="100%"
          playsinline
          autoplay="autoplay"
          muted
          controls
        />
        <dl v-if="videoStats !== null && active" class="row">
          <dt class="col-sm-3">Bitrate</dt>
          <dd class="col-sm-3">{{ videoStats.bitrate }}</dd>
          <dt class="col-sm-3">Packets Lost</dt>
          <dd class="col-sm-3">{{ videoStats.packetsLost }}</dd>
          <dt class="col-sm-3">Frames / Second</dt>
          <dd class="col-sm-3">{{ videoStats.fps }}</dd>
          <dt class="col-sm-3">Video Dimensions</dt>
          <dd class="col-sm-3">
            {{ videoStats.height }} x {{ videoStats.width }}
          </dd>
          <!-- <dt class="col-sm-3">Decoder</dt>
                <dd class="col-sm-3">{{ videoStats.decoderImplementation }}</dd> -->
        </dl>
      </div>
    </div>
    <div class="card-footer text-center">
      <button
        v-if="!active && !loading"
        @click="startMonitoring"
        class="btn btn-dark btn-sm mr-2 ml-2"
      >
        <i class="mdi mdi-camera"></i> Start Monitoring
      </button>
      <button
        v-if="active || loading"
        @click="stopMonitoring"
        class="btn btn-dark btn-sm mr-2 ml-2"
      >
        <i class="mdi mdi-camera"></i> Stop Monitoring
      </button>
    </div>
  </div>
</template>
