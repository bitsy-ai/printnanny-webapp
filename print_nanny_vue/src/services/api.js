import { AlertsApiFactory } from 'print-nanny-client/api'
import { Configuration } from 'print-nanny-client/configuration'

const configuration = new Configuration({
  basePath: process.env.BASE_API_URL,
  baseOptions: {
    xsrfCookieName: 'csrftoken',
    xsrfHeaderName: 'X-CSRFTOKEN',
    withCredentials: true
  }
})

export default {
  async fetchAlerts (opts) {
    const instance = AlertsApiFactory(configuration, process.env.BASE_API_URL)

    const response = await instance.alertsList(opts.page)
    console.log('fetchAlerts', response)
    return response
  }
}
