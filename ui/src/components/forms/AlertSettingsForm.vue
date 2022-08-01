<script setup lang="ts">
import { Suspense } from "vue";
import { useAlertStore } from "@/stores/alerts";
import * as api from "printnanny-api-client";
import * as yup from "yup";
import { useForm, Field } from "vee-validate";
import type { UiAlert } from "@/types";

const alertStore = useAlertStore();
const initialValues = await alertStore.fetchEmailAlertSettings();

console.log("initialValues", initialValues)

const validationSchema = yup.object({
  enabled: yup.boolean(),
  event_types: yup.array().of(yup.string()),
  progress_percent: yup.number().min(1).max(99),
});

const { resetForm, handleSubmit } = useForm({
  validationSchema: validationSchema,
  initialValues: initialValues
});

const alertSettingsFieldset = {
  event_types: [
    {
      value: api.EventTypesEnum.PrintQuality,
      display: "Quality control alerts",
    },
    {
      value: api.EventTypesEnum.PrintStarted,
      display: "Triggered on print job start",
    },
    {
      value: api.EventTypesEnum.PrintDone,
      display: "Triggered when print job is done",
    },
    {
      value: api.EventTypesEnum.PrintProgress,
      display: "Triggered when print job progress reaches %percent",
    },

    {
      value: api.EventTypesEnum.PrintPaused,
      display: "Triggered when print job is paused",
    },

    {
      value: api.EventTypesEnum.PrintCancelled,
      display: "Triggered when print job is cancelled",
    },
  ],
};

const onSubmit = handleSubmit(async (values) => {
  console.log("received form values", values);
  await alertStore.updateEmailAlertSettings(values);
  const success = {color: "green", message: "Saved email notification settings", header: "Success!"} as UiAlert;
  alertStore.push(success)
});
</script>
<template>
    <!-- Suspense: loaded settings from remote -->
    <form
      class="space-y-8 divide-y divide-gray-200"
      @submit="onSubmit"
    >
      <div class="space-y-8 divide-y divide-gray-200">
        <div>
          <div>
            <h3 class="text-lg leading-6 font-medium text-gray-900">
              Email Notifications
            </h3>
            <p class="mt-1 text-sm text-gray-500">
              These settings control the kind of email notifications you will
              receive.
            </p>
          </div>
        </div>

        <div class="pt-8">
          <div>
            <h3 class="text-lg leading-6 font-medium text-gray-900">
              Print Status & Quality Control
            </h3>
            <p class="mt-1 text-sm text-gray-500">
              Pick the notifications you want to receive.
            </p>
          </div>
          <div class="mt-6">
            <fieldset>
              <legend class="sr-only">Printer Alerts</legend>
              <div class="text-base font-medium text-gray-900" aria-hidden="true">
                Printer Alerts
              </div>
              <div class="mt-4 space-y-4">
                <div
                  v-for="(option, index) in alertSettingsFieldset.event_types"
                  :key="index"
                  class="relative flex items-start"
                >
                  <div class="flex items-center h-5">
                    <Field
                      :id="option.value"

                      :value="option.value"
                      name="event_types"
                      type="checkbox"
                      class="focus:ring-indigo-500 h-4 w-4 text-indigo-600 border-gray-300 rounded"
                    />
                  </div>
                  <div class="ml-3 text-sm">
                    <label :for="option.value" class="font-medium text-gray-700"
                      >{{ option.value }} <br /><span
                        class="text-sm text-gray-500"
                        >{{ option.display }}</span
                      >
                    </label>
                  </div>
                </div>
              </div>

              <div class="mt-6 grid grid-cols-1 gap-y-6 gap-x-4 sm:grid-cols-6">
                <div class="sm:col-span-3">
                  <label
                    for="print-progress"
                    class="block text-sm font-medium text-gray-700"
                    >Print progress notification interval</label
                  >
                  <div class="mt-1">
                    <Field
                      type="number"
                      :value="alertStore.emailAlertSettings?.progress_percent"
                      name="print-progress"
                      class="shadow-sm focus:ring-indigo-500 focus:border-indigo-500 block w-full sm:text-sm border-gray-300 rounded-md"
                    />
                    <small
                      >Example: 25 will notify you at 25%, 50%, 75%, and 100%
                      progress</small
                    >
                  </div>
                </div>
              </div>
            </fieldset>
          </div>
        </div>
      </div>

      <div class="pt-5 pb-5">
        <div class="flex justify-end">
          <button
            type="button"
            :click="resetForm"
            class="bg-white py-2 px-4 border border-gray-300 rounded-md shadow-sm text-sm font-medium text-gray-700 hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
          >
            Cancel
          </button>
          <button
            type="submit"
            class="ml-3 inline-flex justify-center py-2 px-4 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
          >
            Save
          </button>
        </div>
      </div>
    </form>
</template>
