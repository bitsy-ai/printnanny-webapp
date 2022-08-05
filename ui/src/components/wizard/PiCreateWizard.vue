<script setup lang="ts">
import { Field, ErrorMessage } from "vee-validate";
import { RouterLink } from "vue-router";
import { RefreshIcon } from "@heroicons/vue/solid";
import { FolderDownloadIcon } from "@heroicons/vue/outline";
import FormWizard from "@/components/forms/FormWizard.vue";
import { useWizardStore } from "@/stores/wizard";

import { PiCreateWizardSteps } from "./piCreateWizard";

const steps = PiCreateWizardSteps();

const props = defineProps({
  piId: {
    type: String,
    required: false,
    default: "",
  },
  activeStep: String
});

const store = useWizardStore();

async function downloadLicense() {
  if (props.piId !== "" && props.activeStep === "download-printnanny-zip") {
    await store.downloadLicenseZip(parseInt(props.piId));
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
        <component v-for="step in steps" :key="step.key" :name="step.key" :is="step.component" />        
      </FormWizard>
    </div>
  </div>
</template>
