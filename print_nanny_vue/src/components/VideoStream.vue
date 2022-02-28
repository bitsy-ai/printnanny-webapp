<script>
import adapter from 'webrtc-adapter'
import Janus from 'janus-gateway-js'
import { mapState, mapActions } from 'vuex'
import {
  DEVICE_MODULE,
  DEVICE,
  GET_DEVICE,
  JANUS_STREAM,
  SET_JANUS_STREAM_DATA
} from '@/store/devices'

import { EVENTS_MODULE, STREAM_START, STREAM_STOP } from '@/store/events'

function initialData () {
  return {
    loading: false,
    active: false,
    error: null
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
      getDevice: GET_DEVICE
    }),
    ...mapActions(EVENTS_MODULE, {
      streamStart: STREAM_START,
      streamStop: STREAM_STOP
    }),
    async startMonitoring () {
      this.loading = true
      this.error = null
      await this.streamStart(this.deviceId)
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
    async connectStream (stream) {
      console.log(stream)
      const janus = new Janus.Client(stream.websocket_url, {
        token: stream.auth.api_token,
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
          console.error('Connection to Janus Gateway succeeded, but no streams are playing.\n Double-check that your camera is connected and try again. \n Check output of `systemctl status printnanny-monitor` and `journalctl -u printnanny-monitor` for details about this failure.')
          // throw Error('Connection to Janus Gateway succeeded, but no streams are playing.\n Double-check that your camera is connected and try again. \n Check output of `systemctl status printnanny-monitor` and `journalctl -u printnanny-monitor` for details about this failure.')
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
    async handleError (error) {
      console.error(error)
      this.error = error
      // this.resetTimer()
      await this.stopMonitoring(this.device)
      this.loading = false
    }
  },
  computed: {
    ...mapState(DEVICE_MODULE, {
      device: DEVICE,
      stream: JANUS_STREAM
    }),
    status () {
      if (this.device.monitoring_active === true) {
        return 'Video Stream is Online'
      } else if (this.loading) {
        return 'Video Stream is Loading'
      } else {
        return 'Video Stream is Offline'
      }
    }
  },
  async created () {
    // fetch device data
    if (this.deviceId) {
      await this.getDevice(this.deviceId)
    }
    // subscribe to mutations in store
    this.$store.subscribe(async mutation => {
      switch (mutation.type) {
        case `${DEVICE_MODULE}/${SET_JANUS_STREAM_DATA}`:
          console.log(mutation)
          await this.connectStream(mutation.payload)
      }
    })
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
