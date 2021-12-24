<script>
import { mapActions, mapState, mapMutations } from 'vuex'
import {
  TASKS,
  TASK_MODULE,
  SET_DATA
} from '@/store/tasks'

export default {
  props: {
    taskId: {
      type: Number,
      required: true
    },
    taskIdx: {
      type: Number,
      required: true
    }
  },
  computed: {
    ...mapState(TASK_MODULE, {
      tasks: TASKS
    })
  },
  methods: {
    ...mapMutations(TASK_MODULE, [
      SET_DATA
    ])
  },
  created: function () {
    // set initial task data from parent TaskStatus.js module
    console.log(this)
    this.SET_DATA({ data: this.$parent.task })
    // this.$store.state[TASK_MODULE].data = this.$parent.task
  }
}
</script>

<template>
<span>
    <b-badge href="#" :variant="tasks[taskId].last_status.css_class" v-bind:id="`task-status-${tasks[taskId].id}`">
    <i class="mdi mdi-information"></i>
    {{ tasks[taskId].task_type_display }}: {{ tasks[taskId].last_status.status }}</b-badge>
  <b-popover v-bind:target="`task-status-${tasks[taskId].id}`" triggers="hover focus click" placement="right">
    <template #title>Task: {{ tasks[taskId].task_type_display }} </template>
    <p>{{ tasks[taskId].last_status.status_display }}</p>
    <p>{{ tasks[taskId].last_status.detail }}</p>
    <a target='_blank' :href="`${ tasks[taskId].last_status.wiki_url }`">See Wiki for more info</a>
  </b-popover>
</span>

</template>
