<script>
import simplebar from 'simplebar-vue'
import 'simplebar/dist/simplebar.min.css'

import { Provider } from '../providers/Provider'

import { Configuration } from 'print-nanny-client/configuration'
import { AlertsApiFactory } from 'print-nanny-client/api'

const alertsApi = AlertsApiFactory(
  {
    basePath: process.env.BASE_API_URL
  }
)

export default {
  components: { simplebar },
  props: {
    provider: {
      required: true,
      type: Provider
    }
  },
  created () {
    this.provider.list()
  }
}
</script>

<template>
<b-nav-item-dropdown
    class="notification-list"
    right
    menu-class="dropdown-menu-animated dropdown-lg"
    toggle-class="nav-link arrow-none"
>
    <template slot="button-content">
    <i class="mdi mdi-bell-outline noti-icon"></i>
    <span class="noti-icon-badge"></span>
    </template>

    <!-- item-->
    <a
    href="javascript: void(0);"
    class="dropdown-item noti-title"
    >
    <h5 class="m-0">
        <span class="float-right">
        <a
            href
            class="text-dark"
        >
            <small>Clear All</small>
        </a>
        </span>Notification
    </h5>
    </a>
    <simplebar style="max-height: 230px;">
    <a
        v-for="item in notificationItems"
        :key="item.id"
        class="dropdown-item notify-item"
    >
        <div
        v-if="item.icon"
        class="notify-icon"
        :class="`bg-${item.iconColor}`"
        >
        <i :class="`${item.icon}`"></i>
        </div>
        <div
        v-if="item.user"
        class="notify-icon"
        >
        <img
            :src="`${item.user}`"
            class="img-fluid rounded-circle"
            alt
        />
        </div>
        <p class="notify-details">{{item.text}}</p>
        <p class="text-muted mb-0 user-msg">
        <small>{{item.subText}}</small>
        </p>
    </a>
    </simplebar>

    <a
    href="javascript:void(0);"
    class="dropdown-item text-center text-primary notify-item notify-all"
    >
    View all
    <i class="fi-arrow-right"></i>
    </a>
</b-nav-item-dropdown>
</template>
