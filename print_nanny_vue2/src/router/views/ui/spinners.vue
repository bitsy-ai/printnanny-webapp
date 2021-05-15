<script>
import appConfig from '@src/app.config'
import Layout from '@layouts/main'
import PageHeader from '@components/page-header'

/**
 * Spinners component
 */
export default {
  page: {
    title: 'Spinners',
    meta: [{ name: 'description', content: appConfig.description }],
  },
  components: { Layout, PageHeader },
  data() {
    return {
      title: 'Spinners',
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
          text: 'Spinners',
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
            <h4 class="header-title">Border spinner</h4>
            <p
              class="text-muted font-14"
            >Use the border spinners for a lightweight loading indicator.</p>
            <b-spinner label="Loading..." class="m-2"></b-spinner>
          </div>
          <!-- end card-body -->
        </div>
        <!-- end card-->
        <div class="card">
          <div class="card-body">
            <h4 class="header-title">Colors</h4>
            <p class="text-muted font-14">
              You can use any
              of our text color utilities on the standard spinner.
            </p>
            <b-spinner class="m-2" variant="primary" role="status"></b-spinner>
            <b-spinner class="m-2" variant="secondary" role="status"></b-spinner>
            <b-spinner class="m-2" variant="success" role="status"></b-spinner>
            <b-spinner class="m-2" variant="danger" role="status"></b-spinner>
            <b-spinner class="m-2" variant="warning" role="status"></b-spinner>
            <b-spinner class="m-2" variant="info" role="status"></b-spinner>
            <b-spinner class="m-2" variant="light" role="status"></b-spinner>
            <b-spinner class="m-2" variant="dark" role="status"></b-spinner>
          </div>
          <!-- end card-body -->
        </div>
        <!-- end card-->
        <div class="card">
          <div class="card-body">
            <h4 class="header-title">Alignment</h4>
            <p
              class="text-muted font-14"
            >Use flexbox utilities, float utilities, or text alignment utilities to place spinners exactly where you need them in any situation.</p>
            <div class="d-flex justify-content-center">
              <b-spinner label="Loading..."></b-spinner>
            </div>
          </div>
          <!-- end card-body -->
        </div>
        <!-- end card-->
        <div class="card">
          <div class="card-body">
            <h4 class="header-title">Size</h4>
            <p class="text-muted font-14">
              Add
              <code>.spinner-border-sm</code> and
              <code>.spinner-border.avatar-**</code> to make a smaller spinner that can quickly be used within other components.
            </p>
            <div class="row">
              <div class="col-lg-6">
                <b-spinner label="Loading..." class="avatar-lg m-2" variant="primary"></b-spinner>
                <b-spinner type="grow" class="avatar-lg m-2" variant="primary" role="status"></b-spinner>
              </div>
              <!-- end col -->

              <div class="col-lg-6">
                <b-spinner label="Loading..." class="avatar-md m-2" variant="primary"></b-spinner>
                <b-spinner type="grow" class="avatar-md m-2" variant="primary" role="status"></b-spinner>
              </div>
              <!-- end col -->

              <div class="col-lg-6">
                <b-spinner label="Loading..." class="avatar-sm m-2" variant="primary"></b-spinner>
                <b-spinner type="grow" class="avatar-sm m-2" variant="primary" role="status"></b-spinner>
              </div>
              <!-- end col -->

              <div class="col-lg-6">
                <b-spinner label="Loading..." class="spinner-border-sm m-2"></b-spinner>
                <b-spinner type="grow" class="spinner-border-sm m-2"></b-spinner>
              </div>
              <!-- end col -->
            </div>
            <!--end row-->
          </div>
          <!-- end card-body -->
        </div>
        <!-- end card-->
      </div>
      <!-- end col -->
      <div class="col-xl-6">
        <div class="card">
          <div class="card-body">
            <h4 class="header-title">Growing spinner</h4>
            <p
              class="text-muted font-14"
            >If you don’t fancy a border spinner, switch to the grow spinner. While it doesn’t technically spin, it does repeatedly grow!</p>
            <b-spinner type="grow" label="Loading..."></b-spinner>
          </div>
          <!-- end card-body -->
        </div>
        <!-- end card-->

        <div class="card">
          <div class="card-body">
            <h4 class="header-title">Color Growing spinner</h4>
            <p
              class="text-muted font-14"
            >You can use any of our text color utilities on the standard spinner.</p>
            <b-spinner type="grow" class="m-2" variant="primary" role="status"></b-spinner>
            <b-spinner type="grow" class="m-2" variant="secondary" role="status"></b-spinner>
            <b-spinner type="grow" class="m-2" variant="success" role="status"></b-spinner>
            <b-spinner type="grow" class="m-2" variant="danger" role="status"></b-spinner>
            <b-spinner type="grow" class="m-2" variant="warning" role="status"></b-spinner>
            <b-spinner type="grow" class="m-2" variant="info" role="status"></b-spinner>
            <b-spinner type="grow" class="m-2" variant="light" role="status"></b-spinner>
            <b-spinner type="grow" class="m-2" variant="dark" role="status"></b-spinner>
          </div>
          <!-- end card-body -->
        </div>
        <!-- end card-->

        <div class="card">
          <div class="card-body">
            <h4 class="header-title">Placement</h4>
            <p class="text-muted font-14">
              Use
              <code>flexbox utilities</code>,
              <code>float utilities</code>, or
              <code>text alignment</code> utilities to place spinners exactly where you need them in any situation.
            </p>
            <div class="d-flex align-items-center">
              <strong>Loading...</strong>
              <b-spinner class="ml-auto"></b-spinner>
            </div>
          </div>
          <!-- end card-body -->
        </div>
        <!-- end card-->

        <div class="card">
          <div class="card-body">
            <h4 class="header-title">Buttons spinner</h4>
            <p class="text-muted font-14">
              Use spinners within buttons to indicate an action is currently processing or taking place.
              You may also swap the text out of the spinner element and utilize button text as needed.
            </p>
            <div class="row">
              <div class="col-lg-6">
                <b-button variant="primary" disabled>
                  <b-spinner small></b-spinner>
                  <span class="sr-only">Loading...</span>
                </b-button>

                <b-button variant="primary" class="ml-2" disabled>
                  <b-spinner small class="mr-1"></b-spinner>Loading...
                </b-button>
              </div>
              <!-- end col -->
              <div class="col-lg-6">
                <b-button variant="primary" disabled>
                  <b-spinner type="grow" small></b-spinner>
                  <span class="sr-only">Loading...</span>
                </b-button>

                <b-button variant="primary" class="ml-2" disabled>
                  <b-spinner type="grow" small class="mr-1"></b-spinner>Loading...
                </b-button>
              </div>
              <!-- end col -->
            </div>
            <!-- end row -->
          </div>
          <!-- end card-body -->
        </div>
        <!-- end card-->
      </div>
      <!-- end col -->
    </div>
  </Layout>
</template>