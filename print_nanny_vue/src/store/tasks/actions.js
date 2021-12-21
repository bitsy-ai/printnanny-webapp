// import api from '@/services/alerts'
import {
  SET_DATA
} from './mutations'

export const RECEIVED_TASK_STATUS = 'received_task_status'

export default {

  async [RECEIVED_TASK_STATUS] ({ commit }, payload) {
    commit(SET_DATA, payload)
  }
}
