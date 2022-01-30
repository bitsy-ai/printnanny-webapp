import { mapMutations, mapState } from 'vuex'

import { Vue, store } from './AppFactory'
// import WebCamStream from '@/components/WebCamStream'
// import {
//   DEVICES,
//   DEVICE_MODULE,
//   SET_DEVICE_DATA
// } from '@/store/devices'
// import {
//   TASKS,
//   TASK_MODULE,
//   SET_TASK_DATA
// } from '@/store/tasks'

const apps = document.querySelectorAll('.webcam-stream-app')
export default Array.prototype.forEach.call(apps, (el, index) => new Vue({
  el,
  // components: { Video },
  store
  // computed: {
  //   ...mapState(DEVICE_MODULE, {
  //     devices: DEVICES,
  //     tasks: TASKS
  //   })
  // },
  // methods: {
  //   ...mapMutations(DEVICE_MODULE, [
  //     SET_DEVICE_DATA
  //   ]),
  //   ...mapMutations(TASK_MODULE, [
  //     SET_TASK_DATA
  //   ])
  // },
  // created: function () {
  //   const deviceHtmlId = el.dataset.deviceHtmlId
  //   const taskHtmlId = el.dataset.taskHtmlId
  //   const d = JSON.parse(JSON.parse(document.getElementById(deviceHtmlId).textContent))
  //   const t = JSON.parse(JSON.parse(document.getElementById(taskHtmlId).textContent))
  //   this.SET_DEVICE_DATA({ data: d })
  //   this.SET_TASK_DATA({ data: t })
  // }
}))
