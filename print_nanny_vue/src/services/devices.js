import * as api from 'printnanny-api-client'

const configuration = new api.Configuration({
  basePath: process.env.BASE_API_URL,
  baseOptions: {
    xsrfCookieName: 'csrftoken',
    xsrfHeaderName: 'X-CSRFTOKEN',
    withCredentials: true
  }
})

export default {
  async createTestEvent (deviceId, eventType) {
    const thisapi = api.DevicesApiFactory(configuration)
    const req = new api.TestEventRequest({
      device: deviceId,
      type: api.TestEventType.Ping,
      status: api.EventStatus.Sent
    })
    const res = await thisapi.devicesEventsCreate(
      deviceId,
      req
    )
    return res
  },
  async startMonitoring (device) {
    const thisapi = api.DevicesApiFactory(configuration, process.env.BASE_API_URL)
    const req = { monitoring_active: true }
    const res = await thisapi.devicesPartialUpdate(
      device.id,
      req
    )
    return res
  },
  async stopMonitoring (device) {
    const thisapi = api.DevicesApiFactory(configuration, process.env.BASE_API_URL)
    const req = { monitoring_active: false }
    const res = await thisapi.devicesPartialUpdate(
      device.id,
      req
    )
    return res
  },

  async getActiveLicense (device) {
    const thisapi = api.DevicesApiFactory(configuration, process.env.BASE_API_URL)
    const res = await thisapi.devicesActiveLicenseRetrieve(
      device.id
    )
    return res
  }
}
