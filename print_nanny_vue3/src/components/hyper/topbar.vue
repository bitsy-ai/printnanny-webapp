<script>
import simplebar from 'simplebar-vue'

import { authComputed, layoutComputed } from '@state/helpers'

export default {
  components: { simplebar },
  props: {
    user: {
      type: Object,
      required: false,
      default: () => ({}),
    },
    layout: {
      type: String,
      default: '',
    },
  },
  data() {
    return {
      notificationItems: [
        {
          id: 1,
          icon: 'mdi mdi-comment-account-outline',
          iconColor: 'primary',
          text: 'Caleb Flakelar commented on Admin',
          subText: '1 min ago',
        },
        {
          id: 2,
          icon: 'mdi mdi-account-plus',
          iconColor: 'info',
          text: 'New user registered.',
          subText: '5 hours ago',
        },
        {
          id: 3,
          user: require('@assets/images/users/avatar-2.jpg'),
          text: 'Cristina Pride',
          subText: 'Hi, How are you? What about our next meeting',
        },
        {
          id: 4,
          icon: 'mdi mdi-comment-account-outline',
          iconColor: 'primary',
          text: 'Caleb Flakelar commented on Admin',
          subText: '4 days ago',
        },
        {
          id: 5,
          user: require('@assets/images/users/avatar-4.jpg'),
          text: 'Karen Robinson',
          subText: 'Wow ! this admin looks good and awesome design',
        },
        {
          id: 6,
          icon: 'mdi mdi-heart',
          iconColor: 'secondary',
          text: 'Carlos Crouch liked Admin',
          subText: '13 days ago',
        },
      ],
    }
  },
  computed: {
    ...authComputed,
    ...layoutComputed,
  },
  methods: {
    toggleMenu() {
      this.$parent.toggleMenu()
    },
    toggleRightSidebar() {
      this.$parent.toggleRightSidebar()
    },
  },
}
</script>

<template>
  <div>
    <ul class="list-unstyled topbar-right-menu float-right mb-0">
      <li class="notification-list">
        <a
          class="nav-link right-bar-toggle toggle-right"
          @click="toggleRightSidebar"
        >
          <i class="dripicons-gear noti-icon toggle-right"></i>
        </a>
      </li>

      <b-nav-item-dropdown
        class="notification-list topbar-dropdown"
        right
        toggle-class="arrow-none"
        menu-class="dropdown-menu-animated topbar-dropdown-menu"
      >
        <template
          slot="button-content"
          class="nav-link dropdown-toggle mr-0"
        >
          <img
            src="@assets/images/flags/us.jpg"
            alt="user-image"
            class="mr-0 mr-sm-1"
            height="12"
          />
          <span class="align-middle d-none d-sm-inline-block">English</span>
          <i class="mdi mdi-chevron-down d-none d-sm-inline-block align-middle font-18 ml-1"></i>
        </template>

        <!-- item-->
        <a
          href="javascript:void(0);"
          class="dropdown-item notify-item"
        >
          <img
            src="@assets/images/flags/germany.jpg"
            alt="user-image"
            class="mr-1"
            height="12"
          />
          <span class="align-middle">German</span>
        </a>

        <!-- item-->
        <a
          href="javascript:void(0);"
          class="dropdown-item notify-item"
        >
          <img
            src="@assets/images/flags/italy.jpg"
            alt="user-image"
            class="mr-1"
            height="12"
          />
          <span class="align-middle">Italian</span>
        </a>

        <!-- item-->
        <a
          href="javascript:void(0);"
          class="dropdown-item notify-item"
        >
          <img
            src="@assets/images/flags/spain.jpg"
            alt="user-image"
            class="mr-1"
            height="12"
          />
          <span class="align-middle">Spanish</span>
        </a>

        <!-- item-->
        <a
          href="javascript:void(0);"
          class="dropdown-item notify-item"
        >
          <img
            src="@assets/images/flags/russia.jpg"
            alt="user-image"
            class="mr-1"
            height="12"
          />
          <span class="align-middle">Russian</span>
        </a>
      </b-nav-item-dropdown>

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

      <b-nav-item-dropdown
        class="notification-list"
        right
        toggle-class="nav-user arrow-none mr-0"
        menu-class="dropdown-menu-animated topbar-dropdown-menu profile-dropdown"
      >
        <template slot="button-content">
          <span class="account-user-avatar">
            <img
              src="@assets/images/users/avatar-1.jpg"
              alt="user-image"
              class="rounded-circle"
            />
          </span>
          <span>
            <span class="account-user-name">{{user ? user.name : ''}}</span>
            <span class="account-position">Founder</span>
          </span>
        </template>

        <!-- item-->
        <div class="dropdown-header noti-title">
          <h6 class="text-overflow m-0">Welcome !</h6>
        </div>

        <!-- item-->
        <a
          href="javascript:void(0);"
          class="dropdown-item notify-item"
        >
          <i class="mdi mdi-account-circle mr-1"></i>
          <span>My Account</span>
        </a>

        <!-- item-->
        <a
          href="javascript:void(0);"
          class="dropdown-item notify-item"
        >
          <i class="mdi mdi-account-edit mr-1"></i>
          <span>Settings</span>
        </a>

        <!-- item-->
        <a
          href="javascript:void(0);"
          class="dropdown-item notify-item"
        >
          <i class="mdi mdi-lifebuoy mr-1"></i>
          <span>Support</span>
        </a>

        <!-- item-->
        <a
          href="javascript:void(0);"
          class="dropdown-item notify-item"
        >
          <i class="mdi mdi-lock-outline mr-1"></i>
          <span>Lock Screen</span>
        </a>

        <!-- item-->
        <a
          href="/logout"
          class="dropdown-item notify-item"
        >
          <i class="mdi mdi-logout mr-1"></i>
          <span>Logout</span>
        </a>
      </b-nav-item-dropdown>
    </ul>
    <button
      v-if="layout !== 'detached'"
      class="button-menu-mobile open-left disable-btn toggle-menu"
      @click="toggleMenu"
    >
      <i class="mdi mdi-menu toggle-menu"></i>
    </button>

    <a
      v-else
      href="javascript: void(0)"
      class="button-menu-mobile open-left disable-btn toggle-menu"
      @click="toggleMenu"
    >
      <div class="lines toggle-menu">
        <span></span>
        <span></span>
        <span></span>
      </div>
    </a>

    <div class="app-search">
      <form>
        <div class="input-group">
          <input
            type="text"
            class="form-control"
            placeholder="Search..."
          />
          <span class="mdi mdi-magnify"></span>
          <div class="input-group-append">
            <button
              class="btn btn-primary"
              type="submit"
            >Search</button>
          </div>
        </div>
      </form>
    </div>
  </div>
</template>

