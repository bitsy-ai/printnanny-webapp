<script setup lang="ts">
import { onBeforeRouteLeave } from "vue-router";
import { RouterLink } from "vue-router";
import { PiCreateWizardSteps } from "../piCreateWizard";
import { useWizardStore } from "@/stores/wizard";
import { ExternalLinkIcon } from "@heroicons/vue/solid";
import { HomeIcon } from "@heroicons/vue/outline";
const step = PiCreateWizardSteps()[4];
const store = useWizardStore();

const props = defineProps({
  piId: {
    type: String,
    required: true,
    icon: ExternalLinkIcon,
  },
});

await store.loadPi(parseInt(props.piId));
await store.finishSetup(parseInt(props.piId));

onBeforeRouteLeave((to, from) => {
  console.log("onBeforeRouteLeave hook", to, from);
  store.$reset();
});
</script>
<template>
  <div
    class="min-h-full flex items-center justify-center py-12 px-4 sm:px-6 lg:px-8 bg-indigo-20 flex-wrap"
  >
    <h2
      class="text-2xl font-bold leading-7 text-gray-900 sm:text-3xl flex-1 w-full text-center"
    >
      {{ step.title }}
    </h2>
    <p class="text-base text-center font-medium text-gray-900 mt-5 w-full">
      {{ step.detail }}
    </p>

    <div
      class="grow min-w-full flex items-center justify-center py-12 px-4 sm:px-6 lg:px-8 bg-indigo-20 flex-wrap text-center"
    >
      <!-- action buttons -->
      <div class="w-full m-auto justify-center flex-1">
        <!-- back to devices -->
        <RouterLink :to="{ name: 'devices' }">
          <button
            class="inline-flex items-center group m-2 relative w-1/4 justify-center py-3 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 disabled:cursor-not-allowed disabled: disabled:opacity-75"
          >
            <HomeIcon class="h-5 w-5 text-white" aria-hidden="true" />
            &nbsp;&nbsp; Return to My Network
          </button>
        </RouterLink>

        <!-- octoprint button -->
        <a :href="store.pi?.urls.octoprint" target="_blank">
          <button
            class="inline-flex items-center group m-2 relative w-1/4 justify-center py-3 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-emerald-600 hover:bg-emerald-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-emerald-500 disabled:cursor-not-allowed disabled: disabled:opacity-75"
          >
            <ExternalLinkIcon class="h-5 w-5 text-white" aria-hidden="true" />
            &nbsp;&nbsp; Open OctoPrint
          </button>
        </a>
      </div>
    </div>
  </div>
</template>
