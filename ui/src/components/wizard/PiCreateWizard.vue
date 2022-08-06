<script setup lang="ts">
import FormWizard from "@/components/wizard/FormWizard.vue";
import { useWizardStore } from "@/stores/wizard";

import { PiCreateWizardSteps, stepKeys } from "./piCreateWizard";

const steps = PiCreateWizardSteps();

const props = defineProps({
  piId: {
    type: String,
    required: false,
    default: "",
  },
  activeStep: {
    type: String,
    default: stepKeys[0].key,
  },
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
      <FormWizard :steps="steps" :active-step="activeStep"> </FormWizard>
    </div>
  </div>
</template>
