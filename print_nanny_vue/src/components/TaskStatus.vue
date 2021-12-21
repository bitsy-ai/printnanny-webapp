<script>
import { mapActions, mapState } from 'vuex'
import { SET_DATA, TASKS_DROPDOWN_MODULE } from '@/store/tasks'

export default {
  props: {
    task: {
      type: Object,
      required: true
    }
  },
  model: {
    prop: 'task',
    event: 'taskupdate'
  },
  computed: {
    taskLocal: {
      get: function () {
        return this.task
      },
      set: function (value) {
        console.log('Setting taskLocal to', value)
        this.$emit('taskupdate', value)
      }
    }
  },
  created: function () {
    const self = this

    const url = process.env.DEVICE_US_URL + this.taskLocal.device + '/'
    console.log('Starting connection to WebSocket Server')
    this.connection = new WebSocket(url)

    this.connection.onmessage = function (msg) {
      const data = JSON.parse(msg.data)
      console.log('Received event', data)
      if (data.type == 'task.status') {
        console.log('Received taskLocal.status event', data)
        console.log(this)
        console.log(self)
        self.taskLocal = data.data
      }
      // if (data.type != 'taskLocal.status') {
      //   console.debug(`TaskStatus id=${this.taskId} ignoring ws event type`, data.type)
      // } else if (data.type == 'taskLocal.status' && data.id != this.taskLocal.id) {
      //   console.debug(`TaskStatus id=${this.taskLocal.id} ignoring event for other task`, data)
      // } else {
      //   console.log('Updating task', data.data)
      //   this.task = data.data
      // }
      // console.log('Received parsed data', data)
    }

    this.connection.onopen = function (event) {
      console.log(event)
      console.log('Successfully connected to the echo websocket server...')
    }

    this.$connect(url)
  }
}
</script>

<template>
<span>
    <b-badge :variant="taskLocal.last_status.css_class" v-bind:id="`task-status-${taskLocal.id}`">
    <i class="mdi mdi-information"></i>
    {{taskLocal.task_type_display}}: {{ taskLocal.last_status.status_display }}</b-badge>
  <b-popover v-bind:target="`task-status-${taskLocal.id}`" triggers="hover focus click" placement="right">
    <template #title>Task: {{taskLocal.task_type_display}} </template>
    <p>{{ taskLocal.last_status.status_display }}</p>
    <p>{{ taskLocal.last_status.detail }}</p>
    <a target='_blank' :href="`${ taskLocal.last_status.wiki_url }`">See Wiki for more info</a>
  </b-popover>
</span>

</template>
