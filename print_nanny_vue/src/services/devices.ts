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

  async startMonitoringTask(deviceId: number) {
    const thisapi = api.DevicesApiFactory(configuration)
    const req: api.JanusTaskRequest = { "task_type": api.JanusTaskType.CloudMonitorStart }
    const res = await thisapi.devicesTasksCreate(deviceId, req)
    console.debug("startMonitoringTask response={}", res)
    return res.data
  },
  async stopMonitoringTask(deviceId: number) {
    const thisapi = api.DevicesApiFactory(configuration)
    const req: api.JanusTaskRequest = { "task_type": api.JanusTaskType.CloudMonitorStop }
    const res = await thisapi.devicesTasksCreate(deviceId, req)
    console.debug("startMonitoringTask response={}", res)
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
