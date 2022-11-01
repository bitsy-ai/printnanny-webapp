<!-- profile menu in top-left dashboard corner -->
<template>
  <!-- User account dropdown -->
  <Menu as="div" class="px-3 relative inline-block text-left">
    <div>
      <MenuButton
        class="group w-full bg-gray-100 rounded-md px-3.5 py-2 text-sm text-left font-medium text-gray-700 hover:bg-gray-200 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-offset-gray-100 focus:ring-purple-500"
      >
        <span class="flex w-full justify-between items-center">
          <span class="flex min-w-0 items-center justify-between space-x-3">
            <span class="flex-1 flex flex-col min-w-0">
              <span class="text-gray-900 text-sm font-medium truncate"
                >👋 Welcome, {{ account.user?.first_name || "Maker" }}</span
              >
              <span class="text-gray-500 text-sm truncate">{{
                account.user?.email
              }}</span>
            </span>
          </span>
          <SelectorIcon
            class="flex-shrink-0 h-5 w-5 text-gray-400 group-hover:text-gray-500"
            aria-hidden="true"
          />
        </span>
      </MenuButton>
    </div>
    <transition
      enter-active-class="transition ease-out duration-100"
      enter-from-class="transform opacity-0 scale-95"
      enter-to-class="transform opacity-100 scale-100"
      leave-active-class="transition ease-in duration-75"
      leave-from-class="transform opacity-100 scale-100"
      leave-to-class="transform opacity-0 scale-95"
    >
      <MenuItems
        class="z-10 mx-3 origin-top absolute right-0 left-0 mt-1 rounded-md shadow-lg bg-white ring-1 ring-black ring-opacity-5 divide-y divide-gray-200 focus:outline-none"
      >
        <!-- menuItems Array -->
        <div class="py-1">
          <MenuItem v-for="item in menuItems" :key="item.name">
            <router-link
              :to="item.link"
              :class="[
                item.active ? 'bg-gray-100 text-gray-900' : 'text-gray-700',
                'block px-4 py-2 text-sm',
              ]"
              >{{ item.name }}</router-link
            >
          </MenuItem>
        </div>
        <!-- linkItems Array -->
        <div class="py-1">
          <MenuItem
            v-for="item in linkItems"
            v-slot="{ active }"
            :key="item.name"
          >
            <a
              :href="item.href"
              :class="[
                active ? 'bg-gray-100 text-gray-900' : 'text-gray-700',
                'block px-4 py-2 text-sm',
              ]"
              >{{ item.name }}</a
            >
          </MenuItem>
        </div>
        <div class="py-1">
          <MenuItem v-slot="{ active }">
            <router-link :to="{ name: 'logout' }" replace>
              <a
                href="#"
                :class="[
                  active ? 'bg-gray-100 text-gray-900' : 'text-gray-700',
                  'block px-4 py-2 text-sm',
                ]"
                >Logout</a
              >
            </router-link>
          </MenuItem>
        </div>
      </MenuItems>
    </transition>
  </Menu>
</template>
<script setup lang="ts">
import { RouterLink, useRouter } from "vue-router";
import { Menu, MenuButton, MenuItem, MenuItems } from "@headlessui/vue";
import { CreditCardIcon, BellIcon, SelectorIcon } from "@heroicons/vue/solid";

import { useAccountStore } from "@/stores/account";
const account = useAccountStore();
const router = useRouter();
// app routes
const menuItems = [
  {
    name: "Subscription & Billing",
    link: { name: "billing" },
    icon: CreditCardIcon,
    active: router.currentRoute.value.name == "billing",
  },
  {
    name: "Notification Settings",
    link: { name: "alertSettings" },
    icon: BellIcon,
    active: router.currentRoute.value.name == "alertSettings",
  },
];

// external links or hrefs
const linkItems = [
  {
    name: "Documentation",
    href: "https://printnanny.ai/docs/category/quick-start/",
  },
  {
    name: "Report Issue",
    href: "https://github.com/bitsy-ai/printnanny-os/issues",
  },
];
</script>
