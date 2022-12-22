<script setup lang="ts">
// import validator rules so all forms can access global rules
import "@/utils/validators";

// only enable tidio in production
const tidioScript = import.meta.env.VITE_TIDIO_SCRIPT_URI;
if (tidioScript !== undefined) {
  const el = document.createElement("script");
  el.setAttribute("src", tidioScript);
  document.body.appendChild(el);
}
</script>

<template><router-view> </router-view></template>
