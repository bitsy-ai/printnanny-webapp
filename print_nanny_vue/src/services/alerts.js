import { AlertsApiFactory, Configuration } from 'printnanny-api-client'
import { PRINTNANNY_API_CONFIG } from './api'

export default {
  async fetchAlertMethods (opts) {

  },
  async fetchAlerts (opts) {
    const instance = AlertsApiFactory(PRINTNANNY_API_CONFIG)
    const pageNum = opts ? opts.page : undefined
    const response = await instance.alertsList(pageNum)
    console.log('fetchAlerts', response)
    return response
  },

  async dismissAll (opts) {
    const instance = AlertsApiFactory(PRINTNANNY_API_CONFIG)
    const response = await instance.alertsDismiss(opts)
    console.log('dismissAll', response)
    return response
  },
  async seenAll (opts) {
    const instance = AlertsApiFactory(PRINTNANNY_API_CONFIG)
    const response = await instance.alertsSeen(opts)
    console.log('seenAll', response, opts)
    return response
  }
}
