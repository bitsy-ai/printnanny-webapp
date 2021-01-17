
import { ALERTS } from './state'

export const UNREAD_ALERTS = 'filter_unread'

export default {
  [UNREAD_ALERTS] (state, getters) {
    console.log(UNREAD_ALERTS, 'getters', state[ALERTS])
    return state[ALERTS].filter(alert => !alert.seen)
  }
}
