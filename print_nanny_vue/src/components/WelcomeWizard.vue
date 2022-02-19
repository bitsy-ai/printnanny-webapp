<script>
import { mapActions, mapMutations, mapState } from 'vuex'
import {
  SET_DEVICE_SCAN_RESULT,
  DEVICE_SCAN_RESULT,
  WIZARD_MODULE
} from '@/store/wizard'
import { DEVICE_MODULE, GET_DEVICE } from '@/store/devices'
import NetworkScanner from '@/components/NetworkScanner'
import VideoStream from '@/components/VideoStream'
import { FormWizard, TabContent, WizardButton } from 'vue-form-wizard'
import 'vue-form-wizard/dist/vue-form-wizard.min.css'
// import MqttPingPong from "./MqttPingPong.vue";

export default {
  components: {
    FormWizard,
    TabContent,
    NetworkScanner,
    WizardButton,
    // MqttPingPong,
    VideoStream
  },
  props: {
    deviceId: String,
    hostname: String
  },
  async created () {
    if (this.deviceId) {
      await this.getDevice(this.deviceId)
    }
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
    scanNextDisabled: function () {
      console.log('scanResult updated', this.scanResult)
      return (
        this.scanResult.loading === true || this.scanResult.success !== true
      )
    },
    ...mapState(WIZARD_MODULE, {
      scanResult: DEVICE_SCAN_RESULT
    })
  },
  methods: {
    ...mapActions(DEVICE_MODULE, {
      getDevice: GET_DEVICE
    }),
    ...mapMutations(WIZARD_MODULE, {
      setScanResult: SET_DEVICE_SCAN_RESULT
    }),
    onComplete: function () {
      window.location.href = '/dashboard'
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
    },
    linkUrl: function () {
      const port = 9001
      const url = `${window.location.protocol}//${this.scanResult.hostname}:${port}`
      window.location = url
    }
  }
}
</script>

<template>
  <div>
    <form-wizard
      @on-complete="onComplete"
      @on-loading="setLoading"
      @on-validate="handleValidation"
      :start-index="startIndex"
      shape="circle"
      color="#02a8b5"
      errorColor="#fa5c7c"
      title="Install in 10 Minutes or Less"
      subtitle="If your install takes longer than 10 minutes, email leigh@print-nanny.com to receive one FREE month of Print Nanny"
    >
      <tab-content title="Getting Started" icon="">
        <hr />
        <div class="row justify-content-around">
          <div class="col-4">
            <h2 class="mb-2">What you'll need</h2>
            <ul>
              <li><h4>Raspberry Pi 4</h4></li>
              <li><h4>Raspberry Pi Camera module</h4></li>
              <li><h4>Micro SD card</h4></li>
            </ul>

            <a
              target="_blank"
              class="btn btn-secondary mb-3 mt-3"
              href="https://bitsy-ai.notion.site/Getting-Started-with-Print-Nanny-OS-817bc65297ff44a085120c663dced5f3#41eb338cca0f4b468ca5ffedd2a6a2f1"
              ><i class="mdi mdi-question"></i>Help Me Choose Hardware</a
            >
          </div>
          <div class="col-8">
            <h2 class="mb-2">Raspberry Pi Imager</h2>
            <ul>
              <li>
                <h4>
                  Download latest image
                  <a href="https://print-nanny.com/devices/releases/"
                    >(see comparison of Print Nanny editions)</a
                  >.
                </h4>
                <a target="_blank" class="btn btn-success mb-3 mt-3" href=""
                  >OctoPrint Edition <br
                /></a>
                <a target="_blank" href="">
                  <button disabled class="disabled btn btn-secondary mb-3 mt-3">
                    Mainsail Edition (coming soon)
                  </button>
                </a>
              </li>
              <li>
                <h4>
                  Install
                  <a href="https://www.raspberrypi.com/software/"
                    >Raspberry Pi Imager</a
                  >.
                </h4>
              </li>
              <li>
                <h4>
                  Follow the
                  <a
                    href="https://bitsy-ai.notion.site/Getting-Started-with-Print-Nanny-OS-817bc65297ff44a085120c663dced5f3"
                    >Help Me Customize</a
                  >
                  guide to set WiFi password
                </h4>
              </li>
            </ul>
          </div>
        </div>
      </tab-content>
      <tab-content title="Link Raspberry Pi" icon="">
        <network-scanner> </network-scanner>
      </tab-content>
      <tab-content title="Test Connection" icon="">
        <div class="text-center row">
          <div class="col-12 col-md-6">
            <h2 class="header-title text-center">Live Camera Feed</h2>
            <p>You should see your Raspberry Pi's camera.</p>
            <video-stream
              v-if="deviceId !== undefined"
              :device-id="deviceId"
              :stream-id="123"
              id="video-stream-123"
            />
          </div>
          <div class="col-12 col-md-6">
            <h2 class="header-title text-center">Print Nanny Vision</h2>
            <p>This is a demonstration of what Print Nanny "sees"</p>
            <video-stream
              v-if="deviceId !== undefined"
              :device-id="deviceId"
              :stream-id="124"
              id="video-stream-124"
            />
          </div>
        </div>

        <!-- <mqtt-ping-pong :device-id="deviceId" :hostname="hostname">
        </mqtt-ping-pong> -->
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
            :style="props.fillButtonStyle"
            >Previous
          </wizard-button>
        </div>
        <div class="wizard-footer-right">
          <wizard-button
            v-if="!props.isLastStep && props.activeTabIndex == 1"
            @click.native="linkUrl"
            class="btn btn-lg wizard-footer-right"
            v-bind:disabled="scanNextDisabled"
            :style="props.fillButtonStyle"
          >
            <span v-show="scanResult.loading"></span>Link
            {{ scanResult.hostname }}
          </wizard-button>
          <wizard-button
            v-else-if="!props.isLastStep && props.activeTabIndex !== 1"
            @click.native="props.nextTab()"
            class="btn btn-lg wizard-footer-right"
            :style="props.fillButtonStyle"
            >Next
          </wizard-button>

          <wizard-button
            v-else
            @click.native="onComplete"
            class="btn btn-lg wizard-footer-right finish-button"
            :style="props.fillButtonStyle"
          >
            {{ props.isLastStep ? "Done" : "Next" }}
          </wizard-button>
        </div>
      </template>
    </form-wizard>
  </div>
</template>
