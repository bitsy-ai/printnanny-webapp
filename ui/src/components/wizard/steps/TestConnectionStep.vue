<script setup lang="ts">
import FormStep from "./FormStep.vue";
import { useRouter } from "vue-router";
import type { PropType } from "vue";
import { useWizardStore } from "@/stores/wizard";
import type { WizardStep } from "@/types";
import { ConnectTestStatus } from "@/types";
import moment from "moment";

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
  const pi = await store.loadPi(piId);
  await store.initConnectTestSteps(pi);
  await store.connectTestSteps[0].run();
}
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
    <p class="text-base text-center text-gray-900 mt-5 w-full">
      To begin the test,
      <strong class="text-amber-500">insert SD card into Raspberry Pi</strong>
      and <strong class="text-amber-500">connect Pi to power source.</strong>
    </p>
    <div
      class="min-h-full min-w-full w-full flex items-center justify-center py-12 px-4 sm:px-6 lg:px-8 bg-indigo-20 flex-wrap text-center"
    >
      <!-- test steps container -->
      <div class="flow-root w-3/4">
        <ul role="list" class="-mb-8">
          <!-- event-based connection tests -->
          <li v-for="(item, itemIdx) in store.connectTestSteps" :key="itemIdx">
            <div class="relative pb-8">
              <span
                v-if="itemIdx !== store.connectTestSteps.length - 1"
                class="absolute top-4 left-4 -ml-px h-full w-0.5 bg-gray-200"
                aria-hidden="true"
              />
              <div class="relative flex space-x-3">
                <div>
                  <span
                    :class="[
                      item.statusComponent().iconBackground,
                      'h-8 w-8 rounded-full flex items-center justify-center ring-8 ring-white',
                    ]"
                  >
                    <component
                      :is="item.statusComponent().icon"
                      v-if="!item.active()"
                      class="h-5 w-5 text-white"
                      aria-hidden="true"
                    />
                    <component
                      :is="item.statusComponent().icon"
                      v-if="item.active()"
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
                      <strong>{{ item.title }}</strong>
                      <br />
                      <i>{{ item.description }}</i>
                    </p>
                  </div>
                  <div
                    class="text-right text-sm whitespace-nowrap text-gray-500"
                  >
                    {{ item.statusComponent().text }}
                    <br />
                    <time
                      v-if="item.events.length > 0"
                      :datetime="moment(item.events[item.events.length -1].created_dt).format()"
                      ><i>Finished {{moment(item.events[item.events.length -1].created_dt).fromNow() }}</i></time
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
