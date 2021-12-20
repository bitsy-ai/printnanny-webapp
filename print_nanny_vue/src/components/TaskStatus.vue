<script>
import { mapActions, mapState } from 'vuex'
import { SET_DATA, TASKS_DROPDOWN_MODULE } from '@/store/tasks'

export default {
  props: {
    deviceId: Number,
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
    const url = process.env.DEVICE_US_URL + this.deviceId + '/'
    console.log('Starting connection to WebSocket Server')
    this.connection = new WebSocket(url)

    this.connection.onmessage = function (msg) {
      const data = JSON.parse(msg.data)
      console.log('Received event', data)
      if (data.type != 'task.status') {
        console.debug(`TaskStatus id=${this.taskId} ignoring ws event type`, data.type)
      } else if (data.type == 'task.status' && data.data.id != this.deviceId) {
        console.debug(`TaskStatus id=${this.taskId} ignoring event for other task`, data)
      } else {
        this.data.taskDisplay = data.data.last_status.status_display
        this.data.status = data.data.last_status.status
        this.data.color = data.data.last_status.css_class
        this.data.taskStatusDisplay = data.data.task_type_display
      }
      console.log('Received parsed data', data)
    }

    this.connection.onopen = function (event) {
      console.log(event)
      console.log('Successfully connected to the echo websocket server...')
    }

    // this.$connect(url)
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
    <a v-if="wikiUrl != 'undefined'" target='_blank' :href="`${wikiUrl}`">See Wiki for more info</a>
  </b-popover>
</span>

</template>
