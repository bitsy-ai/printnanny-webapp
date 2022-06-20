// import { mapMutations, mapState } from 'vuex'
import { Vue, store } from './AppFactory'
import DeviceStatus from '@/components/DeviceStatus'

const apps = document.querySelectorAll('.device-status-app')
console.debug('Initializing .device-status-app from', apps)
export default Array.prototype.forEach.call(apps, (el, index) => new Vue({
  el,
  components: { DeviceStatus },
  store
}))
