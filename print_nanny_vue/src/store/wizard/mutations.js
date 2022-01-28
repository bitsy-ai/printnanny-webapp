import { DEVICE_SCAN_RESULT, MQTT_PING_EVENT, MQTT_PONG_EVENT, MQTT_PING_EVENT_LOG, MQTT_PONG_EVENT_LOG } from './state'

export const SET_DEVICE_SCAN_RESULT = 'SET_DEVICE_SCAN_RESULT'
export const SET_MQTT_PING_EVENT = 'SET_MQTT_PING_EVENT'
export const APPEND_MQTT_PING_EVENT_LOG = 'APPEND_MQTT_PING_EVENT_LOG'
export const SET_MQTT_PONG_EVENT = 'SET_MQTT_PONG_EVENT'
export const APPEND_MQTT_PONG_EVENT_LOG = 'APPEND_MQTT_PONG_EVENT_LOG'

export default {
  [SET_DEVICE_SCAN_RESULT] (state, data) {
    console.debug('setting device data', data, 'state', state)
    state[DEVICE_SCAN_RESULT] = data
  },
  [SET_MQTT_PING_EVENT] (state, data) {
    state[MQTT_PING_EVENT] = data
  },
  [SET_MQTT_PONG_EVENT] (state, data) {
    state[MQTT_PONG_EVENT] = data
  },
  [APPEND_MQTT_PING_EVENT_LOG] (state, data) {
    state[MQTT_PING_EVENT_LOG].push(data)
  },
  [APPEND_MQTT_PONG_EVENT_LOG] (state, data) {
    state[MQTT_PONG_EVENT_LOG].push(data)
  }
}
