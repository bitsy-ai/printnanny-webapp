<script>
import { mapActions, mapState } from 'vuex'
import {
  FETCH_ALERTS,
  SEEN_ALL,
  DISMISS_ALL,
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
      seenAll: SEEN_ALL,
      dismissAll: DISMISS_ALL
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
    this.fetchAlerts({ page: '1', dismissed: false })
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

    <a
    href="javascript: void(0);"
    class="dropdown-item noti-title"
    >
    <h5 class="m-0">
        <span class="float-right">
        <a
            class="text-dark"
            v-on:click="dismissAll"
            v-if="alerts.length"
        >
            <small>Clear All</small>
        </a>
        </span>Notification
    </h5>
    </a>

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
        class="notify-icon"
        :class="`bg-${item.color}`"
        >
        <i :class="`${item.icon}`"></i>
        </div>
        <p class="notify-details">{{item.title}}</p>
        <p class="text-muted mb-0 user-msg">
        <small>{{item.alert_subtype}} {{item.naturaltime}}</small>
        </p>
    </a>
    </simplebar>

    <a
    href="/dashboard/octoprint-devices/"
    class="dropdown-item text-center text-primary notify-item notify-all"
    >
    View history
    <i class="fi-arrow-right"></i>
    </a>
</b-nav-item-dropdown>
</template>
