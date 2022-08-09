<script setup lang="ts">
import moment from "moment";
import FormStep from "./FormStep.vue";
import { useRouter } from "vue-router";
import { ref, computed } from "vue";
import type { PropType } from "vue";
import { useWizardStore } from "@/stores/wizard";
import type { WizardStep } from "@/types";
import {
  ThumbUpIcon,
  UserIcon,
  CheckIcon,
  MoonIcon,
  InformationCircleIcon,
  ClipboardCopyIcon,
  QuestionMarkCircleIcon,
  ChipIcon,
} from "@heroicons/vue/outline";
import CustomSpinner from "@/components/util/CustomSpinner.vue";
import {
  ExclamationCircleIcon,
  FolderDownloadIcon,
} from "@heroicons/vue/solid";
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

if (
  router.currentRoute.value.params.piId !== undefined &&
  router.currentRoute.value.params.activeStep === props.step.key
) {
  const piId = parseInt(router.currentRoute.value.params.piId as string);
  await store.loadPi(piId);
  store.connectNats(piId);
}

const connectTestSteps = [
  new ConnectTestStep("Power On", (event: api.PolymorphicPiEventRequest, currentStep: ConnectTestStep, nextStep: undefined | ConnectTestStep) => {
    console.log("callback event", event);
    console.log("callback currentStep", currentStep);
    console.log("callback nextStep", nextStep)
    if (event.event_type == api.PiBootStatusType.BootStarted){
      console.log("Marking step successful")
      currentStep.success();
      nextStep?.start()
    }
  }),
  new ConnectTestStep(
    "Sync Settings",
    (event: api.PolymorphicPiEventRequest) => {}
  ),
  new ConnectTestStep(
    "Run Remote Command",
    (event: api.PolymorphicPiEventRequest) => {}
  ),
  new ConnectTestStep(
    "Turn on Camera",
    (event: api.PolymorphicPiEventRequest) => {}
  ),
];
store.$patch({ connectTestSteps });

</script>

<template>
  <FormStep :name="step.key">
    <h2
      class="text-2xl font-bold leading-7 text-gray-900 sm:text-3xl flex-1 w-full text-center"
    >
      {{ step.title }}
    </h2>
    <p class="text-base text-center font-medium text-gray-900 mt-5 w-full">
      {{ step.detail }}
    </p>
    <div
      class="min-h-full min-w-full w-full flex items-center justify-center py-12 px-4 sm:px-6 lg:px-8 bg-indigo-20 flex-wrap text-center"
    >
      <!-- test steps container -->
      <div class="flow-root w-3/4">
        <ul role="list" class="-mb-8">

          <!-- event-based connection tests -->
          <li v-for="(step, stepIdx) in connectTestSteps" :key="stepIdx">
            <div class="relative pb-8">
              <span
                v-if="stepIdx !== connectTestSteps.length - 1"
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
                      v-if="!step.active()"
                      class="h-5 w-5 text-white"
                      aria-hidden="true"
                    />
                    <component
                      :is="step.statusComponent().icon"
                      v-if="step.active()"
                      text=""
                      width="w-8"
                      height="w-8"
                      aria-hidden="true"
                    />
                  </span>
                </div>
                <div
                  class="min-w-0 flex-1 pt-1.5 flex justify-between space-x-24"
                >
                  <div>
                    <p class="text-sm text-gray-500 text-left">
                      <strong>{{ step.content }}</strong>
                      <br />
                      <i>{{ step.statusText() }}</i>
                    </p>
                  </div>
                  <div
                    class="text-right text-sm whitespace-nowrap text-gray-500"
                  >
                    {{ step.statusComponent().text }}
                    <br />
                    <time
                      v-if="step.status == ConnectTestStatus.Pending"
                      :datetime="step.start_dt.format()"
                      ><i>{{ step.start_dt.fromNow() }}</i></time
                    >
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
