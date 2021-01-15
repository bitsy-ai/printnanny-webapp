// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import Vuex from 'vuex'

// eslint-disable-next-line
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import AlertApp from './AlertApp'
import router from './router'
import _store from './store'

import './scss/app.scss'

Vue.config.productionTip = false
Vue.use(Vuex)
Vue.use(BootstrapVue)

const store = new Vuex.Store(_store)
/* eslint-disable no-new */
export default {
  alerts: new Vue({
    el: '#alerts',
    router,
    store,
    components: { AlertApp },
    template: '<AlertApp/>'
  })
}
