<script>
import Janus from 'janus-gateway-js'
import { mapActions, mapState, mapMutations } from 'vuex'
import TaskStatus from '@/components/TaskStatus'
// import { JanusSession, JanusConstructorOptions } from '@/services/janus'
import {
  DEVICES,
  DEVICE_MODULE,
  SET_DEVICE_DATA,
  START_MONITORING,
  STOP_MONITORING
} from '@/store/devices'
import {
  TASKS,
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
    ...mapActions(DEVICE_MODULE, {
      startMonitoring: START_MONITORING,
      stopMonitoring: STOP_MONITORING
    }),
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
    })
  },
  created: async function () {
    const _self = this
    const url = `ws://${this.devices[this.deviceId].hostname}:8188/janus`
    const janus = new Janus.Client(url, {
      token: 'token',
      keepalive: 'true'
    })

    const connection = await janus.createConnection('id')
    console.log('Created janus connection', connection)

    const session = await connection.createSession()
      .catch((err) => {
        console.error(err)
        _self.error = err
      })
    console.log('Created janus session', session)

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

        <div v-if="!devices[deviceId].monitoring_active" class="alert alert-info col-12 d-flex" role="alert">
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

        <div v-if="error" class="alert alert-danger col-12 d-flex" role="alert">
          <div class="row">
            <div class="col-8">
              <h4 class="alert-heading"><i class="mdi mdi-warning"></i>Oops, something went wrong!</h4>

              <h4 class="alert-heading"><i class="mdi mdi-warning"></i>Please reboot your Raspberry Pi and then refresh this page</h4>

              <p>Error name: {{ error.name }}
              <br>Error code: {{ error.code}}
              <br>Message: {{ error.message }}
              <br>Transaction: {{ error.janusMessage._plainMessage.transaction }}
              </p>

              <p>Need help? Email <strong>leigh@print-nanny.com</strong> with the error code, message, and transaction id.</p>
            </div>

            <div v-if="!devices[deviceId].monitoring_active" class="col-4">
            <img src="/static/images/sleep.svg" style="opacity: 30%" class="d-none d-md-block img-fluid"/>
            </div>

            <div v-if="error" class="col-4">
            <img src="/static/images/confused.svg" style="opacity: 30%" class="d-none d-md-block img-fluid"/>
            </div>
          </div>
        </div>

        <div v-if="devices[deviceId].monitoring_active">
          <div class="row">

          </div>
        </div>
    </div>
    <div class="card-footer d-flex justify-content-center">
        <a :href="deviceUrl" target="_blank">
            <button class="btn btn-light btn-sm mr-2 ml-2">
                <i class="mdi mdi-printer-3d"></i> Manage Pi
            </button>
        </a>
          <button v-if="!devices[deviceId].monitoring_active"
            @click="startMonitoring(devices[deviceId])" class="btn btn-light btn-sm mr-2 ml-2">
          <i class="mdi mdi-camera"></i> Start Monitoring
          </button>
          <button v-if="devices[deviceId].monitoring_active"
            @click="stopMonitoring(devices[deviceId])" class="btn btn-light btn-sm mr-2 ml-2">
          <i class="mdi mdi-camera"></i> Stop Monitoring
          </button>
    </div>
</div>
</template>
