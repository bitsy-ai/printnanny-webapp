<script setup lang="ts">
import { useRouter, RouterLink } from "vue-router";
const router = useRouter();

async function refresh() {
  console.log("refreshing page");
  await router.go(0);
}
</script>

<template>
  <span>
    <button
      type="button"
      class="order-1 ml-3 inline-flex items-center px-4 py-2 border border-gray-300 shadow-sm text-sm font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-purple-500 sm:order-0 sm:ml-0"
      @click="refresh"
    >
      Refresh
    </button>
    <router-link :to="{ name: 'workspaceCreate' }">
      <button
        type="button"
        class="order-0 inline-flex items-center px-4 py-2 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-purple-500 sm:order-1 ml-3"
      >
        New Workspace
      </button>
    </router-link>
  </span>
</template>
