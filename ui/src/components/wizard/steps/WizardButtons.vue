

<script setup lang="ts">
import { PropType } from "vue";
import CustomSpinner from "@/components/util/CustomSpinner.vue";
import { useWizardStore } from '@/stores/wizard';
import type { WizardStep } from "@/types";

const props = defineProps({
    currentStep: {
        type: Object as PropType<WizardStep>,
        required: true
    }
})
const store = useWizardStore();

</script>
<template>
    <div class="text-center">
    <button
        v-if="currentStep?.nextButton?.onSubmit !== undefined"
        :disabled="store.loading"
        class="inline-flex items-center group m-2 relative w-1/2 justify-center py-3 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 disabled:cursor-not-allowed disabled: disabled:opacity-75"
        type="submit"
        >
    <CustomSpinner
        v-if="store.loading"
        color="indigo"
        text="Processing..."
    ></CustomSpinner>
    <span v-else>{{ currentStep?.nextButton?.text }}</span>
    </button>
    <router-link
    v-else-if="currentStep?.nextButton?.link !== undefined"
    :to="currentStep?.nextButton?.link()"
    >        
        <button
        :disabled="store.loading"
        class="inline-flex items-center group m-2 relative w-1/2 justify-center py-3 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 disabled:cursor-not-allowed disabled: disabled:opacity-75"
        >
    <CustomSpinner
        v-if="store.loading"
        color="indigo"
        text="Processing..."
    ></CustomSpinner>
    <span v-else>{{ currentStep?.nextButton?.text }}</span>
    </button>
    </router-link>
      
    <router-link
    v-if="currentStep?.prevButton"
    :to="currentStep?.prevButton?.link()"
    >
    <button
        type="button"
        class="group m-2 relative w-1/2 justify-center py-3 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-gray-600 hover:bg-gray-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 disabled:opacity-25"
    >
        {{ currentStep?.prevButton?.text }}
    </button>
    </router-link>
</div>
</template>