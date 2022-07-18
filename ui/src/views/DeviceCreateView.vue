<script setup lang="ts">
import StickyAlerts from "@/components/alerts/StickyAlerts.vue";
import DashboardPage from "@/components/pages/DashboardPage.vue";
import DeviceCreateView from "@/components/devices/DeviceCreate.vue";
</script>

<template>
  <div class="flex flex-col h-screen justify-between">
    <StickyAlerts />
    <header></header>
    <main class="mb-auto h-full">
      <DashboardPage>
        <!-- Replace pinned devices with device create form -->
        <template #pinned>
          <h1
            class="text-lg font-medium leading-6 text-gray-900 text-center p-6"
          >
            Connect New Device
          </h1>
        </template>

        <template #content>
          <DeviceCreateView />
        </template>
      </DashboardPage>
    </main>
  </div>
</template>
