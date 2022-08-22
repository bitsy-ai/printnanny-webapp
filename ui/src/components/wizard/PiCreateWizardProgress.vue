<template>
  <div class="relative pt-4">
    <div class="flex mb-2 items-center justify-between">
      <div>
        <span
          class="text-xs font-semibold inline-block py-1 px-2 uppercase rounded-full text-indigo-600 bg-indigo-200"
        >
          {{ currentStep.title }}
        </span>
      </div>
      <div class="text-right">
        <span class="text-xs font-semibold inline-block text-indigo-600">
          {{ currentStep.progress }} completed
        </span>
      </div>
    </div>
    <div class="overflow-hidden h-2 mb-4 text-xs flex rounded bg-indigo-200">
      <div
        :style="currentStep.style"
        class="shadow-none flex flex-col text-center whitespace-nowrap text-white justify-center bg-indigo-500"
      ></div>
    </div>
  </div>
</template>
<script setup lang="ts">
import { computed } from "vue";
import { useRouter } from "vue-router";
import { PiCreateWizardSteps } from "./piCreateWizard";

const router = useRouter()
const steps = PiCreateWizardSteps();

const currentStep = computed(() => {
  const idx = steps.findIndex((step) => step.routeName === router.currentRoute.value.name);
  if (idx === -1) {
    return steps[0];
  }
  return steps[idx];
});
</script>
