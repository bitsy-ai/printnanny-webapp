<script>
import { layoutComputed, layoutMethods } from '@state/helpers'

import Topbar from '@components/topbar'
import AppMenu from '@components/app-menu'
import RightSidebar from '@components/right-sidebar'
import Footer from '@components/footer'

export default {
  components: { Topbar, AppMenu, RightSidebar, Footer },
  data() {
    return {
      user: this.$store ? this.$store.state.auth.currentUser : {} || {},
      showMenu: window.screen.width > 768,
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
    document.body.setAttribute('data-layout', 'topnav')
    document.body.classList.remove('authentication-bg')
    document.body.classList.remove('authentication-bg-pattern')
    this.activateWidth(this.layoutWidth)
  },
  methods: {
    ...layoutMethods,
    toggleMenu() {
      this.showMenu = !this.showMenu
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
          break
        default:
          document.body.removeAttribute('data-layout-mode')
          break
      }
    },
  },
}
</script>

<template>
  <div class="wrapper">
    <div class="content-page">
      <div class="content">
        <div class="navbar-custom topnav-navbar">
          <div class="container-fluid">
            <a
              href
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
                  src="@assets/images/logo_sm_dark.png"
                  alt
                  height="16"
                />
              </span>
            </a>
            <Topbar
              :width="layoutWidth"
              :user="user"
              layout="horizontal"
            />
          </div>
        </div>
        <!-- <Topbar /> -->
        <div class="topnav">
          <div class="container-fluid">
            <nav class="navbar navbar-dark navbar-expand-lg topnav-menu">
              <b-collapse
                id="topnav-menu-content"
                v-model="showMenu"
              >
                <div class="topbar-nav">
                  <AppMenu mode="horizontal" />
                </div>
              </b-collapse>
            </nav>
          </div>
        </div>
        <div class="container-fluid">
          <slot />
        </div>
      </div>
      <Footer />
    </div>
    <RightSidebar />
  </div>
</template>