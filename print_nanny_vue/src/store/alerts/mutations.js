import Vue from 'vue'
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
  }
}
