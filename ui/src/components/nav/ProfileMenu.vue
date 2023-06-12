<!-- profile menu in top-left dashboard corner -->
<template>
  <!-- User account dropdown -->
  <Menu as="div" class="px-3 relative inline-block text-left">
    <div class="flex">
      <MenuButton
        class="group w-full bg-gray-100 rounded-md px-3.5 py-2 text-sm text-left font-medium text-gray-700 hover:bg-gray-200 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-offset-gray-100 focus:ring-purple-500"
      >
        <span class="flex w-full justify-between items-center">
          <span class="flex min-w-0 items-center justify-between space-x-3">
            <div v-if="workspaces.selectedWorkspace?.icon"></div>
            <div
              v-else-if="workspaces.selectedWorkspace?.name"
              class="px-3.5 py-2 text-lg text-left font-medium bg-gray-300 rounded-md text-gray-900"
            >
              <span>{{
                workspaces.selectedWorkspace?.name.charAt(0).toUpperCase()
              }}</span>
            </div>
            <span class="flex-1 flex flex-col min-w-0">
              <span class="text-gray-500 text-sm truncate">{{
                workspaces.selectedWorkspace?.name
              }}</span>
            </span>
          </span>
          <ChevronUpDownIcon
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
        class="z-55 w-[20rem] mx-3 origin-top absolute right-0 left-0 mt-1 rounded-md shadow-lg bg-white ring-1 ring-black ring-opacity-5 divide-y divide-gray-200 focus:outline-none"
      >
        <!-- menuItems Array -->
        <div class="py-1">
          <span class="px-4 py-2 text-xs flex text-gray-500 font-medium"
            >Logged in as: {{ account.user?.email }}</span
          >
          <MenuItem v-for="item in workspaces.workspaces" :key="item.name">
            <button
              :class="[
                workspaces.selectedWorkspace?.id == item.id
                  ? 'bg-gray-100 text-gray-900'
                  : 'text-gray-700',
                'block px-4 py-2 text-sm flex w-full',
              ]"
              :alt="item.name"
              @click="selectWorkspace(item)"
            >
              <span class="flex min-w-0 items-center justify-between space-x-3">
                <div v-if="item.icon"></div>
                <div
                  v-else
                  class="px-3.5 py-2 text-lg text-left font-medium bg-gray-300 rounded-md text-gray-900"
                >
                  <span>{{ item.name.charAt(0).toUpperCase() }}</span>
                </div>
                <span class="flex-1 flex flex-col min-w-0">
                  <span class="text-gray-500 text-sm truncate">{{
                    item.name
                  }}</span>
                </span>
              </span>
            </button>
          </MenuItem>
        </div>
        <!-- linkItems Array -->
        <div class="py-1">
          <MenuItem
            v-for="item in linkItems"
            v-slot="{ active }"
            :key="item.name"
          >
            <router-link
              :to="item.to"
              :class="[
                active ? 'bg-gray-100 text-gray-900' : 'text-gray-700',
                'block px-4 py-2 text-sm w-full',
              ]"
              >{{ item.name }}</router-link
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
                  'block px-4 py-2 text-sm w-full',
                ]"
                >Log out</a
              >
            </router-link>
          </MenuItem>
        </div>
      </MenuItems>
    </transition>
  </Menu>
</template>
<script setup lang="ts">
import { onMounted } from "vue";
import { RouterLink, useRouter } from "vue-router";
import { Menu, MenuButton, MenuItem, MenuItems } from "@headlessui/vue";
import { ChevronUpDownIcon } from "@heroicons/vue/20/solid";
import { CreditCardIcon, BellIcon } from "@heroicons/vue/24/solid";
import { useWorkspaceStore } from "@/stores/workspaces";
import { useAccountStore } from "@/stores/account";
import { useDeviceStore } from "@/stores/devices";
import type * as api from "printnanny-api-client";

const workspaces = useWorkspaceStore();
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

async function selectWorkspace(workspace: api.Workspace) {
  const devices = useDeviceStore();
  workspaces.$patch({ selectedWorkspace: workspace });
  await devices.fetchDevices();
}

// external links or hrefs
const linkItems = [
  {
    name: "Create a Workspace",
    to: { name: "workspaceCreate" },
  },
  {
    name: "Manage Workspaces & Teams",
    to: { name: "workspaceList" },
  },
];

onMounted(async () => {
  await workspaces.fetchWorkspaces();
});
</script>
