<!--  Current Subscription Info -->
<template>
  <div class="bg-white shadow overflow-hidden sm:rounded-lg">
    <div class="px-4 py-5 sm:px-6">
      <h3 class="text-lg leading-6 font-medium text-gray-900">
        Subscription Info
      </h3>
      <p
        v-if="billingStore.summary?.subscription.is_valid"
        class="mt-1 max-w-2xl text-sm text-gray-500"
      >
        Details about your current PrintNanny subscription.
      </p>
      <p
        v-if="!billingStore.summary?.subscription.is_valid"
        class="mt-1 max-w-2xl text-sm text-red-500"
      >
        Needs Attention
      </p>
    </div>
    <div class="border-t border-gray-200">
      <dl>
        <div
          class="bg-gray-50 px-4 py-5 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6"
        >
          <dt class="text-sm font-medium text-gray-500">Plan</dt>
          <dd class="mt-1 text-sm text-gray-900 sm:mt-0 sm:col-span-2">
            {{ billingStore.summary?.subscription.plan.nickname }}
          </dd>
        </div>
        <div
          class="bg-gray-50 px-4 py-5 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6"
        >
          <dt class="text-sm font-medium text-gray-500">Status</dt>
          <dd class="mt-1 text-sm text-gray-900 sm:mt-0 sm:col-span-2">
            {{ billingStore.summary?.subscription.status }}
            <SubscriptionAction />
          </dd>
        </div>
        <div
          class="bg-gray-50 px-4 py-5 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6"
        >
          <dt class="text-sm font-medium text-gray-500">
            Period Start - Period End
          </dt>
          <dd class="mt-1 text-sm text-gray-900 sm:mt-0 sm:col-span-2">
            {{
              formattedDate(
                billingStore.summary?.subscription.current_period_start
              )
            }}
            -
            {{
              formattedDate(
                billingStore.summary?.subscription.current_period_end
              )
            }}
          </dd>
        </div>
        <div class="bg-white px-4 py-5 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
          <dt class="text-sm font-medium text-gray-500">Subscription ID</dt>
          <dd class="mt-1 text-sm text-gray-900 sm:mt-0 sm:col-span-2">
            {{ billingStore.summary?.subscription.id }}
          </dd>
        </div>
        <div class="bg-white px-4 py-5 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
          <dt class="text-sm font-medium text-gray-500">Amount</dt>
          <dd class="mt-1 text-sm text-gray-900 sm:mt-0 sm:col-span-2">
            {{ billingStore.summary?.subscription.plan.amount }}
            {{ billingStore.summary?.subscription.plan.currency }} per
            {{ billingStore.summary?.subscription.plan.interval }}
          </dd>
        </div>
        <div
          class="bg-gray-50 px-4 py-5 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6"
        >
          <dt class="text-sm font-medium text-gray-500">Payment Method</dt>
          <dd class="mt-1 text-sm text-gray-900 sm:mt-0 sm:col-span-2">
            {{
              billingStore.summary?.subscription.default_payment_method.card
                .brand
            }}
            ending in
            {{
              billingStore.summary?.subscription.default_payment_method.card
                .last4
            }}
          </dd>
        </div>
        <div class="bg-white px-4 py-5 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
          <dt class="text-sm font-medium text-gray-500">Receipts</dt>
          <dd class="mt-1 text-sm text-gray-900 sm:mt-0 sm:col-span-2">
            <SubscriptionCharges />
          </dd>
        </div>
      </dl>
    </div>
  </div>
</template>

<script setup lang="ts">
import moment from "moment";
import { PaperClipIcon } from "@heroicons/vue/solid";
import { ExclamationIcon } from "@heroicons/vue/outline";
import { useBillingStore } from "@/stores/billing";
import SubscriptionCharges from "@/components/billing/SubscriptionCharges.vue";
import SubscriptionAction from "@/components/billing/SubscriptionAction.vue";
const billingStore = useBillingStore();

function formattedDate(date: string) {
  return moment(date).format("YYYY-MM-DD");
}
</script>
