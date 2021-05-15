<script>
import appConfig from '@src/app.config'
import Layout from '@layouts/main'
import PageHeader from '@components/page-header'

/**
 * Form Elements component
 */
export default {
  page: {
    title: 'Form Elements',
    meta: [{ name: 'description', content: appConfig.description }],
  },
  components: { Layout, PageHeader },
  data() {
    return {
      title: 'Form Elements',
      items: [
        {
          text: 'Hyper',
          href: '/',
        },
        {
          text: 'Forms',
          href: '/',
        },
        {
          text: 'Form Elements',
          active: true,
        },
      ],
      selected: '1',
      selectedlg: '1',
      selectedsm: '1',
      checked: true,
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
            <h4 class="header-title">Input Types</h4>
            <p class="text-muted font-14">
              Most common form control, text-based input fields. Includes support for all HTML5 types:
              <code>text</code>,
              <code>password</code>,
              <code>datetime</code>,
              <code>datetime-local</code>,
              <code>date</code>,
              <code>month</code>,
              <code>time</code>,
              <code>week</code>,
              <code>number</code>,
              <code>email</code>,
              <code>url</code>,
              <code>search</code>,
              <code>tel</code>, and
              <code>color</code>.
            </p>
            <b-row>
              <b-col lg="6">
                <form>
                  <b-form-group label="Text" label-for="simpleinput" class="mb-3">
                    <b-form-input id="simpleinput"></b-form-input>
                  </b-form-group>
                  <b-form-group label="Email" label-for="example-email" class="mb-3">
                    <b-form-input id="example-email" placeholder="Email"></b-form-input>
                  </b-form-group>
                  <b-form-group label="Password" label-for="example-pwd" class="mb-3">
                    <b-form-input id="example-pwd" type="password" value="password"></b-form-input>
                  </b-form-group>
                  <b-form-group label="Placeholder" label-for="example" class="mb-3">
                    <b-form-input id="example" placeholder="placeholder"></b-form-input>
                  </b-form-group>
                  <b-form-group label="Text area" label-for="example-textarea" class="mb-3">
                    <b-form-textarea id="example-textarea" rows="5"></b-form-textarea>
                  </b-form-group>
                  <b-form-group label="Readonly" label-for="example-readonly" class="mb-3">
                    <b-form-input id="example-readonly" value="Readonly value" readonly></b-form-input>
                  </b-form-group>
                  <b-form-group label="Disabled" label-for="example-disabled" class="mb-3">
                    <b-form-input id="example-disabled" value="Disabled value" disabled></b-form-input>
                  </b-form-group>
                  <b-form-group label="Static control" label-for="example-static" class="mb-3">
                    <b-form-input id="example-static" value="email@example.com" plaintext></b-form-input>
                  </b-form-group>
                  <b-form-group
                    label="Helping text"
                    label-for="example-helping"
                    description="A block of help text that breaks onto a new line and may extend beyond one line."
                  >
                    <b-form-input id="example-helping" placeholder="Helping text"></b-form-input>
                  </b-form-group>
                </form>
              </b-col>
              <b-col lg="6">
                <form>
                  <b-form-group label="Input Select" label-for="example-select" class="mb-3">
                    <select class="form-control custom-select">
                      <option>1</option>
                      <option>2</option>
                      <option>3</option>
                      <option>4</option>
                      <option>5</option>
                    </select>
                  </b-form-group>
                  <b-form-group label="Multiple Select" label-for="example-multiple" class="mb-3">
                    <select id="example-multiselect" multiple class="form-control">
                      <option>1</option>
                      <option>2</option>
                      <option>3</option>
                      <option>4</option>
                      <option>5</option>
                    </select>
                  </b-form-group>
                  <b-form-group label="Default file input" label-for="example-file" class="mb-3">
                    <b-form-file id="example-file" plain></b-form-file>
                  </b-form-group>
                  <b-form-group label="Date" label-for="example-date" class="mb-3">
                    <b-form-input id="example-date" type="date"></b-form-input>
                  </b-form-group>
                  <b-form-group label="Month" label-for="example-month" class="mb-3">
                    <b-form-input id="example-month" type="month"></b-form-input>
                  </b-form-group>
                  <b-form-group label="Time" label-for="example-time" class="mb-3">
                    <b-form-input id="example-time" type="time"></b-form-input>
                  </b-form-group>
                  <b-form-group label="Week" label-for="example-week" class="mb-3">
                    <b-form-input id="example-week" type="week"></b-form-input>
                  </b-form-group>
                  <b-form-group label="Number" label-for="example-number" class="mb-3">
                    <b-form-input id="example-number" type="number"></b-form-input>
                  </b-form-group>
                  <b-form-group label="Color" label-for="example-color" class="mb-3">
                    <b-form-input id="example-color" type="color" value="#727cf5"></b-form-input>
                  </b-form-group>
                  <b-form-group label="Color" label-for="example-range" class="mb-3">
                    <b-form-input id="example-range" :v-model="5" type="range" min="0" max="10"></b-form-input>
                  </b-form-group>
                </form>
              </b-col>
            </b-row>
          </div>
          <!-- end card-body -->
        </div>
        <!-- end card -->
      </div>
      <!-- end col -->
    </div>
    <!-- end row -->

    <div class="row">
      <div class="col-12">
        <div class="card">
          <div class="card-body">
            <div class="row">
              <div class="col-lg-6">
                <h4 class="header-title">Custom select</h4>
                <p class="text-muted font-14">
                  Custom
                  <code>&lt;select&gt;</code> menus need only a custom class,
                  <code>.custom-select</code> to trigger the custom styles.
                </p>
                <b-form-select v-model="selected" class="mb-3">
                  <option value="1">Open this select menu</option>
                  <option value="2">One</option>
                  <option value="3">Two</option>
                  <option value="4">Three</option>
                </b-form-select>
                <b-form-select v-model="selectedlg" size="lg" class="mb-3">
                  <option value="1">Open this select menu</option>
                  <option value="2">One</option>
                  <option value="3">Two</option>
                  <option value="4">Three</option>
                </b-form-select>
                <b-form-select v-model="selectedsm" size="sm" class="mb-3">
                  <option value="1">Open this select menu</option>
                  <option value="2">One</option>
                  <option value="3">Two</option>
                  <option value="4">Three</option>
                </b-form-select>
                <div class="input-group mb-3">
                  <div class="input-group-prepend">
                    <label class="input-group-text" for="inputGroupSelect01">Options</label>
                  </div>
                  <select id="inputGroupSelect01" class="custom-select">
                    <option selected>Choose...</option>
                    <option value="1">One</option>
                    <option value="2">Two</option>
                    <option value="3">Three</option>
                  </select>
                </div>
                <div class="input-group">
                  <select
                    id="inputGroupSelect04"
                    class="custom-select"
                    aria-label="Example select with button addon"
                  >
                    <option selected>Choose...</option>
                    <option value="1">One</option>
                    <option value="2">Two</option>
                    <option value="3">Three</option>
                  </select>
                  <div class="input-group-append">
                    <button class="btn btn-outline-secondary" type="button">Button</button>
                  </div>
                </div>

                <h4 class="header-title mt-4">Switches</h4>
                <p class="text-muted font-14">
                  A switch has the markup of a custom checkbox but uses the
                  <code>.custom-switch</code> class to render a toggle switch. Switches also support the
                  <code>disabled</code> attribute.
                </p>
                <b-form-checkbox name="check-button" switch>Toggle this switch element</b-form-checkbox>
                <b-form-checkbox
                  class="mt-1"
                  name="check-button"
                  switch
                  disabled
                >Disabled switch element</b-form-checkbox>
              </div>
              <div class="col-lg-6">
                <h4 class="header-title mt-5 mt-lg-0">Checkboxes and radios</h4>
                <p class="text-muted font-14">
                  Each checkbox and radio
                  <code>&lt;input&gt;</code> and
                  <code>&lt;label&gt;</code> pairing is wrapped in a
                  <code>&lt;div&gt;</code> to create our custom control. Structurally, this is the same approach as our default
                  <code>.form-check</code>.
                </p>
                <h6 class="font-15">Checkboxes</h6>
                <b-form-checkbox
                  id="checkbox-1"
                  name="checkbox-1"
                  value="accepted"
                  class="mt-3"
                  unchecked-value="not_accepted"
                >Check this custom checkbox</b-form-checkbox>
                <b-form-checkbox
                  id="checkbox-2"
                  name="checkbox-2"
                  value="accepted"
                  unchecked-value="not_accepted"
                >Check this custom checkbox</b-form-checkbox>
                <h6 class="font-15 mt-3">Inline</h6>
                <b-form-checkbox
                  id="checkbox-3"
                  name="checkbox-3"
                  value="accepted"
                  class="mt-1 custom-control-inline"
                  unchecked-value="not_accepted"
                >Check this custom checkbox</b-form-checkbox>
                <b-form-checkbox
                  id="checkbox-4"
                  name="checkbox-4"
                  value="accepted"
                  class="custom-control-inline"
                  unchecked-value="not_accepted"
                >Check this custom checkbox</b-form-checkbox>
                <h6 class="font-15 mt-3">Disabled</h6>
                <b-form-checkbox
                  id="checkbox-5"
                  v-model="checked"
                  name="checkbox-5"
                  class="mt-1 custom-control-inline"
                  disabled
                >Check this custom checkbox</b-form-checkbox>
                <b-form-checkbox
                  id="checkbox-6"
                  name="checkbox-6"
                  value="accepted"
                  class="custom-control-inline"
                  unchecked-value="not_accepted"
                  disabled
                >Check this custom checkbox</b-form-checkbox>
                <h6 class="font-15 mt-3">Radios</h6>
                <b-form-group>
                  <b-form-radio name="some-radios" value="A">Toggle this custom radio</b-form-radio>
                  <b-form-radio name="some-radios" value="B">Or toggle this other custom radio</b-form-radio>
                </b-form-group>
                <h6 class="font-15 mt-3">Inline</h6>
                <b-form-group>
                  <b-form-radio
                    name="some-radios"
                    value="A"
                    class="custom-control-inline"
                  >Toggle this custom radio</b-form-radio>
                  <b-form-radio
                    name="some-radios"
                    value="B"
                    class="custom-control-inline"
                  >Or toggle this other custom radio</b-form-radio>
                </b-form-group>
                <h6 class="font-15 mt-3">Disabled</h6>
                <b-form-group>
                  <b-form-radio
                    name="some-radios"
                    value="A"
                    class="custom-control-inline"
                    disabled
                  >Toggle this custom radio</b-form-radio>
                  <b-form-radio
                    v-model="selected"
                    name="some-radios"
                    value="B"
                    class="custom-control-inline"
                  >Or toggle this other custom radio</b-form-radio>
                </b-form-group>
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

    <div class="row">
      <div class="col-lg-6">
        <div class="card">
          <div class="card-body">
            <h4 class="header-title">Input Sizes</h4>
            <p class="text-muted font-14">
              Set heights using classes like
              <code>.input-lg</code>, and set widths using grid column classes like
              <code>.col-lg-*</code>.
            </p>
            <b-form-group label="Small" label-for="input-small" class="mb-3">
              <b-form-input id="input-small" size="sm" placeholder=".input-sm"></b-form-input>
            </b-form-group>
            <b-form-group label="Normal" label-for="input-normal" class="mb-3">
              <b-form-input id="input-normal" placeholder="Normal"></b-form-input>
            </b-form-group>
            <b-form-group label="Large" label-for="input-large" class="mb-3">
              <b-form-input id="input-large" size="lg" placeholder=".input-lg"></b-form-input>
            </b-form-group>
            <b-form-group label="Grid Sizes" label-for="input-grid">
              <b-row>
                <b-col sm="4">
                  <b-form-input id="input-grid" placeholder=".col-sm-4"></b-form-input>
                </b-col>
              </b-row>
            </b-form-group>
          </div>
        </div>
      </div>
      <!-- end col -->
      <div class="col-lg-6">
        <div class="card">
          <div class="card-body">
            <h4 class="header-title">Input Group</h4>
            <p
              class="text-muted font-14"
            >Easily extend form controls by adding text, buttons, or button groups on either side of textual inputs, custom selects, and custom file inputs</p>
            <label for="inline-form-input-username">Static</label>
            <b-input-group prepend="@" class="mb-2 mr-sm-2 mb-sm-0">
              <b-input id="inline-form-input-username" placeholder="Username"></b-input>
            </b-input-group>

            <label for="input-dropdown" class="mt-3">Dropdowns</label>
            <b-input-group id="input-dropdown" class="mb-3">
              <template v-slot:prepend>
                <b-dropdown text="Dropdown" variant="primary">
                  <b-dropdown-item>Action</b-dropdown-item>
                  <b-dropdown-item>Another action</b-dropdown-item>
                  <b-dropdown-item>Something else here</b-dropdown-item>
                </b-dropdown>
              </template>
              <b-form-input></b-form-input>
            </b-input-group>

            <label for="input-button">Buttons</label>
            <b-input-group id="input-button">
              <b-form-input placeholder="Recipient's username"></b-form-input>
              <b-input-group-append>
                <b-button text="Button" variant="dark">Button</b-button>
              </b-input-group-append>
            </b-input-group>

            <label for="input-file" class="mt-3">Custom file input</label>
            <b-form-file
              id="input-file"
              placeholder="Choose file"
              drop-placeholder="Drop file here..."
            ></b-form-file>
          </div>
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
            <h4 class="header-title">Basic Example</h4>
            <p
              class="text-muted font-14"
            >Here’s a quick example to demonstrate Bootstrap’s form styles. Keep reading for documentation on required classes, form layout, and more.</p>

            <b-form>
              <b-form-group
                id="input-group-1"
                label="Email address:"
                label-for="input-email"
                description="We'll never share your email with anyone else."
              >
                <b-form-input id="input-email" type="email" placeholder="Enter email"></b-form-input>
              </b-form-group>

              <b-form-group label="Password" label-for="example-password" class="mb-2">
                <b-form-input id="example-password" type="password" placeholder="password"></b-form-input>
              </b-form-group>
              <b-form-group id="input-group-4">
                <b-form-checkbox value="me">Check me out</b-form-checkbox>
              </b-form-group>
              <b-button variant="primary" type="submit">Submit</b-button>
            </b-form>
          </div>
          <!-- end card-body -->
        </div>
        <!-- end card -->
      </div>
      <!-- end col -->

      <div class="col-lg-6">
        <div class="card">
          <div class="card-body">
            <h4 class="header-title">Horizontal form</h4>
            <p class="text-muted font-14">
              Create horizontal forms with the grid by adding the
              <code>.row</code> class to form groups and using the
              <code>.col-*-*</code> classes to specify the width of your labels and controls. Be sure to add
              <code>.col-form-label</code> to your
              <code>&lt;label&gt;</code>s as well so they’re vertically centered with their associated form controls.
            </p>
            <form class="form-horizontal" role="form">
              <b-form-group
                id="email-horizontal"
                label-cols-sm="4"
                label-cols-lg="3"
                label="Email"
                label-for="horizontal-email"
              >
                <b-form-input id="horizontal-email" type="email" placeholder="Email"></b-form-input>
              </b-form-group>

              <b-form-group
                id="password-horizontal"
                label-cols-sm="4"
                label-cols-lg="3"
                label="Password"
                label-for="inputPassword3"
              >
                <b-form-input id="inputPassword3" type="password" placeholder="Password"></b-form-input>
              </b-form-group>

              <b-form-group
                id="repassword-horizontal"
                label-cols-sm="4"
                label-cols-lg="3"
                label="Re Password"
                label-for="inputPassword4"
              >
                <b-form-input id="inputPassword4" type="password" placeholder="Retype Password"></b-form-input>
              </b-form-group>

              <div class="form-group row justify-content-end">
                <div class="col-sm-9">
                  <b-form-checkbox value="me">Check me out</b-form-checkbox>
                </div>
              </div>
              <div class="form-group mb-0 justify-content-end row">
                <div class="col-sm-9">
                  <b-button type="submit" variant="info">Sign in</b-button>
                </div>
              </div>
            </form>
          </div>
          <!-- end card-body -->
        </div>
        <!-- end card -->
      </div>
      <!-- end col -->
    </div>
    <!-- end row -->

    <!-- Inline Form -->
    <div class="row">
      <div class="col-md-12">
        <div class="card">
          <div class="card-body">
            <h4 class="header-title">Inline Form</h4>
            <p class="text-muted font-14">
              Use the
              <code>.form-inline</code> class to display a series of labels, form controls, and buttons on a single horizontal row. Form controls within inline forms vary slightly from their default states. Controls only appear inline in viewports that are at least 576px wide to account for narrow viewports on mobile devices.
            </p>
            <div class="row">
              <div class="col-sm-12">
                <form class="form-inline">
                  <div class="form-group">
                    <label for="staticEmail2" class="sr-only">Email</label>
                    <input
                      id="staticEmail2"
                      type="text"
                      readonly
                      class="form-control-plaintext"
                      value="email@example.com"
                    />
                  </div>
                  <div class="form-group mx-sm-3">
                    <label for="inputPassword2" class="sr-only">Password</label>
                    <input
                      id="inputPassword2"
                      type="password"
                      class="form-control"
                      placeholder="Password"
                    />
                  </div>
                  <button type="submit" class="btn btn-primary">Confirm identity</button>
                </form>
              </div>
            </div>
            <div class="row">
              <div class="col-sm-12">
                <h6 class="font-13 mt-4">Auto-sizing</h6>
                <b-form inline>
                  <label class="sr-only" for="inline-form-input-name">Name</label>
                  <b-input
                    id="inline-form-input-name"
                    class="mb-2 mr-sm-2 mb-sm-0"
                    placeholder="Jane Doe"
                  ></b-input>

                  <label class="sr-only" for="inline-form-username">Username</label>
                  <b-input-group prepend="@" class="mb-2 mr-sm-2 mb-sm-0">
                    <b-input id="inline-form-username" placeholder="Username"></b-input>
                  </b-input-group>

                  <b-form-checkbox class="mb-2 mr-sm-2 mb-sm-0">Remember me</b-form-checkbox>

                  <b-button variant="primary">Submit</b-button>
                </b-form>
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

    <!-- Horizontal form -->
    <div class="row">
      <div class="col-12">
        <div class="card">
          <div class="card-body">
            <h4 class="header-title">Horizontal form label sizing</h4>
            <p class="text-muted font-14">
              Be sure to use
              <code>.col-form-label-sm</code> or
              <code>.col-form-label-lg</code> to your
              <code>&lt;label&gt;</code>s or
              <code>&lt;legend&gt;</code>s to correctly follow the size of
              <code>.form-control-lg</code> and
              <code>.form-control-sm</code>.
            </p>
            <form>
              <b-form-group>
                <b-row>
                  <b-col sm="2">
                    <label for="inputEmailsm" class="col-form-label-sm">Email</label>
                  </b-col>
                  <b-col sm="10">
                    <b-form-input
                      id="inputEmailsm"
                      size="sm"
                      type="email"
                      placeholder="col-form-label-sm"
                    ></b-form-input>
                  </b-col>
                </b-row>
                <b-row class="mt-1">
                  <b-col sm="2">
                    <label for="inputEmail" class="col-form-label">Email</label>
                  </b-col>
                  <b-col sm="10">
                    <b-form-input id="inputEmail" type="email" placeholder="col-form-label"></b-form-input>
                  </b-col>
                </b-row>
                <b-row class="mt-2">
                  <b-col sm="2">
                    <label for="inputEmaillg" class="col-form-label-lg">Email</label>
                  </b-col>
                  <b-col sm="10">
                    <b-form-input
                      id="inputEmaillg"
                      size="lg"
                      type="email"
                      placeholder="col-form-label-lg"
                    ></b-form-input>
                  </b-col>
                </b-row>
              </b-form-group>
            </form>
          </div>
          <!-- end card-body -->
        </div>
        <!-- end card -->
      </div>
      <!-- end col -->
    </div>
    <!-- end row -->

    <!-- Form row -->
    <div class="row">
      <div class="col-12">
        <div class="card">
          <div class="card-body">
            <h4 class="header-title">Form Row</h4>
            <p class="text-muted font-14">
              You may also swap
              <code>.row</code> for
              <code>.form-row</code>, a variation of our standard grid row that overrides the default column gutters for tighter and more compact layouts.
            </p>

            <form>
              <b-form-group>
                <b-row>
                  <b-col md="6">
                    <label for="inputEmail4">Email</label>
                    <b-form-input id="inputEmail4" type="email" placeholder="Email"></b-form-input>
                  </b-col>
                  <b-col md="6">
                    <label for="inputPassword5">Password</label>
                    <b-form-input id="inputPassword5" type="password" placeholder="Password"></b-form-input>
                  </b-col>
                </b-row>
              </b-form-group>
              <b-form-group>
                <label for="inputAddress">Address</label>
                <b-form-input id="inputAddress" type="text" placeholder="1234 Main St"></b-form-input>
              </b-form-group>
              <b-form-group>
                <label for="inputAddress2">Address 2</label>
                <b-form-input id="inputAddress2" placeholder="Apartment, studio, or floor"></b-form-input>
              </b-form-group>
              <b-form-group>
                <b-row>
                  <b-col md="6">
                    <label for="inputCity">City</label>
                    <b-form-input id="inputCity"></b-form-input>
                  </b-col>
                  <b-col md="4">
                    <label for="inputState">State</label>
                    <b-form-select id="inputState">
                      <option>Option 1</option>
                      <option>Option 2</option>
                      <option>Option 3</option>
                    </b-form-select>
                  </b-col>
                  <b-col md="2">
                    <label for="inputZip">Zip</label>
                    <b-form-input id="inputZip"></b-form-input>
                  </b-col>
                </b-row>
              </b-form-group>
              <div class="form-group">
                <div class="custom-control custom-checkbox">
                  <input id="customCheck11" type="checkbox" class="custom-control-input" />
                  <label class="custom-control-label" for="customCheck11">Check this custom checkbox</label>
                </div>
              </div>
              <b-button type="submit" variant="primary">Sign in</b-button>
            </form>
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