<script>
import { mapMutations, mapState, macActions } from 'vuex'
import { WIZARD_MODULE} from '@/store/wizard'
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
    mapActions(WIZARD_MODULE)
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
      <button class="btn btn-primary">Ping</button>
    </div>
  </div>
</template>
