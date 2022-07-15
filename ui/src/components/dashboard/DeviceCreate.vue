<script setup lang="ts">
import { RefreshIcon} from "@heroicons/vue/solid";
import { useForm, useField, Field, ErrorMessage, Form } from "vee-validate";
import { ref, reactive } from "vue";
import * as yup from "yup";
import { useDeviceStore } from "@/stores/devices";

const deviceStore = useDeviceStore();
const loading = ref(false);
const state = reactive({
  loading
});

// define a validation schema
const schema = yup.object({
  hostname: yup.string().required(),
});

async function onSubmit(values: any){
    state.loading = true;
    await deviceStore.create(values.hostname);
    state.loading = true;
    await deviceStore.router.push({name: "dashboard"});
}
</script>

<template>
<div class="min-h-full flex items-center justify-center py-12 px-4 sm:px-6 lg:px-8 bg-indigo-20 flex-wrap">
    <Form @submit="onSubmit" v-slot="{ meta }" :validation-schema="schema">
        <label for="hostname" class="sr-only">Hostname</label>
        <error-message className="text-red-500" name="hostname"></error-message>
        <Field
          name="hostname"
          id="hostname"
          type="input"
          className="appearance-none rounded-md relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"
          placeholder="Hostname"
          rules="required"
        />
        <small>Please enter the hostname you set in the Raspberry Pi Imager's Advanced Options menu (without .local extension)</small>

        <button
          :disabled="state.loading || !meta.valid"
          type="submit"
          class="group mt-2 relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 disabled:opacity-25"
        >
          <span class="absolute left-0 inset-y-0 flex items-center pl-3">
            <RefreshIcon
              v-if="state.loading"
              class="animate-spin h-5 w-5 text-indigo-500 group-hover:text-indigo-400"
              aria-hidden="true"
            />
          </span>
          Save
        </button>
    </Form>
    <img class="w-full" src="@/assets/images/onboarding/raspberry-pi-imager-hostname.png" alt="Screenshot of Raspberry Pi Imager showing hostname field highlighted"/>
</div>
</template>