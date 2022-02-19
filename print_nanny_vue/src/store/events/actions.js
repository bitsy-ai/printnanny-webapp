import service from '@/services/devices'
import * as api from 'printnanny-api-client'

import { SET_SENT_EVENT, SET_RECEIVED_EVENT } from './mutations'
export const STREAM_START = 'STREAM_START'
export const STREAM_STOP = 'STREAM_STOP'

export default {
  async [STREAM_START] ({ commit, state, dispatch }, device) {
    const req = {
      event_type: api.WebRTCEventEventTypeEnum.Start,
      device: device,
      source: api.EventSource.PrintnannyWebapp
    }
    const res = await service.createEvent(req)
    commit(SET_SENT_EVENT, res)
  },
  async [STREAM_STOP] ({ commit, state, dispatch }, device) {
    const req = {
      event_type: api.WebRTCEventEventTypeEnum.Stop,
      device: device,
      source: api.EventSource.PrintnannyWebapp
    }
    const res = await service.createEvent(req)
    commit(SET_SENT_EVENT, res)
  }
}
