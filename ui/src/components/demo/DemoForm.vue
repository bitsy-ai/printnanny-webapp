<script setup lang="ts">
import { RouterLink, useRouter } from "vue-router";
import { LockClosedIcon, ArrowPathIcon } from "@heroicons/vue/24/solid";
import { Field, ErrorMessage, Form } from "vee-validate";
import { ref, reactive } from "vue";
import * as yup from "yup";
import type * as apiTypes from "printnanny-api-client";
import { useDemoStore } from "@/stores/demo";

const router = useRouter();
const loading = ref(false);
const submitted = ref(false);

const file = ref(undefined as undefined | string);
const store = useDemoStore();

const state = reactive({
  loading,
});

// define a validation schema
const schema = yup.object({
  email: yup.string().required().email(),
});

async function onSubmit(values: any) {
  state.loading = true;
  await store.submit(values.email, file.value);
  state.loading = false;
}

function onChangeFile(e: any) {
  console.log("Selected file", e);
  const files = e.target.files || e.dataTransfer.files;
  if (!files.length) return;
  file.value = files[0];
}
</script>
<template>
  <div
    class="flex-1 flex items-center justify-center p-12 px-4 sm:px-6 lg:px-8 bg-indigo-20 md:w-1/2 m:0 md:mx-auto rounded bg-white shadow-md"
  >
    <div class="max-w-md w-full space-y-8">
      <img
        class="mx-auto h-30 w-auto"
        src="@/assets/logo/logo-rect-light.svg"
        alt="PrintNanny"
      />
      <h2 class="my-6 text-center text-3xl font-extrabold text-gray-900">
        Can you stump the AI?
      </h2>
      <p class="mt-5 max-w-prose mx-auto text-xl text-gray-500 text-center">
        Upload your gnarliest 3D print failures to test PrintNanny's detection
        system.
      </p>
      <hr class="w-64 h-px my-8 mx-auto bg-gray-200 border-0" />

      <transition
        enter-active-class="transition ease-out duration-100"
        enter-from-class="transform opacity-0 scale-95"
        enter-to-class="transform opacity-100 scale-100"
        leave-active-class="transition ease-in duration-75"
        leave-from-class="transform opacity-100 scale-100"
        leave-to-class="transform opacity-0 scale-95"
      >
        <Form v-slot="{ meta }" :validation-schema="schema" @submit="onSubmit">
          <label class="block text-sm text-gray-900" for="file_input"
            >Select a photo of a 3D print job:</label
          >
          <input
            id="file_input"
            class="p-1 mt-1 block w-full text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-400 focus:outline-none"
            aria-describedby="file_input_help"
            type="file"
            accept="image/png, image/jpeg"
            @change="onChangeFile"
          />
          <hr class="w-64 h-px my-8 mx-auto bg-gray-200 border-0" />
          <label for="email" class="block text-sm text-gray-900"
            >We'll email your results:</label
          >
          <Field
            id="email"
            name="email"
            type="email"
            autocomplete="email"
            class="appearance-none mt-1 relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"
            placeholder="Email address"
            rules="required"
          />
          <error-message
            class="text-red-500 text-sm"
            name="email"
          ></error-message>

          <button
            id="email-submit"
            :disabled="state.loading || !meta.valid || file === undefined"
            type="submit"
            class="group mt-2 relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 disabled:opacity-25"
          >
            <span class="absolute left-0 inset-y-0 flex items-center pl-3">
              <ArrowPathIcon
                v-if="state.loading"
                class="animate-spin h-5 w-5 text-white"
                aria-hidden="true"
              />
            </span>
            Get Results
          </button>
        </Form>
      </transition>
    </div>
  </div>
</template>
