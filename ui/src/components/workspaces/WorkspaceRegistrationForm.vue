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
          Create your account
        </h2>
        <p class="mt-2 text-center text-sm text-gray-600">
          Or
          {{ " " }}
          <a
            id="join-waitlist"
            href="/request-invite"
            class="font-medium text-indigo-600 hover:text-indigo-500"
          >
            join the waitlist.</a
          >
        </p>
      </div>
      <Form v-slot="{ meta }" :validation-schema="schema" @submit="onSubmit" :initialValues="initialValues">
        <label for="email" class="sr-only">Email address</label>
        <error-message class-name="text-red-500" name="email"></error-message>
        <Field
          id="email"
          name="email"
          type="email"
          autocomplete="email"
          disabled
          class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-t-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"
          placeholder="Email address"
          rules="required"
        />
        <label for="password" class="sr-only">Password</label>
        <Field
          id="password"
          name="password"
          type="password"
          autocomplete="current-password"
          class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-b-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"
          placeholder="Password"
          rules="required"
        />
        <error-message
          class-name="text-red-500"
          name="password"
        ></error-message>

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
            <ArrowPathIcon
              v-if="state.loading"
              class="animate-spin h-5 w-5 text-indigo-500 group-hover:text-indigo-400"
              aria-hidden="true"
            />
          </span>
          Sign in
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
<script lang="ts" setup>
import { ref, reactive } from "vue";
import { useRouter } from "vue-router";
import * as yup from "yup";
import { useAccountStore } from "@/stores/account";
import { LockClosedIcon, ArrowPathIcon } from "@heroicons/vue/24/solid";
import { Field, ErrorMessage, Form } from "vee-validate";

const props = defineProps({
    token: {
        type: String,
        required: true
    }
});

const loading = ref(false);
const state = reactive({
  loading,
});

const router = useRouter();
const initialValues = { email: router.currentRoute.value.query.email }

// define a validation schema
const schema = yup.object({
  firstName: yup.string().required('First name is required'),
  lastName: yup.string().required('Last name is required'),
  password: yup.string().required('Password is required'),
  passwordConfirmation: yup.string()
     .oneOf([yup.ref('password'), null], 'Passwords must match')
});

const account = useAccountStore();

async function onSubmit(values: any) {
  state.loading = true;
  const res = await account.login(values as apiTypes.LoginRequest);
  console.log("Got Response", res);
  state.loading = false;
}
</script>