<script>
import { mapMutations, mapState, mapActions } from 'vuex'
import { DEVICE_MODULE, CREATE_TEST_EVENT } from '@/store/devices'
export default {
  props: {
    deviceId: Number
  },
  data: function () {
    return {
      loading: false
    }
  },
  methods: {
    ...mapActions(DEVICE_MODULE, {
      createTestEvent: CREATE_TEST_EVENT
    })
  }
}
</script>
<template>
  <div class="card col-12 col-md-6">
    <div class="card-header">
      <h2 class="header-title">Test Events & Alerts</h2>
    </div>
    <div class="card-body">
      <p>Tests MQTT connection, handles events and alerts.</p>
      <button @click="createTestEvent"
      class="btn btn-primary">Ping</button>
    </div>
  </div>
</template>
