<script>
import router from '@router'
import { layoutComputed, layoutMethods } from '@state/helpers'

import Topbar from '@components/topbar'
import SideBar from '@components/side-bar'
import RightSidebar from '@components/right-sidebar'
import Footer from '@components/footer'

export default {
  components: { Topbar, SideBar, RightSidebar, Footer },
  data() {
    return {
      isMenuCondensed: false,
      user: this.$store ? this.$store.state.auth.currentUser : {} || {},
    }
  },
  computed: {
    ...layoutComputed,
  },
  watch: {
    layoutWidth: function(newVal, oldVal) {
      if (newVal !== oldVal) {
        this.activateWidth(newVal)
      }
    },
  },
  created: function() {
    document.body.setAttribute('data-layout', 'detached')
    if (window.screen.width >= 767 && window.screen.width <= 1028) {
      this.changeLeftSidebarType({ leftSidebarType: 'condensed' })
      this.isMenuCondensed = true
    } else if (window.screen.width > 1028) {
      this.changeLeftSidebarType({ leftSidebarType: 'fixed' })
      this.isMenuCondensed = false
    }
  },
  mounted: function() {
    if (
      /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini|Mobile|mobile|CriOS/i.test(
        navigator.userAgent
      )
    ) {
      router.afterEach((routeTo, routeFrom) => {
        document.body.classList.remove('sidebar-enable')
      })
    }
  },
  methods: {
    ...layoutMethods,
    hideMenu() {
      document.body.classList.remove('sidebar-enable')
    },
    toggleMenu() {
      document.body.classList.toggle('sidebar-enable')
    },
    toggleRightSidebar() {
      document.body.classList.toggle('right-bar-enabled')
    },
    hideRightSidebar() {
      document.body.classList.remove('right-bar-enabled')
    },
  },
}
</script>

<template>
  <div>
    <div class="navbar-custom topnav-navbar topnav-navbar-dark">
      <div class="container-fluid">
        <a
          href="/"
          class="topnav-logo"
        >
          <span class="topnav-logo-lg">
            <img
              src="@assets/images/logo-light.png"
              alt
              height="16"
            />
          </span>
          <span class="topnav-logo-sm">
            <img
              src="@assets/images/logo_sm.png"
              alt
              height="16"
            />
          </span>
        </a>
        <Topbar
          :user="user"
          layout="detached"
        />
      </div>
    </div>
    <div class="container-fluid">
      <div class="wrapper">

        <SideBar
          :is-condensed="isMenuCondensed"
          :theme="leftSidebarTheme"
          :type="leftSidebarType"
          :include-user="true"
          classes='left-side-menu-detached'
        />
        <div class="content-page">
          <div class="content">
            <slot />
          </div>
          <Footer />
        </div>
      </div>
    </div>
    <RightSidebar />
  </div>
</template>