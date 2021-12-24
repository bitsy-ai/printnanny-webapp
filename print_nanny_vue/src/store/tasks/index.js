import state from './state'
import actions from './actions'
import mutations from './mutations'

export const TASK_MODULE = 'TASKS'

export default {
  namespaced: true,
  state: () => state,
  actions,
  mutations
}

export * from './state'
export * from './actions'
export * from './mutations'
