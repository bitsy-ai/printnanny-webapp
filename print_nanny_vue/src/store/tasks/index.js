import state from './state'
import actions from './actions'
import mutations from './mutations'

export const TASK_STATUS_MODULE = 'task_status'

export default {
  namespaced: true,
  state,
  actions,
  mutations
}

export * from './state'
export * from './actions'
export * from './mutations'
