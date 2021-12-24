<script>
import { mapActions, mapState, mapMutations } from 'vuex'
import TaskStatus from '@/components/TaskStatus'
import {
  DEVICES,
  DEVICE_MODULE,
  SET_DEVICE_DATA
} from '@/store/devices'
import {
  TASKS,
  TASK_MODULE,
  SET_TASK_DATA
} from '@/store/tasks'

export default {
  components: { TaskStatus },
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
  methods: {
    ...mapMutations(DEVICE_MODULE, [
      SET_DEVICE_DATA
    ]),
    ...mapMutations(TASK_MODULE, [
      SET_TASK_DATA
    ])
  },
  created: function () {
    // set initial task data from parent WebCamStream.js module
    this.SET_DEVICE_DATA({ data: this.$parent.device })
    this.SET_TASK_DATA({ data: this.$parent.task })
  }
}
</script>

<template>
<div class="card col-12">
  <div class="card-header">
    <h2 class="header-title">
      <a class="badge badge-light" href="" target="_blank">
        <i class="mdi mdi-printer-3d"></i> {{ devices[deviceId].hostname }}

        </a>
        <task-status :task-id="devices[deviceId].last_task.id" />
    </h2>
  </div>
    <div class="card-body">
        <div class="col-6 offset-3 mt-2">
        <img src="/static/images/sleep.svg" style="opacity: 30%" class="d-none d-md-block img-fluid"/>
        </div>
    </div>
    <div class="card-footer d-flex justify-content-center">
        <a href="#" target="_blank">
            <button class="btn btn-light btn-sm mr-2 ml-2">
            <i class="mdi mdi-camera"></i> Start Monitoring
            </button>
        </a>
        <a :href="deviceUrl" target="_blank">
            <button class="btn btn-light btn-sm mr-2 ml-2">
                <i class="mdi mdi-printer-3d"></i> Manage Pi
            </button>
        </a>
    </div>
</div>
</template>
