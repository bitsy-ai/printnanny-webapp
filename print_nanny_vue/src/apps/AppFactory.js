import Vue from 'vue'
import VueNativeSock from 'vue-native-websocket'
import VueCookies from 'vue-cookies'
import store from '../store'
import Vuelidate from '@vuelidate/core'
import VueCompositionAPI from '@vue/composition-api'
import { BootstrapVue } from 'bootstrap-vue'
import { PRINTNANNY_WS_URL } from '../services/api'

Vue.config.productionTip = false
Vue.use(Vuelidate)
Vue.use(VueCompositionAPI)
Vue.use(VueCookies)
Vue.use(BootstrapVue)
Vue.use(
  VueNativeSock,
  PRINTNANNY_WS_URL,
  {
    store: store,
    format: 'json',
    reconnection: true,
    reconnectionAttempts: 10,
    reconnectionDelay: 6,
    connectManually: true
  }
)

export { Vue, store }
