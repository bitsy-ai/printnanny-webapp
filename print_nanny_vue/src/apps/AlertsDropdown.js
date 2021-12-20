import VueNativeSock from 'vue-native-websocket'
import { Vue, store } from './AppFactory'
import AlertsDropdown from '@/components/AlertsDropdown'
// import router from './router'

/* eslint-disable no-new */

export default new Vue({
  el: '#alerts-dropdown-app',
  // router,
  store,
  components: { AlertsDropdown },
  template: '<AlertsDropdown/>'
})
