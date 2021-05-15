<script>
import Layout from '@layouts/default'
import { authMethods } from '@state/helpers'
import appConfig from '@src/app.config'

export default {
  page: {
    title: 'Forget Password',
    meta: [
      { name: 'description', content: `Forget Password to ${appConfig.title}` },
    ],
  },
  components: { Layout },
  data() {
    return {
      email: '',
      error: null,
      tryingToReset: false,
      isResetError: false,
      isSuccess: false,
      successMessage: null,
    }
  },
  computed: {},
  methods: {
    ...authMethods,
    // Try to register the user in with the email, fullname
    // and password they provided.
    tryToReset() {
      this.tryingToReset = true
      // Reset the authError if it existed.
      this.error = null
      return this.resetPassword({
        email: this.email,
      })
        .then((data) => {
          this.tryingToReset = false
          this.isResetError = false
          this.isSuccess = true
          this.successMessage = data.message
        })
        .catch((error) => {
          this.tryingToReset = false
          this.error = error ? error.response.data.message : ''
          this.isResetError = true
          this.isSuccess = false
        })
    },
  },
}
</script>

<template>
  <Layout>
    <div class="row justify-content-center">
      <div class="col-lg-5">
        <div class="card">
          <div class="card-header pt-4 pb-4 text-center bg-primary">
            <a href="index.html">
              <span>
                <img src="@assets/images/logo.png" alt height="18" />
              </span>
            </a>
          </div>
          <div class="card-body p-4">
            <div class="text-center w-75 m-auto">
              <h4 class="text-dark-50 text-center mt-0 font-weight-bold">Reset Password</h4>
              <p
                class="text-muted mb-4"
              >Enter your email address and we'll send you an email with instructions to reset your password.</p>
            </div>

            <b-alert v-model="isResetError" variant="danger" dismissible>{{error}}</b-alert>

            <b-alert v-model="isSuccess" variant="success" dismissible>{{successMessage}}</b-alert>

            <b-form @submit.prevent="tryToReset">
              <b-form-group id="email-group" label="Email address" label-for="email">
                <b-form-input
                  id="email"
                  v-model="email"
                  type="email"
                  required
                  placeholder="Enter your email"
                ></b-form-input>
              </b-form-group>

              <div class="form-group mb-0 text-center">
                <b-button type="submit" variant="primary">Reset Password</b-button>
              </div>
            </b-form>
          </div>
          <!-- end card-body -->
        </div>
        <!-- end card -->

        <div class="row mt-3">
          <div class="col-12 text-center">
            <p class="text-muted">
              Back to
              <router-link tag="a" to="/login" class="text-muted ml-1">
                <b>Log In</b>
              </router-link>
            </p>
          </div>
          <!-- end col -->
        </div>
        <!-- end row -->
      </div>
      <!-- end col -->
    </div>
    <!-- end row -->
  </Layout>
</template>

<style lang="scss" module></style>
