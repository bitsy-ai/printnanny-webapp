<script setup lang="ts">
import { RouterLink, useRouter } from "vue-router";
import { useAccountStore } from "@/stores/account";

const account = useAccountStore();
const props = defineProps({
    demoId: {
        type: String,
        required: true
    }
});

const result = await account.demosApi.demosRetrieve(props.demoId);


</script>
<template>
  <div
    class="flex-1 flex items-center justify-center p-12 px-4 sm:px-6 lg:px-8 bg-indigo-20 md:w-1/2 m:0 md:mx-auto rounded bg-white shadow-md"
  >
    <div class="max-w-md w-full space-y-8">
      <img
        class="mx-auto h-30 w-auto"
        src="@/assets/logo/logo-rect-light.svg"
        alt="PrintNanny"
      />
      <h2 class="my-6 text-center text-3xl font-extrabold text-gray-900">
        Your results are in! 🔮
      </h2>
      <p class="mt-5 max-w-prose mx-auto text-xl text-gray-500 text-center">
        Upload your gnarliest print failures.
      </p>
      <hr class="w-64 h-px my-8 mx-auto bg-gray-200 border-0" />

      <transition
        enter-active-class="transition ease-out duration-100"
        enter-from-class="transform opacity-0 scale-95"
        enter-to-class="transform opacity-100 scale-100"
        leave-active-class="transition ease-in duration-75"
        leave-from-class="transform opacity-100 scale-100"
        leave-to-class="transform opacity-0 scale-95"
      >

      </transition>
    </div>
  </div>
</template>