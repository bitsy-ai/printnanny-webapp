<template>
  <div class="px-4 mt-6 sm:px-6 lg:px-8">
    <h2 class="text-gray-500 text-xs font-medium uppercase tracking-wide">
      Favorite Devices
    </h2>
    <ul
      role="list"
      class="grid grid-cols-1 gap-4 sm:gap-6 sm:grid-cols-2 xl:grid-cols-6 mt-3"
    >
      <li
        v-for="(device, index) in deviceStore.favorites"
        :key="device.id"
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
          class="flex-1 flex items-center justify-between border-t border-b border-gray-200 bg-gray-100"
        >
          <div class="flex-1 px-4 py-2 text-sm truncate">
            <p class="text-gray-900 font-medium hover:text-gray-600">
              {{ device.hostname }}
            </p>
            <p class="text-gray-500">{{ device.last_boot }}</p>
          </div>
          <DeviceActionMenu :device="device" :index="index" />
        </div>
      </li>
    </ul>
  </div>
</template>
<script setup lang="ts">
import { HeartIcon } from "@heroicons/vue/solid";

import { useDeviceStore } from "@/stores/devices";
import DeviceActionMenu from "@/components/devices/DeviceActionMenu.vue";
const deviceStore = useDeviceStore();
const colors = ["bg-pink-500", "bg-green-500", "bg-indigo-500", "bg-blue-500"];
const mod = colors.length + 1;
</script>
