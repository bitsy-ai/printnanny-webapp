<script>
import { layoutComputed, layoutMethods } from '@state/helpers'
import router from '@router'

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
    document.body.classList.remove('authentication-bg')
    document.body.classList.remove('authentication-bg-pattern')
    document.body.removeAttribute('data-layout')
    if (window.screen.width >= 767 && window.screen.width <= 1028) {
      this.changeLeftSidebarType({ leftSidebarType: 'condensed' })
      this.isMenuCondensed = true
    } else if (window.screen.width > 1028) {
      this.changeLeftSidebarType({ leftSidebarType: 'fixed' })
      this.isMenuCondensed = false
    }
    this.activateWidth(this.layoutWidth)
  },
  mounted: () => {
    if (
      /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini|Mobile|mobile|CriOS/i.test(
        navigator.userAgent
      )
    ) {
      if (window.screen.width >= 728 && window.screen.width <= 1028) {
        document.body.setAttribute('data-leftbar-compact-mode', 'condensed')
      }
    }
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
    toggleMenu() {
      document.body.classList.toggle('sidebar-enable')
    },
    hideMenu() {
      document.body.classList.remove('sidebar-enable')
    },
    toggleRightSidebar() {
      document.body.classList.toggle('right-bar-enabled')
    },
    hideRightSidebar() {
      document.body.classList.remove('right-bar-enabled')
    },
    activateWidth(width) {
      switch (width) {
        case 'boxed':
          document.body.setAttribute('data-layout-mode', 'boxed')
          this.changeLeftSidebarType({ leftSidebarType: 'condensed' })
          this.isMenuCondensed = true
          break
        default:
          document.body.removeAttribute('data-layout-mode')
          this.changeLeftSidebarType({ leftSidebarType: 'fixed' })
          this.isMenuCondensed = false
          break
      }
    },
  },
}
</script>

<template>
  <div class="wrapper">
    <SideBar
      :is-condensed="isMenuCondensed"
      :theme="leftSidebarTheme"
      :type="leftSidebarType"
    />

    <!-- ============================================================== -->
    <!-- Start Page Content here -->
    <!-- ============================================================== -->

    <div class="content-page">
      <div class="content">
        <div class="navbar-custom">
          <Topbar
            :user="user"
            layout="vertical"
          />
        </div>
        <!-- Start Content-->
        <div class="container-fluid">
          <slot />
        </div>
      </div>
      <Footer />
    </div>
    <RightSidebar />
  </div>
</template>