<script>
import Janus from 'janus-gateway-js'
import { mapActions, mapState, mapMutations } from 'vuex'
import TaskStatus from '@/components/TaskStatus'
import deviceApi from '@/services/devices'
// import { JanusSession, JanusConstructorOptions } from '@/services/janus'
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
      error: null
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

    onSession () {
      console.log('Janus session initialized')
    },
    onSessionError (error) {
      console.error('Janus session error', error)
    },
    onSessionDetroyed () {
      console.info('Janus session destroyed')
    },
    async handleError (error) {
      this.error = error
      await this.stopMonitoring(this.device)
      this.loading = false
    },
    async connectStream () {
      const url = `ws://${this.device.hostname}:8188/janus`
      const license = (await deviceApi.getActiveLicense(this.device)).data
      console.debug('Retreive license', license)
      const janus = new Janus.Client(url, {
        // token: license.janus_token,
        keepalive: 'true'
      })

      const connection = await janus.createConnection('id')
      console.log('Created janus connection', connection)

      try {
        const session = await connection.createSession()

        console.log('Created janus session', session)

        const plugin = await session.attachPlugin('janus.plugin.streaming')

        console.log('Created janus plugin janus.plugin.streaming', plugin)
      } catch (error) {
        return await this.handleError(error)
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
      return `#webcam-stream-${this.device.id}`
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
      this.connectStream()
    }

    // return janus.createConnection('id').then(function (connection) {
    //   console.log('Created janus connection', connection)
    //   connection.createSession().then(function (session) {
    //     console.log('Created janus session')
    //     session.attachPlugin('janus.plugin.streaming').then(function (plugin) {
    //       console.log('Attached janus.plugin.streaming', plugin)
    //       plugin.send({}).then(function (response) {})
    //       plugin.on('message', function (message) {})
    //       plugin.detach()
    //     })
    //   })
    // }).catch(function (error) {
    //   console.error(error)
    // })
    // JanusSession.init()

    // const sessionOpts = {
    //   server: `http://${this.devices[this.deviceId].hostname}:8088/janus`,
    //   success: this.onSession,
    //   error: this.onSessionError,
    //   destroyed: this.onSessionDetroyed
    // }
    // this.jSession = new JanusSession(sessionOpts)
    // const protocol = 'http://'
    // const hostname = this.devices[this.deviceId].hostname
    // const port = '8088'
    // const url = new URL(
    //   `${protocol}${hostname}${port}/janus`
    // )
    // // const token = this.devices[deviceId].activ
    // this.janusService = new JanusService(
    //   url,
    //   'TODO',
    //   this.devices[this.deviceId]
    // )
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
              class="rounded centered hide" :id="webcamStreamEl"
              width="100%"
              height="100%"
              playsinline
              controls/>
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
