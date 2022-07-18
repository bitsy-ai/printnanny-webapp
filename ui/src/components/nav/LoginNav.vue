<!-- show login / request access to anonymous user, or dashboard button if logged in -->
<template>
  <div class="hidden md:flex md:items-center md:space-x-6">
    <a
      v-if="!account.isAuthenticated"
      href="/login"
      class="text-base font-medium text-white hover:text-gray-300"
    >
      Log in
    </a>
    <a
      v-if="!account.isAuthenticated"
      href="/request-invite"
      class="inline-flex items-center px-4 py-2 border border-transparent text-base font-medium rounded-md text-white bg-gray-600 hover:bg-gray-700"
    >
      Request Access
    </a>
    <a
      v-if="account.isAuthenticated"
      href="/devices"
      class="inline-flex items-center px-4 py-2 border border-transparent text-base font-medium rounded-md text-white bg-gray-600 hover:bg-gray-700"
    >
      Dashboard
    </a>
    <a
      v-if="account.isAuthenticated"
      href="/logout"
      class="inline-flex items-center px-4 py-2 border border-transparent text-base font-medium rounded-md text-white bg-gray-600 hover:bg-gray-700"
    >
      Logout
    </a>
  </div>
</template>
<script setup lang="ts">
import { useAccountStore } from "@/stores/account";

const account = useAccountStore();
</script>
