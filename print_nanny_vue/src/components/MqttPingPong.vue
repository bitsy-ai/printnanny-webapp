<script>

export default {
  props: {
    deviceId: Number
  },
  data: {
    loading: false
  },
  methods: {

  }
}
</script>
<template>
<div class="card col-12 col-md-6">
  <div class="card-header">
    <h2 class="header-title"></h2>
  </div>
  <div class="card-body">
    <button class="btn btn-primary">
      Send MQTT Ping
    </button>
  </div>
</div>
</template>
