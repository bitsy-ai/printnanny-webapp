<script>
import appConfig from '@src/app.config'
import Layout from '@layouts/main'
import PageHeader from '@components/page-header'

/**
 * Popovers component
 */
export default {
  page: {
    title: 'Popovers',
    meta: [{ name: 'description', content: appConfig.description }],
  },
  components: { Layout, PageHeader },
  data() {
    return {
      title: 'Popovers',
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
          text: 'Popovers',
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
            <h4 class="header-title">Simple Popover</h4>
            <p
              class="text-muted font-14"
            >Popover is a component which displays a box with a content after a click on an element - similar to the tooltip but can contain more content.</p>
            <b-button
              v-b-popover="`And here's some amazing content. It's very engaging. Right?`"
              class="mt-2"
              variant="danger"
              title="Popover Title"
            >Click to toggle popover</b-button>
          </div>
          <!-- end card-body -->
        </div>
        <!-- end card -->
        <div class="card">
          <div class="card-body">
            <h4 class="header-title">Variants and custom class</h4>
            <p class="text-muted font-14 mb-3">popovers support contextual color variants.</p>
            <b-button id="popover-button-variant" variant="success">Click button</b-button>
            <b-popover target="popover-button-variant" variant="danger" triggers="focus">
              <template v-slot:title>Danger!</template>
              Danger variant popover
            </b-popover>
          </div>
          <!-- end card-body -->
        </div>
        <!-- end card -->
      </div>
      <!-- end col -->

      <div class="col-xl-6">
        <div class="card">
          <div class="card-body">
            <h4 class="header-title">Four Directions</h4>
            <p
              class="text-muted font-14 mb-3"
            >Four options are available: top, right, bottom, and left aligned.</p>
            <b-button
              v-b-popover.top="`Vivamus sagittis lacus vel augue laoreet rutrum faucibus.`"
              variant="primary"
            >Popover on top</b-button>
            <b-button
              v-b-popover.bottom="`Vivamus sagittis lacus vel augue laoreet rutrum faucibus.`"
              variant="primary"
              class="ml-2"
            >Popover on bottom</b-button>
            <b-button
              v-b-popover.right="`Vivamus sagittis lacus vel augue laoreet rutrum faucibus.`"
              variant="primary"
              class="ml-2"
            >Popover on right</b-button>
            <b-button
              v-b-popover.left="`Vivamus sagittis lacus vel augue laoreet rutrum faucibus.`"
              variant="primary"
              class="ml-2"
            >Popover on left</b-button>
          </div>
          <!-- end card-body -->
        </div>
        <!-- end card -->
        <div class="card">
          <div class="card-body">
            <h4 class="header-title">Hover</h4>
            <p class="text-muted font-14">
              Use the attribute
              <code>hover</code> to show the popover on hovering the element.
            </p>
            <b-button
              v-b-popover.hover.right="`And here's some amazing content. It's very engaging. Right?`"
              variant="dark"
              title="Ohh Wow !"
            >Please Hover Me</b-button>
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