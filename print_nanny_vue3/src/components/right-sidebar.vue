<script>
import simplebar from 'simplebar-vue'

import { layoutMethods } from '@state/helpers'

export default {
  components: { simplebar },
  data() {
    return {
      config: {
        handler: this.handleRightBarClick,
        middleware: this.middleware,
        events: ['click'],
      },
      layout: this.$store ? this.$store.state.layout : {} || {},
    }
  },
  methods: {
    ...layoutMethods,
    hide() {
      this.$parent.toggleRightSidebar()
    },
    handleRightBarClick(e, el) {
      this.$parent.hideRightSidebar()
    },
    middleware(event, el) {
      return !event.target.classList.contains('toggle-right')
    },
    changeLayout(layout) {
      this.changeLayoutType({ layoutType: layout })
    },
    changeTheme(theme) {
      return this.changeLeftSidebarTheme({ leftSidebarTheme: theme })
    },
    changeType(type) {
      return this.changeLeftSidebarType({ leftSidebarType: type })
    },
    changeWidth(width) {
      return this.changeLayoutWidth({ layoutWidth: width })
    },
  },
}
</script>

<template>
  <div>
    <!-- Right Sidebar -->
    <div
      v-click-outside="config"
      class="right-bar"
    >
      <div class="rightbar-title">
        <a
          href="javascript:void(0);"
          class="right-bar-toggle float-right"
          @click="hide"
        >
          <i class="dripicons-cross noti-icon"></i>
        </a>
        <h5 class="m-0">Settings</h5>
      </div>

      <simplebar class="h-100 rightbar-content">
        <div class="p-3">
          <div
            class="alert alert-primary"
            role="alert"
          >
            <strong>Customize the layout, sidebar menu, etc</strong>
          </div>
          <h5 class="mt-3">Layout</h5>
          <hr class="mt-1" />

          <b-form-radio-group
            v-model="layout.layoutType"
            stacked
            @change="changeLayout($event)"
          >
            <b-form-radio
              value="vertical"
              class="mb-1"
            >Vertical</b-form-radio>
            <b-form-radio
              value="horizontal"
              class="mb-1"
            >Horizontal</b-form-radio>
            <b-form-radio value="detached">Detached</b-form-radio>
          </b-form-radio-group>

          <!-- Width -->
          <template v-if="layout.layoutType !== 'detached'">
            <h5 class="mt-3">Width</h5>
            <hr class="mt-1" />

            <b-form-radio-group
              v-model="layout.layoutWidth"
              stacked
              @change="changeWidth($event)"
            >
              <b-form-radio
                value="fluid"
                class="mb-1"
              >Fluid</b-form-radio>
              <b-form-radio value="boxed">Boxed</b-form-radio>
            </b-form-radio-group>
          </template>

          <!-- Left Sidebar-->
          <template v-if="layout.layoutType !== 'horizontal'">
            <h5 class="mt-3">Left Sidebar</h5>
            <hr class="mt-1" />

            <b-form-radio-group
              v-if="layout.layoutType === 'vertical'"
              v-model="layout.leftSidebarTheme"
              stacked
              @change="changeTheme($event)"
            >
              <b-form-radio
                value="default"
                class="mb-1"
              >Default</b-form-radio>
              <b-form-radio
                value="light"
                class="mb-1"
              >Light</b-form-radio>
              <b-form-radio
                value="dark"
                class="mb-2"
              >Dark</b-form-radio>
            </b-form-radio-group>

            <b-form-radio-group
              v-model="layout.leftSidebarType"
              stacked
              @change="changeType($event)"
            >
              <b-form-radio
                value="fixed"
                class="mb-1"
              >Fixed</b-form-radio>
              <b-form-radio
                value="condensed"
                class="mb-1"
              >Condensed</b-form-radio>
              <b-form-radio value="scrollable">Scrollable</b-form-radio>
            </b-form-radio-group>
          </template>
        </div>
        <!-- end padding-->
      </simplebar>
    </div>

    <div class="rightbar-overlay"></div>
    <!-- /Right-bar -->
  </div>
</template>

<style lang="scss"></style>
