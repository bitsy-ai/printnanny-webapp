<template>
  <div v-if="shouldShow">
    <slot />
  </div>
</template>

<script setup lang="ts">
import { computed, inject } from "vue";
const currentIdx = inject("STEP_COUNTER").value++;
// Grabs the live ref to the current form active step
const formStepIdx = inject("CURRENT_STEP_INDEX");

// If this step should be shown
const shouldShow = computed(() => {
  return currentIdx === formStepIdx.value;
});
</script>
