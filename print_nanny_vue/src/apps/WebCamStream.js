import { Vue, store } from './AppFactory'
import WebCamStream from '@/components/WebCamStream'

const apps = document.querySelectorAll('.webcam-stream-app')
export default Array.prototype.forEach.call(apps, (el, index) => new Vue({
  el,
  components: { WebCamStream },
  store,
  data: function () {
    const deviceHtmlId = el.dataset.deviceHtmlId
    const taskHtmlId = el.dataset.taskHtmlId
    const d = JSON.parse(JSON.parse(document.getElementById(deviceHtmlId).textContent))
    const t = JSON.parse(JSON.parse(document.getElementById(taskHtmlId).textContent))

    return { device: d, task: t }
  }
}))
