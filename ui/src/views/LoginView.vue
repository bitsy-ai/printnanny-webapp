<script setup lang="ts">
import LoginForm from "@/components/forms/LoginForm.vue";
import FooterNav from "@/components/nav/FooterNav.vue";
import StickyAlerts from "@/components/alerts/StickyAlerts.vue";
</script>

<template>
  <main>
    <StickyAlerts />
    <LoginForm />
    <FooterNav />
  </main>
</template>
