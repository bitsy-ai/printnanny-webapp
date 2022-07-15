<template>
                <div class="mt-6 px-5">
                  <a
                    href="#"
                    class="block text-center w-full py-3 px-4 rounded-md shadow bg-gradient-to-r from-indigo-300 to-cyan-600 text-white font-medium hover:from-teal-600 hover:to-cyan-700"
                    >Request Acesss</a
                  >
                </div>
                <div class="mt-6 px-5">
                  <p class="text-center text-base font-medium text-gray-500">
                    Existing customer?
                    <a href="#" class="text-gray-900 hover:underline">Login</a>
                  </p>
                </div>
</template>
<script setup lang="ts">
import { useAccountStore } from "@/stores/account";

const account = useAccountStore();
</script>