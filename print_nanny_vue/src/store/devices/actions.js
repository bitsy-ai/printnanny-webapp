import {
  SET_DEVICE_DATA
} from './mutations'
import * as api from 'printnanny-api-client'

export const GET_DEVICE = 'get_device'

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
  }
}
