// import { mapMutations, mapState } from 'vuex'
import { Vue, store } from './AppFactory'
import WelcomeWizard from '@/components/WelcomeWizard'

const apps = document.querySelectorAll('.welcome-wizard-app')
export default Array.prototype.forEach.call(apps, (el, index) => new Vue({
  el,
  components: { WelcomeWizard },
  store
  // methods: {
  //   ...mapMutations(TASK_MODULE, [
  //     SET_TASK_DATA
  //   ])
  // },
  // computed: {
  //   ...mapState(TASK_MODULE, {
  //     tasks: TASKS
  //   })
  // },
}))
