import Vue from 'vue'
import Router from 'vue-router'
import Alerts from '@/components/Alerts'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Alerts',
      component: Alerts
    }
  ]
})
