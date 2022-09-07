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
    <!-- this is a dirty hack to get tailwind to generate css fill-${props.color}-600 -->
    <!-- haven't yet figured out how to work with tailwind + dynamic color props -->
    <span
      class="hidden fill-indigo-600 fill-slate-600 fill-gray-600 fill-zinc-600 fill-stone-600 fill-red-600 fill-orange-600 fill-amber-600 fill-green-600 fill-emerald-600 fill-teal-600 fill-sky-600 fill-blue-600 fill-indigo-600 fill-violet-600 fill-purple-600 fill-pink-600 fill-rose-600"
    ></span>
    <svg
      class="animate-spin-slow text-white"
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
        :stroke="color"
        stroke-width="4"
      ></circle>
      <path
        class="opacity-75"
        :fill="color"
        d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"
      ></path>
    </svg>
    {{ props.text }}
  </div>
</template>
