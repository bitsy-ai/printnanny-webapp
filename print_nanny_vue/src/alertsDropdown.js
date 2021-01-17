import { Vue, store } from './appFactory'
import AlertsDropdown from './widgets/AlertsDropdown'
// import router from './router'

/* eslint-disable no-new */

export default new Vue({
  el: '#alerts-dropdown-app',
  // router,
  store,
  components: { AlertsDropdown },
  template: '<AlertsDropdown/>'
})
