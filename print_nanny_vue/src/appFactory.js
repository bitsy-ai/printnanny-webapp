// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import VueCookies from 'vue-cookies'
import Vuex from 'vuex'
import VueNativeSock from 'vue-native-websocket'

// eslint-disable-next-line
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'

import storeConfig from './store'

import './scss/app.scss'

Vue.config.productionTip = false
Vue.use(Vuex)
Vue.use(VueCookies)
Vue.use(BootstrapVue)

const store = new Vuex.Store(storeConfig)

Vue.use(VueNativeSock, process.env.ALERTS_WEBSOCKET, { store: store, format: 'json', reconnection: true })

export { Vue, store }
