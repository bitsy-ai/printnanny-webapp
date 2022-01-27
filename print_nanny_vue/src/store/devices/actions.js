import {
  SET_DEVICE_DATA,
  SET_CREATE_EVENT_RESPONSE
} from './mutations'
import api from '@/services/devices'

export const CREATE_TEST_EVENT = 'create_test_event'
export const START_MONITORING = 'start_monitoring'
export const STOP_MONITORING = 'stop_monitoring'

export default {
  async [CREATE_TEST_EVENT] ({ commit, state, dispatch }, deviceId, eventType) {
    const res = await api.createTestEvent(deviceId, eventType)
    console.log('Recevied res in CREATE_TEST_EVENT action', res)
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
