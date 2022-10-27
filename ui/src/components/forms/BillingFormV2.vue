<template>
  <div class="">
    <p class="text-base font-medium font-grey-600 w-full">
      PrintNanny uses Stripe to manage your subscription and payment info.
    </p>

    <a :href="stripePortalUrl" target="_blank">
      <button
        class="mt-8 w-1/2 bg-indigo-600 border border-transparent rounded-md py-3 px-8 flex items-center justify-center text-base font-medium text-white hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
      >
        <ExternalLinkIcon
          class="h-5 w-5 mr-2 text-base font-medium text-white"
        />
        Manage Subscription with Stripe
      </button>
    </a>

    <p class="text-base font-medium font-grey-600 w-full mt-4">
      Please email support@printnanny.ai if you have any questions about your
      account.
    </p>
  </div>
</template>
<script setup lang="ts">
import { ExternalLinkIcon } from "@heroicons/vue/solid";

const stripePortalUrl = import.meta.env.VITE_STRIPE_CUSTOMER_PORTAL;
</script>
