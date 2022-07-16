<script setup lang="ts">
import { useBillingStore } from "@/stores/billing";
const billingStore = useBillingStore();
</script>
<template>
  <div class="bg-white overflow-hidden shadow rounded-lg">
    <div class="px-4 py-5 sm:px-6">
      <p>Cancel your subscription?</p>
      <p>
        Your service will remain active until the next billing cycle on
        {{ billingStore.summary.subscription.current_period_end }}
      </p>
    </div>
    <div class="bg-gray-50 px-4 py-5 sm:p-6">
      <button
        class="order-0 inline-flex items-center px-4 py-2 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-red-600 hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500 sm:order-1 sm:ml-3"
        @click="billingStore.cancel"
      >
        Cancel now
      </button>
      <router-link :to="{ name: 'devices' }">
        <button
          class="order-0 inline-flex items-center px-4 py-2 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-gray-600 hover:bg-gray-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-gray-500 sm:order-1 sm:ml-3"
        >
          Return Home
        </button>
      </router-link>
    </div>
  </div>
</template>
