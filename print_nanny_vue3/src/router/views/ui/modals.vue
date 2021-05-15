<script>
import appConfig from '@src/app.config'
import Layout from '@layouts/main'
import PageHeader from '@components/page-header'

/**
 * Modals component
 */
export default {
  page: {
    title: 'Modals',
    meta: [{ name: 'description', content: appConfig.description }],
  },
  components: { Layout, PageHeader },
  data() {
    return {
      title: 'Modals',
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
          text: 'Modals',
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
            <h4 class="header-title">Bootstrap Modals</h4>

            <p
              class="text-muted font-14"
            >A rendered modal with header, body, and set of actions in the footer.</p>
            <div class="button-list">
              <b-button v-b-modal.modal-standard variant="primary">Standard Modal</b-button>
              <b-modal id="modal-standard" title="Modal Heading" title-class="font-18">
                <h5>Text in a modal</h5>
                <p>Duis mollis, est non commodo luctus, nisi erat porttitor ligula.</p>
                <hr />
                <h5>Overflowing text to show scroll behavior</h5>
                <p>Cras mattis consectetur purus sit amet fermentum. Cras justo odio, dapibus ac facilisis in, egestas eget quam. Morbi leo risus, porta ac consectetur ac, vestibulum at eros.</p>
                <p>Praesent commodo cursus magna, vel scelerisque nisl consectetur et. Vivamus sagittis lacus vel augue laoreet rutrum faucibus dolor auctor.</p>
                <p>Aenean lacinia bibendum nulla sed consectetur. Praesent commodo cursus magna, vel scelerisque nisl consectetur et. Donec sed odio dui. Donec ullamcorper nulla non metus auctor fringilla.</p>
              </b-modal>
              <b-button v-b-modal.modal-lg variant="info">Large Modal</b-button>
              <b-modal
                id="modal-lg"
                size="lg"
                title="Large modal"
                title-class="font-18"
                hide-footer
              >...</b-modal>
              <b-button v-b-modal.modal-sm variant="success">Small Modal</b-button>
              <b-modal
                id="modal-sm"
                size="sm"
                title="Small modal"
                title-class="font-18"
                hide-footer
              >...</b-modal>

              <b-button v-b-modal.modal-xl variant="primary">Full width Modal</b-button>
              <b-modal
                id="modal-xl"
                title="Modal Heading"
                title-class="font-18"
                dialog-class="modal-full-width"
              >
                <h6>Text in a modal</h6>
                <p>Duis mollis, est non commodo luctus, nisi erat porttitor ligula.</p>
                <hr />
                <h6>Overflowing text to show scroll behavior</h6>
                <p>Cras mattis consectetur purus sit amet fermentum. Cras justo odio, dapibus ac facilisis in, egestas eget quam. Morbi leo risus, porta ac consectetur ac, vestibulum at eros.</p>
                <p>Praesent commodo cursus magna, vel scelerisque nisl consectetur et. Vivamus sagittis lacus vel augue laoreet rutrum faucibus dolor auctor.</p>
                <p>Aenean lacinia bibendum nulla sed consectetur. Praesent commodo cursus magna, vel scelerisque nisl consectetur et. Donec sed odio dui. Donec ullamcorper nulla non metus auctor fringilla.</p>
              </b-modal>

              <b-button v-b-modal.modal-scrollable>Scrollable Modal</b-button>
              <b-modal
                id="modal-scrollable"
                scrollable
                title="Scrollable Content"
                title-class="font-18"
              >
                <p v-for="i in 15" :key="i">
                  Cras mattis consectetur purus sit amet fermentum. Cras justo odio, dapibus ac facilisis
                  in, egestas eget quam. Morbi leo risus, porta ac consectetur ac, vestibulum at eros.
                </p>
              </b-modal>
            </div>
          </div>
          <!-- end card-body -->
        </div>
        <!-- end card -->
      </div>
      <!-- end col -->

      <div class="col-xl-6">
        <div class="card">
          <div class="card-body">
            <h4 class="header-title">Modal with Pages</h4>
            <p class="text-muted font-14">Examples of custom modals.</p>
            <div class="button-list">
              <!-- Sign Up modal -->
              <b-button v-b-modal.modal-signup variant="primary">Sign Up Modal</b-button>
              <b-modal id="modal-signup" hide-header hide-footer>
                <div class="text-center mt-2 mb-4">
                  <router-link tag="a" to="/" class="text-success">
                    <span>
                      <img src="@assets/images/logo-dark.png" alt height="18" />
                    </span>
                  </router-link>
                </div>

                <form class="pl-3 pr-3" action="#">
                  <b-form-group label="Name" label-for="username">
                    <b-form-input id="username" placeholder="Michael Zenaty" required></b-form-input>
                  </b-form-group>

                  <b-form-group label="Email address" label-for="emailaddress">
                    <b-form-input
                      id="emailaddress"
                      type="email"
                      placeholder="john@deo.com"
                      required
                    ></b-form-input>
                  </b-form-group>

                  <b-form-group label="Password" label-for="password">
                    <b-form-input id="password" placeholder="Enter your password" required></b-form-input>
                  </b-form-group>

                  <b-form-group>
                    <b-form-checkbox
                      id="customCheck1"
                      value="accepted"
                      unchecked-value="not_accepted"
                    >
                      I accept
                      <a href="#">Terms and Conditions</a>
                    </b-form-checkbox>
                  </b-form-group>

                  <b-form-group class="text-center">
                    <b-button type="submit" variant="primary">Sign Up Free</b-button>
                  </b-form-group>
                </form>
              </b-modal>

              <!-- Log In modal -->
              <b-button v-b-modal.modal-login variant="info">Log In Modal</b-button>

              <b-modal id="modal-login" hide-header hide-footer>
                <div class="text-center mt-2 mb-4">
                  <router-link tag="a" to="/" class="text-success">
                    <span>
                      <img src="@assets/images/logo-dark.png" alt height="18" />
                    </span>
                  </router-link>
                </div>

                <form action="#" class="pl-3 pr-3">
                  <b-form-group label="Email address" label-for="emailaddress1">
                    <b-form-input
                      id="emailaddress1"
                      type="email"
                      placeholder="john@deo.com"
                      required
                    ></b-form-input>
                  </b-form-group>

                  <b-form-group label="Password" label-for="password1">
                    <b-form-input id="password1" placeholder="Enter your password" required></b-form-input>
                  </b-form-group>

                  <b-form-group>
                    <b-form-checkbox
                      id="customCheck2"
                      value="accepted"
                      unchecked-value="not_accepted"
                    >Remember me</b-form-checkbox>
                  </b-form-group>
                  <b-form-group class="text-center">
                    <b-button type="submit" variant="primary">Sign In</b-button>
                  </b-form-group>
                </form>
              </b-modal>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- end row -->
  </Layout>
</template>