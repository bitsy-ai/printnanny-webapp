import * as api from 'printnanny-api-client'
import { TestEventType } from 'printnanny-api-client'

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
    console.log("Received api response to get device", res)
    return res.data
  },
  async createTestEvent(deviceId: number, eventType: TestEventType) {
    const thisapi = api.DevicesApiFactory(configuration)
    const req: api.TestEventRequest = {
      event_type: api.TestEventType.Ping,
      status: api.EventStatus.Sent,
      source: api.EventSource.Printnanny,
      model: api.EventModel.TestEvent,
      // command: true
    }
    const res = await thisapi.devicesEventsCreate(
      deviceId,
      req
    )
    return res.data
  },
  async startMonitoring(deviceId: number) {
    const thisapi = api.DevicesApiFactory(configuration, process.env.BASE_API_URL)
    const req = { monitoring_active: true }
    const res = await thisapi.devicesPartialUpdate(
      deviceId,
      req
    )
    return res.data
  },
  async stopMonitoring(deviceId: number) {
    const thisapi = api.DevicesApiFactory(configuration, process.env.BASE_API_URL)
    const req = { monitoring_active: false }
    const res = await thisapi.devicesPartialUpdate(
      deviceId,
      req
    )
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
