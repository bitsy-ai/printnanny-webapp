<script>
// import { mapActions, mapState } from 'vuex'
// import { SET_DATA, TASKS_DROPDOWN_MODULE } from '@/store/tasks'

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
    const url = process.env.DEVICE_WS_URL + this.taskLocal.device + '/'
    this.connection = new WebSocket(url)

    this.connection.onmessage = function (msg) {
      const data = JSON.parse(msg.data)
      console.debug('Received event', data)
      if (data.type === 'task.status') {
        console.debug('Received taskLocal.status event', data)
        self.taskLocal = data.data
      }
    }

    this.connection.onopen = function (event) {
      console.log('Successfully connected to websocket', event)
    }
    this.$connect(url)
  }
}
</script>

<template>
<span>
    <b-badge :variant="taskLocal.last_status.css_class" v-bind:id="`task-status-${taskLocal.id}`">
    <i class="mdi mdi-information"></i>
    {{taskLocal.task_type_display}}: {{ taskLocal.last_status.status }}</b-badge>
  <b-popover v-bind:target="`task-status-${taskLocal.id}`" triggers="hover focus click" placement="right">
    <template #title>Task: {{taskLocal.task_type_display }} </template>
    <p>{{ taskLocal.last_status.status_display }}</p>
    <p>{{ taskLocal.last_status.detail }}</p>
    <a target='_blank' :href="`${ taskLocal.last_status.wiki_url }`">See Wiki for more info</a>
  </b-popover>
</span>

</template>
