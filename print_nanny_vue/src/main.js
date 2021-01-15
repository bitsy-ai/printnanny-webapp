// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import Vuex from 'vuex'

// eslint-disable-next-line
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import App from './App'
import router from './router'

Vue.config.productionTip = false
Vue.use(Vuex)

/* eslint-disable no-new */
const store = new Vuex.Store({
  state: {
    alerts: []
  },
  mutations: {
    dismissAlert (state) {
      state.count++
    }
  }
})

/* eslint-disable no-new */
new Vue({
  el: '#alerts',
  router,
  components: { App },
  template: '<App/>',
  store
})
