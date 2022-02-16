// import { mapMutations, mapState } from 'vuex'
import { Vue, store } from './AppFactory'
import VideoStream from '@/components/VideoStream'

const apps = document.querySelectorAll('.video-stream-app')
export default Array.prototype.forEach.call(apps, (el, index) => new Vue({
  el,
  components: { VideoStream },
  store
}))
