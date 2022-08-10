<script setup lang="ts">
import { RouterLink } from "vue-router";
import { PlusIcon, PrinterIcon } from "@heroicons/vue/solid";
import { stepKeys } from "@/components/wizard/piCreateWizard";
</script>
<template>
  <div class="text-center mx-auto p-6">
    <PrinterIcon class="mx-auto h-12 w-12 text-gray-400" aria-hidden="true" />

    <h3 class="mt-2 text-sm font-medium text-gray-900">No Connections Found</h3>
    <p class="mt-1 text-sm text-gray-500">
      Get started by installing PrintNanny OS.
    </p>
    <div class="mt-6">
      <router-link
        :to="{ name: 'pi-wizard', params: { activeStep: stepKeys[0].key } }"
      >
        <button
          type="button"
          class="inline-flex items-center px-4 py-2 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
        >
          <PlusIcon class="-ml-1 mr-2 h-5 w-5" aria-hidden="true" />
          New Raspberry Pi Connection
        </button>
      </router-link>
    </div>
  </div>
</template>
