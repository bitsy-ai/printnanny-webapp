<script>
// CloudVideoStream component drives video streaming flow using "remote" Janus Gateway
import { mapState, mapActions } from 'vuex'
import { DEVICE_MODULE, GET_DEVICE, DEVICE, START_MONITORING, STOP_MONITORING } from '@/store/devices'

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
    return {
      loading: false,
      active: false
    }
  },
  methods: {
    ...mapActions(DEVICE_MODULE, {
      getDevice: GET_DEVICE,
      startMonitoringTask: START_MONITORING,
      stopMonitoringTask: STOP_MONITORING
    }),
    async startMonitoring () {
      this.loading = true
      this.active = true
      await this.startMonitoringTask(this.deviceId)
    },
    async stopMonitoring () {
      this.loading = false
      this.active = false
      await this.stopMonitoringTask(this.deviceId)
    },
    monitoringActive () {
      return this.device.monitoring_active === true
    }
  },
  computed: {
    ...mapState(DEVICE_MODULE, {
      device: DEVICE
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
    if (this.deviceId) {
      await this.getDevice(this.deviceId)
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
      <img :v-show="!monitoringActive" class="img-responsive w-25 d-block mx-auto" :src="offlineImage" />
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
        v-if="!active"
        @click="startMonitoring"
        class="btn btn-dark btn-sm mr-2 ml-2"
      >
        <i class="mdi mdi-camera"></i> Start Monitoring
      </button>
      <button
        v-if="active"
        @click="stopMonitoring"
        class="btn btn-dark btn-sm mr-2 ml-2"
      >
        <i class="mdi mdi-camera"></i> Stop Monitoring
      </button>
    </div>
  </div>
</template>
