import state from './state'
import actions from './actions'
import mutations from './mutations'

export const SETTINGS_MODULE = 'settings'

export default {
  namespaced: true,
  state,
  actions,
  mutations
}

export * from './state'
export * from './actions'
export * from './mutations'
