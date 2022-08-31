<script setup lang="ts">
const props = defineProps({
  color: {
    type: String,
    default: "indigo",
  },
  text: {
    type: String,
    default: "",
  },
  width: {
    type: String,
    default: "w-4",
  },
  height: {
    type: String,
    default: "h-4",
  },
});

const color = `fill-${props.color}-600`;

const classes = `${color} ${props.width} ${props.height}`;
</script>

<template>
  <div role="status" class="inline-flex items-center">
    <svg
      class="animate-spin text-white"
      :class="classes"
      xmlns="http://www.w3.org/2000/svg"
      fill="none"
      viewBox="0 0 24 24"
    >
      <circle
        class="opacity-25"
        cx="12"
        cy="12"
        r="10"
        stroke="currentColor"
        stroke-width="4"
      ></circle>
      <path
        class="opacity-75"
        fill="currentColor"
        d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"
      ></path>
    </svg>
    {{ props.text }}
  </div>
</template>
