<script setup lang="ts">
import { ExternalLinkIcon } from "@heroicons/vue/solid";
</script>

<template>
  <div
    class="min-h-full flex items-center justify-center py-12 px-4 sm:px-6 lg:px-8 bg-indigo-20 flex-wrap"
  >
    <h2 class="text-2xl font-bold leading-7 text-gray-900 sm:text-3xl">
      Burn PrintNanny OS Image
    </h2>
    <p class="text-base font-medium text-gray-900 mt-5">
      To prepare your SD card, follow the steps in
      <a
        class="focus:ring-indigo-500 h-4 w-4 text-indigo-600 border-gray-300"
        href="https://docs.printnanny.ai/docs/quick-start/create-printnanny-os-image/"
      >
        Create PrintNanny OS Image</a
      >
    </p>
    <p class="text-base font-medium text-gray-900 mt-5">
      Click or tap the "Next" button when the Raspberry Pi imager is finished.
    </p>
  </div>
</template>
