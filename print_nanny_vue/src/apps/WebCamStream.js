import { Vue, store } from './AppFactory'
import WebCamStream from '@/components/WebCamStream'

const apps = document.querySelectorAll('.webrtc-stream-app')
export default Array.prototype.forEach.call(apps, (el, index) => new Vue({
  el,
  components: { WebCamStream },
  store,
  data: function () {
    const htmlId = el.dataset.htmlId
    const d = JSON.parse(JSON.parse(document.getElementById(htmlId).textContent))
    return { device: d }
  },
  template: '<webrtc-stream v-model="device" />'
}))
