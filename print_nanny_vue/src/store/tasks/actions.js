import service from '@/services/devices'
import * as api from 'printnanny-api-client'

import { SET_ACTIVE_MONITORING_TASK } from './mutations'
export const MONITOR_START_TASK = 'MONITOR_START_TASK'
export const MONITOR_STOP_TASK = 'MONITOR_STOP_TASK'

export default {
  async [MONITOR_START_TASK] ({ commit, state, dispatch }, device, stream) {
    const res = await service.createJanusTask(device, stream, api.JanusTaskType.CloudMonitorStart)
    commit(SET_ACTIVE_MONITORING_TASK, res)
  },
  async [MONITOR_STOP_TASK] ({ commit, state, dispatch }, device) {
    const res = await service.createJanusTask(device, stream, api.JanusTaskType.CloudMonitorStop)
    commit(SET_ACTIVE_MONITORING_TASK, res)
  }
}
