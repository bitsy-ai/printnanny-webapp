<script>
import { mapMutations, mapState } from 'vuex'
import useVuelidate from '@vuelidate/core'
import { required } from '@vuelidate/validators'
import {
  SET_DEVICE_SCAN_RESULT,
  DEVICE_SCAN_RESULT,
  WIZARD_MODULE
} from '@/store/wizard'

export default {
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
    },
    ...mapState(WIZARD_MODULE, {
      scanResult: DEVICE_SCAN_RESULT
    })
  },
  methods: {
    ...mapMutations(WIZARD_MODULE, {
      setScanResult: SET_DEVICE_SCAN_RESULT
    }),
    retry () {
      const seconds = this.retryDelay / 1000
      if (this.loading === true) {
        this.messages.push(`Connection timed out after ${seconds} seconds`)
        const retry = seconds * 2
        this.retryDelay = retry * 1000
        this.messages.push(`Retrying in ${retry} seconds`)
        this.connectTimeout = setTimeout(
          function (scope) {
            scope.maxRetry -= 1
            scope.connect()
          },
          this.retryDelay,
          this
        )
      }
    },
    connect () {
      this.messages.push(`Looking for ${this.form.hostname}...`)
      const url = `http://${this.form.hostname}:${this.port}`
      const request = new Request(`http://${this.form.hostname}:${this.port}`, {
        mode: 'no-cors'
      })
      this.setScanResult({
        loading: true,
        hostname: this.form.hostname
      })
      fetch(request)
        .then((response) => response.blob())
        .then((blob) => {
          this.loading = false
          const successMsg = `Found ${this.form.hostname} on your network ✅`
          const redirectMsg = `Click the "Link" button to connect ${this.form.hostname} to your account`
          this.messages.push(successMsg)
          this.messages.push(redirectMsg)
          this.setScanResult({
            loading: false,
            success: true,
            hostname: this.form.hostname,
            url: url
          })
        })
      this.retryTimeout = setTimeout(
        function (scope) {
          scope.maxRetry -= 1
          if (scope.maxRetry >= 0) {
            scope.retry()
          }
        },
        this.retryDelay,
        this
      )
    },
    submit () {
      this.v$.$touch()
      if (this.v$.$error) return
      this.loading = true
      this.connect()
    }
  }
}
</script>

<template>
  <div class="row">
    <div class="col-6 offset-3">
      <h2 class="mb-2">Enter Raspberry Pi's Hostname</h2>
      <p>
        Print Nanny can discover new devices on your network.Click
        <strong>Scan</strong> to search.
      </p>
      <b-form id="network-scanner" @submit.prevent="submit">
        <b-row>
          <b-col sm="8">
            <b-form-input
              v-model="form.hostname"
              placeholder="printnanny.local"
            >
            </b-form-input>
            <div :class="{ error: v$.$errors.length }">
              <div
                class="input-errors text-danger"
                v-for="error of v$.$errors"
                :key="error.$uid"
              >
                <div class="error-msg">{{ error.$message }}</div>
              </div>
            </div>
          </b-col>
          <b-col sm="4">
            <button class="btn btn-secondary" type="submit">
              <span v-if="loading">
                <span
                  class="spinner-border spinner-border-sm"
                  role="status"
                  aria-hidden="true"
                ></span>
                Scanning
              </span>
              <span v-if="loading == false"
                ><i class="mdi mdi-wifi"></i> Scan</span
              >
            </button>
          </b-col>
        </b-row>
      </b-form>
    </div>
    <div class="col-6 offset-3">
      <pre class="text-left">
<br>
<code v-text="logs">

</code>
</pre>
    </div>
  </div>
</template>
