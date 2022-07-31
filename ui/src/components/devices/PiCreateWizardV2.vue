<template>
  <div
    class="min-h-full flex items-center justify-center py-12 px-4 sm:px-6 lg:px-8 bg-indigo-20 flex-wrap"
  >
    <div class="w-full md:w-2/3 m-auto">
      <FormWizard
        :steps="steps"
        :current-step-idx="currentStepIdx"
      >
        <FormStep>
          <div
            class="min-h-full flex items-center justify-center py-12 px-4 sm:px-6 lg:px-8 bg-indigo-20 flex-wrap text-center"
          >
            <h2 class="text-2xl font-bold leading-7 text-gray-900 sm:text-3xl w-full">
              Burn PrintNanny OS Image
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
              class="appearance-none rounded-md relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"
              placeholder="Hostname"
              rules="required"
            />
            <small
              >Please enter the hostname you set in the Raspberry Pi Imager's
              Advanced Options menu (without .local extension)</small
            >
            <img
              class="w-full"
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
            <h2 class="text-2xl font-bold leading-7 text-gray-900 sm:text-3xl flex-1 w-full">
              Download PrintNanny.zip to SD Card
            </h2>
            <p class="text-base font-medium text-red-500 mt-5 w-full">
              Do not share the contents with anyone!
            </p>
            <p class="text-base font-medium text-gray-900 mt-5 w-full">
              PrintNanny.zip contains unique credentials for your Raspberry Pi.
            </p>

            <div class="w-full">
              <button
                :disabled="true"
                v-show="!store.downloadUrl"
                class="group mt-5 relative w-1/2 justify-center py-3 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-amber-600 disabled:opacity-75 cursor-wait"
              >
                <span class="absolute left-0 inset-y-0 flex items-center pl-3">
                  <RefreshIcon
                    v-show=!store.downloadUrl
                    class="animate-spin h-5 w-5 text-white"
                    :aria-hidden="true"
                  />
                </span>
                <span>Preparing download...</span>
              </button>
              <a :href="store.downloadUrl" v-show="store.downloadUrl">
                <button
                  v-show="store.downloadUrl"
                  class="group mt-5 relative w-1/2 justify-center py-3 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-lime-600 hover:bg-lime-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:lime-500 disabled:opacity-75"
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
                      v-model="tosChecked"
                      :unchecked-value="false"
                      required
                      class="focus:ring-indigo-500 h-4 w-4 text-indigo-600 border-gray-300 rounded"
                    />
                  </div>
                  <div class="ml-3 text-sm">
                    <label for="tos" class="font-medium text-gray-700"
                      >Terms of Service & Privacy Policy</label
                    >
                    <p class="text-gray-500">
                      I agree to the
                      <router-link
                        class="focus:ring-indigo-500 h-4 w-4 text-indigo-600 border-gray-300"
                        :to="{name: 'terms'}"
                        >Terms & Conditions</router-link
                      >
                      and acknowledge the
                      <router-link
                        class="focus:ring-indigo-500 h-4 w-4 text-indigo-600 border-gray-300"
                        :to="{name: 'privacy'}"
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
          <FormStep  :idx=3>
          <div
            class="min-h-full flex items-center justify-center py-12 px-4 sm:px-6 lg:px-8 bg-indigo-20 flex-wrap text-center"
          >
            <h2 class="text-2xl font-bold leading-7 text-gray-900 sm:text-3xl flex-1 w-full">
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

<script setup lang="ts">
import { ref, computed } from "vue";
import { Field, ErrorMessage } from "vee-validate";
import * as yup from "yup";
import * as api from "printnanny-api-client";
import { RouterLink } from "vue-router";
import { RefreshIcon } from "@heroicons/vue/solid";
import { FolderDownloadIcon } from "@heroicons/vue/outline"
import FormWizard from "@/components/forms/FormWizard.vue";
import FormStep from "@/components/forms/FormStep.vue";
import { useWizardStore } from "@/stores/wizard";

const store = useWizardStore();

const tosChecked = ref(false);
const zipDownloaded = ref(false);

const props = defineProps({
  piId: {
    type: String,
    required: false,
  },
  activeStep: {
    type: String,
    default: "create-sd-card",
  },
});

async function downloadLicense(){
  if (props.piId !== undefined && props.activeStep === "download-printnanny-zip"){
      await store.downloadLicenseZip(parseInt(props.piId))
  }
}

downloadLicense()

const steps = [
  {
    key: "create-sd-card",
    validationSchema: yup.object(),
    prevButton: undefined,
    nextButton: { text: "Next: Connect New Pi", link: undefined },
    buttonText: ["Hidden", "Next: Connect New Pi"],
    onSubmit: (_formData: any) => {
      console.debug("create-sd-card onSubmit")
    },
  },
  {
    key: "create-new-device",
    validationSchema: yup.object({
      hostname: yup.string().required(),
      edition: yup.string().required(),
      sbc: yup.string().required(),
    }),
    nextButton: { text: "Next: Download PrintNanny.zip", disabled: store.loading },
    prevButton: { text: "Previous: Burn PrintNanny OS Image"},
    onSubmit:  async (formData: any) => {
    console.log("create-new-device onSubmit", formData)
    // WIREGUARD TODO: allow user to specify fqdn
    const { hostname, edition, sbc} = formData
    const req: api.PiRequest = {
      fqdn: `${hostname}.local`,
      favorite: false,
      hostname,
      edition,
      sbc,
    };
    store.createPi(req);
    }
  },
  {
    key: "download-printnanny-zip",
    validationSchema: yup.object({
      tos: yup
        .boolean(),
    }),
    nextButton: { text: "Next: Test Connection", disabled: computed(() => {
      console.log(tosChecked.value)
      return tosChecked.value === false || zipDownloaded.value === false 
  })},
    prevButton: { text: "Previous: Connect New Device"},
    onSubmit: async(_formData: any) => {
      // tosChecked.value = true
    }
  },
  {
    key: "test-connection",
    validationSchema: yup.object(),
    nextButton: { text: "Next: Download PrintNanny.zip"},
    prevButton: { text: "Finish"},
    onSubmit:   async (formData) => {
      // await deviceStore.
    },

  },
];

const currentStepIdx = computed(() => {
    const idx = steps.findIndex(step => step.key === props.activeStep);
    if (idx === -1){ return 0;}
    return idx
})

// break down the validation steps into multiple schemas
const validationSchema = [
  // step 0: burn os image
  yup.object(),
  // step 1: create new device
  yup.object({
    hostname: yup.string().required(),
    edition: yup.string().required(),
    sbc: yup.string().required(),
  }),
  // step 2: download PrintNanny.zip
  yup.object({
    tos: yup
      .boolean()
      .oneOf(
        [true],
        "I agree to the Terms of Service and acknowledge the Privacy Policy"
      ),
  }),
  // step 3: test connection
];

// const buttonText = [
//   ["Hidden", "Next: Connect New Device"],
//   ["Previous: Burn PrintNanny OS Image", "Next: Download PrintNanny.zip"],
//   ["Previous: Connect New Device", "Next: Download PrintNanny.zip"],
//   ["Next: Download PrintNanny.zip", "Finish"],
// ];

// const onNextCallbacks = [
//   async (_idx, _formData) => {},

//   async (_idx, _formData) => {},
// ];

// async function onNext(idx, formData) {
//     console.log(idx, formData)
//   await steps[idx].onNext(idx, formData);
// }

// function onSubmit(formData) {
//   await steps[idx].onSubmit(formData);

//   console.log(JSON.stringify(formData, null, 2));
// }
</script>
