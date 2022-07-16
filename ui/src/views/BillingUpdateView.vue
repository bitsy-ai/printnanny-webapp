<script setup lang="ts">
import FooterNav from "@/components/nav/FooterNav.vue";
import StickyAlerts from "@/components/alerts/StickyAlerts.vue";
import DashboardPage from "@/components/pages/DashboardPage.vue";
import BillingUpdateForm from "@/components/forms/BillingUpdateForm.vue";
</script>

<template>
  <div class="flex flex-col h-screen justify-between">
    <StickyAlerts />
    <header></header>
    <main class="mb-auto h-full">
      <DashboardPage>
        <!-- Replace pinned devices with billing header -->
        <template #pinned>
          <span></span>
        </template>
        <template #content>
          <BillingUpdateForm />
        </template>
      </DashboardPage>
    </main>
  </div>
</template>
