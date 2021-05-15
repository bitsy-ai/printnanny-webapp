<script>
import appConfig from '@src/app.config'
import Layout from '@layouts/main'
import PageHeader from '@components/page-header'

/**
 * Notifications component
 */
export default {
  page: {
    title: 'Notifications',
    meta: [{ name: 'description', content: appConfig.description }],
  },
  components: { Layout, PageHeader },
  data() {
    return {
      title: 'Notifications',
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
          text: 'Notifications',
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
      <div class="col-12">
        <div class="card">
          <div class="card-body">
            <h4 class="header-title">Bootstrap Toasts</h4>
            <p class="text-muted font-14">
              Push notifications to your visitors with a toast, a
              lightweight and easily customizable alert message.
            </p>
            <div class="row">
              <div class="col-md-6">
                <h5 class="mb-2">Basic</h5>
                <p class="text-muted">
                  Toasts are as flexible as you need and have very little required markup. At a minimum, we
                  require a single element to contain your “toasted” content and strongly encourage a dismiss button.
                </p>
                <div class="p-3">
                  <b-toast visible static no-auto-hide>
                    <div slot="toast-title" class="d-flex flex-grow-1 align-items-center">
                      <b-img
                        :src="require('@assets/images/logo_sm_dark.png')"
                        class="mr-1 rounded"
                        height="12"
                      ></b-img>
                      <strong class="mr-auto">Hyper</strong>
                      <small class="mr-2">11 mins ago</small>
                    </div>Hello, world! This is a toast message.
                  </b-toast>
                  <!--end toast-->
                </div>
              </div>
              <!-- end col-->
              <div class="col-md-6">
                <h5 class="mb-2">Translucent</h5>
                <p class="text-muted">
                  Toasts are slightly translucent, too, so they blend over whatever they might appear over.
                  For browsers that support the backdrop-filter CSS property, we’ll also attempt to blur the elements under a toast.
                </p>

                <div class="p-3 bg-secondary">
                  <b-toast visible static no-auto-hide>
                    <div slot="toast-title" class="d-flex flex-grow-1 align-items-center">
                      <b-img
                        :src="require('@assets/images/logo_sm_dark.png')"
                        class="mr-1 rounded"
                        height="12"
                      ></b-img>
                      <strong class="mr-auto">Hyper</strong>
                      <small class="mr-2">11 mins ago</small>
                    </div>Hello, world! This is a toast message.
                  </b-toast>
                  <!--end toast-->
                </div>
              </div>
              <!-- end col-->
            </div>
            <!-- end row-->
            <div class="row">
              <div class="col-md-6 mt-4">
                <h5 class="mb-2">Stacking</h5>
                <p
                  class="text-muted"
                >When you have multiple toasts, we default to vertiaclly stacking them in a readable manner.</p>
                <div class="p-3">
                  <div
                    aria-live="polite"
                    aria-atomic="true"
                    style="position: relative; min-height: 200px;"
                  >
                    <!-- Position it -->
                    <div style="position: absolute; top: 0; right: 0;">
                      <b-toast visible static no-auto-hide>
                        <div slot="toast-title" class="d-flex flex-grow-1 align-items-center">
                          <b-img
                            :src="require('@assets/images/logo_sm_dark.png')"
                            class="mr-1 rounded"
                            height="12"
                          ></b-img>
                          <strong class="mr-auto">Hyper</strong>
                          <small class="mr-2">just now</small>
                        </div>See? Just like this.
                      </b-toast>
                      <!--end toast-->

                      <b-toast visible static no-auto-hide>
                        <div slot="toast-title" class="d-flex flex-grow-1 align-items-center">
                          <b-img
                            :src="require('@assets/images/logo_sm_dark.png')"
                            class="mr-1 rounded"
                            height="12"
                          ></b-img>
                          <strong class="mr-auto">Hyper</strong>
                          <small class="mr-2">2 seconds ago</small>
                        </div>Heads up, toasts will stack automatically
                      </b-toast>
                      <!--end toast-->
                    </div>
                  </div>
                </div>
              </div>
              <!-- end col-->
              <div class="col-md-6 mt-4">
                <h5 class="mb-2">Placement</h5>
                <p class="text-muted">
                  Place toasts with custom CSS as you need them. The top right is often used for
                  notifications, as is the top middle. If you’re only ever going to show one toast at a time, put the positioning
                  styles right on the
                  <code>.toast</code>.
                </p>
                <div class="p-3">
                  <div
                    aria-live="polite"
                    aria-atomic="true"
                    class="d-flex justify-content-center align-items-center"
                    style="min-height: 200px;"
                  >
                    <b-toast visible static no-auto-hide>
                      <div slot="toast-title" class="d-flex flex-grow-1 align-items-center">
                        <b-img
                          :src="require('@assets/images/logo_sm_dark.png')"
                          class="mr-1 rounded"
                          height="12"
                        ></b-img>
                        <strong class="mr-auto">Hyper</strong>
                        <small class="mr-2">11 mins ago</small>
                      </div>Hello, world! This is a toast message.
                    </b-toast>
                    <!--end toast-->
                  </div>
                </div>
              </div>
              <!-- end col-->
            </div>
            <!-- end row-->
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