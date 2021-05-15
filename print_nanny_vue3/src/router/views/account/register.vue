<script>
import Layout from '@layouts/default'
import { authMethods } from '@state/helpers'
import appConfig from '@src/app.config'

/**
 * Register component
 */
export default {
  page: {
    title: 'Register',
    meta: [{ name: 'description', content: `Register to ${appConfig.title}` }],
  },
  components: { Layout },
  data() {
    return {
      fullname: '',
      email: '',
      password: '',
      regError: null,
      tryingToRegister: false,
      isRegisterError: false,
    }
  },
  computed: {},
  methods: {
    ...authMethods,
    // Try to register the user in with the email, fullname
    // and password they provided.
    tryToRegisterIn() {
      this.tryingToRegister = true
      // Reset the regError if it existed.
      this.regError = null
      return this.register({
        fullname: this.fullname,
        email: this.email,
        password: this.password,
      })
        .then((token) => {
          this.tryingToRegister = false
          this.isRegisterError = false
          // Redirect to the originally requested page, or to the confirm-account page
          this.$router.push(
            this.$route.query.redirectFrom || { name: 'confirm-account' }
          )
        })
        .catch((error) => {
          this.tryingToRegister = false
          this.regError = error.response ? error.response.data.message : ''
          this.isRegisterError = true
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
          <!-- Logo-->
          <div class="card-header pt-4 pb-4 text-center bg-primary">
            <router-link to="/">
              <span>
                <img src="@assets/images/logo.png" alt height="18" />
              </span>
            </router-link>
          </div>
          <div class="card-body p-4">
            <div class="text-center w-75 m-auto">
              <h4 class="text-dark-50 text-center mt-0 font-weight-bold">Free Sign Up</h4>
              <p
                class="text-muted mb-4"
              >Don't have an account? Create your account, it takes less than a minute</p>
            </div>

            <b-alert v-model="isRegisterError" variant="danger" dismissible>{{regError}}</b-alert>

            <b-form @submit.prevent="tryToRegisterIn">
              <b-form-group id="fullname-group" label="Full Name" label-for="fullname">
                <b-form-input
                  id="fullname"
                  v-model="fullname"
                  type="text"
                  required
                  placeholder="Enter your name"
                ></b-form-input>
              </b-form-group>

              <b-form-group id="email-group" label="Email address" label-for="email">
                <b-form-input
                  id="email"
                  v-model="email"
                  type="email"
                  required
                  placeholder="Enter your email"
                ></b-form-input>
              </b-form-group>

              <b-form-group id="password-group" label="Password" label-for="password">
                <b-form-input
                  id="password"
                  v-model="password"
                  type="password"
                  required
                  placeholder="Enter your password"
                ></b-form-input>
              </b-form-group>
              <div class="form-group">
                <div class="custom-control custom-checkbox">
                  <input id="checkbox-signup" type="checkbox" class="custom-control-input" />
                  <label class="custom-control-label" for="checkbox-signup">
                    I accept
                    <a href="#" class="text-muted">Terms and Conditions</a>
                  </label>
                </div>
              </div>

              <div class="form-group mb-0 text-center">
                <b-button type="submit" variant="primary">Sign Up</b-button>
              </div>
            </b-form>
          </div>
          <!-- end card-body -->
        </div>
        <!-- end card -->

        <div class="row mt-3">
          <div class="col-12 text-center">
            <p class="text-muted">
              Already have account?
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
