import Vue from 'vue'
import Vuex from 'vuex'

import alerts, { ALERTS_MODULE } from './alerts'
import mutations from './mutations'

Vue.use(Vuex)

console.log(ALERTS_MODULE)
console.log(alerts)

export default new Vuex.Store({
  strict: !process.env === 'production',
  modules: {
    [ALERTS_MODULE]: alerts
  },
  state: () => ({
    socket: {
      isConnected: false,
      message: '',
      reconnectError: false
    }
  }),
  mutations: mutations
})
