<script setup lang="ts">
import { Field, ErrorMessage } from "vee-validate";
import { RouterLink } from "vue-router";
import { RefreshIcon } from "@heroicons/vue/solid";
import { FolderDownloadIcon } from "@heroicons/vue/outline";
import FormWizard from "@/components/forms/FormWizard.vue";
import FormStep from "@/components/forms/FormStep.vue";
import { useWizardStore } from "@/stores/wizard";

import { PiCreateWizardSteps } from "./piCreateWizard";

const steps = PiCreateWizardSteps();

const props = defineProps({
  piId: {
    type: String,
    required: false,
    default: undefined,
  },
  activeStep: {
    type: String,
    default: "create-sd-card",
  },
});

const store = useWizardStore();

async function downloadLicense() {
  if (props.piId !== "" && props.activeStep === "download-printnanny-zip") {
    await store.downloadLicenseZip(parseInt(props?.piId));
  }
}
downloadLicense();
</script>

<template>
  <div
    class="min-h-full flex items-center justify-center py-12 px-4 sm:px-6 lg:px-8 bg-indigo-20 flex-wrap"
  >
    <div class="w-full md:w-2/3 m-auto">
      <FormWizard :steps="steps" :active-step="activeStep">
        <FormStep>
          <div
            class="min-h-full flex items-center justify-center py-12 px-4 sm:px-6 lg:px-8 bg-indigo-20 flex-wrap text-center"
          >
            <h2
              class="text-2xl font-bold leading-7 text-gray-900 sm:text-3xl w-full"
            >
              1) Burn PrintNanny OS Image
            </h2>
            <p class="text-base font-medium text-gray-900 mt-5 w-full">
              To prepare your SD card, follow the steps in
              <a
                class="focus:ring-indigo-500 h-4 w-4 text-indigo-600 border-gray-300"
                href="https://docs.printnanny.ai/docs/quick-start/create-printnanny-os-image/"
              >
                docs.printnanny.ai/docs/quick-start/create-printnanny-os-image/</a
              >
            </p>
            <p class="text-base font-medium text-gray-900 mt-5 w-full">
              Click or tap the "Next" button when Raspberry Pi imager is
              finished.
            </p>
          </div>
        </FormStep>
        <FormStep>
          <h2 class="text-2xl font-bold leading-7 text-gray-900 sm:text-3xl">
            Connect New Device
          </h2>

          <!-- hostname fieldset -->
          <fieldset class="mt-6">
            <legend class="text-base font-medium text-gray-900">
              1) What is the hostname of your Raspberry Pi?
            </legend>
            <error-message class="text-red-500" name="hostname"></error-message>
            <Field
              id="hostname"
              name="hostname"
              type="input"
              class="md:w-2/3 appearance-none rounded-md relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"
              placeholder="Hostname"
              rules="required"
            />
            <small
              >Please enter the hostname you set in the Raspberry Pi Imager's
              Advanced Options menu (without .local extension)</small
            >
            <img
              class="w-full md:w-2/3"
              src="@/assets/images/onboarding/raspberry-pi-imager-hostname.png"
              alt="Screenshot of Raspberry Pi Imager showing hostname field highlighted"
            />
          </fieldset>

          <hr class="m-5" />
          <fieldset class="mt-6">
            <legend class="text-base font-medium text-gray-900">
              2) Choose PrintNanny OS Edition
            </legend>
            <p class="text-sm text-gray-500 mt-2">
              <a
                target="_blank"
                href="https://docs.printnanny.ai/docs/quick-start/choose-os-edition/"
                class="focus:ring-indigo-500 h-4 w-4 text-indigo-600 border-gray-300"
              >
                Click to learn more
              </a>
              about each edition.
            </p>
            <div class="mt-4 space-y-4">
              <div class="flex items-center">
                <Field
                  id="edition"
                  name="edition"
                  type="radio"
                  value="octoprint_lite"
                  required
                  class="focus:ring-indigo-500 h-4 w-4 text-indigo-600 border-gray-300"
                />
                <label for="edition" class="ml-3">
                  <span class="block text-sm font-medium text-gray-700"
                    >OctoPrint Lite</span
                  >
                </label>
              </div>
            </div>
          </fieldset>
          <hr class="m-5" />

          <fieldset class="mt-6">
            <legend class="text-base font-medium text-gray-900">
              3) Choose hardware
            </legend>
            <p class="text-sm text-gray-500 mt-2">
              Which Raspberry Pi board are you using?
              <a
                target="_blank"
                href="https://github.com/bitsy-ai/printnanny-os/issues?q=is%3Aissue+is%3Aopen+label%3Araspberrypi3"
                class="focus:ring-indigo-500 h-4 w-4 text-indigo-600 border-gray-300"
              >
                Click see progress towards other boards.
              </a>
            </p>
            <div class="mt-4 space-y-4">
              <div class="flex items-center">
                <Field
                  id="sbc"
                  name="sbc"
                  type="radio"
                  value="rpi_4"
                  required
                  class="focus:ring-indigo-500 h-4 w-4 text-indigo-600 border-gray-300"
                />
                <label for="edition" class="ml-3">
                  <span class="block text-sm font-medium text-gray-700"
                    >Raspberry Pi 4</span
                  >
                </label>
              </div>
            </div>
          </fieldset>
          <hr class="m-5" />
        </FormStep>
        <FormStep>
          <div
            class="min-h-full flex items-center justify-center py-12 px-4 sm:px-6 lg:px-8 bg-indigo-20 flex-wrap text-center"
          >
            <h2
              class="text-2xl font-bold leading-7 text-gray-900 sm:text-3xl flex-1 w-full"
            >
              Download PrintNanny.zip to SD Card
            </h2>
            <a
              v-show="store.downloadUrl"
              :href="store.downloadUrl"
              class="w-full"
            >
              <button
                v-show="store.downloadUrl"
                class="group mt-5 relative w-1/2 justify-center py-3 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-red-600 hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:red-500 disabled:opacity-75"
              >
                <span class="absolute left-0 inset-y-0 flex items-center pl-3">
                  <FolderDownloadIcon
                    class="h-5 w-5 text-white group-hover:text-gray-400"
                    :aria-hidden="true"
                  />
                </span>
                <span>Click here if download does not start automatically</span>
              </button>
            </a>
            <p class="text-base font-medium text-red-500 mt-5 w-full">
              Do not share contents with anyone!
            </p>
            <p class="text-base font-medium text-gray-900 mt-5 w-full">
              PrintNanny.zip contains unique credentials for your Raspberry Pi.
            </p>

            <div class="w-full">
              <button
                v-show="!store.downloadUrl"
                :disabled="true"
                class="group mt-5 relative w-1/2 justify-center py-3 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-amber-600 disabled:opacity-75 cursor-wait"
              >
                <span class="absolute left-0 inset-y-0 flex items-center pl-3">
                  <RefreshIcon
                    v-show="!store.downloadUrl"
                    class="animate-spin h-5 w-5 text-white"
                    :aria-hidden="true"
                  />
                </span>
                <span>Preparing download...</span>
              </button>
            </div>
            <hr class="m-5" />

            <fieldset class="mt-6">
              <div class="mt-4 space-y-4">
                <div class="flex items-start">
                  <div class="h-5 flex items-center">
                    <Field
                      id="tos"
                      name="tos"
                      type="checkbox"
                      :value="false"
                      :unchecked-value="false"
                      required
                      class="focus:ring-indigo-500 h-4 w-4 text-indigo-600 border-gray-300 rounded"
                    />
                  </div>
                  <div class="ml-3 text-sm">
                    <p class="text-gray-500">
                      I agree to the
                      <router-link
                        class="focus:ring-indigo-500 h-4 w-4 text-indigo-600 border-gray-300"
                        :to="{ name: 'terms' }"
                        >Terms & Conditions</router-link
                      >
                      and acknowledge the
                      <router-link
                        class="focus:ring-indigo-500 h-4 w-4 text-indigo-600 border-gray-300"
                        :to="{ name: 'privacy' }"
                        >Privacy Policy</router-link
                      >
                    </p>
                  </div>
                </div>
              </div>
            </fieldset>
            <hr class="m-5" />
          </div>
        </FormStep>
        <FormStep :idx="3">
          <div
            class="min-h-full flex items-center justify-center py-12 px-4 sm:px-6 lg:px-8 bg-indigo-20 flex-wrap text-center"
          >
            <h2
              class="text-2xl font-bold leading-7 text-gray-900 sm:text-3xl flex-1 w-full"
            >
              Test Raspberry Pi Connections
            </h2>
            <p class="text-base font-medium text-red-500 mt-5 w-full">
              Do not share the contents of PrintNanny.zip with anyone!
            </p>
          </div>
        </FormStep>
      </FormWizard>
    </div>
  </div>
</template>
