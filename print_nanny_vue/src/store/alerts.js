
import { AlertsApiFactory } from 'print-nanny-client/api'
import { Configuration } from 'print-nanny-client/configuration'

const configuration = new Configuration({
  basePath: process.env.BASE_API_URL
})

// const alertService = AlertsApiFactory(configuration, process.env.BASE_API_URL)

export default {
  state: () => ({
    recent: []
  }),
  mutations: {
    FETCH_RECENT_ALERTS (state, recent) {
      state.recent = recent
    }
  },
  actions: {
    async fetchRecentAlerts ({ commit }) {
      const response = await AlertsApiFactory(configuration, process.env.BASE_API_URL).alertsRecentRetrieve()
      commit('FETCH_RECENT_ALERTS', response.data.results)
    },
    async dismissAll ({}) {
      // const response = await AlertsApiFactory(configuration, process.env.BASE_API_URL).alertsRecentRetrieve()
      // commit('DISMISS_RECENT_ALERTS', response.data.results)
    }
  }
}
