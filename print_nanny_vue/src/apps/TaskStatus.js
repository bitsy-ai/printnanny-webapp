import { mapMutations, mapState } from 'vuex'
import { Vue, store } from './AppFactory'
import TaskStatus from '@/components/TaskStatus'
import {
  TASKS,
  TASK_MODULE,
  SET_TASK_DATA
} from '@/store/tasks'

const apps = document.querySelectorAll('.task-status-app')
export default Array.prototype.forEach.call(apps, (el, index) => new Vue({
  el,
  components: { TaskStatus },
  store,
  methods: {
    ...mapMutations(TASK_MODULE, [
      SET_TASK_DATA
    ])
  },
  data: {
    taskId: {
      type: Number,
      required: true
    }
  },
  computed: {
    ...mapState(TASK_MODULE, {
      tasks: TASKS
    })
  },
  data: function () {
    const taskId = parseInt(el.dataset.taskId)
    return { taskId }
  },
  created: function () {
    const htmlId = el.dataset.htmlId
    const d = JSON.parse(JSON.parse(document.getElementById(htmlId).textContent))
    this.SET_TASK_DATA({ data: d })
  },
  template: '<task-status :task-id=taskId />'
}))
