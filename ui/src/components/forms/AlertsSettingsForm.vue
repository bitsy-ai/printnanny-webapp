<script setup lang="ts">
import { useBillingStore } from "@/stores/billing";
const billingStore = useBillingStore();
</script>
<template>
  <div class="bg-white overflow-hidden shadow rounded-lg">
      <Form v-slot="{ meta }" :validation-schema="schema" @submit="onSubmit">
        <label for="email" class="sr-only">Notification types</label>
        <error-message class-name="text-red-500" name="email"></error-message>
        <Field
          id="email"
          name="notificationTypes"
          type="checkbox"
          autocomplete="email"
          class-name="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-t-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"
          placeholder="Email address"
          rules="required"
        />
        <label for="password" class="sr-only">Password</label>
        <Field
          id="password"
          name="password"
          type="password"
          autocomplete="current-password"
          class-name="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-b-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"
          placeholder="Password"
          rules="required"
        />
        <error-message
          class-name="text-red-500"
          name="password"
        ></error-message>

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
          Sign in
        </button>
      </Form>
  </div>
</template>
