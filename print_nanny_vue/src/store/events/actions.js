import service from '@/services/devices'
import * as api from 'printnanny-api-client'

import { SET_SENT_EVENT, SET_RECEIVED_EVENT } from './mutations'
export const STREAM_START = 'STREAM_START'
export const STREAM_STOP = 'STREAM_STOP'

export default {
  async [STREAM_START] ({ commit, state, dispatch }, device, stream) {
    const res = await service.createJanusTask(device, stream, api.JanusTaskType.CloudMonitorStart)
    commit(SET_SENT_EVENT, res)
  },
  async [STREAM_STOP] ({ commit, state, dispatch }, device) {
    const res = await service.createJanusTask(device, stream, api.JanusTaskType.CloudMonitorStop)
    commit(SET_SENT_EVENT, res)
  }
}
