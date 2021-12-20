import { Vue, store } from './AppFactory'
import TaskStatus from '@/components/TaskStatus'
// import router from './router'

/* eslint-disable no-new */

// export default new Vue({
//   el: '.task-status-app',
//   // router,
//   store,
//   components: { TaskStatus },
//   template: '<TaskStatus/>'
// })

const apps = document.querySelectorAll('.task-status-app')
export default Array.prototype.forEach.call(apps, (el, index) => new Vue({
  el,
  components: { TaskStatus },
  store,
  data: function () { return Object.assign({}, el.dataset) },
  template: `<task-status 
    v-bind:task-id='${el.dataset.taskId}'
    v-bind:task-status-display="'${el.dataset.taskStatusDisplay}'"
    v-bind:task-type-display="'${el.dataset.taskTypeDisplay}'"
    v-bind:wiki-url="'${el.dataset.taskWikiUrl}'"
    v-bind:msg="'${el.dataset.taskMsg}'"
    v-bind:color="'${el.dataset.color}'"
    v-bind:status="'${el.dataset.taskStatus}'"
    />`
}))
