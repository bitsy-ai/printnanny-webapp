import {
  SET_DEVICE_DATA,
  SET_JANUS_STREAM_DATA
} from './mutations'
import * as api from 'printnanny-api-client'
import { PRINTNANNY_API_CONFIG } from '../../services/api'
import { JanusStream } from 'printnanny-api-client'

export const GET_DEVICE = 'get_device'
export const SETUP_JANUS_CLOUD = 'setup_janus_cloud'
export const SETUP_JANUS_EDGE = 'setup_janus_edge'
export const GET_JANUS_STREAM = 'get_janus_stream'

export default {
  // TODO
  // import { ActionContext } from "vuex";
  // context: ActionContext<S,R>
  async [GET_DEVICE](context: any, deviceId: number): Promise<api.Device> {
    const thisapi = api.DevicesApiFactory(PRINTNANNY_API_CONFIG)
    const res = await thisapi.devicesRetrieve(deviceId)
    console.log('Response to devicesRetrieve', res)
    context.commit(SET_DEVICE_DATA, res.data)
    return res.data
  },
  async [GET_JANUS_STREAM](context: any, { device, configType }: { device: number, configType: api.JanusConfigType }): Promise<api.JanusEdgeStream | api.JanusCloudStream> {
    const thisapi = api.DevicesApiFactory(PRINTNANNY_API_CONFIG)
    let res;
    switch (configType) {
      case api.JanusConfigType.Cloud:
        res = await thisapi.devicesJanusCloudStreamsList(device)
        break;
      case api.JanusConfigType.Edge:
        res = await thisapi.devicesJanusEdgeStreamsList(device)
        break;
    }
    console.log('Response to devicesRetrieve', res)
    if (res.data.results.length >= 1) {
      context.commit(SET_JANUS_STREAM_DATA, res.data.results[0])
      return res.data.results[0]
    }
    throw new Error(`No JanusStream found for device=${device} config_type=${configType}`)
  },
  async [SETUP_JANUS_CLOUD](context: any, deviceId: number): Promise<api.JanusCloudStream> {
    const thisapi = api.DevicesApiFactory(PRINTNANNY_API_CONFIG)
    const req = { device: deviceId }
    const res = await thisapi.devicesJanusCloudStreamGetOrCreate(deviceId, req)
    console.log('Response to devicesJanusCloudStreamGetOrCreate', res)
    context.commit(SET_JANUS_STREAM_DATA, res.data)
    return res.data
  }
}
