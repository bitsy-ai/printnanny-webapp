<script>
import { mapActions } from 'vuex'

export default {
  components: { },
  async created () {

  },
  methods: {
    ...mapActions('alerts', [

    ])
  }
}
</script>

<template>
    <div>alert history</div>
</template>
