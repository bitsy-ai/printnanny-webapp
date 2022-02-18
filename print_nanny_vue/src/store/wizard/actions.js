import {
  SET_MQTT_PING_EVENT,
  APPEND_MQTT_PING_EVENT_LOG

} from './mutations'
import api from '@/services/devices'

export const CREATE_MQTT_PING_EVENT = 'create_mqtt_ping_event'
export default {
  async [CREATE_MQTT_PING_EVENT] ({ commit, state, dispatch }, data) {
    // const { hostname, deviceId } = data
    // console.log('CREATE_MQTT_PING_EVENT CALLED WITH', deviceId, hostname)
    // const res = await api.createTestEvent(deviceId, TestEventType.Ping)
    // console.log('Created event', res)
    // commit(SET_MQTT_PING_EVENT, res.data)
    // commit(APPEND_MQTT_PING_EVENT_LOG, `Sent event ${res.data.event_type} to ${hostname}`)
    // commit(APPEND_MQTT_PING_EVENT_LOG, `Waiting for ${hostname} to acknowledge ${res.data.event_type}`)
  }
}
