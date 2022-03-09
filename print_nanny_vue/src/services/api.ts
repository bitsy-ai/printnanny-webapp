import * as api from 'printnanny-api-client'

const API_URL: string = window.location.origin
const WS_PROTOCOL: string = window.location.protocol === "https:" ? "wss:" : "ws:"
const WS_URL: string = `${WS_PROTOCOL}//${window.location.host}/ws/events/`

const API_CONFIG: api.Configuration = new api.Configuration({
    basePath: API_URL,
    baseOptions: {
        xsrfCookieName: 'csrftoken',
        xsrfHeaderName: 'X-CSRFTOKEN',
        withCredentials: true
    }
})

export {
    API_CONFIG,
    API_URL,
    WS_PROTOCOL,
    WS_URL
}