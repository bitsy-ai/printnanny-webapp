<template>
  <div class="absolute bottom-0 right-2 p-2">
    <span class="text-sm font-medium text-gray-400">API Version: </span>
    <span class="mt-1 text-sm text-gray-400 sm:mt-0 sm:col-span-2">
      {{ apiVersion }} |
    </span>
    <span class="text-sm font-medium text-gray-400">UI Build: </span>
    <span class="mt-1 text-sm text-gray-400 sm:mt-0 sm:col-span-2">
      {{ commitBranch }}/{{ commitHash }}
    </span>
  </div>
</template>
<script setup lang="ts">
// const commitDate = new Date(import.meta.env.VITE_GIT_COMMIT_DATE);
const apiVersion = import.meta.env.VITE_PRINTNANNY_API_VERSION;
const commitBranch = import.meta.env.VITE_GIT_BRANCH_NAME;
const commitHash = import.meta.env.VITE_GIT_COMMIT_HASH;
</script>
