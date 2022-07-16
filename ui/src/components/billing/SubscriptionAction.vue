<template>
<span>
    <router-link :to="{name: 'billing-cancel'}">
        <button v-if="isActive" class="order-0 inline-flex items-center px-4 py-2 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-red-600 hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500 sm:order-1 sm:ml-3">
            Cancel
        </button>
    </router-link>
    <button v-if="!isActive" class="order-0 inline-flex items-center px-4 py-2 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 sm:order-1 sm:ml-3">
        Reactivate
    </button>
</span>
</template>
<script setup lang="ts">
import * as apiTypes from "printnanny-api-client";
const props = defineProps({
    subscription: apiTypes.StripeSubscription
})

function isActive(){
    return this.subscription.status == active
}
</script>