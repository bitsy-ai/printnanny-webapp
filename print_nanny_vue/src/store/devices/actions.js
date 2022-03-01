import {
  SET_DEVICE_DATA,
  SET_JANUS_STREAM_DATA
} from './mutations'
import * as api from 'printnanny-api-client'

export const GET_DEVICE = 'get_device'
export const GET_JANUS_STREAM = 'get_janus_stream'

const configuration = new api.Configuration({
  basePath: process.env.BASE_API_URL,
  baseOptions: {
    xsrfCookieName: 'csrftoken',
    xsrfHeaderName: 'X-CSRFTOKEN',
    withCredentials: true
  }
})
export default {
  async [GET_DEVICE] ({ commit, state, dispatch }, deviceId) {
    const thisapi = api.DevicesApiFactory(configuration)
    const res = await thisapi.devicesRetrieve(deviceId)
    console.log('Response to devicesRetrieve', res)
    commit(SET_DEVICE_DATA, res.data)
  },
  async [GET_JANUS_STREAM] ({ commit, state, dispatch }, deviceId) {
    const thisapi = api.DevicesApiFactory(configuration)
    const res = await thisapi.devicesJanusStreamsList(deviceId)
    console.log('Response to devicesRetrieve', res)
    commit(SET_JANUS_STREAM_DATA, res.data.results[0])
  }
}
