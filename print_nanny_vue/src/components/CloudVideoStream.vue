<script>
// CloudVideoStream component drives video streaming flow using "remote" Janus Gateway
import { defineComponent } from "@vue/composition-api";

export default defineComponent({
  setup() {},
});
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
        v-if="active"
        @click="stopMonitoring"
        class="btn btn-light btn-sm mr-2 ml-2"
      >
        <i class="mdi mdi-camera"></i> Stop Monitoring
      </button>
    </div>
    <div class="card-body">
      <div v-show="loading">
        <span
          class="spinner-border spinner-border-sm"
          role="status"
          aria-hidden="true"
        ></span>
        Loading Stream
      </div>
    </div>
  </div>
</template>