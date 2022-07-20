<script setup lang="ts">
import { useDeviceStore } from "@/stores/devices";

const deviceStore = useDeviceStore();
deviceStore.fetch();
</script>
<template>
  <ul role="list" class="space-y-3">
    <li
      v-for="device in deviceStore.devices"
      :key="device.id"
      class="bg-white shadow overflow-hidden px-4 py-4 sm:px-6 sm:rounded-md"
    ></li>
  </ul>
</template>
