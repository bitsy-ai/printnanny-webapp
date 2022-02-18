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
    console.log("Response to devicesRetrieve", res)
    return res.data
  },
  async getOrCreateJanusStream(deviceId: number) {
    const thisapi = api.DevicesApiFactory(configuration)
    const req: api.JanusStreamRequest = { config_type: api.JanusConfigType.Cloud }
    const res = await thisapi.devicesJanusStreamGetOrCreate(deviceId)
    console.log("Response to devicesJanusStreamGetOrCreate", res)
    return res.data
  },
  async createJanusTask(deviceId: number, streamId: number, taskType: api.JanusTaskType) {
    const thisapi = api.TasksApiFactory(configuration)
    const req: api.JanusTaskRequest = { task_type: taskType, stream: streamId }
    const res = await thisapi.devicesTasksCreate(deviceId, req)
    console.log("Response to devicesJanusStreamGetOrCreate", res)
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
