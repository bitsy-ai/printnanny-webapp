import { AlertsApiFactory } from 'print-nanny-client/api'
import { Configuration } from 'print-nanny-client/configuration'

const configuration = new Configuration({
  basePath: process.env.BASE_API_URL
})

export default {
  list: AlertsApiFactory(configuration, process.env.BASE_API_URL).alertsRecentRetrieve
}
