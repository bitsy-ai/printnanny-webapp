<script setup lang="ts">
import { useForm } from "vee-validate";
import type { PropType, ComputedRef } from 'vue';
import { ref, computed, provide, toRef } from "vue";
import { RefreshIcon } from "@heroicons/vue/solid";

import { useWizardStore } from "@/stores/wizard";
import type { WizardButton, WizardStep } from "@/types";
import { AnyObjectSchema } from "yup";

const store = useWizardStore();

const props = defineProps({
  steps: {
    type: Object as PropType<Array<WizardStep>>,
    required: true
  },
  currentStepIdx: {
    type: Number,
    default: 0
  }
});

const emit = defineEmits(["next", "submit"]);

const formData = ref({});
const currentStepIdx = ref(props.currentStepIdx);

// // Injects the starting step, child <form-steps> will use this to generate their ids
const stepCounter = ref(0);
provide("STEP_COUNTER", stepCounter);
// Inject the live ref of the current index to child components
// will be used to toggle each form-step visibility
provide("CURRENT_STEP_INDEX", currentStepIdx);

// if this is the last step
const isLastStep = computed(() => {
  return currentStepIdx.value === props.steps.length - 1;
});

const currentStep: ComputedRef<WizardStep> = computed(() => {
  return props.steps[currentStepIdx.value]
})

// If the `previous` button should appear
const hasPrevious = computed(() => {
  return currentStepIdx.value > 0;
});

// extracts the indivdual step schema
const currentSchema = computed(() => {
  return currentStep.value.validationSchema;
});

// vee-validate will be aware of computed schema changes
const { resetForm, handleSubmit } = useForm({
  validationSchema: currentStep.value.validationSchema
});

// We are using the "submit" handler to progress to next steps
// and to submit the form if its the last step
// parent can opt to listen to either events if interested
const onSubmit = handleSubmit(async (values) => {
  console.log("values submitted")
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
  await currentStep.value.onSubmit(formData.value)

  currentStepIdx.value++;
});

function goToPrev() {
  if (currentStepIdx.value === 0) {
    return;
  }

  currentStepIdx.value--;
  resetForm({
    values: {
      ...formData.value,
    },
  });
}
</script>
<template>
  <form @submit="onSubmit">
    <slot />

    <div class="text-center">
      <button
        :disabled="currentStep?.nextButton.disabled.value"
        class="group m-2 relative w-1/2 justify-center py-3 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 disabled:opacity-25"
        type="submit"
      >
        <span class="absolute left-0 inset-y-0 flex items-center pl-3">
          <RefreshIcon
            v-if="store.loading"
            class="animate-spin h-5 w-5 text-indigo-500 group-hover:text-indigo-400"
            :aria-hidden="true"
          />
        </span>
        {{ currentStep?.nextButton.text }}
      </button>
      <button
        v-if="hasPrevious"
        :disabled="store.loading"
        type="button"
        class="group m-2 relative w-1/2 justify-center py-3 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-gray-600 hover:bg-gray-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 disabled:opacity-25"
        @click="goToPrev"
      >
        {{ currentStep?.prevButton.text }}
      </button>
    </div>
  </form>
</template>
