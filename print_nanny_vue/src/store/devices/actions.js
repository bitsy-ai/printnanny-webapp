
import {
  SET_DEVICE_DATA,
  SET_JANUS_STREAM_DATA
} from './mutations'
import * as api from 'printnanny-api-client'
import { API_CONFIG } from '../../services/api'

export const GET_DEVICE = 'get_device'
export const SETUP_JANUS_CLOUD = 'setup_janus_cloud'
export const SETUP_JANUS_EDGE = 'setup_janus_edge'
export const GET_JANUS_STREAM = 'get_janus_stream'

export default {
  async [GET_DEVICE] ({ commit, state, dispatch }, deviceId) {
    const thisapi = api.DevicesApiFactory(API_CONFIG)
    const res = await thisapi.devicesRetrieve(deviceId)
    console.log('Response to devicesRetrieve', res)
    commit(SET_DEVICE_DATA, res.data)
  },
  async [GET_JANUS_STREAM] ({ commit, state, dispatch }, deviceId) {
    const thisapi = api.DevicesApiFactory(API_CONFIG)
    const res = await thisapi.devicesJanusStreamsList(deviceId)
    console.log('Response to devicesRetrieve', res)
    commit(SET_JANUS_STREAM_DATA, res.data.results[0])
  },
  async [SETUP_JANUS_CLOUD] ({ commit, state, dispatch }, device) {
    const thisapi = api.DevicesApiFactory(API_CONFIG)
    const req = { device: device.id }
    const res = await thisapi.devicesJanusCloudStreamGetOrCreate(device.id, req)
    console.log('Response to devicesJanusCloudStreamGetOrCreate', res)
    commit(SET_JANUS_STREAM_DATA, res.data)
    return res.data
  },
  async [SETUP_JANUS_EDGE] ({ commit, state, dispatch }, device) {
    const thisapi = api.DevicesApiFactory(API_CONFIG)
    const req = { device: device.id }
    const res = await thisapi.devicesJanusEdgeStreamGetOrCreate(device.id, req)
    console.log('Response to devicesJanusEdgeStreamGetOrCreate', res)
    commit(SET_JANUS_STREAM_DATA, res.data)
    return res.data
  }
}
