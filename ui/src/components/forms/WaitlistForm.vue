<template>
  <Form
    class="sm:max-w-xl sm:mx-auto lg:mx-0"
    :validation-schema="schema"
    @submit="onSubmit"
  >
    <div class="sm:flex">
      <div class="min-w-0 flex-1">
        <label for="email" class="sr-only">Email address</label>
        <Field
          id="email"
          name="email"
          type="email"
          autocomplete="email"
          class="block w-full px-4 py-3 rounded-md border-0 text-base text-gray-900 placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-cyan-400 focus:ring-offset-gray-900"
          placeholder="Email address"
          rules="required"
        />
        <error-message class="text-red-500" name="email"></error-message>
      </div>
      <div class="mt-3 sm:mt-0 sm:ml-3">
        <button
          type="submit"
          class="block w-full py-3 px-4 rounded-md shadow bg-gradient-to-r from-indigo-500 to-violet-600 text-white font-medium hover:from-indigo-600 hover:to-violet-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-cyan-400 focus:ring-offset-gray-900"
        >
          Join the Waitlist
        </button>
      </div>
    </div>
    <p class="mt-3 text-sm text-gray-300 sm:mt-4">
      By providing your email, you agree to our
      <a href="/terms" class="font-medium text-white">Terms of Service.</a>
    </p>
  </Form>
</template>
<script setup lang="ts">
import { ref, reactive } from "vue";
import * as yup from "yup";
import { Field, ErrorMessage, Form } from "vee-validate";
import { useAccountStore } from "@/stores/account";

const accountStore = useAccountStore();

// define a validation schema
const schema = yup.object({
  email: yup.string().required().email(),
});

const loading = ref(false);

const state = reactive({
  loading,
});
async function onSubmit(values: any) {
  state.loading = true;
  await accountStore.submitEmailWaitlist(values.email);
  state.loading = false;
}
</script>