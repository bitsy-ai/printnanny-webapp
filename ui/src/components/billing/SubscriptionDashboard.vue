<template>
<!-- subscription status -->
  <div>
      <SubscriptionInfo v-if="billingStore.summary.subscription" />
  </div>

</template>
<script setup lang="ts">
import SubscriptionInfo from "@/components/billing/SubscriptionInfo.vue";
import { useBillingStore } from "@/stores/billing";
const billingStore = useBillingStore();
</script>