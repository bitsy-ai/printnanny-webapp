<script>
import appConfig from '@src/app.config'
import Layout from '@layouts/main'
import PageHeader from '@components/page-header'

/**
 * Dropdowns component
 */
export default {
  page: {
    title: 'Dropdowns',
    meta: [{ name: 'description', content: appConfig.description }],
  },
  components: { Layout, PageHeader },
  data() {
    return {
      title: 'Dropdowns',
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
          text: 'Dropdowns',
          active: true,
        },
      ],
    }
  },
  methods: {
    onClick() {
      // Close the menu and (by passing true) return focus to the toggle button
      this.$refs.dropdown.hide(true)
    },
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
            <h4 class="header-title">Single button dropdowns</h4>
            <p class="text-muted font-14">
              Any single
              <code>.btn</code> can be turned into a dropdown
              toggle with some markup changes. Here’s how you can put them to work
              with either
              <code>&lt;button&gt;</code>
              elements:
            </p>
            <b-dropdown variant="light" text="Dropdown button" class="m-md-2">
              <b-dropdown-item>Action</b-dropdown-item>
              <b-dropdown-item>Another action</b-dropdown-item>
              <b-dropdown-item>Something else here</b-dropdown-item>
            </b-dropdown>
          </div>
          <!-- end card-body -->
        </div>
        <!-- end card -->
        <div class="card">
          <div class="card-body">
            <h4 class="header-title">Variant</h4>
            <p
              class="text-muted font-14"
            >The best part is you can do this with any button variant, too:</p>
            <b-dropdown text="Primary" variant="primary">
              <b-dropdown-item href="#">Action</b-dropdown-item>
              <b-dropdown-item href="#">Another action</b-dropdown-item>
              <b-dropdown-item href="#">Something else here</b-dropdown-item>
              <b-dropdown-divider></b-dropdown-divider>
              <b-dropdown-item href="#">Separated link</b-dropdown-item>
            </b-dropdown>

            <b-dropdown text="Light" variant="light" class="ml-1">
              <b-dropdown-item href="#">Action</b-dropdown-item>
              <b-dropdown-item href="#">Another action</b-dropdown-item>
              <b-dropdown-item href="#">Something else here</b-dropdown-item>
              <b-dropdown-divider></b-dropdown-divider>
              <b-dropdown-item href="#">Separated link</b-dropdown-item>
            </b-dropdown>
            <b-dropdown text="Success" variant="success" class="ml-1">
              <b-dropdown-item href="#">Action</b-dropdown-item>
              <b-dropdown-item href="#">Another action</b-dropdown-item>
              <b-dropdown-item href="#">Something else here</b-dropdown-item>
              <b-dropdown-divider></b-dropdown-divider>
              <b-dropdown-item href="#">Separated link</b-dropdown-item>
            </b-dropdown>
            <b-dropdown text="Info" variant="info" class="ml-1">
              <b-dropdown-item href="#">Action</b-dropdown-item>
              <b-dropdown-item href="#">Another action</b-dropdown-item>
              <b-dropdown-item href="#">Something else here</b-dropdown-item>
              <b-dropdown-divider></b-dropdown-divider>
              <b-dropdown-item href="#">Separated link</b-dropdown-item>
            </b-dropdown>
            <b-dropdown text="Warning" variant="warning" class="ml-1">
              <b-dropdown-item href="#">Action</b-dropdown-item>
              <b-dropdown-item href="#">Another action</b-dropdown-item>
              <b-dropdown-item href="#">Something else here</b-dropdown-item>
              <b-dropdown-divider></b-dropdown-divider>
              <b-dropdown-item href="#">Separated link</b-dropdown-item>
            </b-dropdown>
            <b-dropdown text="Danger" variant="danger" class="ml-1">
              <b-dropdown-item href="#">Action</b-dropdown-item>
              <b-dropdown-item href="#">Another action</b-dropdown-item>
              <b-dropdown-item href="#">Something else here</b-dropdown-item>
              <b-dropdown-divider></b-dropdown-divider>
              <b-dropdown-item href="#">Separated link</b-dropdown-item>
            </b-dropdown>
          </div>
          <!-- end card-body -->
        </div>
        <!-- end card -->

        <div class="card">
          <div class="card-body">
            <h4 class="header-title">Dropup variation</h4>
            <p class="text-muted font-14">
              Trigger dropdown menus above elements
              by adding
              <code>dropup</code> to the parent
              element.
            </p>
            <b-dropdown id="dropdown-dropup" dropup text="Dropup" variant="light">
              <b-dropdown-item href="#">Action</b-dropdown-item>
              <b-dropdown-item href="#">Another action</b-dropdown-item>
              <b-dropdown-item href="#">Something else here</b-dropdown-item>
              <b-dropdown-divider></b-dropdown-divider>
              <b-dropdown-item href="#">Separated link</b-dropdown-item>
            </b-dropdown>

            <b-dropdown split dropup text="Split dropup" variant="light" class="ml-1">
              <b-dropdown-item href="#">Action</b-dropdown-item>
              <b-dropdown-item href="#">Another action</b-dropdown-item>
              <b-dropdown-item href="#">Something else here...</b-dropdown-item>
              <b-dropdown-divider></b-dropdown-divider>
              <b-dropdown-item href="#">Separated link</b-dropdown-item>
            </b-dropdown>
          </div>
          <!-- end card-body -->
        </div>
        <!-- end card -->

        <div class="card">
          <div class="card-body">
            <h4 class="header-title">Dropright variation</h4>
            <p class="text-muted font-14">
              Trigger dropdown menus at the right of the elements by adding
              <code>dropright</code> to the parent element.
            </p>
            <b-dropdown dropright text="Dropright" variant="primary">
              <b-dropdown-item href="#">Action</b-dropdown-item>
              <b-dropdown-item href="#">Another action</b-dropdown-item>
              <b-dropdown-item href="#">Something else here</b-dropdown-item>
              <b-dropdown-divider></b-dropdown-divider>
              <b-dropdown-item href="#">Separated link</b-dropdown-item>
            </b-dropdown>

            <b-dropdown split dropright text="Split dropright" variant="primary" class="ml-1">
              <b-dropdown-item href="#">Action</b-dropdown-item>
              <b-dropdown-item href="#">Another action</b-dropdown-item>
              <b-dropdown-item href="#">Something else here...</b-dropdown-item>
              <b-dropdown-divider></b-dropdown-divider>
              <b-dropdown-item href="#">Separated link</b-dropdown-item>
            </b-dropdown>
          </div>
          <!-- end card-body -->
        </div>
        <!-- end card -->

        <div class="card">
          <div class="card-body">
            <h4 class="header-title">Disabled Item</h4>
            <p class="text-muted font-14">
              Add
              <code>disabled</code> to items in the dropdown to
              <strong>style them as disabled</strong>.
            </p>
            <b-dropdown text="Disabled" variant="primary">
              <b-dropdown-item>Regular link</b-dropdown-item>
              <b-dropdown-item disabled>Disabled link</b-dropdown-item>
              <b-dropdown-item>Another link</b-dropdown-item>
            </b-dropdown>
          </div>
          <!-- end card-body -->
        </div>
        <!-- end card -->

        <div class="card">
          <div class="card-body">
            <h4 class="header-title">Forms</h4>
            <p
              class="text-muted font-14"
            >Put a form within a dropdown menu, or make it into a dropdown menu, and use margin or padding utilities to give it the negative space you require.</p>

            <b-dropdown
              id="dropdown-text"
              text="Text Dropdown"
              menu-class="text-muted"
              variant="primary"
            >
              <b-dropdown-text>Some example text that's free-flowing within the dropdown menu.</b-dropdown-text>
              <b-dropdown-text>And this is more example text.</b-dropdown-text>
            </b-dropdown>
          </div>
          <!-- end card-body -->
        </div>
        <!-- end card -->
      </div>
      <!-- end col -->

      <div class="col-xl-6">
        <div class="card">
          <div class="card-body">
            <h4 class="header-title">Menu alignment</h4>
            <p class="text-muted font-14">
              Add
              <code>.dropdown-menu-right</code>
              to a
              <code>.dropdown-menu</code> to right
              align the dropdown menu.
            </p>
            <b-dropdown
              id="dropdown-right"
              right
              text="Right-aligned menu"
              variant="light"
              class="m-2"
            >
              <b-dropdown-item href="#">Action</b-dropdown-item>
              <b-dropdown-item href="#">Another action</b-dropdown-item>
              <b-dropdown-item href="#">Something else here</b-dropdown-item>
            </b-dropdown>
          </div>
          <!-- end card-body -->
        </div>
        <!-- end card -->
        <div class="card">
          <div class="card-body">
            <h4 class="header-title">Split button dropdowns</h4>
            <p class="text-muted font-14">
              Similarly, create split button dropdowns with virtually the same markup as single button dropdowns, but with the addition of
              <code>.dropdown-toggle-split</code> for proper spacing around the dropdown caret.
            </p>
            <b-dropdown split variant="primary" text="Primary">
              <b-dropdown-item href="#">Action</b-dropdown-item>
              <b-dropdown-item href="#">Another action</b-dropdown-item>
              <b-dropdown-item href="#">Something else here</b-dropdown-item>
              <b-dropdown-divider></b-dropdown-divider>
              <b-dropdown-item href="#">Separated link</b-dropdown-item>
            </b-dropdown>
            <b-dropdown split variant="light" text="Secondary" class="ml-1">
              <b-dropdown-item href="#">Action</b-dropdown-item>
              <b-dropdown-item href="#">Another action</b-dropdown-item>
              <b-dropdown-item href="#">Something else here</b-dropdown-item>
              <b-dropdown-divider></b-dropdown-divider>
              <b-dropdown-item href="#">Separated link</b-dropdown-item>
            </b-dropdown>
            <b-dropdown split variant="success" text="Success" class="ml-1">
              <b-dropdown-item href="#">Action</b-dropdown-item>
              <b-dropdown-item href="#">Another action</b-dropdown-item>
              <b-dropdown-item href="#">Something else here</b-dropdown-item>
              <b-dropdown-divider></b-dropdown-divider>
              <b-dropdown-item href="#">Separated link</b-dropdown-item>
            </b-dropdown>
            <b-dropdown split variant="info" text="Info" class="ml-1">
              <b-dropdown-item href="#">Action</b-dropdown-item>
              <b-dropdown-item href="#">Another action</b-dropdown-item>
              <b-dropdown-item href="#">Something else here</b-dropdown-item>
              <b-dropdown-divider></b-dropdown-divider>
              <b-dropdown-item href="#">Separated link</b-dropdown-item>
            </b-dropdown>
            <b-dropdown split variant="warning" text="Warning" class="ml-1">
              <b-dropdown-item href="#">Action</b-dropdown-item>
              <b-dropdown-item href="#">Another action</b-dropdown-item>
              <b-dropdown-item href="#">Something else here</b-dropdown-item>
              <b-dropdown-divider></b-dropdown-divider>
              <b-dropdown-item href="#">Separated link</b-dropdown-item>
            </b-dropdown>
            <b-dropdown split variant="danger" text="Danger" class="ml-1">
              <b-dropdown-item href="#">Action</b-dropdown-item>
              <b-dropdown-item href="#">Another action</b-dropdown-item>
              <b-dropdown-item href="#">Something else here</b-dropdown-item>
              <b-dropdown-divider></b-dropdown-divider>
              <b-dropdown-item href="#">Separated link</b-dropdown-item>
            </b-dropdown>
          </div>
          <!-- end card-body -->
        </div>
        <!-- end card -->

        <div class="card">
          <div class="card-body">
            <h4 class="header-title">Dropleft variation</h4>
            <p class="text-muted font-14">
              Trigger dropdown menus at the right of the elements by adding
              <code>.dropleft</code> to the parent element.
            </p>
            <b-dropdown dropleft text="Dropleft" variant="light">
              <b-dropdown-item href="#">Action</b-dropdown-item>
              <b-dropdown-item href="#">Another action</b-dropdown-item>
              <b-dropdown-item href="#">Something else here</b-dropdown-item>
              <b-dropdown-divider></b-dropdown-divider>
              <b-dropdown-item href="#">Separated link</b-dropdown-item>
            </b-dropdown>

            <b-dropdown split dropleft text="Split dropleft" variant="light" class="ml-1">
              <b-dropdown-item href="#">Action</b-dropdown-item>
              <b-dropdown-item href="#">Another action</b-dropdown-item>
              <b-dropdown-item href="#">Something else here...</b-dropdown-item>
              <b-dropdown-divider></b-dropdown-divider>
              <b-dropdown-item href="#">Separated link</b-dropdown-item>
            </b-dropdown>
          </div>
          <!-- end card-body -->
        </div>
        <!-- end card -->

        <div class="card">
          <div class="card-body">
            <h4 class="header-title">Active Item</h4>
            <p class="text-muted font-14">
              Add
              <code>.active</code> to item in the dropdown to
              <strong>style them as active</strong>.
            </p>
            <b-dropdown text="Active Item">
              <b-dropdown-item>Regular link</b-dropdown-item>
              <b-dropdown-item active>Active link</b-dropdown-item>
              <b-dropdown-item>Another link</b-dropdown-item>
            </b-dropdown>
          </div>
          <!-- end card-body -->
        </div>
        <!-- end card -->
        <div class="card">
          <div class="card-body">
            <h4 class="header-title">Headers</h4>
            <p
              class="text-muted font-14"
            >Add a header to label sections of actions in any dropdown menu.</p>
            <b-dropdown text="Header">
              <b-dropdown-header id="dropdown-header-label" tag="h6">Dropdown header</b-dropdown-header>
              <b-dropdown-item-button aria-describedby="dropdown-header-label">Action</b-dropdown-item-button>
              <b-dropdown-item-button aria-describedby="dropdown-header-label">Another Action</b-dropdown-item-button>
            </b-dropdown>
          </div>
          <!-- end card-body -->
        </div>
        <!-- end card -->
        <div class="card">
          <div class="card-body">
            <h4 class="header-title">Forms</h4>
            <p
              class="text-muted font-14"
            >Put a form within a dropdown menu, or make it into a dropdown menu, and use margin or padding utilities to give it the negative space you require.</p>
            <b-dropdown id="dropdown-form" text="Form" menu-class="p-2 text-muted">
              <b-dropdown-form>
                <b-form-group label="Email" label-for="dropdown-form-email" @submit.stop.prevent>
                  <b-form-input id="dropdown-form-email" size="sm" placeholder="email@example.com"></b-form-input>
                </b-form-group>

                <b-form-group label="Password" label-for="dropdown-form-password">
                  <b-form-input
                    id="dropdown-form-password"
                    type="password"
                    size="sm"
                    placeholder="Password"
                  ></b-form-input>
                </b-form-group>

                <b-form-checkbox class="mb-3" plain>Remember me</b-form-checkbox>
                <b-button variant="primary" size="sm" @click="onClick">Sign In</b-button>
              </b-dropdown-form>
              <b-dropdown-divider></b-dropdown-divider>
              <b-dropdown-item>New around here? Sign up</b-dropdown-item>
              <b-dropdown-item>Forgot Password?</b-dropdown-item>
            </b-dropdown>
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