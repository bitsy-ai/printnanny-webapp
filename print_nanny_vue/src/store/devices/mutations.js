import { DEVICE, JANUS_AUTH } from './state'

export const SET_DEVICE_DATA = 'SET_DEVICE_DATA'
export const SET_JANUS_AUTH = 'SET_JANUS_AUTH'

export default {
  [SET_JANUS_AUTH] (state, data) {
    console.debug('setting janus auth', data)
    state[JANUS_AUTH] = data.data
  },
  [SET_DEVICE_DATA] (state, data) {
    console.debug('setting device data', data, 'state', state)
    state[DEVICE] = data.data
  }
}
