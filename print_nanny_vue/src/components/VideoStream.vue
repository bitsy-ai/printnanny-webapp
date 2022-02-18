<script>
// CloudVideoStream component drives video streaming flow using "remote" Janus Gateway
import { mapState, mapActions } from 'vuex'
import {
  DEVICE_MODULE,
  DEVICE,
  GET_DEVICE,
  GET_OR_CREATE_JANUS_STREAM,
  JANUS_STREAM
} from '@/store/devices'

import {
  TASK_MODULE,
  MONITOR_START_TASK,
  MONITOR_STOP_TASK
} from '@/store/tasks'

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
      getOrCreateJanusStream: GET_OR_CREATE_JANUS_STREAM
    }),
    ...mapActions(TASK_MODULE, {
      startMonitor: MONITOR_START_TASK,
      stopMonitor: MONITOR_STOP_TASK
    }),
    async startMonitoring () {
      this.loading = true
      await this.startMonitor(this.deviceId)
    },
    async stopMonitoring () {
      this.loading = false
      await this.stopMonitor(this.deviceId)
    },
    monitoringActive () {
      return this.device.monitoring_active === true
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
    }
  },
  async created () {
    if (this.deviceId) {
      await this.getDevice(this.deviceId)
      console.debug('Fetched device: ', this.device)
      await this.getOrCreateJanusStream(this.deviceId)
      console.debug('Fetched JanusStream: ', this.janusStream)
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
