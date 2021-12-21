export const SET_PAGINATION = 'set_pagination'
export const SET_DATA = 'set_data'
export const APPEND_DATA = 'append_data'

export default {
  [APPEND_DATA] (state, data) {
    state.data.concat(data)
  },
  [SET_PAGINATION] (state, pagination) {
    console.log('setting pagination state', pagination)
    state.pagination = pagination
  },

  [SET_DATA] (state, data) {
    console.log('setting data state', data)
    state.data = data
  },

  SOCKET_ONOPEN (state, event) {
    // Vue.prototype.$socket = event.currentTarget
    // state.socket.isConnected = true
    console.log('Socket connected', event)
  },
  SOCKET_ONCLOSE (state, event) {
    state.socket.isConnected = false
  },
  SOCKET_ONERROR (state, event) {
    console.error(state, event)
  },
  // default handler called for all methods
  SOCKET_ONMESSAGE (state, message) {
    console.log('Socket message received', message)
    state.socket.message = message
  },
  // mutations for reconnect methods
  SOCKET_RECONNECT (state, count) {
    console.info(state, count)
  },
  SOCKET_RECONNECT_ERROR (state) {
    state.socket.reconnectError = true
  }
}
