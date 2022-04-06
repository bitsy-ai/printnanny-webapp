import * as api from 'printnanny-api-client'

export const DEVICE = 'device'
export const JANUS_STREAM = 'janus_stream'

export interface State {
  [DEVICE]: api.Device
  [JANUS_STREAM]: api.JanusCloudStream | api.JanusEdgeStream
}

export default {
  [DEVICE]: {},
  [JANUS_STREAM]: {}
}
