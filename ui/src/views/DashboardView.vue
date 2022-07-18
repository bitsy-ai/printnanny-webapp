<script setup lang="ts">
import StickyAlerts from "@/components/alerts/StickyAlerts.vue";
import DashboardPage from "@/components/pages/DashboardPage.vue";
</script>

<template>
  <div class="flex flex-col h-screen justify-between">
    <StickyAlerts />
    <header></header>
    <main class="mb-auto h-full">
      <DashboardPage />
    </main>
  </div>
</template>
