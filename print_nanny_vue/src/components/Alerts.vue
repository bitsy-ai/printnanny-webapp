<script>
import simplebar from 'simplebar-vue'
import 'simplebar/dist/simplebar.min.css'

import alertService from '../services/alerts'

export default {
  components: { simplebar },
  data: function () {
    return {
      items: []
    }
  },
  async created () {
    const response = await alertService.list()
    this.items = response.data.results
    console.log('Loaded alerts:', this.items)
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
        v-for="item in items"
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
    href="javascript:void(0);"
    class="dropdown-item text-center text-primary notify-item notify-all"
    >
    View all
    <i class="fi-arrow-right"></i>
    </a>
</b-nav-item-dropdown>
</template>
