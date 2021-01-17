
import { Vue, store } from './appFactory'
import AlertsTable from './widgets/AlertsTable'
// import { createResources } from './store/alerts'

// import router from './router'
// import css files
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import { TablePlugin } from 'bootstrap-vue'
Vue.use(TablePlugin)

// createResources()

export default new Vue({
  el: '#alerts-table-app',
  //   router,
  store,
  components: { AlertsTable },
  template: '<AlertsTable />'
})
