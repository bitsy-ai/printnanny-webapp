<script setup lang="ts">
import RegisterAccount from "@/components/auth/RegisterAccount.vue";
</script>

<template>
  <div
    class="min-h-full flex items-center justify-center py-12 px-4 sm:px-6 lg:px-8 bg-indigo-20"
  >
    <div class="max-w-md w-full space-y-8">
      <div>
        <img
          class="mx-auto h-30 w-auto"
          src="@/assets/logo/logo-rect-light.svg"
          alt="PrintNanny"
        />
      </div>

      <RegisterAccount :create-user="true" />
    </div>
  </div>
</template>
