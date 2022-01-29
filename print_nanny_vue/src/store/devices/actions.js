import {
  SET_DEVICE_DATA,
  SET_JANUS_AUTH
} from './mutations'
import api from '@/services/devices'

export const GET_JANUS_AUTH = 'get_janus_auth'
export const GET_DEVICE = 'get_device'
export const START_MONITORING = 'start_monitoring'
export const STOP_MONITORING = 'stop_monitoring'

export default {
  async [GET_DEVICE] ({ commit, state, dispatch }, deviceId) {
    const res = await api.getDevice(deviceId)
    commit(SET_DEVICE_DATA, res)
  },
  async [START_MONITORING] ({ commit, state, dispatch }, device) {
    const res = await api.startMonitoring(device)
    commit(SET_DEVICE_DATA, res)
  },
  async [STOP_MONITORING] ({ commit, state, dispatch }, device) {
    const res = await api.stopMonitoring(device)
    commit(SET_DEVICE_DATA, res)
  }
}
