import {
  SET_MQTT_PING_EVENT,
  APPEND_MQTT_PING_EVENT_LOG

} from './mutations'
import api from '@/services/devices'
import { TestEventType } from 'printnanny-api-client'

export const CREATE_MQTT_PING_EVENT = 'create_mqtt_ping_event'
export default {
  async [CREATE_MQTT_PING_EVENT] ({ commit, state, dispatch }, deviceId) {
    const res = await api.createTestEvent(deviceId, TestEventType.Ping)
    commit(SET_MQTT_PING_EVENT, res)
    commit(APPEND_MQTT_PING_EVENT_LOG, res)
  }
}
