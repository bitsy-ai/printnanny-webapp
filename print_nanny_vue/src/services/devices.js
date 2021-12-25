import { AlertsApiFactory, Configuration, DeviceRequest } from 'print-nanny-client'

const configuration = new Configuration({
  basePath: process.env.BASE_API_URL,
  baseOptions: {
    xsrfCookieName: 'csrftoken',
    xsrfHeaderName: 'X-CSRFTOKEN',
    withCredentials: true
  }
})

export default {
  async startMonitoring(device) {
    const instance = AlertsApiFactory(configuration, process.env.BASE_API_URL)
    const request = 
  },
  async stopMonitoring(device){
    const instance = AlertsApiFactory(configuration, process.env.BASE_API_URL)
    const response = await instance.alertsList(pageNum)
  }
}