import * as api from 'printnanny-api-client'
import { PolymorphicEventRequest } from 'printnanny-api-client'

const configuration = new api.Configuration({
  basePath: process.env.BASE_API_URL,
  baseOptions: {
    xsrfCookieName: 'csrftoken',
    xsrfHeaderName: 'X-CSRFTOKEN',
    withCredentials: true
  }
})

export default {
  async getDevice(deviceId: number) {
    const thisapi = api.DevicesApiFactory(configuration)
    const res = await thisapi.devicesRetrieve(deviceId)
    console.log("Response to devicesRetrieve", res)
    return res.data
  },
  async eventsCreate(req: api.PolymorphicEventRequest) {
    const thisapi = api.EventsApiFactory(configuration)
    const res = await thisapi.eventsCreate(req)
    console.log("eventsCreate response", res)
    return res.data
  },
  async setupComplete(deviceId: number) {
    const thisapi = api.DevicesApiFactory(configuration, process.env.BASE_API_URL)
    const req = { setup_complete: true }
    const res = await thisapi.devicesPartialUpdate(
      deviceId,
      req
    )
    return res.data
  },
}
