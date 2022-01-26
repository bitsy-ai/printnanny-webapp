<script>
import { mapMutations, mapState } from 'vuex'
import { SET_DEVICE_SCAN_RESULT, DEVICE_SCAN_RESULT, WIZARD_MODULE } from '@/store/wizard'
import NetworkScanner from '@/components/NetworkScanner'
// import MqttPingPong from '@/components/MqttPingPong'
import { FormWizard, TabContent, WizardButton } from 'vue-form-wizard'
import 'vue-form-wizard/dist/vue-form-wizard.min.css'

export default {
  components: { FormWizard, TabContent, NetworkScanner, WizardButton },
  props: {
    getttingStartedUrl: String,
    deviceId: Number
  },
  data: function () {
    return {
      loading: false
    }
  },
  computed: {
    startIndex: function startIndex () {
      const url = new URL(window.location.href)
      return parseInt(url.searchParams.get('step')) || 0
    },
    ...mapState(WIZARD_MODULE, {
      scan_result: DEVICE_SCAN_RESULT
    }),
    scanNextDisabled: function () {
      return this.scan_result.loading === true || this.scan_result.success !== true
    }
  },
  methods: {
    ...mapMutations(WIZARD_MODULE, {
      set_scan_result: SET_DEVICE_SCAN_RESULT
    }),
    onComplete: function () {
      alert('Yay. Done!')
    },
    setLoading: function (value) {
      this.loading = value
    },
    handleValidation: function (isValid, tabIndex) {
      console.log('Tab: ' + tabIndex + ' valid: ' + isValid)
    },
    validateAsync: function () {
      return new Promise((resolve, reject) => {
        setTimeout(() => {
          resolve(true)
        }, 1000)
      })
    }
  }
}

</script>

<template>
<div>
    <form-wizard @on-complete="onComplete"
                @on-loading="setLoading"
                @on-validate="handleValidation"
                :start-index="startIndex"
                shape="circle"
                color="#02a8b5"
                errorColor="#fa5c7c"
                title="Install in 10 Minutes or Less"
                subtitle="If your install takes longer than 10 minutes, email leigh@print-nanny.com to receive one FREE month of Print Nanny">
      <tab-content title="Getting Started"
                   icon="">
      <hr>
      <div class="row justify-content-around">
        <div class="col-4">
            <h2 class="mb-2">What you'll need</h2>
            <ul>
              <li><h4>Raspberry Pi 4</h4></li>
              <li><h4>Raspberry Pi Camera module</h4></li>
              <li><h4>Micro SD card</h4></li>
            </ul>

            <a target="_blank" class="btn btn-secondary btn-lg mb-3 mt-3" href="https://bitsy-ai.notion.site/Getting-Started-with-Print-Nanny-OS-817bc65297ff44a085120c663dced5f3#41eb338cca0f4b468ca5ffedd2a6a2f1"><i class="mdi mdi-plus"></i>Help Me Find Hardware</a>
        </div>
        <div class="col-6">
          <h2 class="mb-2">Raspberry Pi Imager</h2>
          <ul>
            <li><h4>Visit the <a href="https://print-nanny.com/devices/releases/">Releases</a> page to download latest version.</h4></li>
            <li><h4>Download <a href="https://www.raspberrypi.com/software/">Raspberry Pi Imager</a>.</h4></li>
            <li><h4>Follow the <a href="https://bitsy-ai.notion.site/Getting-Started-with-Print-Nanny-OS-817bc65297ff44a085120c663dced5f3">Help Me Customize</a> guide to set WiFi password</h4></li>
          </ul>
          <a target="_blank" class="btn btn-secondary btn-lg mb-3 mt-3" href="https://bitsy-ai.notion.site/Getting-Started-with-Print-Nanny-OS-817bc65297ff44a085120c663dced5f3"><i class="mdi mdi-plus"></i>Help Me Customize</a>
        </div>
      </div>
      </tab-content>
      <tab-content
        title="Link Raspberry Pi"
        icon="">
        <network-scanner>
        </network-scanner>
      </tab-content>
      <tab-content title="Test Connection"
                   icon="">
      </tab-content>

      <tab-content title="Finish Setup"
                   icon="">
      Send MQTT ping / pong
      Try live streaming video
      </tab-content>
      <!--
      <tab-content title="Restore OctoPrint"
                   icon="">
      Restore OctoPrint from backup
      </tab-content>
      -->

      <div class="loader" v-if="loading"></div>
      <template slot="footer" slot-scope="props">
       <div class="wizard-footer-left">
           <wizard-button
            v-if="props.activeTabIndex > 0 && !props.isLastStep"
            @click.native="props.prevTab()"
            class="btn btn-lg"
            :style="props.fillButtonStyle">Previous
            </wizard-button>
        </div>
        <div class="wizard-footer-right">
          <wizard-button
            v-if="!props.isLastStep && props.activeTabIndex == 1"
            @click.native="props.nextTab()"
            class="btn btn-lg wizard-footer-right"
            v-bind:disabled="scanNextDisabled"
            :style="props.fillButtonStyle">
            <span v-show="scan_result.loading"></span>Link {{scan_result.hostname}}
          </wizard-button>
          <wizard-button
            v-else-if="!props.isLastStep && props.activeTabIndex !== 1"
            @click.native="props.nextTab()"
            class="btn btn-lg wizard-footer-right"
            :style="props.fillButtonStyle">Next
          </wizard-button>

          <wizard-button
            v-else
            @click.native="onComplete"
            class="btn btn-lg wizard-footer-right finish-button"
            :style="props.fillButtonStyle">  {{props.isLastStep ? 'Done' : 'Next'}}
          </wizard-button>
        </div>
      </template>
    </form-wizard>
 </div>
</template>
