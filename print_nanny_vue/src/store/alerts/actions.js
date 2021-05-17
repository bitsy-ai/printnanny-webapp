import api from '@/services/alerts'
import {
  SET_DATA,
  SET_PAGINATION,
  APPEND_DATA
} from './mutations'
import { ALERTS } from './state'

export const FETCH_ALERTS = 'load_alerts'
export const DISMISS_ALL = 'dismiss_alerts'
export const SEEN_ALL = 'seen_alerts'
export const RECEIVED_ALERT = 'received_alert'

export default {
  async [DISMISS_ALL] ({ commit, state, dispatch }, payload) {
    console.log('action', DISMISS_ALL, state)
    const request = { ids: state[ALERTS].results.map(a => a.id) }
    await api.dismissAll(request)
    await dispatch(FETCH_ALERTS)
  },
  async [SEEN_ALL] ({ commit, state, dispatch }, payload) {
    console.log('action', SEEN_ALL, state)
    const request = { ids: state[ALERTS].results.map(a => a.id) }
    await api.seenAll(request)
    await dispatch(FETCH_ALERTS)
  },

  async [RECEIVED_ALERT] ({ commit }, payload) {
    commit(APPEND_DATA, payload)
  },

  async [FETCH_ALERTS] ({ commit, state }, opts) {
    let data = await api.fetchAlerts(opts)

    data = data.data

    commit(SET_PAGINATION, {
      pageSize: data.page_size,
      totalPages: data.total_pages,
      currentPage: data.current_page,
      nextPage: data.next_page,
      previousPage: data.previous_page,
      count: data.count,
      linkGen: (pageNum) => '/alerts/' + pageNum
    })
    commit(SET_DATA, data)
  }
}
