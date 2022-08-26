<template>
  <span>
    <!-- fix a problem with billing info -->
    <a
      v-if="!billingStore.summary?.subscription?.is_valid"
      :href="billingStore.summary?.billing_portal_url"
      target="_blank"
    >
      <button
        class="inline-flex items-center px-4 py-2 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-red-600 hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500 sm:order-1 sm:ml-3"
      >
        <ExclamationIcon
          class="text-white-400 group-hover:text-gray-500 mr-3 flex-shrink-0 h-6 w-6"
          aria-hidden="true"
        />
        Update Billing Info
      </button>
    </a>
    <!-- show billing portal url -->
    <a
      v-else
      :href="billingStore.summary?.billing_portal_url"
      target="_blank"
    >
      <button
        class="inline-flex items-center px-4 py-2 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 sm:order-1 sm:ml-3"
      >
        Manage Subscription
      </button>
    </a>
  </span>
</template>
<script setup lang="ts">
import { useBillingStore } from "@/stores/billing";
import { ExclamationIcon } from "@heroicons/vue/outline";
const billingStore = useBillingStore();
</script>
