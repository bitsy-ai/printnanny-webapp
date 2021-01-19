
import { Vue, store } from './appFactory'
import AlertsTableApp from './widgets/AlertsTableApp'
import router from './router'
// import router from './router'
// import css files
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import { TablePlugin } from 'bootstrap-vue'
Vue.use(TablePlugin)

export default new Vue({
  el: '#alerts-table-app',
  router,
  store,
  components: { AlertsTableApp },
  template: '<AlertsTableApp />'
})
