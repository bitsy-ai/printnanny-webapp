import { DevicesApiFactory, Configuration } from 'printnanny-api-client'

const configuration = new Configuration({
  basePath: process.env.BASE_API_URL,
  baseOptions: {
    xsrfCookieName: 'csrftoken',
    xsrfHeaderName: 'X-CSRFTOKEN',
    withCredentials: true
  }
})

export default {
  async startMonitoring (device) {
    const thisapi = DevicesApiFactory(configuration, process.env.BASE_API_URL)
    const req = { monitoring_active: true }
    const res = await thisapi.devicesPartialUpdate(
      device.id,
      req
    )
    return res
  },
  async stopMonitoring (device) {
    const thisapi = DevicesApiFactory(configuration, process.env.BASE_API_URL)
    const req = { monitoring_active: false }
    const res = await thisapi.devicesPartialUpdate(
      device.id,
      req
    )
    return res
  },

  async getActiveLicense  (device) {
    const thisapi = DevicesApiFactory(configuration, process.env.BASE_API_URL)
    const res = await thisapi.devicesActiveLicenseRetrieve(
      device.id
    )
    return res
  }
}
