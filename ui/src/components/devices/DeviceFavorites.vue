<template>
  <div class="px-4 mt-6 sm:px-6 lg:px-8">
    <h2 class="text-gray-500 text-xs font-medium uppercase tracking-wide">
      Favorite Devices
    </h2>
    <ul
      role="list"
      class="grid grid-cols-1 xl:gap-2 sm:gap-6 sm:grid-cols-2 xl:grid-cols-6 mt-3"
    >
      <li
        v-for="(pi, index) in deviceStore.favorites"
        :key="pi.id"
        class="relative col-span-2 flex shadow-sm rounded-md"
      >
        <div
          :class="[
            colors[index % mod],
            'flex-shrink-0 flex items-center justify-center w-8 text-white text-sm font-medium rounded-l-md',
          ]"
        >
          <HeartIcon class="text-white" />
        </div>
        <div
          class="flex-1 flex items-center justify-between border-t border-b border-r border-gray-200 bg-gray-100 rounded-r-lg"
        >
          <div class="flex-1 px-4 py-2 text-sm truncate">
            <p class="text-gray-900 font-medium hover:text-gray-600">
              {{ pi.hostname }}
            </p>
          </div>
          <DeviceActionMenu :pi="pi" :index="index" />
        </div>
      </li>
    </ul>
    <span
      class="hidden bg-fuchsia-500 bg-blue-500 bg-indigo-500 bg-red-500 bg-orange-500 bg-amber-500 bg-yellow-500 bg-lime-500 bg-green-500 bg-teal-500 bg-cyan-500 bg-sky-500 bg-blue-500 bg-indigo-500 bg-violet-500 bg-purple-500 bg-pink-500 bg-rose-500"
    ></span>
  </div>
</template>
<script setup lang="ts">
import moment from "moment";
import { HeartIcon } from "@heroicons/vue/24/solid";
import { useDeviceStore, buildDeviceActions } from "@/stores/devices";
import DeviceActionMenu from "@/components/devices/DeviceActionMenu.vue";
const deviceStore = useDeviceStore();
const colors = [
  "bg-rose-500",
  "bg-lime-500",
  "bg-sky-500",
  "bg-amber-500",
  "bg-pink-500",
  "bg-emerald-500",
  "bg-indigo-500",
  "bg-yellow-500",
  "bg-fuchsia-500",
  "bg-blue-500",
  "bg-orange-500",
  "bg-teal-500",
  "bg-purple-500",
  "bg-green-500", 
  "bg-cyan-500"
];
const mod = colors.length + 1;
</script>
