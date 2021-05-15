<script>
import appConfig from '@src/app.config'
import Layout from '@layouts/main'
import PageHeader from '@components/page-header'

/**
 * Tooltips component
 */
export default {
  page: {
    title: 'Tooltips',
    meta: [{ name: 'description', content: appConfig.description }],
  },
  components: { Layout, PageHeader },
  data() {
    return {
      title: 'Tooltips',
      items: [
        {
          text: 'Hyper',
          href: '/',
        },
        {
          text: 'Base UI',
          href: '/',
        },
        {
          text: 'Tooltips',
          active: true,
        },
      ],
    }
  },
}
</script>

<template>
  <Layout>
    <PageHeader :title="title" :items="items" />
    <div class="row">
      <div class="col-xl-6">
        <div class="card">
          <div class="card-body">
            <h4 class="header-title">Examples</h4>
            <p
              class="text-muted font-14"
            >Hover over the buttons below to see the four tooltips directions: top, right, bottom, and left.</p>
            <div class="button-list">
              <b-button id="tooltip-top" variant="info">Tooltip on top</b-button>
              <b-tooltip target="tooltip-top">Tooltip on top</b-tooltip>
              <b-button id="tooltip-button" variant="info">Tooltip on bottom</b-button>
              <b-tooltip target="tooltip-button" placement="bottom">Tooltip on bottom</b-tooltip>
              <b-button id="tooltip-left-button" variant="info">Tooltip on left</b-button>
              <b-tooltip target="tooltip-left-button">Tooltip on left</b-tooltip>
              <b-button id="tooltip-right-button" variant="info">Tooltip on right</b-button>
              <b-tooltip target="tooltip-right-button" placement="bottom">Tooltip on right</b-tooltip>
            </div>
          </div>
          <!-- end card-body -->
        </div>
        <!-- end card -->
        <div class="card">
          <div class="card-body">
            <h4 class="header-title">Disabled elements</h4>
            <p class="text-muted font-14">
              Elements with the
              <code>disabled</code> attribute
              aren’t interactive, meaning users cannot focus, hover, or click them to trigger
              a tooltip (or popover). As a workaround, you’ll want to trigger the tooltip from
              a wrapper
              <code>&lt;div&gt;</code> or
              <code>&lt;span&gt;</code>, ideally made
              keyboard-focusable using
              <code>tabindex="0"</code>, and override the
              <code>pointer-events</code> on the disabled element.
            </p>
            <span id="disabled-wrapper" class="d-inline-block" tabindex="0">
              <b-button variant="primary" style="pointer-events: none;" disabled>Disabled button</b-button>
            </span>
            <b-tooltip target="disabled-wrapper">Disabled tooltip</b-tooltip>
          </div>
          <!-- end card-body -->
        </div>
        <!-- end card -->
      </div>
      <!-- end col -->
      <div class="col-xl-6">
        <div class="card">
          <div class="card-body">
            <h4 class="header-title">HTML Tags</h4>
            <p class="text-muted font-14">And with custom HTML added:</p>
            <b-button
              v-b-tooltip.html
              title="<em>Tooltip</em> <u>with</u> <b>HTML</b>"
              variant="secondary"
            >Tooltip with HTML</b-button>
          </div>
          <!-- end card-body -->
        </div>
        <!-- end card -->
      </div>
      <!-- end col -->
    </div>
    <!-- end row -->
  </Layout>
</template>