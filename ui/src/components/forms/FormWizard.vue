<template>
  <form @submit="onSubmit">
    <slot />

    <div>
      <button v-if="hasPrevious" type="button" @click="goToPrev">
        Previous
      </button>
      <button type="submit">{{ isLastStep ? "Submit" : "Next" }}</button>
    </div>
  </form>
</template>

<script lang="ts">
import { useForm } from "vee-validate";
import { ref, computed, provide } from "vue";

export default {
  name: "FormWizard",
  emits: ["next", "submit"],
  props: {
    validationSchema: {
      type: Array,
      required: true,
    },
  },
  setup(props, { emit }) {
    const formData = ref({});
    const currentStepIdx = ref(0);

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
        emit("next", formData.value);

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

    return {
      onSubmit,
      hasPrevious,
      isLastStep,
      goToPrev,
    };
  },
};
</script>
