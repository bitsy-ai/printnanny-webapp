<script setup lang="ts">
import { useForm } from "vee-validate";
import { ref, computed, provide, toRef } from "vue";
import { RefreshIcon } from "@heroicons/vue/solid";

const props = defineProps({
  validationSchema: {
    type: Array,
    required: true,
  },
  buttonText: {
    type: Array,
    required: true,
  },
  loading: {
    type: Boolean,
    default: false,
  },
  currentStepIdx: {
    type: Number,
    default: 0
  }
});

const emit = defineEmits(["next", "submit"]);

const formData = ref({});
const currentStepIdx = ref(props.currentStepIdx);

// Injects the starting step, child <form-steps> will use this to generate their ids
const stepCounter = ref(0);
provide("STEP_COUNTER", stepCounter);
// Inject the live ref of the current index to child components
// will be used to toggle each form-step visibility
provide("CURRENT_STEP_INDEX", currentStepIdx);

// if this is the last step
const isLastStep = computed(() => {
  return currentStepIdx.value === stepCounter.value - 1;
});

// If the `previous` button should appear
const hasPrevious = computed(() => {
  return currentStepIdx.value > 0;
});

// extracts the indivdual step schema
const currentSchema = computed(() => {
  return props.validationSchema[currentStepIdx.value];
});

const nextButton = computed(() => {
  return props.buttonText[currentStepIdx.value][1];
});

const prevButton = computed(() => {
  return props.buttonText[currentStepIdx.value][0];
});

// vee-validate will be aware of computed schema changes
const { resetForm, handleSubmit } = useForm({
  validationSchema: currentSchema,
});

// We are using the "submit" handler to progress to next steps
// and to submit the form if its the last step
// parent can opt to listen to either events if interested
const onSubmit = handleSubmit((values) => {
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

  if (!isLastStep.value) {
    currentStepIdx.value++;
    emit("next", currentStepIdx.value, formData.value);

    return;
  }

  emit("submit", formData.value);
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
        :disabled="loading"
        class="group m-2 relative w-1/2 justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 disabled:opacity-25"
        type="submit"
      >
        <span class="absolute left-0 inset-y-0 flex items-center pl-3">
          <RefreshIcon
            v-if="loading"
            class="animate-spin h-5 w-5 text-indigo-500 group-hover:text-indigo-400"
            :aria-hidden="true"
          />
        </span>
        {{ nextButton }}
      </button>
      <button
        v-if="hasPrevious"
        :disabled="loading"
        type="button"
        class="group m-2 relative w-1/2 justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-gray-600 hover:bg-gray-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 disabled:opacity-25"
        @click="goToPrev"
      >
        {{ prevButton }}
      </button>
    </div>
  </form>
</template>
