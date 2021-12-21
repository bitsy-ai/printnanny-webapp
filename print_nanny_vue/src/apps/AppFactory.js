// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import VueNativeSock from 'vue-native-websocket'
import VueCookies from 'vue-cookies'
import store from '../store'
// eslint-disable-next-line
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'

import '@/scss/app.scss'

Vue.config.productionTip = false

Vue.use(VueCookies)
Vue.use(BootstrapVue)
// Vue.use(VueNativeSock, process.env.ALERTS_WS_URL, { store: store, format: 'json', reconnection: true })

export { Vue, store }
