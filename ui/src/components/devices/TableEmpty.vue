<script setup lang="ts">
import { RouterLink } from "vue-router";
import { PlusIcon, PrinterIcon } from "@heroicons/vue/24/solid";
defineProps({
  icon: {
    default: PrinterIcon,
  },
  header: {
    default: "No Connections Found",
  },
  body: {
    default: "Get started by installing PrintNanny OS.",
  },
});
</script>
<template>
  <div class="text-center mx-auto p-6">
    <component
      :is="icon"
      class="mx-auto h-12 w-12 text-gray-400"
      aria-hidden="true"
    ></component>
    <h3 class="mt-2 text-sm font-medium text-gray-900">{{ header }}</h3>
    <p class="mt-1 text-sm text-gray-500">
      {{ body }}
    </p>
    <div class="mt-6">
      <slot>
        <a href="https://printnanny.ai/docs/category/quick-start/">
          <button
            type="button"
            class="inline-flex items-center px-4 py-2 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
          >
            <PlusIcon class="-ml-1 mr-2 h-5 w-5" aria-hidden="true" />
            Quick Start
          </button>
        </a>
      </slot>
    </div>
  </div>
</template>
