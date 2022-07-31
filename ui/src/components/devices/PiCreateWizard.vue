<template>
  <div class="w-1/2 m-auto">
    <div class="relative pt-4">
      <div class="flex mb-2 items-center justify-between">
        <div>
          <span
            class="text-xs font-semibold inline-block py-1 px-2 uppercase rounded-full text-indigo-600 bg-indigo-200"
          >
            {{ steps[currentStep].label }}
          </span>
        </div>
        <div class="text-right">
          <span class="text-xs font-semibold inline-block text-indigo-600">
            {{ steps[currentStep].progress }} completed
          </span>
        </div>
      </div>
      <div class="overflow-hidden h-2 mb-4 text-xs flex rounded bg-indigo-200">
        <div
          :style="steps[currentStep].style"
          class="shadow-none flex flex-col text-center whitespace-nowrap text-white justify-center bg-indigo-500"
        ></div>
      </div>
    </div>
    <div>
      <component
        :is="steps[currentStep].component"
        @formValueChange="updateFormValue"
      />
      <div class="text-center">
        <button
          v-if="currentStep < steps.length - 1"
          :disabled="!formValue[steps[currentStep].key].valid"
          class="group m-2 relative w-1/2 justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 disabled:opacity-25"
          @click="next"
        >
          <span
            class="absolute left-0 inset-y-0 flex items-center pl-3 text-white"
          >
            <ArrowCircleRightIcon
              class="h-5 w-5 text-white"
              :aria-hidden="true"
            />
          </span>
          Next: {{ steps[currentStep + 1].label }}
        </button>

        <button
          v-if="currentStep !== 0"
          class="group m-2 relative w-1/2 justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-amber-600 hover:bg-amber-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 disabled:opacity-25"
          @click="previous"
        >
          <span
            class="absolute left-0 inset-y-0 flex items-center pl-3 text-white"
          >
            <ArrowCircleLeftIcon
              class="h-5 w-5 text-white"
              :aria-hidden="true"
            />
          </span>
          Previous: {{ steps[currentStep - 1].label }}
        </button>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";
import CreateForm from "./steps/CreateForm.vue";
import InstallGuide from "./steps/InstallGuide.vue";
import TestConnection from "./steps/TestConnection.vue";
import {
  ArrowCircleLeftIcon,
  ArrowCircleRightIcon,
} from "@heroicons/vue/solid";

const currentStep = ref(0);
const formSubmitted = ref(false);
const formValue = ref({
  connect: { fields: {}, valid: false },
  install: { fields: {}, valid: true },
  test: { fields: {}, valid: false },
});

const steps = [
  {
    component: InstallGuide,
    key: "install",
    label: "Burn PrintNanny OS Image",
    progress: "33%",
    style: "width: 0%",
  },
  {
    component: CreateForm,
    key: "connect",
    label: "Connect New Device",
    progress: "0%",
    style: "width: 33%",
  },
  {
    component: TestConnection,
    key: "test",
    label: "Test Connection",
    progress: "66%",
    style: "width: 66%",
  },
];

function next() {
  currentStep.value += 1;
}

function previous() {
  currentStep.value -= 1;
}

function updateFormValue(payload) {}

function submit() {}
</script>
