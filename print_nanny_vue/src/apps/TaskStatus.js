import VueNativeSock from 'vue-native-websocket'
import { Vue, store } from './AppFactory'
import TaskStatus from '@/components/TaskStatus'

// Vue.use(VueNativeSock, process.env.DEVICE_US_URL, { store: store, format: 'json', reconnection: true, connectManually: true })

const apps = document.querySelectorAll('.task-status-app')
export default Array.prototype.forEach.call(apps, (el, index) => new Vue({
  el,
  components: { TaskStatus },
  store,
  data: function () { return Object.assign({}, el.dataset) },
  template: `<task-status
    v-bind:device-id='${el.dataset.deviceId}'
    v-bind:task-id='${el.dataset.taskId}'
    v-bind:task-status-display="'${el.dataset.taskStatusDisplay}'"
    v-bind:task-type-display="'${el.dataset.taskTypeDisplay}'"
    v-bind:wiki-url="'${el.dataset.taskWikiUrl}'"
    v-bind:msg="'${el.dataset.taskMsg}'"
    v-bind:color="'${el.dataset.color}'"
    v-bind:status="'${el.dataset.taskStatus}'"
    />`
}))
