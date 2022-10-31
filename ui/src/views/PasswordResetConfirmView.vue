<script setup lang="ts">
import PasswordResetConfirmForm from "@/components/forms/PasswordResetConfirmForm.vue";
import FooterNav from "@/components/nav/FooterNav.vue";
import StickyAlerts from "@/components/alerts/StickyAlerts.vue";

defineProps({
  userId: {
    required: true
  },
  token: {
    required: true
  }
})
</script>

<template>
  <div class="flex flex-col h-screen justify-between">
    <StickyAlerts />
    <main class="mb-auto h-full">
      <PasswordResetConfirmForm :userId="userId" :token="token"/>
    </main>
    <FooterNav />
  </div>
</template>
