<script>
import { mapActions } from 'vuex'

export default {
  components: { },
  async created () {
    this.fetchUnreadAlerts()
    this.fetchRecentAlerts()
  },
  methods: {
    ...mapActions('alerts', [
      'fetchRecentAlerts', 'fetchUnreadAlerts', 'dismissAll', 'seenAll'

    ])
  }
}
</script>

<template>
    <div>alert history</div>
</template>
