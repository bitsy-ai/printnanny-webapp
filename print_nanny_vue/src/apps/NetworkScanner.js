// import { mapMutations, mapState } from 'vuex'
import { Vue, store } from './AppFactory'
import NetworkScanner from '@/components/NetworkScanner'

const apps = document.querySelectorAll('.network-scanner-app')
console.log('found apps:', apps)
export default Array.prototype.forEach.call(apps, (el, index) => new Vue({
  el,
  components: { NetworkScanner },
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
  // created: function () {
  //   // const htmlId = el.dataset.htmlId
  //   // const d = JSON.parse(JSON.parse(document.getElementById(htmlId).textContent))
  // }
}))
