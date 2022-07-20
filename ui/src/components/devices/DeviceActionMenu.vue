<!-- This example requires Tailwind CSS v2.0+ -->
<template>
  <Menu as="div" class="relative inline-block text-left">
    <div>
      <MenuButton
        class="inline-flex justify-center w-full rounded-md border border-gray-300 shadow-sm px-4 py-2 bg-white text-sm font-medium text-gray-700 hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-offset-gray-100 focus:ring-indigo-500"
      >
        Select action
        <ChevronDownIcon class="-mr-1 ml-2 h-5 w-5" aria-hidden="true" />
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
        class="z-50 origin-top-right absolute right-0 mt-2 w-56 rounded-md shadow-lg bg-white ring-1 ring-black ring-opacity-5 divide-y divide-gray-100 focus:outline-none"
      >
        <div class="py-1">
          <MenuItem
            v-for="link in externalLinks"
            v-slot="{ active }"
            :key="link.name"
          >
            <a
              :href="link.href"
              target="_blank"
              class="text-gray-700 group flex items-center px-4 py-2 text-sm"
            >
              <component
                :is="link.icon"
                class="mr-3 h-5 w-5 text-gray-400 group-hover:text-gray-500"
                aria-hidden="true"
              />
              {{ link.name }}
            </a>
          </MenuItem>
        </div>
        <div class="py-1">
          <MenuItem v-if="!device.favorite" v-slot="{ active }">
            <a
              :class="[
                active ? 'bg-gray-100 text-gray-900' : 'text-gray-700',
                'group flex items-center px-4 py-2 text-sm',
              ]"
              @click="addFavorite"
            >
              <HeartIcon
                class="mr-3 h-5 w-5 text-gray-400 group-hover:text-gray-500"
                aria-hidden="true"
              />
              Add to favorites
            </a>
          </MenuItem>
          <MenuItem v-if="device.favorite" v-slot="{ active }">
            <a
              :class="[
                active ? 'bg-gray-100 text-gray-900' : 'text-gray-700',
                'group flex items-center px-4 py-2 text-sm',
              ]"
              @click="removeFavorite"
            >
              <HeartIcon
                class="mr-3 h-5 w-5 text-gray-400 group-hover:text-gray-500"
                aria-hidden="true"
              />
              Remove from favorites
            </a>
          </MenuItem>
        </div>
        <div class="py-1">
          <MenuItem
            v-for="action in footerActions"
            v-slot="{ active }"
            :key="action.name"
          >
            <router-link
              :to="action.link"
              class="text-gray-700 group flex items-center px-4 py-2 text-sm"
            >
              <component
                :is="action.icon"
                class="mr-3 h-5 w-5 text-gray-400 group-hover:text-gray-500"
                aria-hidden="true"
              />
              {{ action.name }}
            </router-link>
          </MenuItem>
        </div>
      </MenuItems>
    </transition>
  </Menu>
</template>

<script setup lang="ts">
import { Menu, MenuButton, MenuItem, MenuItems } from "@headlessui/vue";
import {
  ArchiveIcon,
  ArrowCircleRightIcon,
  ChevronDownIcon,
  DuplicateIcon,
  HeartIcon,
  PencilAltIcon,
  TrashIcon,
  UserAddIcon,
  ExternalLinkIcon,
} from "@heroicons/vue/solid";
import * as api from "printnanny-api-client";
import { useDeviceStore } from "@/stores/devices";

const props = defineProps({
  device: api.Device,
  index: Number
});
const deviceStore = useDeviceStore();

async function addFavorite() {
  await deviceStore.partialUpdate(props.device.id, props.index, { favorite: true } as api.PatchedDeviceRequest);
}

async function removeFavorite() {
  await deviceStore.partialUpdate(props.device.id, props.index, { favorite: false } as api.PatchedDeviceRequest);
}

const externalLinks = [
  {
    href: props.device.urls.octoprint,
    name: "OctoPrint",
    icon: ExternalLinkIcon,
  },
  {
    href: props.device.urls.swupdate,
    name: "Software Update",
    icon: ExternalLinkIcon,
  },
];

// TODO: pin / add to favorites
const footerActions = [
  {
    name: "Delete",
    link: {
      name: "device-delete",
      params: { id: props.device.id },
      query: { hostname: props.device.hostname }
    },
    icon: TrashIcon,
  },
];
</script>
