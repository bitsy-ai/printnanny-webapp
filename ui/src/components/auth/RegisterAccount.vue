<template>
  <Form
    v-if="success == false"
    v-slot="{ meta }"
    :validation-schema="schema"
    @submit="onSubmit"
  >
    <label for="email" class="text-sm text-gray-500">Email address</label>
    <error-message class-name="text-red-500" name="email"></error-message>
    <Field
      id="email"
      name="email"
      type="email"
      class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-t-md rounded-b-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm mb-2"
      :placeholder="emailPlaceholder"
      rules="required"
      :readonly="emailDisabled"
      :disabled="emailDisabled"
    />
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
      Set Password
    </button>
  </Form>
  <div v-else class="flex w-full items-center py-4 text-gray-600">
    <CheckCircleIcon class="w-10 h-10 text-emerald-500" />
    <p class="pl-2">Success! Created account for {{ email }}</p>
    <router-link v-if="showDashboardButton" :to="{ name: 'devices' }">
      <button
        class="group mt-2 relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 disabled:opacity-25"
      >
        Open Dashboard
      </button>
    </router-link>
  </div>
</template>
<script setup lang="ts">
import { ref, reactive, computed } from "vue";
import { LockClosedIcon, RefreshIcon } from "@heroicons/vue/solid";
import { RouterLink } from "vue-router";
import { CheckCircleIcon } from "@heroicons/vue/solid";
import type * as api from "printnanny-api-client";
import * as yup from "yup";
import { Field, ErrorMessage, Form } from "vee-validate";
import { useAccountStore } from "@/stores/account";
import { useAlertStore } from "@/stores/alerts";
import type { UiAlert } from "@/types";

const loading = ref(false);
const success = ref(false);
const state = reactive({
  loading,
  success,
});

const props = defineProps({
  createUser: {
    type: Boolean,
    default: false,
  },
  email: {
    type: String,
    default: "",
  },
  showDashboardButton: {
    type: Boolean,
    default: true,
  },
  emailDisabled: {
    default: false,
  },
});

const email = ref(props.email);

const emailSchema =
  props.email === ""
    ? yup.string().email().default(props.email)
    : yup.string().email().required();

const emailPlaceholder = computed(() =>
  props.email === "" ? "Enter your email address" : props.email
);

const schema = yup.object({
  email: emailSchema,
  password: yup.string().required("Password is required"),
  passwordConfirmation: yup
    .string()
    .oneOf([yup.ref("password"), null], "Passwords must patch"),
});

const account = useAccountStore();
const alerts = useAlertStore();
async function onSubmit(values: any) {
  state.loading = true;
  email.value = props.email === "" ? values.email : props.email;
  const res = await account.createAccount({
    email: email.value,
    password1: values.password,
    password2: values.passwordConfirmation,
  } as api.RegisterRequest);
  state.loading = false;
  if (res) {
    state.success = true;
    const success = {
      color: "green",
      message: `Created account for ${email.value}`,
      header: "Success!",
      actions: [],
      error: undefined,
    } as UiAlert;
    alerts.push(success);
  }
}
</script>
