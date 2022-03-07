import * as api from 'printnanny-api-client'
import { WebRTCEvent } from 'printnanny-api-client'
import { DEVICE_MODULE, SET_JANUS_STREAM_DATA } from '../devices'
import { SET_SENT_EVENT, SET_RECEIVED_EVENT } from './mutations'
export const STREAM_START = 'STREAM_START'
export const STREAM_STOP = 'STREAM_STOP'

const configuration = new api.Configuration({
  basePath: process.env.BASE_API_URL,
  baseOptions: {
    xsrfCookieName: 'csrftoken',
    xsrfHeaderName: 'X-CSRFTOKEN',
    withCredentials: true
  }
})
export default {
  async [STREAM_START](context: any, device: number) {
    const thisapi = api.EventsApiFactory(configuration)
    const req: api.WebRTCEventCreateRequest = {
      event_type: api.WebRTCEventEventTypeEnum.WebRtcEvent,
      event_name: api.WebRTCEventName.Start,
      device: device,
      source: api.EventSource.PrintnannyWebapp,
    }
    const res = await thisapi.eventsCreate(req)
    const event = res.data as WebRTCEvent
    console.log("eventsCreate response", res)
    context.commit(SET_SENT_EVENT, event)
    // committing mutation to DEVICE_MODULE namespace requires root: true option on broadcast
    context.commit(`${DEVICE_MODULE}/${SET_JANUS_STREAM_DATA}`, event.stream, { root: true })
  },
  async [STREAM_STOP](context: any, device: number) {
    const thisapi = api.EventsApiFactory(configuration)
    const req = {
      event_type: api.WebRTCEventEventTypeEnum.WebRtcEvent,
      event_name: api.WebRTCEventName.Stop,
      device: device,
      source: api.EventSource.PrintnannyWebapp
    }
    const res = await thisapi.eventsCreate(req)
    console.log("eventsCreate response", res)
    context.commit(SET_SENT_EVENT, res.data)
  }
}
