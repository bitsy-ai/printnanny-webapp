import { PrintNannyPluginEventRequest, EventApiFactory, Configuration } from 'printnanny-api-client'

const configuration = new Configuration({
  basePath: process.env.BASE_API_URL,
  baseOptions: {
    xsrfCookieName: 'csrftoken',
    xsrfHeaderName: 'X-CSRFTOKEN',
    withCredentials: true
  }
})

export default {
  async sendPrintNannyEvent(eventType, payload) {
    const thisapi = TelemetryApiFactory(configuration, process.env.BASE_API_URL)
    const req: PrintNannyPluginEventRequest = {

    }
  },
}