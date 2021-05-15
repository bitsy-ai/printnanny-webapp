<script>
import appConfig from '@src/app.config'
import Layout from '@layouts/main'
import PageHeader from '@components/page-header'

/**
 * Buttons component
 */
export default {
  page: {
    title: 'Buttons',
    meta: [{ name: 'description', content: appConfig.description }],
  },
  components: { Layout, PageHeader },
  data() {
    return {
      title: 'Buttons',
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
          text: 'Buttons',
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
      <div class="col-lg-6">
        <div class="card">
          <div class="card-body">
            <h4 class="header-title">Default Buttons</h4>
            <p class="text-muted font-14">
              Use the button classes on an
              <code>&lt;a&gt;</code>,
              <code>&lt;button&gt;</code>, or
              <code>&lt;input&gt;</code> element.
            </p>
            <b-button variant="primary">Primary</b-button>
            <b-button class="ml-2">Secondary</b-button>
            <b-button variant="success" class="ml-2">Success</b-button>
            <b-button variant="danger" class="ml-2">Danger</b-button>
            <b-button variant="warning" class="ml-2">Warning</b-button>
            <b-button variant="info" class="ml-2">Info</b-button>
            <b-button variant="light" class="ml-2">Light</b-button>
            <b-button variant="dark" class="ml-2">Dark</b-button>
          </div>
          <!-- end card-body -->
        </div>
        <!-- end card -->
      </div>
      <div class="col-lg-6">
        <div class="card">
          <div class="card-body">
            <h4 class="header-title">Button Outline</h4>
            <p class="text-muted font-14">
              Use a classes
              <code>outline-**</code> to quickly create a bordered buttons.
            </p>
            <b-button variant="outline-primary">Primary</b-button>
            <b-button variant="outline-secondary" class="ml-2">Secondary</b-button>
            <b-button variant="outline-success" class="ml-2">
              <i class="uil-cloud-computing"></i> Success
            </b-button>
            <b-button variant="outline-danger" class="ml-2">Danger</b-button>
            <b-button variant="outline-warning" class="ml-2">Warning</b-button>
            <b-button variant="outline-info" class="ml-2">
              <i class="uil-circuit"></i> Info
            </b-button>
            <b-button variant="outline-light" class="ml-2">Light</b-button>
            <b-button variant="outline-dark" class="ml-2">Dark</b-button>
          </div>
          <!-- end card-body -->
        </div>
        <!-- end card -->
      </div>
      <!-- end col -->
    </div>

    <div class="row">
      <div class="col-lg-6">
        <div class="card">
          <div class="card-body">
            <h4 class="header-title">Button-Rounded</h4>
            <p class="text-muted font-14">
              Add
              <code>pill</code> to default button to get rounded corners.
            </p>
            <b-button pill variant="primary">Primary</b-button>
            <b-button pill class="ml-2">Secondary</b-button>
            <b-button pill variant="success" class="ml-2">Success</b-button>
            <b-button pill variant="danger" class="ml-2">Danger</b-button>
            <b-button pill variant="warning" class="ml-2">Warning</b-button>
            <b-button pill variant="info" class="ml-2">Info</b-button>
            <b-button pill variant="light" class="ml-2">Light</b-button>
            <b-button pill variant="dark" class="ml-2">Dark</b-button>
          </div>
          <!-- end card-body -->
        </div>
        <!-- end card -->
      </div>
      <!-- end col -->
      <div class="col-lg-6">
        <div class="card">
          <div class="card-body">
            <h4 class="header-title">Button Outline Rounded</h4>
            <p class="text-muted font-14">
              Use a classes
              <code>outline-**</code> to quickly create a bordered buttons.
            </p>
            <b-button pill variant="outline-primary">Primary</b-button>
            <b-button pill variant="outline-secondary" class="ml-2">Secondary</b-button>
            <b-button pill variant="outline-success" class="ml-2">
              <i class="uil-cloud-computing"></i> Success
            </b-button>
            <b-button pill variant="outline-danger" class="ml-2">Danger</b-button>
            <b-button pill variant="outline-warning" class="ml-2">Warning</b-button>
            <b-button pill variant="outline-info" class="ml-2">
              <i class="uil-circuit"></i> Info
            </b-button>
            <b-button pill variant="outline-light" class="ml-2">Light</b-button>
            <b-button pill variant="outline-dark" class="ml-2">Dark</b-button>
          </div>
          <!-- end card-body -->
        </div>
        <!-- end card -->
      </div>
      <!-- end col -->
    </div>
    <!-- end row -->

    <div class="row">
      <div class="col-lg-6">
        <div class="card">
          <div class="card-body">
            <h4 class="header-title">Button-Sizes</h4>
            <p class="text-muted font-14">
              Add
              <code>lg</code>,
              <code>sm</code> for additional sizes.
            </p>
            <b-button size="lg" variant="primary">Large</b-button>
            <b-button variant="info" class="ml-2">Normal</b-button>
            <b-button size="sm" variant="success" class="ml-2">Small</b-button>
          </div>
          <!-- end card-body -->
        </div>
        <!-- end card -->
      </div>
      <!-- end col -->
      <div class="col-lg-6">
        <div class="card">
          <div class="card-body">
            <h4 class="header-title">Button-Disabled</h4>
            <p class="text-muted font-14">
              Add the
              <code>disabled</code> attribute to
              <code>&lt;button&gt;</code> buttons.
            </p>
            <b-button disabled variant="info">Info</b-button>
            <b-button disabled variant="success" class="ml-2">Success</b-button>
            <b-button disabled variant="danger" class="ml-2">Danger</b-button>
            <b-button disabled variant="dark" class="ml-2">Dark</b-button>
          </div>
          <!-- end card-body -->
        </div>
        <!-- end card -->
      </div>
      <!-- end col -->
    </div>
    <!-- end row -->

    <div class="row">
      <div class="col-lg-6">
        <div class="card">
          <div class="card-body">
            <h4 class="header-title">Icon Buttons</h4>
            <p class="text-muted font-14">Icon only button.</p>
            <b-button variant="light">
              <i class="mdi mdi-heart-outline"></i>
            </b-button>
            <b-button variant="danger" class="ml-2">
              <i class="mdi mdi-window-close"></i>
            </b-button>
            <b-button variant="dark" class="ml-2">
              <i class="mdi mdi-music"></i>
            </b-button>
            <b-button variant="primary" class="ml-2">
              <i class="mdi mdi-star"></i>
            </b-button>
            <b-button variant="success" class="ml-2">
              <i class="mdi mdi-thumb-up-outline"></i>
            </b-button>
            <b-button variant="info" class="ml-1">
              <i class="mdi mdi-keyboard"></i>
            </b-button>
            <b-button variant="warning" class="ml-2">
              <i class="mdi mdi-wrench"></i>
            </b-button>
            <div class="mt-2">
              <b-button variant="light">
                <i class="mdi mdi-heart mr-1"></i>
                <span>Like</span>
              </b-button>
              <b-button variant="warning" class="ml-1">
                <i class="mdi mdi-rocket mr-1"></i>
                <span>Launch</span>
              </b-button>
              <b-button variant="info" class="ml-1">
                <i class="mdi mdi-cloud mr-1"></i>
                <span>Cloud Hosting</span>
              </b-button>
            </div>
            <div class="mt-2">
              <b-button variant="outline-success">
                <i class="uil-money-withdrawal"></i> Money
              </b-button>
              <b-button variant="outline-primary" class="ml-1">
                <i class="uil-paypal"></i> PayPal
              </b-button>
              <b-button variant="outline-danger" class="ml-1">
                <i class="uil-cog"></i> Settings
              </b-button>
            </div>
          </div>
          <!-- end card-body -->
        </div>
        <!-- end card -->
      </div>
      <!-- end col -->

      <div class="col-lg-6">
        <div class="card">
          <div class="card-body">
            <h4 class="header-title">Block Button</h4>

            <p class="text-muted font-14">
              Create block level buttons,with by adding add
              <code>block</code>.
            </p>
            <b-button block variant="primary">Block Button</b-button>
            <b-button block variant="info">Block Button</b-button>
            <b-button block variant="success">Block Button</b-button>
          </div>
          <!-- end card-body -->
        </div>
        <!-- end card -->
      </div>
      <!-- end col -->
    </div>
    <!-- end row -->

    <div class="row">
      <div class="col-lg-6">
        <div class="card">
          <div class="card-body">
            <h4 class="header-title">Button Group</h4>
            <p class="text-muted font-14">
              Wrap a series of buttons with
              <code>b-button-group</code>.
            </p>
            <div class="btn-group mb-2">
              <b-button-group>
                <b-button variant="light">Left</b-button>
                <b-button variant="light">Middle</b-button>
                <b-button variant="light">Right</b-button>
              </b-button-group>
            </div>
            <br />
            <div class="btn-group mb-2">
              <b-button-group>
                <b-button variant="light">1</b-button>
                <b-button variant="light">2</b-button>
                <b-button variant="light">3</b-button>
                <b-button variant="light">4</b-button>
              </b-button-group>
            </div>
            <div class="btn-group mb-2 ml-1">
              <b-button-group>
                <b-button variant="light">5</b-button>
                <b-button variant="light">6</b-button>
                <b-button variant="light">7</b-button>
              </b-button-group>
            </div>
            <div class="btn-group mb-2 ml-1">
              <b-button-group>
                <b-button variant="light">8</b-button>
              </b-button-group>
            </div>
            <br />
            <div class="btn-group">
              <b-button-group>
                <b-button variant="light">1</b-button>
                <b-button variant="primary">2</b-button>
                <b-button variant="light">3</b-button>
                <b-dropdown variant="light" text="Dropdown">
                  <b-dropdown-item>Dropdown Link</b-dropdown-item>
                  <b-dropdown-item>Dropdown Link</b-dropdown-item>
                </b-dropdown>
              </b-button-group>
            </div>
            <div class="row">
              <div class="col-md-3">
                <div class="mt-2">
                  <b-button-group vertical>
                    <b-button variant="light">Top</b-button>
                    <b-button variant="light">Middle</b-button>
                    <b-button variant="light">Bottom</b-button>
                  </b-button-group>
                </div>
              </div>
              <div class="col-md-3">
                <div class="mt-2">
                  <b-button-group vertical>
                    <b-button variant="light">Button 1</b-button>
                    <b-button variant="light">Button 2</b-button>
                    <b-dropdown variant="light" text="Button 3">
                      <b-dropdown-item>Dropdown Link</b-dropdown-item>
                      <b-dropdown-item>Dropdown Link</b-dropdown-item>
                    </b-dropdown>
                  </b-button-group>
                </div>
              </div>
            </div>
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