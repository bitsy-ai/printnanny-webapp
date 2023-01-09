<script setup lang="ts">
import { onMounted, ref } from "vue";
import * as api from "printnanny-api-client";
import * as yup from "yup";
import { Form, Field } from "vee-validate";
import type { UiAlert } from "@/types";
import FadeOutIn from "@/components/transitions/FadeOutIn.vue";
import { useDeviceStore } from "@/stores/devices";
import { useAlertStore } from "@/stores/alerts";
import TextSpinner from "@/components/util/TextSpinner.vue";

const alertStore = useAlertStore();
const store = useDeviceStore();
await store.fetchNetworkSettings();

const savingForm = ref(false);

const validationSchema = yup.object({
  preferred_dns: yup.string(),
});

const preferredDNSFieldset = [
  {
    value: api.PreferredDnsType.Multicast,
    label: "Multicast DNS (mDNS)",
    display: "Your Raspberry Pis will be discoverable using .local domain.",
  },
  {
    value: api.PreferredDnsType.Tailscale,
    label: "Tailscale DNS",
    display: "Requires Tailscale to be enabled on your Raspberry Pi.",
  },
];

async function onSubmit(values) {
  savingForm.value = true;
  console.log("received form values", values);
  await store.saveNetworkSettings(values as api.PatchedNetworkSettingsRequest);
  const success = {
    color: "green",
    message: "Saved network settings",
    header: "Success!",
    actions: [],
    error: undefined,
  } as UiAlert;
  alertStore.push(success);
  savingForm.value = false;
}
</script>
<template>
  <Form
    class="space-y-8 divide-y divide-gray-200"
    :initial-values="store.networkSettings"
    :validation-schema="validationSchema"
    @submit="onSubmit"
  >
    <div class="space-y-8 divide-y divide-gray-200">
      <div>
        <div>
          <h3 class="text-lg leading-6 font-medium text-gray-900">
            Network Settings
          </h3>
          <p class="mt-1 text-sm text-gray-500">
            These settings are related to how you connect to you Raspberry Pi.
          </p>
        </div>
      </div>

      <div class="pt-8">
        <div>
          <h3 class="text-lg leading-6 font-medium text-gray-900">
            Hostname & DNS
          </h3>
          <p class="mt-1 text-sm text-gray-500">
            Choose your preferred method for DNS.
          </p>
        </div>
        <div class="mt-6">
          <fieldset>
            <legend class="sr-only">DNS Method</legend>
            <div class="text-base font-medium text-gray-900" aria-hidden="true">
              DNS Method
            </div>
            <div class="mt-4 space-y-4">
              <div
                v-for="(option, index) in preferredDNSFieldset"
                :key="index"
                class="relative flex items-start"
              >
                <div class="flex items-center h-5">
                  <Field
                    :id="option.value"
                    :value="option.value"
                    name="preferred_dns"
                    type="checkbox"
                    class="focus:ring-indigo-500 h-4 w-4 text-indigo-600 border-gray-300 rounded"
                  />
                </div>
                <div class="ml-3 text-sm">
                  <label :for="option.value" class="font-medium text-gray-700"
                    >{{ option.label }} <br /><span
                      class="text-sm text-gray-500"
                      >{{ option.display }}</span
                    >
                  </label>
                </div>
              </div>
            </div>
          </fieldset>
        </div>
      </div>
    </div>

    <div class="pt-5 pb-5">
      <div class="flex justify-end">
        <TextSpinner v-if="savingForm" text="Saving..." class="mr-2" />
        <button
          type="reset"
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
  </Form>
</template>
