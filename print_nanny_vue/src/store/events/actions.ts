import * as api from 'printnanny-api-client'

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
    const req: api.WebRTCEventRequest = {
      event_type: api.WebRTCEventEventTypeEnum.Start,
      device: device,
      source: api.EventSource.PrintnannyWebapp
    }
    const res = await thisapi.eventsCreate(req)
    console.log("eventsCreate response", res)
    context.commit(SET_SENT_EVENT, res.data)
  },
  async [STREAM_STOP](context: any, device: number) {
    const thisapi = api.EventsApiFactory(configuration)
    const req = {
      event_type: api.WebRTCEventEventTypeEnum.Stop,
      device: device,
      source: api.EventSource.PrintnannyWebapp
    }
    const res = await thisapi.eventsCreate(req)
    console.log("eventsCreate response", res)
    context.commit(SET_SENT_EVENT, res.data)
  }
}
