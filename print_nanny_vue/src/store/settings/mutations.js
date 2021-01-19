import Vue from 'vue'
export const SET_DATA = 'set_data'
export const SET_ALERT_METHODS = 'set_alert_methods'

export default {

  [SET_DATA] (state, data) {
    console.log('setting data state', data)
    state.data = data
  }
}
