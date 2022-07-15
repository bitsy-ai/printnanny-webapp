<script setup lang="ts">
import LoginForm from "@/components/forms/LoginForm.vue";
import FooterNav from "@/components/nav/FooterNav.vue";
import StickyAlerts from "@/components/alerts/StickyAlerts.vue";
</script>

<template>
<div class="flex flex-col h-screen justify-between">
  <StickyAlerts />
  <main class="mb-auto h-full">
    <LoginForm />
  </main>
  <FooterNav />

</div>


</template>
