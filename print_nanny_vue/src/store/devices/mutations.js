import { DEVICES, CREATE_EVENT_RESPONSE } from './state'

export const SET_DEVICE_DATA = 'SET_DEVICE_DATA'
export const SET_CREATE_EVENT_RESPONSE = 'SET_CREATE_EVENT_RESPONSE'

export default {
  [SET_DEVICE_DATA] (state, data) {
    console.debug('setting device data', data, 'state', state)
    state[DEVICES] = { ...state[DEVICES], [data.data.id]: data.data }
  },
  [SET_CREATE_EVENT_RESPONSE] (state, data) {
    state[CREATE_EVENT_RESPONSE] = data
  }
}
