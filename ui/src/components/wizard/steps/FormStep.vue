<template>
  <div v-if="shouldShow">
    <slot />
  </div>
</template>

<script setup lang="ts">
import { computed } from "vue";
import { useRouter } from "vue-router";

const router = useRouter();
const props = defineProps({
  name: {
    type: String,
    required: true,
  },
});

// If this step should be shown
const shouldShow = computed(() => {
  console.log(router.currentRoute);
  return props.name === router.currentRoute.value.params.activeStep;
});
</script>
