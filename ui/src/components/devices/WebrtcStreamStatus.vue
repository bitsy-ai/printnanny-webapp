<template>
  <span>
    <RefreshIcon
      v-if="loading"
      class="animate-spin h-5 w-5 text-indigo-500 group-hover:text-indigo-400"
      aria-hidden="true"
    />
  </span>
</template>
<script setup lang="ts">
import { ref } from "vue";

const loading = ref(false);

// const props = defineProps({
//   device: {
//     type: Object as PropType<Device>,
//     required: true,
//   },
//   index: {
//     type: Number,
//     required: true,
//   },
// });
</script>
