import { SENT_EVENTS, RECEIVED_EVENTS, EVENTS } from './state'

export const APPEND_EVENT = 'APPEND_EVENT'
export const SET_SENT_EVENT = 'SET_SENT_EVENT'
export const SET_RECEIVED_EVENT = 'SET_RECEIVED_EVENT'
export default {
  [SET_SENT_EVENT] (state, data) {
    console.debug('setting sent events data', data, 'state', state)
    // state[SENT_EVENTS] = state[SENT_EVENTS].push(data)
  },
  [SET_RECEIVED_EVENT] (state, data) {
    console.debug('setting received events data', data, 'state', state)
    // state[RECEIVED_EVENTS] = state[RECEIVED_EVENTS].push(data)
  },
  [APPEND_EVENT] (state, data) {
    console.debug('Appending to EVENTS array')
    state[EVENTS] = state[EVENTS].push(data)
  }
}
