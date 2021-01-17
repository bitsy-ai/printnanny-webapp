// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import VueCookies from 'vue-cookies'
import Vuex from 'vuex'
import VueNativeSock from 'vue-native-websocket'

// eslint-disable-next-line
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import AlertsDropdown from './widgets/AlertsDropdown'
import AlertsHistory from './widgets/AlertsHistory'

import router from './router'
import storeConfig from './store'

import './scss/app.scss'

Vue.config.productionTip = false
Vue.use(Vuex)
Vue.use(VueCookies)
Vue.use(BootstrapVue)

const store = new Vuex.Store(storeConfig)

Vue.use(VueNativeSock, process.env.ALERTS_WEBSOCKET, { store: store, format: 'json', reconnection: true })

/* eslint-disable no-new */
export default {
  alertsDropdown: new Vue({
    el: '#alerts-dropdown-app',
    router,
    store,
    components: { AlertsDropdown },
    template: '<AlertsDropdown/>'
  }),
  alertsHistory: new Vue({
    el: '#alerts-history-app',
    router,
    store,
    components: { AlertsHistory },
    template: '<AlertsHistory />'
  })
}
