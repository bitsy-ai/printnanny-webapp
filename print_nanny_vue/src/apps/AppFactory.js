import Vue from 'vue'
import VueNativeSock from 'vue-native-websocket'
import VueCookies from 'vue-cookies'
import store from '../store'
import Vuelidate from '@vuelidate/core'
import VueCompositionAPI from '@vue/composition-api'
import { BootstrapVue } from 'bootstrap-vue'
import { WS_URL } from '../services/api'
import '@/scss/app.scss'

Vue.config.productionTip = false
Vue.use(Vuelidate)
Vue.use(VueCompositionAPI)
Vue.use(VueCookies)
Vue.use(BootstrapVue)
Vue.use(
  VueNativeSock,
  WS_URL,
  { store: store, format: 'json', reconnection: true }
)

export { Vue, store }
