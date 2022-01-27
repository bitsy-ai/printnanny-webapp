import { DEVICE_SCAN_RESULT, MQTT_PING_RESULT } from './state'

export const SET_DEVICE_SCAN_RESULT = 'SET_DEVICE_SCAN_RESULT'
export const SET_MQTT_PING_RESULT = 'SET_MQTT_PING_RESULT'
export default {
  [SET_DEVICE_SCAN_RESULT] (state, data) {
    console.debug('setting device data', data, 'state', state)
    state[DEVICE_SCAN_RESULT] = data
  },
  [SET_MQTT_PING_RESULT] (state, data) {
    state[MQTT_PING_RESULT] = data
  }
}
