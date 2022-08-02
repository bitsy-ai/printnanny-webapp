<template>
  <div v-if="shouldShow">
    <slot />
  </div>
</template>

<script setup lang="ts">
import { computed } from "vue";

const props = defineProps({
  name: String,
  activeStep: String,
});

// If this step should be shown
const shouldShow = computed(() => {
  return props.name === props.activeStep;
});
</script>
