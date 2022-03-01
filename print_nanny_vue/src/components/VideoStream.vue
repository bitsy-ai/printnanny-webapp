<script>
import adapter from 'webrtc-adapter'
import Janus from 'janus-gateway-js'
import { mapState, mapActions } from 'vuex'
import {
  DEVICE_MODULE,
  DEVICE,
  GET_DEVICE,
  JANUS_STREAM,
  GET_JANUS_STREAM
} from '@/store/devices'

import { EVENTS_MODULE, STREAM_START, STREAM_STOP } from '@/store/events'

function initialData () {
  return {
    loading: false,
    active: false,
    error: null,
    timer: null,
    videoStats: null
  }
}

export default {
  props: {
    deviceId: {
      type: String,
      required: true
    },
    offlineImage: {
      type: String,
      required: true
    }
  },
  data: function () {
    return initialData()
  },
  methods: {
    ...mapActions(DEVICE_MODULE, {
      getDevice: GET_DEVICE,
      getJanusStream: GET_JANUS_STREAM
    }),
    ...mapActions(EVENTS_MODULE, {
      streamStart: STREAM_START,
      streamStop: STREAM_STOP
    }),
    async startMonitoring () {
      this.loading = true
      this.active = true

      this.error = null
      await this.connectStream()
    },
    async stopMonitoring () {
      this.loading = false
      await this.streamStop(this.deviceId)
      await this.reset()
    },
    monitoringActive () {
      return this.device.monitoring_active === true
    },
    async reset () {
      await this.resetJanus()
      // this.resetTimer()
      this.data = initialData()
    },
    async resetJanus () {
      if (this.plugin) {
        await this.plugin.detach()
        console.info('Detatched plugin', this.plugin)
        await this.plugin.cleanup()
        console.info('Cleaned up all streaming resources')
      }
    },

    async getOrCreateStreamMountpoint (plugin) {
      try {
        const res = await plugin.connect(this.janusStream.id, {
          type: 'rtp',
          secret: this.janusStream.secret,
          pin: this.janusStream.pin,
          is_private: true,
          audio: false,
          video: true,
          data: false,
          videoport: this.janusStream.rtp_port,
          videopt: 96,
          videortpmap: 'H264/90000',
          videofmtp: 'profile-level-id=42e028;packetization-mode=1'
        })
        console.log('plugin.connect response', res)
        return await plugin.start()
      } catch (error) {
        console.log(
          'plugin.connect returned error, attempting to create mountpoint',
          error
        )
        const res = await plugin.create(this.janusStream.id, {
          type: 'rtp',
          secret: this.janusStream.secret,
          pin: this.janusStream.pin,
          is_private: true,
          audio: false,
          video: true,
          data: false,
          videoport: this.janusStream.rtp_port,
          videortpmap: 'H264/90000',
          videopt: 96,
          videofmtp: 'profile-level-id=42e028;packetization-mode=1'
        })
        console.log('plugin.create response', res)
        return await this.getOrCreateStreamMountpoint(plugin)
      }
    },
    videoReady () {
      this.loading = false
    },
    setupRemoteTrack (plugin, el) {
      const videoReady = this.videoReady
      plugin.on('pc:track:remote', function (event) {
        console.log('plugin.on pc:track:remote', event)
        if (event.type === 'track') {
          const video = document.getElementById(el)
          video.onloadeddata = function (e) {
            console.log('loadeddata event called')
            // video.play()
            // return videoReady()
          }
          video.onloadedmetadata = function (e) {
            console.log('onloadedmetadata event called')
            video.play()
            return videoReady()
          }
          const mediaStream = event.streams[0]
          console.log(
            'Attaching stream',
            mediaStream,
            'to video element',
            video
          )
          if ('srcObject' in video) {
            console.log('Attaching video.srcObject = medisStream')
            video.srcObject = mediaStream
          } else {
            console.log(
              'Attaching video.src = URL.createObjectURL(mediaStream)'
            )
            video.src = URL.createObjectURL(mediaStream)
          }
          video.play()
        }
      })
    },
    async connectStream () {
      console.log('connectStream called with JanusStream', this.janusStream)
      const janus = new Janus.Client(this.janusStream.websocket_url, {
        token: this.janusStream.auth.api_token,
        keepalive: 'true'
      })

      console.log(
        'Browser details detected',
        adapter.browserDetails.browser,
        adapter.browserDetails.version
      )
      const connection = await janus.createConnection(this.videoStreamEl)
      this.connection = connection
      console.log('Created janus connection', connection)

      try {
        const session = await connection.createSession()
        this.session = session

        console.log('Created janus session', session)

        const plugin = await session.attachPlugin(Janus.StreamingPlugin.NAME)
        this.plugin = plugin

        this.timer = setInterval(this.getVideoStats, 200)
        this.setupRemoteTrack(plugin, this.videoStreamEl)
        console.log('Plugin attached', plugin)
        plugin.on('message', (message, jesp) => {
          console.log('plugin.on message', message, jesp)
        })

        const streamInfo = await this.getOrCreateStreamMountpoint(plugin)
        console.log('got streamInfo', streamInfo)
      } catch (error) {
        return await this.handleError(error)
      }
    },
    async handleError (error) {
      console.error(error)
      this.error = error
      // this.resetTimer()
      await this.stopMonitoring(this.device)
      this.loading = false
    },

    parseInboundRtpStat (stat) {
      const prevStat = this.videoStats
      const nextStat = {}
      nextStat.bsnow = stat.bytesReceived
      nextStat.tsnow = stat.timestamp
      nextStat.fps = stat.framesPerSecond
      nextStat.packetsLost = stat.packetsLost
      nextStat.height = stat.frameHeight
      nextStat.width = stat.frameWidth
      nextStat.decoderImplementation = stat.decoderImplementation

      if (prevStat == null) {
        nextStat.bsbefore = nextStat.bsnow
        nextStat.tsbefore = nextStat.tsnow
      } else {
        nextStat.bsbefore = prevStat.bsbefore
        nextStat.tsbefore = prevStat.tsbefore
        let timePassed = nextStat.tsnow - nextStat.tsbefore
        // timestamp is in microseconds in Safari, otherwise miliseconds
        if (adapter.browserDetails.browser === 'safari') {
          timePassed = timePassed / 1000
        }
        let bitRate = Math.round(
          ((nextStat.bsnow - nextStat.bsbefore) * 8) / timePassed
        )
        if (adapter.browserDetails.browser === 'safari') {
          bitRate = parseInt(bitRate / 1000)
        }
        bitRate = bitRate + ' kbits/sec'

        nextStat.bsbefore = nextStat.bsnow
        nextStat.tsbefore = nextStat.tsnow
        nextStat.bitrate = bitRate
      }
      this.videoStats = nextStat
    },
    async getVideoStats () {
      const _self = this
      const peer = this.plugin.getPeerConnection()
      if (peer) {
        const stats = await peer.getStats()
        stats.forEach((stat) => {
          switch (stat.type) {
            case 'inbound-rtp':
              _self.parseInboundRtpStat(stat)
              break
            default:
              break
          }
        })
      }
    }
  },
  computed: {
    ...mapState(DEVICE_MODULE, {
      device: DEVICE,
      janusStream: JANUS_STREAM
    }),
    status () {
      if (this.device.monitoring_active === true) {
        return 'Video Stream is Online'
      } else if (this.loading) {
        return 'Video Stream is Loading'
      } else {
        return 'Video Stream is Offline'
      }
    },
    showVideo: function () {
      return true
      // return this.loading === false && this.active === true
    },
    videoStreamEl: function () {
      return `video-${this.janusStream.id}`
    }
  },
  async created () {
    // fetch device data
    if (this.deviceId) {
      await this.getDevice(this.deviceId)
      await this.getJanusStream(this.deviceId)
    }
  }
}
</script>
<template>
  <div class="card">
    <div class="card-header">
      <h3 class="card-title text-center">
        {{ status }}
      </h3>
    </div>
    <div class="card-body">
      <img
        :v-show="!monitoringActive"
        class="img-responsive w-25 d-block mx-auto"
        :src="offlineImage"
      />
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
