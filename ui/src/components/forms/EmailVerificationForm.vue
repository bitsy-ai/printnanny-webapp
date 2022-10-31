<script setup lang="ts">
import { RouterLink } from "vue-router";
import { LockClosedIcon, RefreshIcon } from "@heroicons/vue/solid";
import { useAccountStore } from "@/stores/account";
import { Field, ErrorMessage, Form } from "vee-validate";
import { ref, reactive } from "vue";
import * as yup from "yup";
import type * as apiTypes from "printnanny-api-client";
import type { UiAlert } from "@/types";
import { useAlertStore } from "@/stores/alerts";

const loading = ref(false);
const state = reactive({
  loading,
});

const alerts = useAlertStore();

// define a validation schema
const schema = yup.object({
  email: yup.string().required().email(),
});

const account = useAccountStore();
async function onSubmit(values: any) {
  state.loading = true;
  const req = {
    email: values.email,
  } as apiTypes.ResendEmailVerificationRequest;
  const res = await account.resendAccountVerificationEmail(req);
  state.loading = false;
  if (res !== undefined && res?.status === 200) {
    const alert = {
      color: "green",
      message: `A verification code was sent to ${values.email}`,
      header: "Check your email",
      actions: [],
      error: undefined,
    } as UiAlert;

    alerts.push(alert);
  }
}
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
        <h2 class="mt-6 text-center text-3xl font-extrabold text-gray-900">
          Verify Email Address
        </h2>
      </div>
      <Form v-slot="{ meta }" :validation-schema="schema" @submit="onSubmit">
        <label for="email" class="sr-only">Email address</label>
        <error-message class-name="text-red-500" name="email"></error-message>
        <Field
          id="email"
          name="email"
          type="email"
          autocomplete="email"
          class="appearance-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"
          placeholder="Email address"
          rules="required"
        />
        <label for="password" class="sr-only">Password</label>
        <button
          id="email-submit"
          :disabled="state.loading || !meta.valid"
          type="submit"
          class="group mt-2 relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 disabled:opacity-25"
        >
          <span class="absolute left-0 inset-y-0 flex items-center pl-3">
            <LockClosedIcon
              v-if="!state.loading"
              class="h-5 w-5 text-indigo-500 group-hover:text-indigo-400"
              aria-hidden="true"
            />
            <RefreshIcon
              v-if="state.loading"
              class="animate-spin h-5 w-5 text-indigo-500 group-hover:text-indigo-400"
              aria-hidden="true"
            />
          </span>
          Send verification email
        </button>
      </Form>

      <p class="text-center my-2 text-sm text-gray-900">Trouble signing in?</p>
      <p class="text-center my-2 text-sm">
        <RouterLink
          :to="{ name: 'reset-password' }"
          class="font-medium text-indigo-600 hover:text-indigo-500"
        >
          Reset Password
        </RouterLink>
      </p>
    </div>
  </div>
</template>
