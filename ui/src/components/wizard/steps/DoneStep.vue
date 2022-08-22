<script setup lang="ts">
import type { PropType } from "vue";
import type { WizardStep } from "@/types";

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
