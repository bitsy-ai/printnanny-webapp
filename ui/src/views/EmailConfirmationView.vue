<script setup lang="ts">
import PasswordResetConfirmForm from "@/components/forms/PasswordResetConfirmForm.vue";
import FooterNav from "@/components/nav/FooterNav.vue";
import StickyAlerts from "@/components/alerts/StickyAlerts.vue";
import CustomSpinner from "@/components/util/CustomSpinner.vue";
import { ref, onMounted } from "vue";
import { useAccountStore } from "@/stores/account";
import type * as apiTypes from "printnanny-api-client";
import { useRouter } from "vue-router";

const account = useAccountStore();

const loading = ref(true);
const success = ref(false);

const props = defineProps({
  verificationKey: {
    required: true,
  },
});

const router = useRouter();

onMounted(async () => {
  const req = { key: props.verificationKey } as apiTypes.VerifyEmailRequest;

  const res = await account.verifyConfirmEmailKey(req);
  loading.value = false;
  if (res !== undefined && res?.status === 200) {
    success.value = true;
  }
});
</script>

<template>
  <div class="flex flex-col h-screen justify-between">
    <StickyAlerts />
    <main class="mb-auto h-full">
      <div class="grid grid-cols-1 flex">
        <CustomSpinner
          v-if="loading"
          color="indigo"
          class="m-auto h-24 text-2xl font-extrabold mt-6"
          width="w-12"
          height="h-12"
          text="Finishing account setup..."
        ></CustomSpinner>

        <div
          class="m-auto h-24 text-2xl font-extrabold text-gray-900 my-6 text-center"
        >
          <h2>Your email is confirmed.</h2>
          <a href="/login/">
            <button
              class="group mt-2 relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 disabled:opacity-25"
            >
              Login
            </button>
          </a>
        </div>
      </div>
    </main>
    <FooterNav />
  </div>
</template>
