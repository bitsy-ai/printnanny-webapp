<script setup lang="ts">
import { RouterLink, useRouter } from "vue-router";
import { Menu, MenuButton, MenuItem, MenuItems } from "@headlessui/vue";
import { CogIcon, CreditCardIcon, BellIcon } from "@heroicons/vue/24/solid";

const router = useRouter();

// app routes
const menuItems = [
  {
    name: "Settings",
    link: { name: "settings" },
    icon: CogIcon,
    active: router.currentRoute.value.name == "settings",
  },
  {
    name: "Subscription & Billing",
    link: { name: "billing" },
    icon: CreditCardIcon,
  },
  {
    name: "Notification Settings",
    link: { name: "alertSettings" },
    icon: BellIcon,
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
<template>
  <Menu as="div" class="ml-3 relative">
    <div>
      <MenuButton
        class="max-w-xs bg-white flex items-center text-sm rounded-full focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-purple-500"
      >
        <span class="sr-only">Open user menu</span>
        <CogIcon class="h-8 w-8 rounded-full text-gray-500" />
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
        class="origin-top-right absolute right-0 mt-2 w-48 rounded-md shadow-lg bg-white ring-1 ring-black ring-opacity-5 divide-y divide-gray-200 focus:outline-none"
      >
        <div class="py-1">
          <MenuItem
            v-for="item in menuItems"
            v-slot="{ active }"
            :key="item.name"
          >
            <router-link
              :to="item.link"
              :class="[
                active ? 'bg-gray-100 text-gray-900' : 'text-gray-700',
                'block px-4 py-2 text-sm',
              ]"
              >{{ item.name }}</router-link
            >
          </MenuItem>
        </div>
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
            <a
              href="#"
              :class="[
                active ? 'bg-gray-100 text-gray-900' : 'text-gray-700',
                'block px-4 py-2 text-sm',
              ]"
              >Logout</a
            >
          </MenuItem>
        </div>
      </MenuItems>
    </transition>
  </Menu>
</template>
