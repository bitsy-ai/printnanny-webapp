<template>
  <ul
    role="list"
    class="border border-gray-200 rounded-md divide-y divide-gray-200"
  >
    <li
      v-for="charge in billingStore.summary?.charges"
      :key="charge.id"
      class="pl-3 pr-4 py-3 flex items-center justify-between text-sm"
    >
      <div class="w-0 flex-1 flex items-center">
        <PaperClipIcon
          class="flex-shrink-0 h-5 w-5 text-gray-400"
          aria-hidden="true"
        />
        <span class="ml-2 flex-1 w-0 truncate"> {{ charge.description }} </span>
      </div>
      <div class="ml-4 flex-shrink-0">
        <a
          target="_blank"
          :href="charge.receipt_url"
          class="font-medium text-indigo-600 hover:text-indigo-500"
        >
          Download
        </a>
      </div>
    </li>
  </ul>
</template>
<script setup lang="ts">
import { PaperClipIcon } from "@heroicons/vue/solid";
import { useBillingStore } from "@/stores/billing";

const billingStore = useBillingStore();
</script>
