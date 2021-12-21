export const SET_DATA = 'set_data'

export default {
  [SET_DATA] (state, data) {
    console.log('setting data state', data)
    state.data = data
  }
}
