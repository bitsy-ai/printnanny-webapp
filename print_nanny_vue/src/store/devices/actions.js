import {
  SET_DEVICE_DATA,
  SET_JANUS_STREAM_DATA
} from './mutations'
import api from '@/services/devices'

export const GET_DEVICE = 'get_device'
export const SETUP_COMPLETE = 'setup_complete'
export const GET_OR_CREATE_JANUS_STREAM = 'get_or_create_janus_stream'

export default {
  async [SETUP_COMPLETE] ({ commit, state, dispatch }, device) {
    const res = await api.setupComplete(device)
    commit(SET_DEVICE_DATA, res)
  },
  async [GET_DEVICE] ({ commit, state, dispatch }, deviceId) {
    const res = await api.getDevice(deviceId)
    commit(SET_DEVICE_DATA, res)
  },
  async [GET_OR_CREATE_JANUS_STREAM] ({ commit, state, dispatch }, deviceId) {
    const res = await api.getOrCreateJanusStream(deviceId)
    commit(SET_JANUS_STREAM_DATA)
  }
}
