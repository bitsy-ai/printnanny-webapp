import { DEVICE, JANUS_AUTH } from './state'

export const SET_DEVICE_DATA = 'SET_DEVICE_DATA'

export default {
  [SET_DEVICE_DATA] (state, data) {
    console.debug('setting device data', data, 'state', state)
    state[DEVICE] = data
  }
}
