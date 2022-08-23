<script setup lang="ts">
import { markRaw } from "vue";
import { useWizardStore } from "@/stores/wizard";
import moment from "moment";
import WebrtcVideo from "../../video/WebrtcVideo.vue";
import WizardButtons from "@/components/wizard/steps/WizardButtons.vue";
import { PiCreateWizardSteps } from "../piCreateWizard";

const props = defineProps({
  piId: {
    type: String,
    required: true,
  },
});
const step = PiCreateWizardSteps()[3];

const store = useWizardStore();

if (store.pi == undefined || store.pi.id !== parseInt(props.piId)) {
  await store.loadPi(parseInt(props.piId));
}
await store.initConnectTestSteps();
await store.connectTestSteps.map((s) => s.run());
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
      <br />
      To begin the test,
      <strong class="text-amber-500">insert SD card into Raspberry Pi</strong>
      and <strong class="text-amber-500">connect Pi to power source.</strong>
    </p>
    <div
      class="grow min-w-full flex items-center justify-center py-12 px-4 sm:px-6 lg:px-8 bg-indigo-20 flex-wrap text-center"
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
                      :is="markRaw(item.statusComponent().icon)"
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
                      :datetime="
                        moment(
                          item.events[item.events.length - 1].created_dt
                        ).format()
                      "
                      ><i>{{
                        moment(
                          item.events[item.events.length - 1].created_dt
                        ).fromNow()
                      }}</i></time
                    >
                  </div>
                </div>
              </div>
            </div>
          </li>
        </ul>

        <!-- webrtc component -->
        <div class="w-full m-auto justify-center flex-1">
          <WebrtcVideo :pi-id="parseInt(props.piId)" />
        </div>
      </div>
    </div>

    <!-- footer buttons -->
    <div class="w-full m-auto justify-center flex-1">
      <WizardButtons :current-step="step" />
    </div>
  </div>
</template>
