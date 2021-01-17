<script>
import { mapActions } from 'vuex'

import simplebar from 'simplebar-vue'
import 'simplebar/dist/simplebar.min.css'

export default {
  components: { simplebar },
  async created () {
    this.fetchUnreadAlerts()
    this.fetchRecentAlerts()
  },
  methods: {
    ...mapActions('alerts', [
      'fetchRecentAlerts', 'fetchUnreadAlerts', 'dismissAll', 'seenAll'

    ])
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
        <span class="noti-icon-badge" v-if="$store.state.alerts.unread.length"></span>
    </template>

    <!-- item-->
    <a
    href="javascript: void(0);"
    class="dropdown-item noti-title"
    >
    <h5 class="m-0">
        <span class="float-right">
        <a
            class="text-dark"
            v-on:click="dismissAll"
            v-if="$store.state.alerts.recent.length"
        >
            <small>Clear All</small>
        </a>
        </span>Notification
    </h5>
    </a>

    <simplebar style="max-height: 230px;" v-if="!$store.state.alerts.recent.length">
       <p class="text-muted mb-0 user-msg"><center>You're all caught up!</center></p>
    </simplebar>

    <simplebar style="max-height: 230px;">
    <a
        v-for="item in $store.state.alerts.recent"
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
