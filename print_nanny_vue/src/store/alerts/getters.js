
import { ALERTS } from './state'

export const UNREAD_ALERTS = 'filter_unread'
export const UNDISMISSED_ALERTS = 'filter_undismissed'
export default {

  [UNREAD_ALERTS] (state, getters) {
    console.log(UNREAD_ALERTS, 'getters', state[ALERTS])
    return state[ALERTS].filter(alert => !alert.seen)
  },

  [UNDISMISSED_ALERTS] (state, getters) {
    console.log(UNDISMISSED_ALERTS, 'getters', state[ALERTS])
    return state[ALERTS].filter(alert => !alert.dismissed)
  }
}
