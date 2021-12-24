import state from './state'
import actions from './actions'
import mutations from './mutations'

export const ALERTS_MODULE = 'ALERTS'

export default {
  namespaced: true,
  state,
  actions,
  mutations
}

export * from './state'
export * from './actions'
export * from './mutations'
