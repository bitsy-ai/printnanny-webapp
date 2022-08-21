<script setup lang="ts">
import  WizardButtons  from "@/components/wizard/steps/WizardButtons.vue"
import { PiCreateWizardSteps } from "../piCreateWizard"

const step = PiCreateWizardSteps()[0]
</script>
<template>
  <div
    class="min-h-full flex items-center justify-center py-12 px-4 sm:px-6 lg:px-8 bg-indigo-20 flex-wrap"
  >
    <!-- main component -->
    <div
      class="min-h-full flex items-center justify-center py-12 px-4 sm:px-6 lg:px-8 bg-indigo-20 flex-wrap text-left"
    >
      <h2 class="text-2xl font-bold leading-7 text-gray-900 sm:text-3xl w-full">
        Customize SD Card
      </h2>
      <p class="text-base font-medium text-gray-900 mt-5 w-full text-left">
        To prepare your SD card, follow the steps in:
        <br />
        <a
          class="focus:ring-indigo-500 h-4 w-4 text-indigo-600 border-gray-300"
          href="https://docs.printnanny.ai/docs/quick-start/create-printnanny-os-image/"
        >
          docs.printnanny.ai/docs/quick-start/create-printnanny-os-image/</a
        >
      </p>
      <p class="text-base font-medium text-gray-900 mt-5 w-full text-left">
        When the Raspberry Pi Imager finishes, continue to the next step.
        <br />
        <span class="text-red-500">Do not eject your SD card yet! </span>
      </p>
    </div>
    <!-- footer buttons -->
    <div class="w-full m-auto justify-center flex-1">
      <WizardButtons :currentStep="step"/>
    </div>
</div>
</template>
