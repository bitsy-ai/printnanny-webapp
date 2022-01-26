import { DEVICE_SCAN_RESULT } from './state'

export const SET_DEVICE_SCAN_RESULT = 'SET_DEVICE_SCAN_RESULT'
export default {
  [SET_DEVICE_SCAN_RESULT] (state, data) {
    console.debug('setting device data', data, 'state', state)
    state[DEVICE_SCAN_RESULT] = data
  }
}
