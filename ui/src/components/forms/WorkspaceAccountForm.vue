<template>
  <transition
    enter-active-class="transform ease-out duration-300 transition"
    enter-from-class="translate-y-2 opacity-0 sm:translate-y-0 sm:translate-x-2"
    enter-to-class="translate-y-0 opacity-100 sm:translate-x-0"
    leave-active-class="transition ease-in duration-100"
    leave-from-class="opacity-100"
    leave-to-class="opacity-0"
  >
    <div v-if="store.workspaces.length > 0" class="w-full">
      <p class="text-center">
        The Team feature is currently in alpha. Please email your
        <strong>support@printnanny.ai</strong> to let us know about any issues,
        or how we can better serve you.
      </p>
    </div>
    <div v-else class="w-full space-y-4">
      <h2 class="text-4xl font-extrabold text-gray-900 text-center">
        Request Access to Add Team Members
      </h2>
      <p class="text-center">Your account is limited to one member.</p>
      <p class="text-center">
        To request access for additional team members, please fill out the form
        below.
      </p>
      <a :href="formUrl" target="_blank">
        <button
          class="m-auto w-1/2 mb-2 transform md-shadow hover:scale-110 ease-in-out delay-150 duration-300 mt-6 block w-full sm:text-xl lg:text-lg xl:text-xl py-3 px-4 rounded-md shadow bg-gradient-to-r rounded-md shadow bg-gradient-to-r from-indigo-500 to-violet-600 text-white font-medium hover:from-indigo-600 hover:to-violet-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-cyan-400 focus:ring-offset-gray-900"
        >
          Request Access
        </button>
      </a>
      <p class="text-center">
        This feature is currently in alpha. Please email
        <strong>support@printnanny.ai</strong> to let us know about any issues.
      </p>
    </div>
  </transition>
</template>
<script setup lang="ts">
import { useWorkspaceStore } from "@/stores/workspaces";

const formUrl = import.meta.env.VITE_WORKSPACE_ALPHA_FORM;

const store = useWorkspaceStore();
await store.fetchWorkspaces();
</script>
