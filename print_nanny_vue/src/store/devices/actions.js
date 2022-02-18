import {
  SET_DEVICE_DATA
} from './mutations'
import api from '@/services/devices'

export const GET_DEVICE = 'get_device'
export const START_MONITORING = 'start_monitoring'
export const STOP_MONITORING = 'stop_monitoring'
export const SETUP_COMPLETE = 'setup_complete'

export default {
  async [SETUP_COMPLETE] ({ commit, state, dispatch }, device) {
    const res = await api.setupComplete(device)
    commit(SET_DEVICE_DATA, res)
  },
  async [GET_DEVICE] ({ commit, state, dispatch }, deviceId) {
    const res = await api.getDevice(deviceId)
    commit(SET_DEVICE_DATA, res)
  },
  async [START_MONITORING] ({ commit, state, dispatch }, device) {
    const res = await api.startMonitoringTask(device)
    commit(SET_DEVICE_DATA, res)
  },
  async [STOP_MONITORING] ({ commit, state, dispatch }, device) {
    const res = await api.stopMonitoringTask(device)
    commit(SET_DEVICE_DATA, res)
  }
}
