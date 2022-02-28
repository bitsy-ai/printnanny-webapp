<script>
import adapter from 'webrtc-adapter'
import Janus from 'janus-gateway-js'

import { mapActions, mapState } from 'vuex'
import {
  DEVICE,
  DEVICE_MODULE,
  GET_DEVICE
  // START_MONITORING,
  // STOP_MONITORING
} from '@/store/devices'

function initialData () {
  return {
    error: null,
    loading: false,
    active: false,
    janusConnection: null,
    janusSession: null,
    janusPlugin: null,
    janusStream: null,
    timer: null,
    videoStats: null
  }
}
export default {
  components: {},
  data: function () {
    return initialData()
  },
  async created () {
    if (this.active) {
      await this.connectStream()
    }
  },
  methods: {
    ...mapActions(DEVICE_MODULE, {
      getDevice: GET_DEVICE
    }),
    async handleError (error) {
      this.error = error
      this.resetTimer()
      await this.stopMonitoring(this.device)
      this.loading = false
    },
    resetTimer () {
      if (this.timer !== null) {
        clearInterval(this.timer)
      }
    },
    async resetJanus () {
      if (this.plugin) {
        await this.plugin.detach()
        console.info('Detatched plugin', this.plugin)
        await this.plugin.cleanup()
        console.info('Cleaned up all streaming resources')
      }
    },
    async reset () {
      await this.resetJanus()
      this.resetTimer()
      this.data = initialData()
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
            video.srcObject = mediaStream
          } else {
            // Avoid using this in new browsers, as it is going away.
            video.src = URL.createObjectURL(mediaStream)
          }
        }
      })
    },

    async connectStream () {
      const url = `wss://${this.device.hostname}:8989`
      const janusToken = this.device.janus_auth.janus_token
      console.log('Authenticating with janus token', janusToken)
      const janus = new Janus.Client(url, {
        token: janusToken,
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
        const videoStreamEl = this.videoStreamEl
        console.log('Plugin attached', plugin)
        plugin.on('message', (message, jesp) => {
          console.log('plugin.on message', message, jesp)
        })
        const streamsList = await plugin.list()
        console.log('retrieved stream list: ', streamsList)
        if (streamsList._plainMessage.plugindata.data.list.length === 0) {
          throw Error('Connection to Janus Gateway succeeded, but no streams are playing.\n Double-check that your camera is connected and try again. \n Check output of `systemctl status printnanny-gst` and `journalctl -u printnanny-gst` for details about this failure.')
        }

        for (const stream of streamsList._plainMessage.plugindata.data.list) {
          if (stream.id === this.streamId) {
            this.setupRemoteTrack(plugin, videoStreamEl)
            console.log('Selected stream', stream)

            const watch = await plugin.watch(stream.id, {
              video: true
            })
            console.log('Now watching stream', watch)
            const start = await plugin.start()

            console.log('Started stream', start)

            const info = await plugin.send({
              body: { request: 'info', id: stream.id },
              janus: 'message'
            })

            console.log('retrieved stream info', info)
          } else {
            console.log(`Skipping stream ${stream.id} (component is subscribed to ${this.streamId})`)
          }
        }
      } catch (error) {
        return await this.handleError(error)
      }
    },
    async startMonitoring () {
      this.loading = true
      this.active = true
      this.error = null
      await this.connectStream()
    },
    async stopMonitoring () {
      await this.reset()
    },
    videoReady () {
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
  props: {
    deviceId: {
      type: String,
      required: true
    },
    streamId: {
      type: Number,
      required: true
    }
  },
  computed: {
    ...mapState(DEVICE_MODULE, {
      device: DEVICE
    }),
    videoStreamEl: function () {
      return `video-${this.streamId}`
    },
    showVideo: function () {
      return this.loading === false && this.active === true
    },
    showLoading: function () {
      return this.loading
    },
    showInfo: function () {
      return this.active === false && this.error === null
    },
    remoteAccessEl: function () {
      return `remote-access-${this.device.id}`
    }
  }
}
</script>

<template>
  <div class="card col-12">
    <div class="card-header text-center">
      <button
        v-if="!active"
        @click="startMonitoring"
        class="btn btn-light btn-sm mr-2 ml-2"
      >
        <i class="mdi mdi-camera"></i> Start
      </button>
      <button
        v-if="active && loading"
        class="btn btn-light mr-2 ml-2"
        disabled
      >
        <span
          class="spinner-border spinner-border-sm"
          role="status"
          aria-hidden="true"
        ></span>
        Loading Stream
      </button>
      <button
        v-if="active"
        @click="stopMonitoring"
        class="btn btn-light btn-sm mr-2 ml-2"
      >
        <i class="mdi mdi-camera"></i> Stop Monitoring
      </button>
    </div>
    <div class="card-body">
      <div>
        <div v-show="loading">
          <h3 class="header-title">Video is loading...</h3>
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
        </div>
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

      <div v-if="error" class="alert alert-danger col-12 d-flex" role="alert">
        <div class="row">
          <div class="col-8">
            <h4 class="alert-heading">
              <i class="mdi mdi-warning"></i>Oops, something went wrong!
            </h4>

            <h4 class="alert-heading">
              <i class="mdi mdi-warning"></i>Please reboot your Raspberry Pi and
              then try again.
            </h4>

            <p>
              Need help? Email <strong>leigh@print-nanny.com</strong> with error
              code, message, and transaction id.
            </p>

            <pre>
Name: {{ error.name }}
Code: {{ error.code }}
Message: {{ error.message }}
              </pre
            >
          </div>

          <div v-show="error" class="col-4">
            <img
              src="/static/images/confused.svg"
              style="opacity: 30%"
              class="d-none d-md-block img-fluid"
            />
          </div>
        </div>
      </div>

      <div v-if="showInfo" class="alert alert-info col-12 d-flex" role="alert">
        <div class="row">
          <div class="col-8">
            <h4 class="alert-heading">
              <i class="mdi mdi-warning"></i>Camera is offline
            </h4>
            <p>
              Click/tap <i class="mdi mdi-camera"></i
              ><strong>Start</strong> button to start.
            </p>
          </div>
          <div class="col-4">
            <img
              src="/static/images/sleep.svg"
              style="opacity: 30%"
              class="d-none d-md-block img-fluid"
            />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
