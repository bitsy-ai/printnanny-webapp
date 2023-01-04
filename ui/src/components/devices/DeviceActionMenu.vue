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
          <MenuItem v-for="action in actions[0]" :key="action.name" as="div"  v-slot="{ active }">
            <!-- href link action -->
            <a
              :href="action.href"
              v-if="action.href !== undefined"
              target="_blank"
              class="text-gray-700 group flex items-center px-4 py-2 text-sm"
            >
              <component
                :is="action.icon"
                class="mr-3 h-5 w-5 text-gray-400 group-hover:text-gray-500"
                aria-hidden="true"
              />
              {{ action.name }}
            </a>

            <!-- router link action -->
            <router-link
              :to="action.routerLink"
              v-else-if="action.routerLink !== undefined"

              class="text-gray-700 group flex items-center px-4 py-2 text-sm"
            >
              <component
                :is="action.icon"
                class="mr-3 h-5 w-5 text-gray-400 group-hover:text-gray-500"
                aria-hidden="true"
              />
              {{ action.name }}
            </router-link>

            <!-- custom menu item content-->
          </MenuItem>
        </div>
        <div class="py-1">

          <MenuItem v-if="!pi.favorite" v-slot="{ active }">
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
    <MenuItem v-if="pi.favorite" v-slot="{ active }">
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
          <MenuItem v-for="action in actions[1]" :key="action.name" as="div"  v-slot="{ active }">
            <!-- href link action -->
            <a
              :href="action.href"
              v-if="action.href !== undefined"
              target="_blank"
              class="text-gray-700 group flex items-center px-4 py-2 text-sm"
            >
              <component
                :is="action.icon"
                class="mr-3 h-5 w-5 text-gray-400 group-hover:text-gray-500"
                aria-hidden="true"
              />
              {{ action.name }}
            </a>

            <!-- router link action -->
            <router-link
              :to="action.routerLink"
              v-else-if="action.routerLink !== undefined"

              class="text-gray-700 group flex items-center px-4 py-2 text-sm"
            >
              <component
                :is="action.icon"
                class="mr-3 h-5 w-5 text-gray-400 group-hover:text-gray-500"
                aria-hidden="true"
              />
              {{ action.name }}
            </router-link>

            <!-- custom menu item content-->
          </MenuItem>
        </div>
      </MenuItems>
    </transition>
  </Menu>
</template>

<script setup lang="ts">
import type { PropType } from "vue";
import type { Pi, PatchedPiRequest } from "printnanny-api-client";

import { Menu, MenuButton, MenuItem, MenuItems } from "@headlessui/vue";
import {
  ChevronDownIcon,
  HeartIcon,
  TrashIcon,
  ExternalLinkIcon,
} from "@heroicons/vue/solid";
import { ExclamationIcon } from "@heroicons/vue/outline";
import { useDeviceStore, buildDeviceActions} from "@/stores/devices";
import type { TableActionLink} from "@/types";

const deviceStore = useDeviceStore();


const props = defineProps({
  pi: {
    type: Object as PropType<Pi>,
    required: true,
  },
  index: {
    type: Number,
    required: true
  }
});
async function addFavorite() {
  await deviceStore.partialUpdate(props.pi.id, props.index, {
    favorite: true,
  } as PatchedPiRequest);
}

async function removeFavorite() {
  await deviceStore.partialUpdate(props.pi.id, props.index, {
    favorite: false,
  } as PatchedPiRequest);
}

const actions = buildDeviceActions(props.pi, props.index);


</script>
