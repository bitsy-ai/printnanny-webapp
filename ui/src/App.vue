<script setup lang="ts">
import { RouterView } from "vue-router";
import { defineComponent } from "vue";

// import validator rules so all forms can access global rules
import "@/utils/validators";
</script>

<template>
  <RouterView />
</template>
