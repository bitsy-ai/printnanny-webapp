import Vue from 'vue'
import Router from 'vue-router'
import AlertsTable from '@/widgets/AlertsTable'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/alerts/',
      name: 'AlertsTable',
      component: AlertsTable
    }
  ]
})
