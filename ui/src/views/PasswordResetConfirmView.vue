<script setup lang="ts">
import PasswordResetFormForm from "@/components/forms/PasswordResetConfirmForm.vue";
import FooterNav from "@/components/nav/FooterNav.vue";
import StickyAlerts from "@/components/alerts/StickyAlerts.vue";
</script>

<template>
  <div class="flex flex-col h-screen justify-between">
    <StickyAlerts />
    <main class="mb-auto h-full">
      <PasswordResetConfirmForm />
    </main>
    <FooterNav />
  </div>
</template>
