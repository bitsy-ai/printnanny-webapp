<script setup lang="ts">
import type { PropType } from "vue";
import { ref } from "vue";
import { FolderDownloadIcon } from "@heroicons/vue/solid";
import {
  CheckIcon,
  ClipboardCopyIcon,
  QuestionMarkCircleIcon,
  ChipIcon,
} from "@heroicons/vue/outline";
import { useWizardStore } from "@/stores/wizard";
import type { WizardStep } from "@/types";
import FormStep from "./FormStep.vue";
import { useRouter } from "vue-router";
import type { ActionButton } from "@/types";
import { ManualTestStep } from "@/types";

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
  await store.downloadLicenseZip(piId);
}

function nextManualStep(currentStep: ManualTestStep, currentitemIdx: number) {
  // mark current step done
  currentStep.finish();
  // start next step
  if (currentitemIdx < manualSteps.value.length - 1) {
    manualSteps.value[currentitemIdx + 1].start();
  }
}

const manualSteps = ref([
  new ManualTestStep(
    "Download PrintNanny.zip (your license key)",
    "Do not share contents with anyone!",
    FolderDownloadIcon,
    [
      {
        text: "Download PrintNanny.zip",
        href: store.downloadUrl,
        onClick: nextManualStep,
        bgColor: "bg-amber-500",
        bgColorHover: "hover:bg-amber-600",
        bgColorFocus: "focus:ring-amber-500",
        icon: FolderDownloadIcon,
      } as ActionButton,
      {
        text: "Done",
        icon: CheckIcon,
        color: "emerald",
        bgColor: "bg-emerald-500",
        bgColorHover: "hover:bg-emerald-600",
        bgColorFocus: "focus:ring-emerald-500",
        onClick: nextManualStep,
      } as ActionButton,
    ]
  ),
  new ManualTestStep(
    "Copy PrintNanny.zip to SD Card",
    "Copy your license to the 'boot' partition of SD card.",
    ClipboardCopyIcon,
    [
      {
        text: "Show me how",
        bgColor: "bg-sky-500",
        bgColorHover: "hover:bg-sky-600",
        bgColorFocus: "focus:ring-sky-500",
        icon: QuestionMarkCircleIcon,
        href: "https://docs.printnanny.ai/docs/quick-start/copy-zip-to-sd-card",
      } as ActionButton,
      {
        text: "Done",
        icon: CheckIcon,
        bgColor: "bg-emerald-500",
        bgColorHover: "hover:bg-emerald-600",
        bgColorFocus: "focus:ring-emerald-500",
        onClick: nextManualStep,
      } as ActionButton,
    ]
  ),
  new ManualTestStep(
    "Eject SD Card & Insert into Raspberry Pi",
    "Connect Raspberry Pi to power to finish setup.",
    ChipIcon,
    [
      {
        text: "Show me how",
        bgColor: "bg-sky-500",
        bgColorHover: "hover:bg-sky-600",
        bgColorFocus: "focus:ring-sky-500",
        icon: QuestionMarkCircleIcon,
        href: "https://docs.printnanny.ai/docs/quick-start/copy-zip-to-sd-card",
      } as ActionButton,
      {
        text: "Done",
        icon: CheckIcon,
        bgColor: "bg-emerald-500",
        bgColorHover: "hover:bg-emerald-600",
        bgColorFocus: "focus:ring-emerald-500",
        onClick: nextManualStep,
      } as ActionButton,
    ]
  ),
]);

// start first step
manualSteps.value[0].start();
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
      <!-- setup steps container -->
      <div class="flow-root w-3/4">
        <ul role="list" class="-mb-8">
          <li v-for="(item, itemIdx) in manualSteps" :key="itemIdx">
            <div class="relative pb-8">
              <span
                v-if="itemIdx !== manualSteps.length - 1"
                class="absolute top-4 left-4 -ml-px h-full w-0.5 bg-gray-200"
                aria-hidden="true"
              />
              <div class="relative flex space-x-3">
                <div>
                  <span
                    :class="[
                      item.iconBackground(),
                      'h-8 w-8 rounded-full flex items-center justify-center ring-8 ring-white',
                    ]"
                  >
                    <component
                      :is="item.icon"
                      v-if="!item.done"
                      class="h-5 w-5 text-white"
                      aria-hidden="true"
                    />
                    <CheckIcon
                      v-else
                      class="h-5 w-5 text-white"
                      aria-hidden="true"
                    />
                  </span>
                </div>
                <div
                  class="min-w-0 flex-1 pt-1.5 flex justify-between space-x-24"
                >
                  <div>
                    <p class="text-sm text-gray-500 text-left">
                      <strong>{{ item.text }}</strong>
                      <br />
                      <i>{{ item.detail }}</i>
                    </p>
                  </div>
                  <div
                    v-if="item.active == true"
                    class="text-right text-sm whitespace-nowrap text-gray-500"
                  >
                    <span
                      v-for="(action, actionIdx) in item.actions"
                      :key="actionIdx"
                    >
                      <!-- href used for external documentation and other links -->
                      <a
                        v-if="action.href !== undefined"
                        :href="action.href"
                        target="_blank"
                      >
                        <button
                          type="button"
                          :class="[
                            action.bgColor,
                            action.bgColorHover,
                            action.bgColorFocus,
                            'focus:outline-none focus:ring-2 focus:ring-offset-2 inline-flex items-center group m-2 relative justify-center py-3 px-4 border border-transparent text-sm font-medium rounded-md text-white shadow-lg',
                          ]"
                          @click="action.onClick(item, itemIdx)"
                        >
                          <component
                            :is="action.icon"
                            v-if="action.icon"
                            class="h-5 w-5 mr-2 text-white"
                            aria-hidden="true"
                          />
                          {{ action.text }}
                        </button>
                      </a>
                      <!-- @click event is used for in-app navigation -->
                      <button
                        v-else
                        type="button"
                        :class="[
                          action.bgColor,
                          action.bgColorHover,
                          action.bgColorFocus,
                          'focus:outline-none focus:ring-2 focus:ring-offset-2 inline-flex items-center group m-2 relative justify-center py-3 px-4 border border-transparent text-sm font-medium rounded-md text-white shadow-lg',
                        ]"
                        @click="action.onClick(item, itemIdx)"
                      >
                        <component
                          :is="action.icon"
                          v-if="action.icon"
                          class="h-5 w-5 mr-2 text-white"
                          aria-hidden="true"
                        />
                        {{ action.text }}
                      </button>
                    </span>
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
