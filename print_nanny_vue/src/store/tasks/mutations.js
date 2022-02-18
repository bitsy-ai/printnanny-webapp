import { ACTIVE_MONITORING_TASK } from './state'

export const SET_ACTIVE_MONITORING_TASK = 'SET_MONITOR_START_TASK'
export const SET_MONITOR_STOP_TASK = 'SET_MONITOR_STOP_TASK'
export default {
  [ACTIVE_MONITORING_TASK] (state, data) {
    console.debug('setting task data', data, 'state', state)
    state[ACTIVE_MONITORING_TASK] = data
  }
}
