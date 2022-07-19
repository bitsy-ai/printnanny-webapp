<template>
  <dl>
    <dt class="text-sm font-medium text-gray-500">Build date</dt>
    <dd class="mt-1 text-sm text-gray-900 sm:mt-0 sm:col-span-2">
      {{ commitDate.toLocaleString() }}
    </dd>
    <dt class="text-sm font-medium text-gray-500">Branch/Commit</dt>
    <dd class="mt-1 text-sm text-gray-900 sm:mt-0 sm:col-span-2">
      {{ commitBranch }}/{{ commitHash }}
    </dd>
  </dl>
</template>
<script setup lang="ts">
const commitDate = new Date(import.meta.env.VITE_GIT_COMMIT_DATE);
const commitBranch = import.meta.env.VITE_GIT_BRANCH_NAME;
const commitHash = import.meta.env.VITE_GIT_COMMIT_HASH;
</script>
