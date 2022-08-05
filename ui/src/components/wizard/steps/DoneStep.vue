<script setup lang="ts">
import type { PropType } from "vue";
import type { WizardStep } from "@/types";
import FormStep from "./FormStep.vue";

defineProps({
  step: {
    type: Object as PropType<WizardStep>,
    required: true,
  },
});
</script>
<template>
  <FormStep :name="step.key"> </FormStep>
</template>
