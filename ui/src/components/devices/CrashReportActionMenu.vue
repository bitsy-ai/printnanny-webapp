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
        <MenuItem v-slot="{ active }" as="div">
            <!-- href link action -->
            <a
            @click="openReport"
            target="_blank"
            :class="[
                active ? 'bg-gray-100 text-gray-900' : 'text-gray-700',
                'group flex items-center px-4 py-2 text-sm',
            ]"
            >
            <DownloadIcon
                class="mr-3 h-5 w-5 text-gray-400 group-hover:text-gray-500"
                aria-hidden="true"
            />
            Show Details
            </a>
            
            <!-- custom menu item content-->
        </MenuItem>
        </div>
    </MenuItems>
    </transition>
</Menu>
</template>
  
<script setup lang="ts">
import { Menu, MenuButton, MenuItem, MenuItems } from "@headlessui/vue";
import {
  DownloadIcon,
  ChevronDownIcon,

} from "@heroicons/vue/solid";
import { useCrashReportStore } from "@/stores/crash-reports";
import { PropType } from "@vue/runtime-core";
import type { CrashReport } from "printnanny-api-client";

const props = defineProps({
    crashReport: {
        type: Object as PropType<CrashReport>,
        required: true
    }
});

const store = useCrashReportStore();

function openReport(){
    return store.openReport(props.crashReport)
}


</script>
