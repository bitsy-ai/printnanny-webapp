import { Vue, store } from './AppFactory'
import TaskStatus from '@/components/TaskStatus'

const apps = document.querySelectorAll('.task-status-app')
export default Array.prototype.forEach.call(apps, (el, index) => new Vue({
  el,
  components: { TaskStatus },
  store,
  data: function () {
    const htmlId = el.dataset.htmlId
    const d = JSON.parse(JSON.parse(document.getElementById(htmlId).textContent))
    return { task: d, taskIdx: index }
  },
  template: '<task-status :task-id="task.id" :task-idx="taskIdx" />'
}))
