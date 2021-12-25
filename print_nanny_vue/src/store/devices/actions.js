import {
  SET_DATA
} from './mutations'
import api from '@/services/devices'

export const START_MONITORING = 'start_monitoring'
export const STOP_MONITORING = 'stop_monitoring'
export default {
  [START_MONITORING] ({ commit, state, dispatch }, device) {
    await api.startMonitoring(device)
  },
  [STOP_MONITORING] ({ device, commit, state, dispatch }, device) {
    await api.stopMonitoring(device)
  }
}
