import state from './state'
import actions from './actions'
import mutations from './mutations'

export const ALERTS_DROPDOWN_MODULE = 'alerts_dropdown'
export const ALERTS_TABLE_MODULE = 'alerts_table'

export default {
  namespaced: true,
  state,
  actions,
  mutations
}

export * from './state'
export * from './actions'
export * from './mutations'
