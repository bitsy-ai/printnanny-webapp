export const SET_DATA = 'SET_DATA'
export const SET_INDEX = 'SET_INDEX'
export default {
  [SET_INDEX] (state, index, data) {

  },
  [SET_DATA] (state, data) {
    console.debug('setting task data', data, 'state', state)
    state.data = { ...state.data, [data.data.id]: data.data }
  }
}
