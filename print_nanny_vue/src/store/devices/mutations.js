import { DEVICE } from './state'

export const SET_DEVICE_DATA = 'SET_DEVICE_DATA'
export const SET_JANUS_STREAM_DATA = 'SET_JANUS_STREAM_DATA'
export default {
  [SET_DEVICE_DATA] (state, data) {
    console.debug('setting Device data', data, 'previous state', state)
    state[DEVICE] = data
  },
  [SET_JANUS_STREAM_DATA] (state, data) {
    console.debug('setting JanusStream data', data, 'previous state', state)
    state[SET_JANUS_STREAM_DATA] = data
  }
}
