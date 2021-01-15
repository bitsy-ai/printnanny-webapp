import { AlertsApiFactory } from 'print-nanny-client/api'

const alertsApi = AlertsApiFactory(
  {
    basePath: process.env.BASE_API_URL
  }
)

export default {
  list: alertsApi.alertsRecentRetrieve()
}
