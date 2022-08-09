<script setup lang="ts">
import moment from "moment";
import FormStep from "./FormStep.vue";
import { useRouter } from "vue-router";
import { ref } from 'vue';
import type { PropType } from "vue";
import { useWizardStore } from "@/stores/wizard";
import type { WizardStep } from "@/types";
import { ThumbUpIcon, UserIcon, CheckIcon, MoonIcon, InformationCircleIcon } from "@heroicons/vue/outline";
import CustomSpinner from "@/components/util/CustomSpinner.vue";
import { ExclamationCircleIcon, FolderDownloadIcon } from "@heroicons/vue/solid";
import { ConnectTestStep, ConnectTestStatus, ManualTestStep } from "@/types";
import * as api from "printnanny-api-client";

const props = defineProps({
  step: {
    type: Object as PropType<WizardStep>,
    required: true,
  },
});

const store = useWizardStore();
const router = useRouter();


const manualSteps = ref([
  new ManualTestStep("Download PrintNanny.zip (your license key)", "Do not share contents with anyone!", FolderDownloadIcon),
]);

if (router.currentRoute.value.params.piId !== undefined && router.currentRoute.value.params.activeStep === props.step.key){
  const piId = parseInt(router.currentRoute.value.params.piId as string)
  store.connectNats(piId);
  store.downloadLicenseZip(piId);
  manualSteps.value[0].start();
  // set href & activate license download step
}

store.$subscribe((mutation, state) => {
  if (state.downloadUrl !== undefined){
    manualSteps.value[0].extraButtonhHref = state.downloadUrl;
    manualSteps.value[0].extraButtonText = "Download PrintNanny.zip";
  }
})


const testConnectSteps = [
  new ConnectTestStep("Power On",(event: api.PolymorphicPiEventRequest) => {}),
  new ConnectTestStep("Sync Settings",(event: api.PolymorphicPiEventRequest) => {}),
  new ConnectTestStep("Run Remote Command",(event: api.PolymorphicPiEventRequest) => {}),
  new ConnectTestStep("Turn on Camera",(event: api.PolymorphicPiEventRequest) => {}),

];
store.$patch({ testConnectSteps });
// store.startTest();



</script>

<template>
  <FormStep :name="step.key">
      <h2
        class="text-2xl font-bold leading-7 text-gray-900 sm:text-3xl flex-1 w-full text-center"
      >
        {{ step.title }}
      </h2>
      <p class="text-base font-medium text-gray-900 mt-5 w-full">
        {{ step.detail }}
      </p>
    <div
      class="min-h-full flex items-center justify-center py-12 px-4 sm:px-6 lg:px-8 bg-indigo-20 flex-wrap text-center"
    >
      <!-- test steps container -->
      <div class="flow-root">
        <ul role="list" class="-mb-8">
          <!-- manual setup/test steps where user confirms they are done -->
          <li v-for="(step, stepIdx) in manualSteps" :key="stepIdx">
            <div class="relative pb-8">
              <span
                class="absolute top-4 left-4 -ml-px h-full w-0.5 bg-gray-200"
                aria-hidden="true"
              />
              <div class="relative flex space-x-3">
                <div>
                  <span
                    :class="[
                      step.iconBackground(),
                      'h-8 w-8 rounded-full flex items-center justify-center ring-8 ring-white',
                    ]"
                  >
                    <component
                      :is="step.icon"
                      class="h-5 w-5 text-white"
                      aria-hidden="true"
                      v-if="step.active"
                    />
                    <component
                      :is="step.icon"
                      class="h-5 w-5 text-white"
                      aria-hidden="true"
                      v-if="!step.active"
                    />
                  </span>
                </div>
                <div
                  class="min-w-0 flex-1 pt-1.5 flex justify-between space-x-24"
                >
                  <div>
                    <p class="text-sm text-gray-500 text-left">
                      <strong>{{ step.text }}</strong>
                      <br>
                      <i>{{ step.detail }}</i>
                    </p>
                  </div>
                  <div
                    class="text-right text-sm whitespace-nowrap text-gray-500"
                  >
                    <a v-if="step.extraButtonhHref !== undefined" :href="step.extraButtonhHref" target="_blank">
                      <button         
                        @click="step.finished()"
                        :class="[
                          step.extraButtonBackground(),
                        'inline-flex items-center group m-2 relative justify-center py-3 px-4 border border-transparent text-sm font-medium rounded-md text-white',
                        ]">
                        <component
                          :is="step.icon"
                          class="h-5 w-5 mr-2 text-white"
                          aria-hidden="true"
                        />
                        {{ step.extraButtonText }}
                      </button>
                    </a>
                  </div>
                </div>
              </div>
            </div>
          </li>

          <!-- event-based connection tests -->
          <li v-for="(step, stepIdx) in testConnectSteps" :key="stepIdx">
            <div class="relative pb-8">
              <span
                v-if="stepIdx !== testConnectSteps.length - 1"
                class="absolute top-4 left-4 -ml-px h-full w-0.5 bg-gray-200"
                aria-hidden="true"
              />
              <div class="relative flex space-x-3">
                <div>
                  <span
                    :class="[
                      step.statusComponent().iconBackground,
                      'h-8 w-8 rounded-full flex items-center justify-center ring-8 ring-white',
                    ]"
                  >
                    <component
                      :is="step.statusComponent().icon"
                      class="h-5 w-5 text-white"
                      aria-hidden="true"
                      v-if="!step.active()"
                    />
                    <component
                      :is="step.statusComponent().icon"
                      text=""
                      width="w-8"
                      height="w-8"

                      aria-hidden="true"
                      v-if="step.active()"
                    />
                  </span>
                </div>
                <div
                  class="min-w-0 flex-1 pt-1.5 flex justify-between space-x-24"
                >
                  <div>
                    <p class="text-sm text-gray-500 text-left">
                      <strong>{{ step.content }}</strong>
                      <br>
                      <i>{{ step.statusText() }}</i>
                    </p>
                  </div>
                  <div
                    class="text-right text-sm whitespace-nowrap text-gray-500"
                  >
                    {{ step.statusComponent().text }}
                    <br>
                    <time v-if="step.status == ConnectTestStatus.Pending" :datetime="step.start_dt.format()" ><i>{{ step.start_dt.fromNow() }}</i></time>
                  </div>
                </div>
              </div>
            </div>
          </li>
        </ul>
      </div>
    </div>
  </FormStep>
</template>
