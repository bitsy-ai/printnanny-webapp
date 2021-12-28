<script>
import adapter from 'webrtc-adapter'
import Janus from 'janus-gateway-js'

import { mapState, mapMutations } from 'vuex'
import TaskStatus from '@/components/TaskStatus'
import deviceApi from '@/services/devices'
import {
  DEVICES,
  DEVICE_MODULE,
  SET_DEVICE_DATA,
  START_MONITORING,
  STOP_MONITORING
} from '@/store/devices'
import {
  TASK_MODULE,
  SET_TASK_DATA
} from '@/store/tasks'

const initialData = {
  error: null,
  loading: false,
  janusConnection: null,
  janusSession: null,
  janusPlugin: null,
  janusStream: null,
  timer: null,
  videoStats: null
}
export default {
  components: { TaskStatus },
  data: function () {
    return initialData
  },
  methods: {
    ...mapMutations(DEVICE_MODULE, [
      SET_DEVICE_DATA
    ]),
    ...mapMutations(TASK_MODULE, [
      SET_TASK_DATA
    ]),
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
      if (this.plugin !== null) {
        await this.plugin.detach()
        console.info('Detatched plugin', this.plugin)
        await this.plugin.cleanup()
        console.info('Cleaned up all streaming resources')
      }
    },
    async reset () {
      await this.resetJanus()
      this.resetTimer()
      this.data = initialData
    },

    async connectStream () {
      this.loading = true
      const url = `ws://${this.device.hostname}:8188/janus`
      const license = (await deviceApi.getActiveLicense(this.device)).data
      console.debug('Retreive license', license)
      const janus = new Janus.Client(url, {
        token: license.janus_token,
        keepalive: 'true'
      })

      console.log('Browser details detected', adapter.browserDetails.browser, adapter.browserDetails.version)
      const connection = await janus.createConnection('id')
      this.connection = connection
      console.log('Created janus connection', connection)

      try {
        const session = await connection.createSession()
        this.session = session

        console.log('Created janus session', session)

        const plugin = await session.attachPlugin(Janus.StreamingPlugin.NAME)
        this.plugin = plugin

        this.timer = setInterval(this.getVideoStats, 200)
        const webcamStreamEl = this.webcamStreamEl
        const videoReady = this.videoReady
        console.log('Plugin attached', plugin)
        plugin.on('message', (message, jesp) => {
          console.log('plugin.on message', message, jesp)
        })
        plugin.on('pc:track:remote', function (event) {
          console.log('plugin.on pc:track:remote', event)
          const video = document.getElementById(webcamStreamEl)
          const mediaStream = event.streams[0]
          console.log('Attaching stream', mediaStream, 'to video element', video)
          if ('srcObject' in video) {
            video.srcObject = mediaStream
          } else {
            // Avoid using this in new browsers, as it is going away.
            video.src = URL.createObjectURL(mediaStream)
          }
          video.onloadedmetadata = function (e) {
            video.play()
            return videoReady()
          }
        })

        const streamsList = await plugin.list()
        console.log('Retreived stream list: ', streamsList)

        const stream = streamsList._plainMessage.plugindata.data.list[0]
        console.log('Selected stream', stream)

        const watch = await plugin.watch(stream.id, {
          video: true
        })
        console.log('Now watching stream', watch)
        // const start = await plugin.start(watch._plainMessage.jsep)
        const start = await plugin.start()

        console.log('Started stream', start)

        const info = await plugin.send({ body: { request: 'info', id: stream.id }, janus: 'message' })
        //   .then(msg => console.log('After msg', msg))

        // const peer = await plugin.getPeerConnection()
        console.log('Retreived stream info', info)
      } catch (error) {
        if (error.name === 'JanusError') {
          return await this.handleError(error)
        }
        throw error
      }
    },
    async startMonitoring () {
      this.loading = true
      this.error = null
      this.$store.dispatch(`${DEVICE_MODULE}/${START_MONITORING}`, this.device)
      await this.connectStream()
    },
    async stopMonitoring () {
      this.$store.dispatch(`${DEVICE_MODULE}/${STOP_MONITORING}`, this.device)
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
        let bitRate = Math.round((nextStat.bsnow - nextStat.bsbefore) * 8 / timePassed)
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
  },
  props: {
    deviceId: {
      type: String,
      required: true
    },
    deviceUrl: {
      type: String,
      required: true
    }
  },
  computed: {
    ...mapState(DEVICE_MODULE, {
      devices: DEVICES
    }),
    device: function () {
      return this.devices[this.deviceId]
    },
    webcamStreamEl: function () {
      return `webcam-stream-${this.device.id}`
    },
    showVideo: function () {
      return this.loading === false && this.device.monitoring_active === true
    },
    showLoading: function () {
      return this.loading
    },
    showInfo: function () {
      return this.device.monitoring_active === false && this.error === null
    },
    remoteAccessEl: function () {
      return `remote-access-${this.device.id}`
    }
  },
  created: async function () {
    if (this.device.monitoring_active) {
      await this.connectStream()
    }
  }
}
</script>

<template>
<div class="card col-12">
  <div class="card-header">
    <h2 class="header-title">
      <a class="badge badge-light" :href="deviceUrl" target="_blank">
        <i class="mdi mdi-printer-3d"></i> {{ devices[deviceId].hostname }}

        </a>
        <task-status :task-id="devices[deviceId].last_task.id" />
    </h2>
  </div>
    <div class="card-body">

        <div>
          <div v-show="loading">
            <h3 class="header-title">Video is loading...</h3>
          </div>
            <video
              v-show="showVideo"
              class="rounded centered" :id="webcamStreamEl"
              width="100%"
              height="100%"
              playsinline
              autoplay="autoplay"
              muted
              controls
              />
              <dl v-if="videoStats !== null && device.monitoring_active" class="row">
                <dt class="col-sm-3">Bitrate</dt>
                <dd class="col-sm-3">{{ videoStats.bitrate }}</dd>
                <dt class="col-sm-3">Packets Lost</dt>
                <dd class="col-sm-3">{{ videoStats.packetsLost }}</dd>
                <dt class="col-sm-3">Frames / Second</dt>
                <dd class="col-sm-3">{{ videoStats.fps }}</dd>
                <dt class="col-sm-3">Video Dimensions</dt>
                <dd class="col-sm-3">{{ videoStats.height }} x {{ videoStats.width }}</dd>
                <!-- <dt class="col-sm-3">Decoder</dt>
                <dd class="col-sm-3">{{ videoStats.decoderImplementation }}</dd> -->
              </dl>
        </div>

        <div v-if="error" class="alert alert-danger col-12 d-flex" role="alert">
          <div class="row">
            <div class="col-8">
              <h4 class="alert-heading"><i class="mdi mdi-warning"></i>Oops, something went wrong!</h4>

              <h4 class="alert-heading"><i class="mdi mdi-warning"></i>Please reboot your Raspberry Pi and then try again.</h4>

              <p>Need help? Email <strong>leigh@print-nanny.com</strong> with error code, message, and transaction id.</p>

              <pre>
Name: {{ error.name }}
Code: {{ error.code}}
Message: {{ error.message }}
Transaction: {{ error.janusMessage._plainMessage.transaction }}
              </pre>

            </div>

            <div v-show="error" class="col-4">
            <img src="/static/images/confused.svg" style="opacity: 30%" class="d-none d-md-block img-fluid"/>
            </div>
          </div>
        </div>

        <div v-if="showInfo" class="alert alert-info col-12 d-flex" role="alert">
          <div class="row">
            <div class="col-8">
              <h4 class="alert-heading"><i class="mdi mdi-warning"></i>Camera is offline</h4>
              <p>Click/tap <i class="mdi mdi-camera"></i><strong>Start Monitoring</strong> button to start.</p>
            </div>
            <div class="col-4">
            <img src="/static/images/sleep.svg" style="opacity: 30%" class="d-none d-md-block img-fluid"/>
            </div>
          </div>
        </div>

    </div>
    <div class="card-footer d-flex justify-content-center">
        <a :href="deviceUrl" target="_blank">
            <button class="btn btn-light btn-sm mr-2 ml-2">
                <i class="mdi mdi-printer-3d"></i> Manage Pi
            </button>
        </a>
          <button v-if="!device.monitoring_active"
            @click="startMonitoring" class="btn btn-light btn-sm mr-2 ml-2">
          <i class="mdi mdi-camera"></i> Start Monitoring
          </button>
          <button v-if="device.monitoring_active && loading"
            class="btn btn-light btn-sm mr-2 ml-2"
            disabled>
          <span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>
          Loading Stream
          </button>
          <button v-if="device.monitoring_active && !loading"
            @click="stopMonitoring" class="btn btn-light btn-sm mr-2 ml-2">
          <i class="mdi mdi-camera"></i> Stop Monitoring
          </button>

          <b-button :id="remoteAccessEl">
            Remote Access
          </b-button>
          <b-popover :target="remoteAccessEl" triggers="hover" placement="bottom">
            <template #title>Coming in the next stable release!</template>
            <strong>Remote Access</strong> allows you to access your Raspberry Pi from anywhere in the world.

            <a href="">Click here to let me know</a> you're interested in <strong>Remote Access</strong>
          </b-popover>
          </button>
    </div>
</div>
</template>
