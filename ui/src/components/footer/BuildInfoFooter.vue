<template>
  <div class="hidden md:inline-block">
    <span class="text-right flex-1">
    <span class="text-sm font-medium text-gray-400">API Version: </span>
    <span class="mt-1 text-sm text-gray-400 sm:mt-0 sm:col-span-2">
      {{ apiVersion }} |
    </span>
    <span class="text-sm font-medium text-gray-400">UI Build: </span>
    <span class="mt-1 text-sm text-gray-400 sm:mt-0 sm:col-span-2">
      {{ commitBranch }}/{{ commitHash }}
    </span>
  </span>
  </div>

</template>
<script setup lang="ts">
// const commitDate = new Date(import.meta.env.VITE_GIT_COMMIT_DATE);
const apiVersion = import.meta.env.VITE_PRINTNANNY_API_VERSION;
const commitBranch = import.meta.env.VITE_GIT_BRANCH_NAME;
const commitHash = import.meta.env.VITE_GIT_COMMIT_HASH;
</script>
