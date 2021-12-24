import Vue from 'vue'
import Vuex from 'vuex'

import alerts, { ALERTS_MODULE } from './alerts'
import devices, { DEVICE_MODULE } from './devices'
import settings, { SETTINGS_MODULE } from './settings'
import tasks, { TASK_MODULE } from './tasks'

import mutations from './mutations'

Vue.use(Vuex)

export default new Vuex.Store({
  strict: !process.env === 'production',
  modules: {
    [ALERTS_MODULE]: alerts,
    [SETTINGS_MODULE]: settings,
    [TASK_MODULE]: tasks,
    [DEVICE_MODULE]: devices
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
