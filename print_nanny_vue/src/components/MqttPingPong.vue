<script>
import { mapActions, mapState } from 'vuex'
import {
  WIZARD_MODULE,
  CREATE_MQTT_PING_EVENT,
  MQTT_PING_EVENT,
  MQTT_PING_EVENT_LOG,
  MQTT_PONG_EVENT,
  MQTT_PONG_EVENT_LOG
} from '@/store/wizard'
export default {
  props: {
    deviceId: String,
    hostname: String
  },
  data: function () {
    return {
      loading: false
    }
  },
  methods: {
    ...mapActions(WIZARD_MODULE, {
      createMqttPing: CREATE_MQTT_PING_EVENT
    }),
    capitalize (str) {
      return str.charAt(0).toUpperCase() + str.slice(1)
    },
    startTest: function () {
      this.loading = true
      this.createMqttPing(this.deviceId)
    },
    resetTest: function () {
      this.loading = false
    },
    statusClass: function (event) {
      switch (event.status) {
        case 'waiting':
          return 'text-secondary'
        case 'sent':
          return 'text-warning spinner-grow spinner-grow-sm'
      }
    }
  },
  computed: {
    ...mapState(WIZARD_MODULE, {
      mqttPingEvent: MQTT_PING_EVENT,
      mqttPingEventLog: MQTT_PING_EVENT_LOG,
      mqttPongEvent: MQTT_PONG_EVENT,
      mqttPongEventLog: MQTT_PONG_EVENT_LOG
    })
  }
}
</script>
<template>
  <div class="card col-12">
    <div v-if="!loading" class="card-header">
        <button @click="startTest" class="btn btn-block btn-primary col-6 offset-3">
        Start MQTT Test
      </button>
    </div>
    <div v-if="loading" class="card-header">
        <button @click="resetTest" class="btn btn-block btn-primary col-6 offset-3">
        <span class="spinner-border-sm spinner-border" role="status"></span>
          Reset Test
        </button>
    </div>
    <div class="card-body">
      <p class="text-center">Print Nanny uses MQTT to send/receive events from your device. </p>

      <div class="row chart-content-bg text-center">
        <div class="col-6">
          <h2>
            Print Nanny Network
          </h2>
          <h3 class="text-muted mb-0 mt-3">
            <small :class="statusClass(mqttPingEvent)" class="mdi mdi-checkbox-blank-circle align-middle me-1"></small>

          {{ capitalize(mqttPingEvent.status) }}</h3>
          <pre>

          </pre>
        </div>

        <div class="col-6">
          <h2>
            Raspberry Pi
          </h2>
          <h3 class="text-muted mb-0 mt-3">
            <small :class="statusClass(mqttPongEvent)" class="mdi mdi-checkbox-blank-circle align-middle me-1"></small>

          {{ capitalize(mqttPongEvent.status) }}</h3>
          <pre>

          </pre>
        </div>
      </div>
    </div>

  </div>
</template>
