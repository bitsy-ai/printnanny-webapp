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

// reset Wizard store if this is a new form
if (props.activeStep == stepKeys[0].key) {
  store.$reset();
  console.log("Reset setup Wizard store");
}
</script>

<template>
  <div
    class="min-h-full flex items-center justify-center py-12 px-4 sm:px-6 lg:px-8 bg-indigo-20 flex-wrap"
  >
    <div class="w-full m-auto justify-center flex-1">
      <FormWizard :steps="steps" :active-step="activeStep"> </FormWizard>
    </div>
  </div>
</template>
