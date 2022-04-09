import {
  SET_DEVICE_DATA,
  SET_JANUS_STREAM_DATA
} from './mutations'
import * as api from 'printnanny-api-client'
import { PRINTNANNY_API_CONFIG } from '../../services/api'

export const GET_DEVICE = 'get_device'
export const SETUP_JANUS_CLOUD = 'setup_janus_cloud'
export const SETUP_JANUS_EDGE = 'setup_janus_edge'
export const GET_JANUS_STREAM = 'get_janus_stream'

export default {
  // TODO
  // import { ActionContext } from "vuex";
  // context: ActionContext<S,R>
  async [GET_DEVICE](context: any, deviceId: number) {
    const thisapi = api.DevicesApiFactory(PRINTNANNY_API_CONFIG)
    const res = await thisapi.devicesRetrieve(deviceId)
    console.log('Response to devicesRetrieve', res)
    context.commit(SET_DEVICE_DATA, res.data)
  },
  async [GET_JANUS_STREAM](context: any, { deviceId, configType }: { deviceId: number, configType: api.JanusConfigType }) {
    const thisapi = api.DevicesApiFactory(PRINTNANNY_API_CONFIG)
    let res;
    switch (configType) {
      case api.JanusConfigType.Cloud:
        res = await thisapi.devicesJanusCloudStreamsList(deviceId)
        break;
      case api.JanusConfigType.Edge:
        res = await thisapi.devicesJanusEdgeStreamsList(deviceId)
        break;
    }
    console.log('Response to devicesRetrieve', res)
    context.commit(SET_JANUS_STREAM_DATA, res.data.results[0])
  },
  async [SETUP_JANUS_CLOUD](context: any, deviceId: number) {
    const thisapi = api.DevicesApiFactory(PRINTNANNY_API_CONFIG)
    const req = { device: deviceId }
    const res = await thisapi.devicesJanusCloudStreamGetOrCreate(deviceId, req)
    console.log('Response to devicesJanusCloudStreamGetOrCreate', res)
    context.commit(SET_JANUS_STREAM_DATA, res.data)
    return res.data
  }
}
