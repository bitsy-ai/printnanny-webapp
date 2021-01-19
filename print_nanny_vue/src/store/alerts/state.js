export const ALERTS = 'data'
export const PAGINATION = 'pagination'
export const UNREAD_ALERTS = 'filter_unread'
export const UNDISMISSED_ALERTS = 'filter_undismissed'

export default {
  [ALERTS]: { results: [] },
  [UNREAD_ALERTS]: { results: [] },
  [UNDISMISSED_ALERTS]: { results: [] },
  [PAGINATION]: {
    pageSize: 25,
    totalPages: 1,
    currentPage: 1,
    count: 1
  }
}
