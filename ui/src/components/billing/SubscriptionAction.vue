<template>
<span>
    <!-- cancel active subscription -->
    <router-link :to="{name: 'billing-cancel'}" v-if="billingStore.summary.subscription.is_valid">
        <button class="inline-flex items-center px-4 py-2 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-red-600 hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500 sm:order-1 sm:ml-3">
            Cancel
        </button>
    </router-link>
    <!-- reactivate a subscription that will be cancelled at billing end -->
    <button v-if="billingStore.summary.subscription.is_status_temporarily_current" @click="billingStore.reactivate" class="order-0 inline-flex items-center px-4 py-2 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 sm:order-1 sm:ml-3">
        Reactivate
    </button>
    <!-- fix a problem with billing info -->
    <router-link :to="{name: 'billing-update'}" v-if="!billingStore.summary.subscription.is_valid">
        <button class="inline-flex items-center px-4 py-2 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-red-600 hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500 sm:order-1 sm:ml-3">
            <ExclamationIcon />
            Fix Billing Issue
        </button>
    </router-link>
</span>
</template>
<script setup lang="ts">
import * as apiTypes from "printnanny-api-client";
import { useBillingStore } from "@/stores/billing";
import { ExclamationIcon } from "@heroicons/vue/outline";
const billingStore = useBillingStore();

</script>