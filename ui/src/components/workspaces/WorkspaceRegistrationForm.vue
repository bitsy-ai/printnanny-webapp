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
        <h2 class="mt-6 text-center text-2xl font-medium text-gray-900">
          Finish registration for {{ decodeURIComponent(email) }}
        </h2>
      </div>
      <Form
        v-slot="{ meta }"
        :validation-schema="schema"
        class="space-y-4"
        @submit="onSubmit"
      >
        <div>
          <label
            for="firstName"
            class="block text-sm font-medium leading-6 text-gray-900"
            >First Name</label
          >
          <Field
            id="firstName"
            type="text"
            name="firstName"
            class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
          />
          <error-message
            class="text-red-500 text-sm"
            name="firstName"
          ></error-message>
        </div>

        <div>
          <label
            for="lastName"
            class="block text-sm font-medium leading-6 text-gray-900"
            >Last Name</label
          >
          <Field
            id="lastName"
            type="text"
            name="lastName"
            class="block w-full rounded-md border-0 px-3 py-2 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
          />
          <error-message
            class="text-red-500 text-sm"
            name="lastName"
          ></error-message>
        </div>

        <div>
          <label
            for="password"
            class="block text-sm font-medium leading-6 text-gray-900"
            >Password</label
          >
          <Field
            id="password"
            name="password"
            type="password"
            class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-t-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"
            placeholder="Password"
          />
          <label for="password" class="sr-only">Password</label>
          <Field
            id="passwordConfirmation"
            name="passwordConfirmation"
            type="password"
            class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-b-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"
            placeholder="Confirm Password"
          />
          <error-message
            class="text-red-500 text-sm"
            name="password"
          ></error-message>
          <error-message
            class="text-red-500 text-sm"
            name="passwordConfirmation"
          ></error-message>
        </div>
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
import { useWorkspaceStore } from "@/stores/workspaces";

const props = defineProps({
  token: {
    type: String,
    required: true,
  },
  email: {
    type: String,
    required: true,
  },
});

const loading = ref(false);
const state = reactive({
  loading,
});

const router = useRouter();
const store = useWorkspaceStore();

// define a validation schema
const schema = yup.object({
  firstName: yup.string().required("First name is required"),
  lastName: yup.string().required("Last name is required"),
  password: yup.string().required("Password is required"),
  passwordConfirmation: yup
    .string()
    .oneOf([yup.ref("password"), null], "Passwords must match")
    .required(),
});

const account = useAccountStore();

async function onSubmit(values: any) {
  state.loading = true;
  const req = {
    email: decodeURIComponent(props.email),
    first_name: values.firstName,
    last_name: values.lastName,
    password: values.password,
    token: props.token,
  };
  await store.verifyInvite(req);
  state.loading = false;
}
</script>
