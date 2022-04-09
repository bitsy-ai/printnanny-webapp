import * as api from 'printnanny-api-client'

const PRINTNANNY_API_URL: string = process.env.PRINTNANNY_API_URL
const PRINTNANNY_WS_URL: string = process.env.PRINTNANNY_API_URL

let PRINTNANNY_API_CONFIG: api.Configuration = new api.Configuration({
    basePath: PRINTNANNY_API_URL
})

declare global {
    interface Window {
        PRINTNANNY_API_TOKEN: string;
    }
}

// if loading javascript same-origin, prefer to authenticate with cookies + csrftoken
if (PRINTNANNY_API_URL.includes(window.location.origin)) {
    PRINTNANNY_API_CONFIG = new api.Configuration({
        basePath: PRINTNANNY_API_URL,
        baseOptions: {
            xsrfCookieName: 'csrftoken',
            xsrfHeaderName: 'X-CSRFTOKEN',
            withCredentials: true
        }
    })
    // require api token to authenticate x-origin requests
} else if (window.PRINTNANNY_API_TOKEN !== undefined) {
    PRINTNANNY_API_CONFIG = new api.Configuration({
        basePath: PRINTNANNY_API_URL,
        accessToken: window.PRINTNANNY_API_TOKEN
    })
} else {
    console.warn(`PRINTNANNY_API_TOKEN not set, requests to ${PRINTNANNY_API_URL} will be anonymous`, PRINTNANNY_API_URL)
}


export {
    PRINTNANNY_API_CONFIG,
    PRINTNANNY_API_URL,
    PRINTNANNY_WS_URL
}