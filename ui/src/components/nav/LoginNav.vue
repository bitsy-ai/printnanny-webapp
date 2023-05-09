<!-- show login / request access to anonymous user, or dashboard button if logged in -->
<template>
  <div class="hidden lg:flex md:items-center md:space-x-6">
    <a
      v-if="!account.isAuthenticated"
      id="nav-login"
      href="/login"
      class="inline-flex items-center px-4 py-2 border border-transparent text-base font-medium rounded-md text-white bg-gray-600 hover:bg-gray-700"
    >
      Log in
    </a>
    <a
      v-if="account.isAuthenticated"
      id="nav-dashboard"
      href="/devices"
      class="inline-flex items-center px-4 py-2 border border-transparent text-base font-medium rounded-md text-white bg-gray-600 hover:bg-gray-700"
    >
      Dashboard
    </a>
    <a
      v-if="account.isAuthenticated"
      id="nav-logout"
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
