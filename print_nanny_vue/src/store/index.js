import Vue from 'vue'
import Vuex from 'vuex'

import alerts, { ALERTS_MODULE } from './alerts'
import devices, { DEVICE_MODULE } from './devices'
import settings, { SETTINGS_MODULE } from './settings'
import tasks, { EVENTS_MODULE } from './events'
import wizard, { WIZARD_MODULE } from './wizard'

import mutations from './mutations'

Vue.use(Vuex)

export default new Vuex.Store({
  strict: !process.env === 'production',
  modules: {
    [ALERTS_MODULE]: alerts,
    [SETTINGS_MODULE]: settings,
    [EVENTS_MODULE]: tasks,
    [DEVICE_MODULE]: devices,
    [WIZARD_MODULE]: wizard
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
