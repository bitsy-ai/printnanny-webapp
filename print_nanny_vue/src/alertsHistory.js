
import { Vue, store } from './appFactory'
import AlertsHistory from './widgets/AlertsHistory'

import router from './router'

export default new Vue({
  el: '#alerts-history-app',
  router,
  store,
  components: { AlertsHistory },
  template: '<AlertsHistory />'
})
