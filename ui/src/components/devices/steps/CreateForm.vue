<script setup lang="ts">
import { RefreshIcon } from "@heroicons/vue/solid";
import { Field, ErrorMessage, Form } from "vee-validate";
import { ref, reactive } from "vue";
import * as yup from "yup";
import { useDeviceStore } from "@/stores/devices";
import { useRouter } from "vue-router";

const router = useRouter();
const deviceStore = useDeviceStore();
const loading = ref(false);
const state = reactive({
  loading,
});

// define a validation schema
const schema = yup.object({
  hostname: yup.string().required(),
});

async function onSubmit(values: any) {
  state.loading = true;
  await deviceStore.create(values.hostname);
  state.loading = true;
  await router.push({ name: "devices" });
}
</script>

<template>
  <div
    class="min-h-full flex items-center justify-center py-12 px-4 sm:px-6 lg:px-8 bg-indigo-20 flex-wrap"
  >
    <h2 class="text-2xl font-bold leading-7 text-gray-900 sm:text-3xl">
      Connect New Device
    </h2>

    <Form v-slot="{ valid }" :validation-schema="schema" @submit="onSubmit">
      <fieldset class="mt-6">
        <legend class="text-base font-medium text-gray-900">
          1) What is the hostname of your Raspberry Pi?
        </legend>
        <error-message class="text-red-500" name="hostname"></error-message>
        <Field
          id="hostname"
          name="hostname"
          type="input"
          class="appearance-none rounded-md relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"
          placeholder="Hostname"
          rules="required"
        />
        <small
          >Please enter the hostname you set in the Raspberry Pi Imager's
          Advanced Options menu (without .local extension)</small
        >
        <img
          class="w-full"
          src="@/assets/images/onboarding/raspberry-pi-imager-hostname.png"
          alt="Screenshot of Raspberry Pi Imager showing hostname field highlighted"
        />
      </fieldset>

      <hr class="m-5" />
      <fieldset class="mt-6">
        <legend class="text-base font-medium text-gray-900">
          2) Choose PrintNanny OS Edition
        </legend>
        <p class="text-sm text-gray-500">
          <a
            target="_blank"
            href="https://docs.printnanny.ai/docs/quick-start/choose-os-edition/"
            class="focus:ring-indigo-500 h-4 w-4 text-indigo-600 border-gray-300"
          >
            Click to learn more
          </a>
          about what's inside each edition.
        </p>
        <div class="mt-4 space-y-4">
          <div class="flex items-center">
            <Field
              id="edition"
              name="edition"
              type="radio"
              value="OCTOPRINT_LITE"
              required
              class="focus:ring-indigo-500 h-4 w-4 text-indigo-600 border-gray-300"
            />
            <label for="edition" class="ml-3">
              <span class="block text-sm font-medium text-gray-700"
                >OctoPrint Lite</span
              >
            </label>
          </div>
        </div>
      </fieldset>
      <hr class="m-5" />

      <fieldset class="mt-6">
        <legend class="text-base font-medium text-gray-900">
          3) Choose hardware
        </legend>
        <p class="text-sm text-gray-500">
          Which Raspberry Pi board are you using?
          <a
            target="_blank"
            href="https://github.com/bitsy-ai/printnanny-os/issues?q=is%3Aissue+is%3Aopen+label%3Araspberrypi3"
            class="focus:ring-indigo-500 h-4 w-4 text-indigo-600 border-gray-300"
          >
            Click see progress towards other boards.
          </a>
        </p>
        <div class="mt-4 space-y-4">
          <div class="flex items-center">
            <Field
              id="sbc"
              name="sbc"
              type="radio"
              value="rpi4"
              required
              class="focus:ring-indigo-500 h-4 w-4 text-indigo-600 border-gray-300"
            />
            <label for="edition" class="ml-3">
              <span class="block text-sm font-medium text-gray-700"
                >Raspberry Pi 4</span
              >
            </label>
          </div>
        </div>
      </fieldset>
      <hr class="m-5" />
    </Form>
  </div>
</template>
