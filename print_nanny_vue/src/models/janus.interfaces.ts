import * as api from 'printnanny-api-client'

interface JanusVideoStats {
    bitrate?: string,
    bsbefore?: number,
    bsnow: number,
    decoderImplementation: string
    fps: string,
    height: string,
    packetsLost: string,
    tsbefore?: number
    tsnow: number,
    width: string,
}
interface JanusStreamComponentData {
    loading: boolean,
    active: boolean,
    error?: string,
    timer?: string,
    videoStats?: JanusVideoStats,
    device?: api.Device,
    janusStream?: api.JanusEdgeStream | api.JanusCloudStream
}
export {
    JanusStreamComponentData,
    JanusVideoStats
}