<script>
import { mapActions, mapState } from 'vuex'
import { SET_DATA, TASKS_DROPDOWN_MODULE } from '@/store/tasks'

export default {
  props: {
    taskId: Number,
    taskTypeDisplay: String,
    taskStatusDisplay: String,
    wikiUrl: String,
    msg: String,
    color: String,
    status: String
  },
  //   data: function () {
  //     return {
  //       taskId: 0,
  //       taskDisplay: 'Loading',
  //       wikiUrl: '',
  //       msg: '',
  //       color: 'secondary',
  //       status: ''
  //     }
  //   },
  created: function () {
    console.log(this) // And here is - in $attrs object
    // this.data = this.$attrs
  }
}
</script>

<template>
<span>
    <b-badge :variant="color" v-bind:id="`task-status-${taskId}`">
    <i class="mdi mdi-information"></i>
    {{taskTypeDisplay}}: {{ status }}</b-badge>
  <b-popover v-bind:target="`task-status-${taskId}`" triggers="hover focus click" placement="right">
    <template #title>Task: {{taskTypeDisplay}} </template>
    Status: <strong>{{ status }}</strong>
    <p>{{ taskStatusDisplay }}</p>
    <p v-if="msg != 'undefined'">{{ msg }}</p>
    <a v-if="wikiUrl != 'undefined'" target='_blank' :href="`${wikiUrl}">See Wiki for more info</a>
  </b-popover>
</span>

</template>
