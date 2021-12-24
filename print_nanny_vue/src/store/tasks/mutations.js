import { TASKS } from './state'
export const SET_TASK_DATA = 'SET_TASK_DATA'
export default {
  [SET_TASK_DATA] (state, data) {
    console.debug('setting task data', data, 'state', state)
    state[TASKS] = { ...state[TASKS], [data.data.id]: data.data }
  }
}
