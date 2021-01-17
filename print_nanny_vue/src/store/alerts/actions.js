import api from '@/services/api'
import {
  SET_DATA,
  SET_PAGINATION
} from './mutations'
import state from './state'

export const FETCH_ALERTS = 'load_alerts'

export default {
  async [FETCH_ALERTS] ({ commit }, payload) {
    let data = await api.fetchAlerts({
      ...state.pagination,
      ...payload
    })

    data = data.data

    commit(SET_DATA, data)
    commit(SET_PAGINATION, {
      pageSize: data.page_size,
      totalPages: data.total_pages,
      currentPage: data.current_page,
      nextPage: data.next_page,
      previousPage: data.previous_page,
      count: data.count
    //   linkGen: (pageNum) => ({
    //       path: data.links.base, query: { page: pageNum }
    //     })
    })
  }
}
