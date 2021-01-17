import Vue from 'vue'
import Vuex from 'vuex'

import alerts, { ALERTS_DROPDOWN_MODULE, ALERTS_TABLE_MODULE } from './alerts'
import mutations from './mutations'

Vue.use(Vuex)

export default new Vuex.Store({
  strict: !process.env === 'production',
  modules: {
    [ALERTS_DROPDOWN_MODULE]: alerts,
    [ALERTS_TABLE_MODULE]: alerts
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
