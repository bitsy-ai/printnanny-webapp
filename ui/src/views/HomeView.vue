<script setup lang="ts">
import HomePage from "@/components/landing/HomePage.vue";
import FooterNav from "@/components/nav/FooterNav.vue";
import StickyAlerts from "../components/alerts/StickyAlerts.vue";
</script>

<template>
  <main>
    <StickyAlerts />
    <HomePage />
    <FooterNav />
  </main>
</template>
