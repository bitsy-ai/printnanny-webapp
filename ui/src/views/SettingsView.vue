<script setup lang="ts">
import BillingForm from "@/components/forms/BillingForm.vue";

import BillingFormV2 from "@/components/forms/BillingFormV2.vue";
import AlertSettingsForm from "@/components/forms/AlertSettingsForm.vue";
import { RouterLink, useRouter } from "vue-router";

import { CreditCardIcon, BellIcon } from "@heroicons/vue/outline";
const router = useRouter();

const navigation = [
  {
    name: "Email Notifications",
    link: { name: "alertSettings" },
    icon: BellIcon,
    key: "alertSettings",
    component: AlertSettingsForm,
  },
  {
    name: "Subscription & Billing",
    link: { name: "billing" },
    icon: CreditCardIcon,
    key: "billing",
    component: BillingFormV2,
  },
];

function isActiveRoute(key: string) {
  return router.currentRoute.value.name == key;
}
</script>

<template>
  <div class="lg:grid lg:grid-cols-12 lg:gap-x-5 p-6">
    <!-- secondary sidebar navigation -->
    <aside class="py-6 px-2 sm:px-6 lg:py-0 lg:px-0 lg:col-span-3">
      <nav class="space-y-1">
        <router-link
          v-for="item in navigation"
          :key="item.key"
          :to="item.link"
          :class="[
            isActiveRoute(item.key)
              ? 'bg-gray-50 text-indigo-700 hover:text-indigo-700 hover:bg-white'
              : 'text-gray-900 hover:text-gray-900 hover:bg-gray-50',
            'group rounded-md px-3 py-2 flex items-center text-sm font-medium',
          ]"
          :aria-current="isActiveRoute(item.key) ? 'page' : undefined"
        >
          <component
            :is="item.icon"
            :class="[
              isActiveRoute(item.key)
                ? 'text-indigo-500 group-hover:text-indigo-500'
                : 'text-gray-400 group-hover:text-gray-500',
              'flex-shrink-0 -ml-1 mr-3 h-6 w-6',
            ]"
            aria-hidden="true"
          />
          <span class="truncate">
            {{ item.name }}
          </span>
        </router-link>
      </nav>
    </aside>

    <!-- settings section content -->
    <section class="space-y-6 sm:px-6 lg:px-0 lg:col-span-9">
      <main v-for="item in navigation" :key="item.key">
        <component :is="item.component" v-show="isActiveRoute(item.key)" />
      </main>
    </section>
  </div>
</template>
