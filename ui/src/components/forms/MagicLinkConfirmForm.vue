<script setup lang="ts">
import { RouterLink, useRouter } from "vue-router";
import { LockClosedIcon, RefreshIcon } from "@heroicons/vue/solid";
import { useAccountStore } from "@/stores/account";
import { Field, ErrorMessage, Form } from "vee-validate";
import { ref, reactive, onMounted } from "vue";
import * as yup from "yup";
import type * as apiTypes from "printnanny-api-client";
const router = useRouter();
const loading = ref(false);
const state = reactive({
  loading,
});

const props = defineProps({
  email: {
    type: String,
    required: true,
  },
  token: {
    type: String,
  },
});

const initialValues = {
  token: props.token,
};

// define a validation schema
const schema = yup.object({
  token: yup.string().required().matches(/\d+$/),
});

onMounted(() => {
  if (props.token !== undefined) {
    initialValues.token = props.token;
  }
});

const account = useAccountStore();
async function onSubmit(values: any) {
  state.loading = true;
  const res = await account.twoFactorStage2(props.email, values.token);
  console.log("Got Response", res);
  state.loading = false;
  router.push({ name: "devices" });
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
          Check your email
        </h2>
        <p class="mt-2 text-center text-sm text-gray-600">
          We've sent a 6-character code to <strong>{{ email }}</strong
          >. The code expires, so please enter it soon.
        </p>
      </div>
      <Form
        v-slot="{ meta }"
        :validation-schema="schema"
        :initial-values="initialValues"
        @submit="onSubmit"
      >
        <label for="email" class="sr-only">Email address</label>
        <error-message class-name="text-red-500" name="email"></error-message>
        <Field
          id="token"
          name="token"
          type="text"
          maxlength="6"
          class="appearance-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"
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
          Login
        </button>
      </Form>
    </div>
  </div>
</template>
