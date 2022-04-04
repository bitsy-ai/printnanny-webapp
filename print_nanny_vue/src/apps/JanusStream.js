// import { mapMutations, mapState } from 'vuex'
import { Vue, store } from './AppFactory'
import JanusStream from '@/components/JanusStream'

const apps = document.querySelectorAll('.janus-stream-app')
export default Array.prototype.forEach.call(apps, (el, index) => new Vue({
  el,
  components: { JanusStream },
  store
}))
