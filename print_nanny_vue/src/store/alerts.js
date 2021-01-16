
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

// const alertService = AlertsApiFactory(configuration, process.env.BASE_API_URL)

export default {
  namespaced: true,
  state: () => ({
    recent: [],
    unread: []
  }),
  mutations: {
    FETCH_RECENT_ALERTS (state, recent) {
      state.recent = recent
    },
    FETCH_UNREAD_ALERTS (state, unread) {
      state.unread = unread
    },
    RECEIVED_ALERT (state, data) {
      state.recent.concat(data)
      state.unread.concat(data)
    }
  },
  actions: {
    // https://github.com/nathantsoi/vue-native-websocket#with-format-json-enabled
    async alertCreated ({ context, commit }) {
      console.log(context)
      commit('RECEIVED_ALERT', context)
    },
    async fetchRecentAlerts ({ commit }) {
      const response = await AlertsApiFactory(configuration, process.env.BASE_API_URL).alertsRecentRetrieve()
      commit('FETCH_RECENT_ALERTS', response.data.results)
    },
    async fetchUnreadAlerts ({ commit }) {
      const response = await AlertsApiFactory(configuration, process.env.BASE_API_URL).alertsUnreadRetrieve()
      commit('FETCH_UNREAD_ALERTS', response.data.results)
    },
    async seenAll ({ dispatch, commit, state }) {
      console.log(state)
      const request = { ids: state.recent.map(a => a.id) }
      console.log('Marking seen', request)
      await AlertsApiFactory(configuration, process.env.BASE_API_URL).alertsSeen(request)
      await dispatch('fetchRecentAlerts')
      await dispatch('fetchUnreadAlerts')
    },
    async dismissAll ({ dispatch, commit, state }) {
      const request = { ids: state.recent.map(a => a.id) }
      await AlertsApiFactory(configuration, process.env.BASE_API_URL).alertsDismiss(request)
      await dispatch('fetchRecentAlerts')
      await dispatch('fetchUnreadAlerts')
    }
  }
}
