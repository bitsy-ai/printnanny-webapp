<!-- This example requires Tailwind CSS v2.0+ -->
<template>
  <div class="bg-white">
    <div class="mx-auto max-w-3xl px-4 py-16 sm:px-6 sm:py-24 lg:px-8">
      <div class="max-w-xl">
        <h1 class="text-base font-medium text-indigo-600">
          Thank you,
          {{ order?.stripe_checkout_session_data?.customer_details?.name }}!
        </h1>
        <p
          v-if="order?.products[0].is_preorder"
          class="mt-2 text-2xl font-bold tracking-tight md:text-3xl"
        >
          Your pre-order was accepted!
        </p>
        <p
          v-if="order?.products[0].is_shippable"
          class="mt-2 text-base text-gray-500"
        >
          You'll receive a confirmation email when your order is ready to ship.
        </p>
        <div class="grid grid-cols-2">
          <dl class="mt-12 text-sm font-medium">
            <dt class="text-gray-900">Email Address</dt>
            <dd class="mt-2 text-indigo-600">{{ order?.email }}</dd>
          </dl>
          <dl class="mt-12 text-sm font-medium">
            <dt class="text-gray-900">Order Number</dt>
            <dd class="mt-2 text-indigo-600">{{ order?.id }}</dd>
          </dl>
        </div>
        <a
          :href="
            order?.stripe_checkout_session_data?.payment_intent?.charges[0]
              ?.receipt_url
          "
        >
          <button
            class="mt-6 block w-full py-3 px-4 rounded-md shadow bg-gradient-to-r from-indigo-500 to-violet-600 text-white font-medium hover:from-indigo-600 hover:to-violet-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-cyan-400 focus:ring-offset-gray-900"
          >
            Download/Print Receipt
          </button>
        </a>
      </div>

      <order-item-summary :order="order"></order-item-summary>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useShopStore } from "@/stores/shop";
import OrderItemSummary from "@/components/shop/OrderItemSummary.vue";

const shopStore = useShopStore();
const props = defineProps({
  sessionId: {
    type: String,
    required: true,
  },
});

const order = await shopStore.fetchCheckoutSession(props.sessionId);
</script>
