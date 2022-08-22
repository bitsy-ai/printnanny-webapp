<script setup lang="ts">
import { ref } from "vue";
import { useRouter } from "vue-router";
import { Field, ErrorMessage } from "vee-validate";
import { PiCreateWizardSteps } from "../piCreateWizard";
import { useForm } from "vee-validate";
import WizardButtons from "@/components/wizard/steps/WizardButtons.vue";

const step = PiCreateWizardSteps()[1];
const router = useRouter();

const formData = ref({});
// vee-validate will be aware of computed schema changes
const { resetForm, handleSubmit } = useForm({
  validationSchema: step.validationSchema,
});
const onSubmit = handleSubmit(async (values) => {
  console.log("values submitted");
  formData.value = {
    ...formData.value,
    ...values,
  };

  // Sets initial values for the values already filled
  // effectively fills the inputs when clicking on "previous"
  resetForm({
    values: {
      ...formData.value,
    },
  });
  if (step.nextButton && step.nextButton.onSubmit) {
    await step.nextButton?.onSubmit(formData.value);
  }

  const link = step.nextButton?.link();
  if (link) {
    await router.push(link);
  }
});
</script>
<template>
  <div
    class="min-h-full flex items-center justify-center py-12 px-4 sm:px-6 lg:px-8 bg-indigo-20 flex-wrap"
  >
    <!-- main component -->
    <div class="w-full m-auto justify-center flex-1">
      <form @submit.prevent="onSubmit">
        <h2 class="text-2xl font-bold leading-7 text-gray-900 sm:text-3xl">
          {{ step.title }}
        </h2>
        <p class="text-base font-medium text-gray-900 mt-5 w-full">
          {{ step.detail }}
        </p>
        <!-- hostname fieldset -->
        <fieldset class="mt-6">
          <legend class="text-base font-medium text-gray-900">
            1) What is the hostname of your Raspberry Pi?
          </legend>
          <error-message class="text-red-500" name="hostname"></error-message>
          <Field
            id="hostname"
            name="hostname"
            type="input"
            class="md:w-2/3 appearance-none rounded-md relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"
            placeholder="Hostname"
            rules="required"
          />
          <small
            >Please enter the hostname you set in the Raspberry Pi Imager's
            Advanced Options menu (without .local extension)</small
          >
          <img
            class="w-full md:w-2/3"
            src="@/assets/images/onboarding/raspberry-pi-imager-hostname.png"
            alt="Screenshot of Raspberry Pi Imager showing hostname field highlighted"
          />
        </fieldset>

        <hr class="m-5" />
        <fieldset class="mt-6">
          <legend class="text-base font-medium text-gray-900">
            2) Choose PrintNanny OS Edition
          </legend>
          <p class="text-sm text-gray-500 mt-2">
            <a
              target="_blank"
              href="https://docs.printnanny.ai/docs/quick-start/choose-os-edition/"
              class="focus:ring-indigo-500 h-4 w-4 text-indigo-600 border-gray-300"
            >
              Click to learn more
            </a>
            about each edition.
          </p>
          <div class="mt-4 space-y-4">
            <div class="flex items-center">
              <Field
                id="edition"
                name="edition"
                type="radio"
                value="octoprint_lite"
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
          <p class="text-sm text-gray-500 mt-2">
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
                value="rpi_4"
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

        <!-- footer buttons -->
        <div class="w-full m-auto justify-center flex-1">
          <WizardButtons :current-step="step" />
        </div>
      </form>
    </div>
  </div>
</template>
