import * as api from 'printnanny-api-client'
import { WebRTCEvent } from 'printnanny-api-client'
import { DEVICE_MODULE, SET_JANUS_STREAM_DATA } from '../devices'
import { SET_SENT_EVENT, SET_RECEIVED_EVENT } from './mutations'
import { PRINTNANNY_API_CONFIG } from '../../services/api'

export const STREAM_START = 'STREAM_START'
export const STREAM_STOP = 'STREAM_STOP'

export default {
  // TODO
  // import { ActionContext } from "vuex";
  // context: ActionContext<S,R>
  async [STREAM_START](context: any, { device, stream }: { device: number, stream: number }) {
    const thisapi = api.EventsApiFactory(PRINTNANNY_API_CONFIG)
    const req: api.WebRTCCommandCreateRequest = {
      model: api.WebRTCCommandModel.WebRtcCommand,
      event_name: api.WebRTCCommandName.Start,
      device: device,
      source: api.EventSource.PrintnannyWebapp,
      stream: stream
    }
    console.log("eventsCreate req", req)
    const res = await thisapi.eventsCreate(req)
    const event = res.data as WebRTCEvent
    console.log("eventsCreate response", res)
    context.commit(SET_SENT_EVENT, event)
  },
  async [STREAM_STOP](context: any, { device, stream }: { device: number, stream: number }) {
    const thisapi = api.EventsApiFactory(PRINTNANNY_API_CONFIG)
    const req: api.WebRTCCommandCreateRequest = {
      model: api.WebRTCCommandModel.WebRtcCommand,
      event_name: api.WebRTCCommandName.Stop,
      device: device,
      source: api.EventSource.PrintnannyWebapp,
      stream: stream
    }
    console.log("eventsCreate req", req)
    const res = await thisapi.eventsCreate(req)
    const event = res.data as WebRTCEvent
    console.log("eventsCreate response", res)
    context.commit(SET_SENT_EVENT, event)
  }
}
