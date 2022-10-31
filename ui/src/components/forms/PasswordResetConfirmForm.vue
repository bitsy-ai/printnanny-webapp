<script setup lang="ts">
import { useRouter } from "vue-router";
import { LockClosedIcon, RefreshIcon } from "@heroicons/vue/solid";
import { useAccountStore } from "@/stores/account";
import { Field, ErrorMessage, Form } from "vee-validate";
import { ref, reactive } from "vue";
import * as yup from "yup";
import type * as apiTypes from "printnanny-api-client";

const props = defineProps({
  userId: {
    required: true
  },
  token: {
    required: true
  }
})

const router = useRouter();

const loading = ref(false);
const sent = ref(false);
const state = reactive({
  loading,
  sent
});

// define a validation schema
const schema = yup.object({
  password: yup.string().required("Password is required"),
  passwordConfirmation: yup
    .string()
    .oneOf([yup.ref("password"), null], "Passwords must patch"),
});

const account = useAccountStore();
async function onSubmit(values: any) {
  state.loading = true;
  const req = {
    uid: props.userId,
    token: props.token,
    new_password1: values.password,
    new_password2: values.passwordConfirmation
  } as api.PasswordResetConfirmRequest;
  const res = await account.resetPasswordConfirm(req);
  state.loading = false;
  if (res.status === 200){
    router.push({name: "login"})
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
          Set a New Password
        </h2>
      </div>
      <Form v-slot="{ meta }" :validation-schema="schema" @submit="onSubmit">
    <label for="password" class="text-sm text-gray-500">Password</label>

        <Field
          id="password"
          name="password"
          type="password"
          autocomplete="current-password"
          class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-t-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"
          placeholder="Password"
          rules="required"
        />
        <Field
          id="passwordConfirmation"
          name="passwordConfirmation"
          type="password"
          autocomplete="current-password"
          class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-b-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"
          placeholder="Confirm Password"
          rules="required"
        />

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
          Save Password
        </button>
      </Form>
    </div>
  </div>
</template>
