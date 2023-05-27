<!-- This example requires Tailwind CSS v2.0+ -->
<template>
  <div>
    <Menu as="div" class="relative inline-block text-left">
      <div>
        <MenuButton
          class="inline-flex justify-center w-full rounded-md border border-gray-300 shadow-sm px-4 py-2 bg-white text-sm font-medium text-gray-700 hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-offset-gray-100 focus:ring-indigo-500"
        >
          <span v-if="pi.workspace"> Change workspace </span>
          <span v-else> Assign to workspace </span>
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
              v-for="workspace in store.workspaces"
              :key="workspace.name"
              v-slot="{ active }"
              as="div"
            >
              <!-- href link action -->
              <button
                :class="[
                  active ? 'bg-gray-100 text-gray-900' : 'text-gray-700',
                  'group flex items-center px-4 py-2 text-sm',
                ]"
                class="text-gray-700 group flex items-center px-4 py-2 text-sm w-full"
                @click="() => onClick(pi.id, workspace.id)"
              >
                {{ workspace.slug }}
              </button>

              <!-- custom menu item content-->
            </MenuItem>
          </div>
        </MenuItems>
      </transition>
    </Menu>
    <span v-if="loading" class="inline-block ml-4">
      <TextSpinner text="Saving..." text-size="sm" spinner-size="4"></TextSpinner>
    </span>
    <span v-else-if="pi.workspace" class="text-left inline-block ml-4">
      {{ pi.workspace.name }}
    </span>
    <span v-else class="text-left ml-4"> No workspace assigned </span>
  </div>
</template>

<script setup lang="ts">
import { onMounted, ref } from "vue";
import type { PropType } from "vue";
import type { Pi, PatchedPiRequest } from "printnanny-api-client";
import TextSpinner from "../util/TextSpinner.vue";

import { Menu, MenuButton, MenuItem, MenuItems } from "@headlessui/vue";
import {
  ChevronDownIcon,
  HeartIcon,
  TrashIcon,
  ArrowTopRightOnSquareIcon,
} from "@heroicons/vue/24/solid";
import { ExclamationTriangleIcon } from "@heroicons/vue/24/outline";
import { useDeviceStore, buildDeviceActions } from "@/stores/devices";
import type { TableActionLink } from "@/types";

import { useWorkspaceStore } from "@/stores/workspaces";
import type workspaces from "@/router/workspaces";

const store = useWorkspaceStore();

const loading = ref(false);

const deviceStore = useDeviceStore();

const props = defineProps({
  pi: {
    type: Object as PropType<Pi>,
    required: true,
  },
  index: {
    type: Number,
    required: true,
  },
});

async function onClick(pi_id: number, workspace_id: number) {
    console.log(`Assigning pi=${pi_id} to ${workspace_id}`)
  loading.value = true;
  const res = await store.assignPiToWorkspace(pi_id, workspace_id);
  await deviceStore.fetchDevices();
  loading.value = false;
}

onMounted(async () => {
  if (store.workspaces.length === 0) {
    const result = await store.fetchWorkspaces();
    if (result) {
    }
  }
});
</script>
