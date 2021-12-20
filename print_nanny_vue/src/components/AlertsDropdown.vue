<script>
import { mapActions, mapState } from 'vuex'
import {
  FETCH_ALERTS,
  SEEN_ALL,
  ALERTS_DROPDOWN_MODULE,
  ALERTS
} from '@/store/alerts'
import simplebar from 'simplebar-vue'
import 'simplebar/dist/simplebar.min.css'

export default {
  components: { simplebar },
  methods: {
    ...mapActions(ALERTS_DROPDOWN_MODULE, {
      fetchAlerts: FETCH_ALERTS,
      seenAll: SEEN_ALL
    })
  },
  computed: {
    ...mapState(ALERTS_DROPDOWN_MODULE, {
      alerts: ALERTS
    }),
    unreadAlerts () {
      console.log('this.$store.state', this.$store.state)
      return this.$store.state[ALERTS_DROPDOWN_MODULE].data.results.filter(alert => !alert.seen)
    }
  },
  created () {
    // this.$connect(process.env.ALERT_WS_URL)
    this.fetchAlerts({ page: '1', seen: false })
  }
}
</script>

<template>
<b-nav-item-dropdown
    class="notification-list"
    right
    menu-class="dropdown-menu-animated dropdown-lg"
    toggle-class="nav-link arrow-none"
    v-on:toggle="seenAll"
>
    <template slot="button-content" >
        <i class="mdi mdi-bell-outline noti-icon"></i>
        <span class="noti-icon-badge" v-if="unreadAlerts.length"></span>
    </template>

    <div class="dropdown-item noti-title">
        <h5 class="m-0">
            Notification
        </h5>
    </div>

    <simplebar style="max-height: 230px;" v-if="!alerts.results.length">
       <p class="text-muted mb-0 user-msg"><center>You're all caught up!</center></p>
    </simplebar>

    <simplebar style="max-height: 230px;">
    <a
        v-for="item in alerts.results"
        :key="item.id"
        class="dropdown-item notify-item"
    >
        <div
        class="notify-icon bg-info"
        >
        <i class="mdi mdi-bell-outline"></i>
        </div>
        <p class="notify-details">{{item.message}}</p>
        <p class="text-muted mb-0 user-msg">
        <small>{{item.event_type}} {{item.time}}</small>
        </p>
    </a>
    </simplebar>

    <a
    href="/alerts/"
    class="dropdown-item text-center text-primary notify-item notify-all"
    >
    View history
    <i class="fi-arrow-right"></i>
    </a>
</b-nav-item-dropdown>
</template>
