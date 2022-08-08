<script setup lang="ts">
import type { PropType } from "vue";
import { Field } from "vee-validate";
import { RefreshIcon, FolderDownloadIcon } from "@heroicons/vue/solid";
import { useWizardStore } from "@/stores/wizard";
import type { WizardStep } from "@/types";
import FormStep from "./FormStep.vue";

defineProps({
  step: {
    type: Object as PropType<WizardStep>,
    required: true,
  },
});

const store = useWizardStore();
</script>
<template>
  <FormStep :name="step.key">
    <div
      class="min-h-full flex items-center justify-center py-12 px-4 sm:px-6 lg:px-8 bg-indigo-20 flex-wrap text-center"
    >
      <h2
        class="text-2xl font-bold leading-7 text-gray-900 sm:text-3xl flex-1 w-full"
      >
        Download PrintNanny.zip to SD Card
      </h2>
      <a v-show="store.downloadUrl" :href="store.downloadUrl" class="w-full">
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
</template>
