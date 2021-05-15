<script>
import appConfig from '@src/app.config'
import Layout from '@layouts/main'
import PageHeader from '@components/page-header'
import { required } from 'vuelidate/lib/validators'
/**
 * Form Validation component
 */
export default {
  page: {
    title: 'Form Validation',
    meta: [{ name: 'description', content: appConfig.description }],
  },
  components: { Layout, PageHeader },
  data() {
    return {
      title: 'Form Validation',
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
          text: 'Form Validation',
          active: true,
        },
      ],
      form: {
        fname: '',
        lname: '',
        username: '',
        city: '',
        state: '',
        zipcode: '',
      },
      tooltipform: {
        fname: '',
        lname: '',
        username: '',
        city: '',
        state: '',
        zipcode: '',
      },
      submitted: false,
      submitform: false,
    }
  },
  validations: {
    form: {
      fname: { required },
      lname: { required },
      username: { required },
      city: { required },
      state: { required },
      zipcode: { required },
    },
    tooltipform: {
      fname: { required },
      lname: { required },
      username: { required },
      city: { required },
      state: { required },
      zipcode: { required },
    },
  },
  methods: {
    formSubmit(e) {
      this.submitted = true
      // stop here if form is invalid
      this.$v.$touch()
    },

    tooltipForm() {
      this.submitform = true
      this.$v.$touch()
    },
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
            <h4 class="header-title">Custom styles</h4>
            <p class="text-muted font-14">
              Custom feedback styles apply custom colors, borders,
              focus styles, and background
              icons to better communicate feedback.
            </p>
            <form class="needs-validation" @submit.prevent="formSubmit">
              <div class="form-group mb-3">
                <label for="validationCustom01">First name</label>
                <input
                  id="validationCustom01"
                  v-model="form.fname"
                  type="text"
                  class="form-control"
                  placeholder="First name"
                  value="Mark"
                  :class="{ 'is-invalid': submitted && $v.form.fname.$error }"
                />
                <div v-if="submitted && $v.form.fname.$error" class="invalid-feedback">
                  <span v-if="!$v.form.fname.required">Please provide a first name.</span>
                </div>
              </div>

              <div class="form-group mb-3">
                <label for="validationCustom02">Last name</label>
                <input
                  id="validationCustom02"
                  v-model="form.lname"
                  type="text"
                  class="form-control"
                  placeholder="Last name"
                  value="Otto"
                  :class="{ 'is-invalid': submitted && $v.form.lname.$error }"
                />
                <div v-if="submitted && $v.form.lname.$error" class="invalid-feedback">
                  <span v-if="!$v.form.lname.required">Please provide a last name.</span>
                </div>
              </div>

              <div class="form-group mb-3">
                <label for="inline-form-input-username">Username</label>
                <b-input-group prepend="@" class="mb-2 mr-sm-2 mb-sm-0">
                  <b-input
                    id="inline-form-input-username"
                    v-model="form.username"
                    placeholder="Username"
                    :class="{ 'is-invalid': submitted && $v.form.username.$error }"
                  ></b-input>
                  <div v-if="submitted && $v.form.username.$error" class="invalid-feedback">
                    <span v-if="!$v.form.username.required">Please choose a username.</span>
                  </div>
                </b-input-group>
              </div>

              <div class="form-group mb-3">
                <label for="validationCustom03">City</label>
                <input
                  id="validationCustom03"
                  v-model="form.city"
                  type="text"
                  class="form-control"
                  placeholder="City"
                  :class="{ 'is-invalid': submitted && $v.form.city.$error }"
                />
                <div v-if="submitted && $v.form.city.$error" class="invalid-feedback">
                  <span v-if="!$v.form.city.required">Please provide a valid city.</span>
                </div>
              </div>

              <div class="form-group mb-3">
                <label for="validationCustom04">State</label>
                <input
                  id="validationCustom04"
                  v-model="form.state"
                  type="text"
                  class="form-control"
                  placeholder="State"
                  :class="{ 'is-invalid': submitted && $v.form.state.$error }"
                />
                <div v-if="submitted && $v.form.state.$error" class="invalid-feedback">
                  <span v-if="!$v.form.state.required">Please provide a valid state.</span>
                </div>
              </div>

              <div class="form-group mb-3">
                <label for="validationCustom05">Zip</label>
                <input
                  id="validationCustom05"
                  v-model="form.zipcode"
                  type="text"
                  class="form-control"
                  placeholder="Zip"
                  :class="{ 'is-invalid': submitted && $v.form.zipcode.$error }"
                />
                <div v-if="submitted && $v.form.zipcode.$error" class="invalid-feedback">
                  <span v-if="!$v.form.zipcode.required">Please provide a valid zip.</span>
                </div>
              </div>

              <div class="form-group mb-3">
                <div class="custom-control custom-checkbox">
                  <input id="invalidCheck" type="checkbox" class="custom-control-input" />
                  <label
                    class="custom-control-label"
                    for="invalidCheck"
                  >Agree to terms and conditions</label>
                  <div class="invalid-feedback">You must agree before submitting.</div>
                </div>
              </div>

              <b-button variant="primary" type="submit">Submit form</b-button>
            </form>
          </div>
          <!-- end card-body -->
        </div>
        <!-- end card -->
      </div>
      <!-- end col -->

      <div class="col-lg-6">
        <div class="card">
          <div class="card-body">
            <h4 class="header-title">Tooltips</h4>
            <p class="text-muted font-14">
              If your form layout allows it, you can swap the
              <code>.{valid|invalid}-feedback</code> classes for
              <code>.{valid|invalid}-tooltip</code> classes to display validation feedback in
              a styled tooltip. Be sure to have a parent with
              <code>position: relative</code>
              on it for tooltip positioning. In the example below, our column classes have
              this already, but your project may require an alternative setup.
            </p>
            <form class="needs-validation" @submit.prevent="tooltipForm">
              <div class="form-group position-relative mb-3">
                <label for="validationTooltip01">First name</label>
                <input
                  id="validationTooltip01"
                  v-model="tooltipform.fname"
                  type="text"
                  class="form-control"
                  placeholder="First name"
                  value="Mark"
                  :class="{ 'is-invalid': submitform && $v.tooltipform.fname.$error }"
                />
                <div v-if="submitform && $v.tooltipform.fname.$error" class="invalid-tooltip">
                  <span v-if="!$v.tooltipform.fname.required">Please provide valid First name.</span>
                </div>
              </div>

              <div class="form-group position-relative mb-3">
                <label for="validationTooltip02">Last name</label>
                <input
                  id="validationTooltip02"
                  v-model="tooltipform.lname"
                  type="text"
                  class="form-control"
                  placeholder="Last name"
                  value="Otto"
                  :class="{ 'is-invalid': submitform && $v.tooltipform.lname.$error }"
                />
                <div v-if="submitform && $v.tooltipform.lname.$error" class="invalid-tooltip">
                  <span v-if="!$v.tooltipform.lname.required">Please provide valid Last name.</span>
                </div>
              </div>

              <div class="form-group position-relative mb-3">
                <label for="validationTooltipUsername">Username</label>
                <div class="input-group">
                  <div class="input-group-prepend">
                    <span id="validationTooltipUsernamePrepend" class="input-group-text">@</span>
                  </div>
                  <input
                    id="validationTooltipUsername"
                    v-model="tooltipform.username"
                    type="text"
                    class="form-control"
                    placeholder="Username"
                    aria-describedby="validationTooltipUsernamePrepend"
                    :class="{ 'is-invalid': submitform && $v.tooltipform.username.$error }"
                  />
                  <div v-if="submitform && $v.tooltipform.username.$error" class="invalid-tooltip">
                    <span
                      v-if="!$v.tooltipform.username.required"
                    >Please choose a unique and valid username.</span>
                  </div>
                </div>
              </div>

              <div class="form-group position-relative mb-3">
                <label for="validationTooltip03">City</label>
                <input
                  id="validationTooltip03"
                  v-model="tooltipform.city"
                  type="text"
                  class="form-control"
                  placeholder="City"
                  :class="{ 'is-invalid': submitform && $v.tooltipform.city.$error }"
                />
                <div v-if="submitform && $v.tooltipform.city.$error" class="invalid-tooltip">
                  <span v-if="!$v.tooltipform.city.required">Please provide a valid city.</span>
                </div>
              </div>
              <div class="form-group position-relative mb-3">
                <label for="validationTooltip04">State</label>
                <input
                  id="validationTooltip04"
                  v-model="tooltipform.state"
                  type="text"
                  class="form-control"
                  placeholder="State"
                  :class="{ 'is-invalid': submitform && $v.tooltipform.state.$error }"
                />
                <div v-if="submitform && $v.tooltipform.state.$error" class="invalid-tooltip">
                  <span v-if="!$v.tooltipform.state.required">Please provide a valid state.</span>
                </div>
              </div>
              <div class="form-group position-relative mb-3">
                <label for="validationTooltip05">Zip</label>
                <input
                  id="validationTooltip05"
                  v-model="tooltipform.zipcode"
                  type="text"
                  class="form-control"
                  placeholder="zipcode"
                  :class="{ 'is-invalid': submitform && $v.tooltipform.zipcode.$error }"
                />
                <div v-if="submitform && $v.tooltipform.zipcode.$error" class="invalid-tooltip">
                  <span v-if="!$v.tooltipform.zipcode.required">Please provide a valid zip.</span>
                </div>
              </div>
              <b-button variant="primary" type="submit">Submit form</b-button>
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