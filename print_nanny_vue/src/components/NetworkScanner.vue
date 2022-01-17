<script>
import useVuelidate from '@vuelidate/core'
import { required } from '@vuelidate/validators'

export default {
  props: {
  },
  data: function () {
    return {
      form: { hostname: '' },
      loading: false,
      maxRetry: 5,
      retryDelay: 5000,
      messages: [],
      retryTimeout: null,
      port: 9001
    }
  },
  setup () {
    return { v$: useVuelidate() }
  },
  validations () {
    return {
      form: { hostname: { required } }
    }
  },
  computed: {
    logs: function () {
      return this.messages.join('\n')
    }
  },
  methods: {
    scan () {

    },
    retry () {
      const seconds = this.retryDelay / 1000
      if (this.loading === true) {
        this.messages.push(`Connection timed out after ${seconds} seconds`)
        const retry = (seconds * 2)
        this.retryDelay = retry * 1000
        this.messages.push(`Retrying in ${retry} seconds`)
        this.connectTimeout = setTimeout(function (scope) {
          scope.maxRetry -= 1
          scope.connect()
        }, this.retryDelay, this)
      }
    },
    connect () {
      this.messages.push(`Initializing connection to ${this.form.hostname}...`)
      const url = `http://${this.form.hostname}:${this.port}`
      const request = new Request(`http://${this.form.hostname}:${this.port}`, { mode: 'no-cors' })
      fetch(request)
        .then(response => response.blob())
        .then(blob => {
          this.loading = false
          const successMsg = `Success connecting to ${url} ✅`
          const redirectMsg = 'Redirecting in 4 seconds...'
          this.messages.push(successMsg)
          setTimeout((scope) => {
            const redirectMsg = 'Redirecting in 3 seconds...'
            this.messages.push(redirectMsg)
          }, 1000)
          setTimeout((scope) => {
            const redirectMsg = 'Redirecting in 2 seconds...'
            this.messages.push(redirectMsg)
          }, 2000)
          setTimeout((scope) => {
            const redirectMsg = 'Redirecting in 1 second...'
            this.messages.push(redirectMsg)
          }, 3000)
          setTimeout((scope) => {
            window.location.href = url
          }, 4000)
          this.messages.push(redirectMsg)
        })
      this.retryTimeout = setTimeout(function (scope) {
        scope.maxRetry -= 1
        if (scope.maxRetry >= 0) {
          scope.retry()
        }
      }, this.retryDelay, this)
    },
    submit () {
      console.log(this)
      console.log(this.$v)
      this.v$.$touch()
      console.log(this.v$.$error)
      if (this.v$.$error) return
      this.loading = true
      this.connect()
    }
  }
}
</script>

<template>
  <b-container fluid>
    <b-form id="network-scanner" @submit.prevent="submit">
      <b-row>
        <b-col sm="8">
              <b-form-input v-model="form.hostname" placeholder="printnanny.local">
              </b-form-input>
              <div :class="{ error: v$.$errors.length }">
                <div class="input-errors text-danger" v-for="error of v$.$errors" :key="error.$uid">
                <div class="error-msg">{{ error.$message }}</div>
                </div>
              </div>
        </b-col>
        <b-col sm="4">
        <button class="btn btn-secondary" type="submit" >
          <span v-if="loading">
            <span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>
             Scanning
          </span>
          <span v-if="loading == false"><i class="mdi mdi-wifi"></i> Scan</span>
        </button>
        </b-col>
      </b-row>
    </b-form>
    <b-row>
<pre class="text-left">
<br>
<code v-text="logs">

</code>
</pre>
    </b-row>
  </b-container>

</template>
