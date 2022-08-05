<script setup lang="ts">
import FormStep from "./FormStep.vue";
import { PropType } from "vue";
import { useWizardStore } from "@/stores/wizard";
import type { WizardStep } from "@/types";

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
        Test Raspberry Pi Connection
      </h2>
      <p
        v-if="!store.pi?.setup_finished"
        class="text-base font-medium text-grey-500 mt-5 w-full"
      >
        Waiting for Raspberry Pi to boot
      </p>
    </div>
  </FormStep>
</template>
