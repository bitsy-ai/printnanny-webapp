import * as api from 'printnanny-api-client'

interface JanusVideoStats {
    bitrate: string,
    packetsLost: string,
    fps: string,
    height: string,
    width: string
}
interface JanusStreamComponentData {
    loading: boolean,
    active: boolean,
    error?: string,
    timer?: string,
    videoStats?: JanusVideoStats,
    device?: api.Device
}
export {
    JanusStreamComponentData,
    JanusVideoStats
}