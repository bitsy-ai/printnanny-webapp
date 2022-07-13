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
  async [GET_DEVICE](context: any, deviceId: number): Promise<api.Device> {
    const thisapi = api.DevicesApiFactory(PRINTNANNY_API_CONFIG)
    const res = await thisapi.devicesRetrieve(deviceId)
    console.log('Response to devicesRetrieve', res)
    context.commit(SET_DEVICE_DATA, res.data)
    return res.data
  },
  async [GET_JANUS_STREAM](context: any, { deviceId, janusStreamId, configType }: { deviceId: number, janusStreamId: number, configType: api.JanusConfigType }): Promise<api.JanusStream> {
    const thisapi = api.DevicesApiFactory(PRINTNANNY_API_CONFIG)
    let res;

    res = await thisapi.devicesJanusStreamsRetrieve(deviceId, janusStreamId);
    console.log('Response to GET_JANUS_STREAM', res)
    context.commit(SET_JANUS_STREAM_DATA, res.data)
    return res.data
  },
}
