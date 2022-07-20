<script setup lang="ts">
import { useRouter } from "vue-router";
import { useDeviceStore } from "@/stores/devices";
const router = useRouter();
const device = useDeviceStore();
const props = defineProps({
  hostname: {
    type: String,
    required: true,
  },
  id: {
    type: String,
    required: true,
  },
});

async function onClick() {
  await device.delete(parseInt(props.id));
  await router.push({ name: "devices" });
}
</script>
<template>
  <div class="bg-white overflow-hidden shadow rounded-lg">
    <div class="px-4 py-5 sm:px-6">
      <h1 class="prose prose-2xl">
        Are you sure you want to delete
        {{ router.currentRoute.value.query.hostname }}?
      </h1>
      <p class="prose">
        This cannot be un-done!
        {{ router.currentRoute.value.query.hostname }} will be reset to factory
        defaults.
      </p>
    </div>
    <div class="bg-gray-50 px-4 py-5 sm:p-6">
      <button
        type="button"
        class="order-0 inline-flex items-center px-4 py-2 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-red-600 hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-purple-500 sm:order-1 sm:ml-3"
        @click="onClick"
      >
        Delete
      </button>

      <router-link :to="{ name: 'devices' }">
        <button
          type="button"
          class="order-0 inline-flex items-center px-4 py-2 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-indigo-600 hover:indigo-red-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-purple-500 sm:order-1 sm:ml-3"
        >
          Return Home
        </button>
      </router-link>
    </div>
  </div>
</template>
