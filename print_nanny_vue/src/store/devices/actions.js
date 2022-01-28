import {
  SET_DEVICE_DATA

} from './mutations'
import api from '@/services/devices'

export const START_MONITORING = 'start_monitoring'
export const STOP_MONITORING = 'stop_monitoring'

export default {
  async [START_MONITORING] ({ commit, state, dispatch }, device) {
    const res = await api.startMonitoring(device)
    commit(SET_DEVICE_DATA, res)
  },
  async [STOP_MONITORING] ({ commit, state, dispatch }, device) {
    const res = await api.stopMonitoring(device)
    commit(SET_DEVICE_DATA, res)
  }
}
