import state from './state'
import actions from './actions'
import mutations from './mutations'
import getters from './getters'

export const ALERTS_MODULE = 'alerts'

export default {
  namespaced: true,
  state,
  actions,
  mutations,
  getters
}

export * from './state'
export * from './actions'
export * from './mutations'
export * from './getters'
