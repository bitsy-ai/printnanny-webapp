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
  async fetchAlertMethods (opts){
    
  },
  async fetchAlerts (opts) {
    const instance = AlertsApiFactory(configuration, process.env.BASE_API_URL)
    const pageNum = opts ? opts.page : undefined
    const response = await instance.alertsList(pageNum)
    console.log('fetchAlerts', response)
    return response
  },

  async dismissAll (opts) {
    const instance = AlertsApiFactory(configuration, process.env.BASE_API_URL)
    const response = await instance.alertsDismiss(opts)
    console.log('dismissAll', response)
    return response
  },
  async seenAll (opts) {
    const instance = AlertsApiFactory(configuration, process.env.BASE_API_URL)
    const response = await instance.alertsSeen(opts)
    console.log('seenAll', response)
    return response
  }
}
