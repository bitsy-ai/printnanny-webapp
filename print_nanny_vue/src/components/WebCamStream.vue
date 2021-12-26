<script>
import adapter from 'webrtc-adapter'
import Janus from 'janus-gateway-js'

import { mapActions, mapState, mapMutations } from 'vuex'
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

export default {
  components: { TaskStatus },
  data: function () {
    return {
      error: null,
      loading: false,
      janusConnection: null,
      janusSession: null,
      janusPlugin: null,
      janusStream: null
    }
  },
  methods: {
    // ...mapActions(DEVICE_MODULE, {
    //   startMonitoring: START_MONITORING,
    //   stopMonitoring: STOP_MONITORING
    // }),
    ...mapMutations(DEVICE_MODULE, [
      SET_DEVICE_DATA
    ]),
    ...mapMutations(TASK_MODULE, [
      SET_TASK_DATA
    ]),
    async handleError (error) {
      this.error = error
      await this.stopMonitoring(this.device)
      this.loading = false
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

      const mountId = Math.floor(Math.random() * 1000 + 1)

      try {
        const session = await connection.createSession()
        this.session = session

        console.log('Created janus session', session)

        const plugin = await session.attachPlugin(Janus.StreamingPlugin.NAME)
        this.plugin = plugin

        // plugin.createPeerConnection()
        // plugin._addPcEventListener('addstream', function (event) {
        //   plugin.emit('pc:track:remote', { streams: [event.stream] })
        // })
        // const video = document.getElementById(this.webcamStreamEl)
        // console.
        // video.srcObject = stream
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
          }
          videoReady()
        })

        // await plugin.createPeerConnection()
        // plugin._addPcEventListener('ontrack', function (event) {
        //   console.log('RTCPeerConnection.ontrack event', event)
        // })
        // console.log('Created peer connection', peerConn)

        // await plugin.create(mountId)
        // await plugin.connect(mountId)
        // await plugin.start()

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

        // stream.getTracks().forEach(function (track) {
        //   self.addTrack(track, stream)
        // })
        // const start = await plugin.start()
        // console.log('Started stream', start)

        // plugin.send({ body: { request: 'info', id: stream.id }, janus: 'message' })
        //   .then(msg => console.log('After msg', msg))local-vue
      } catch (error) {
        if (error.name == 'JanusError') {
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
    stopMonitoring () {
      this.$store.dispatch(`${DEVICE_MODULE}/${STOP_MONITORING}`, this.device)
    },
    videoReady () {
      this.loading = false
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
            <video
              v-show="showVideo"
              class="rounded centered" :id="webcamStreamEl"
              width="100%"
              height="100%"
              playsinline
              autoplay="autoplay"
              />
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
    </div>
</div>
</template>
