<script setup lang="ts">
import { LockClosedIcon } from "@heroicons/vue/solid";
import { useUserStore } from "@/stores/user";
import { useForm, useField, Field, ErrorMessage, Form } from "vee-validate";
import { toRef, ref } from "vue";
import * as yup from "yup";
import type * as apiTypes from "printnanny-api-client";

const isLoading = ref(false);
// define a validation schema
const schema = yup.object({
  email: yup.string().required().email(),
  password: yup.string().required(),
});

const user = useUserStore();
async function onSubmit(values: any) {
  const res = await user.login(values as apiTypes.LoginRequest);
  console.log("Got Response", res);
}
</script>
<template>
  <div
    class="min-h-full flex items-center justify-center py-12 px-4 sm:px-6 lg:px-8 bg-indigo-50"
  >
    <div class="max-w-md w-full space-y-8">
      <div>
        <img
          class="mx-auto h-30 w-auto"
          src="@/assets/logo/logo-rect-light.svg"
          alt="PrintNanny"
        />
        <h2 class="mt-6 text-center text-3xl font-extrabold text-gray-900">
          Sign in to your account
        </h2>
        <p class="mt-2 text-center text-sm text-gray-600">
          Or
          {{ " " }}
          <a
            href="/request-invite"
            class="font-medium text-indigo-600 hover:text-indigo-500"
          >
            join the waitlist.</a
          >
        </p>
      </div>
      <Form @submit="onSubmit" v-slot="{ meta }" :validation-schema="schema">
        <label for="email" class="sr-only">Email address</label>
        <error-message className="text-red-500" name="email"></error-message>
        <Field
          name="email"
          id="email"
          type="email"
          autocomplete="email"
          className="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-t-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"
          placeholder="Email address"
          rules="required"
        />
        <label for="password" class="sr-only">Password</label>
        <Field
          name="password"
          id="password"
          type="password"
          autocomplete="current-password"
          className="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-b-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"
          placeholder="Password"
          rules="required"
        />
        <error-message className="text-red-500" name="password"></error-message>

        <button
          :disabled="isLoading || !meta.valid"
          type="submit"
          class="group mt-2 relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 disabled:opacity-25"
        >
          <span class="absolute left-0 inset-y-0 flex items-center pl-3">
            <LockClosedIcon
              class="h-5 w-5 text-indigo-500 group-hover:text-indigo-400"
              aria-hidden="true"
            />
          </span>
          Sign in
        </button>
      </Form>
    </div>
  </div>
</template>
