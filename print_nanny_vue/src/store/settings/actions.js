import api from '@/services/alerts'
import {
  SET_DATA,
  SET_ALERT_METHODS
} from './mutations'

export const FETCH_SETTINGS = 'load_settings'
export const SAVE_SETTING = 'save_setting'
export const FETCH_ALERT_METHODS = 'load_alert_methods'

export default {

  async [FETCH_ALERT_METHODS] ({ commit }, opts) {
    const data = await api.fetchAlertMethods(opts)
    commit(SET_ALERT_METHODS, data.data.results)
  },

  async [SAVE_SETTING] ({ commit }, opts) {
    const data = await api.updateAlertSetting(opts)
    return data
  },

  async [FETCH_SETTINGS] ({ commit, state }, opts) {
    let data = await api.fetchAlerts(opts)
    data = data.data
    commit(SET_DATA, data)
  }
}
