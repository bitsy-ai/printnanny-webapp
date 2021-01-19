import { Vue, store } from './appFactory'
import AlertSettingsApp from '@/widgets/AlertSettingsApp'

/* eslint-disable no-new */

export default new Vue({
  el: '#alert-settings-app',
  store,
  components: { AlertSettingsApp },
  template: '<AlertSettingsApp/>'
})
