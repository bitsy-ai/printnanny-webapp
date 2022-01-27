import {
  SET_DEVICE_DATA,
  SET_CREATE_EVENT_RESPONSE
} from './mutations'
import api from '@/services/devices'
import { TestEventType } from 'printnanny-api-client'

export const MQTT_PING_EVENT = 'mqtt_ping_event'
export const START_MONITORING = 'start_monitoring'
export const STOP_MONITORING = 'stop_monitoring'

export default {
  async [MQTT_PING_EVENT] ({ commit, state, dispatch }, deviceId) {
    const res = await api.createTestEvent(deviceId, TestEventType.Ping)
    console.log('Got res', res)
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
