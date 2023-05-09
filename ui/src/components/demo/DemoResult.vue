<script setup lang="ts">
import { ref, toRaw } from "vue";
import { RouterLink, useRouter } from "vue-router";
import * as api from "printnanny-api-client";

import { useDemoStore } from "@/stores/demo";
import { useAccountStore } from "@/stores/account";
import { handleApiError } from "@//utils/api";
import {
  HandThumbUpIcon as ThumbUpIconSolid,
  HandThumbDownIcon as ThumbDownIconSolid,
  XMarkIcon as XIconSolid,
} from "@heroicons/vue/24/solid";
import {
  HandThumbUpIcon as ThumbUpIconOutline,
  HandThumbDownIcon as ThumbDownIconOutline,
  XMarkIcon as XIconOutline,
} from "@heroicons/vue/24/outline";
import TextSpinner from "@/components/util/TextSpinner.vue";

const store = useDemoStore();
const props = defineProps({
  demoId: {
    type: String,
    required: true,
  },
});

await store.load(props.demoId);
console.debug("Loaded demo", toRaw(store.demo));
</script>
<template>
  <div
    class="flex-1 flex items-center justify-center p-12 px-4 sm:px-6 lg:px-8 bg-indigo-20 md:w-3/4 m:0 md:mx-auto rounded bg-white shadow-md"
  >
    <div class="max-w-2xl w-full space-y-8">
      <img
        class="mx-auto h-24 w-auto"
        src="@/assets/logo/logo-rect-light.svg"
        alt="PrintNanny"
      />
      <h2 class="my-6 text-center text-3xl font-extrabold text-gray-900">
        Your results are in! 🔮
      </h2>
      <img v-if="store.demo" :src="store.demo.result" class="m-auto" />

      <p class="mt-5 max-w-prose mx-auto text-xl text-gray-500 text-center">
        How'd we do? <br />
        Your feedback helps PrintNanny learn. 🧠
      </p>
      <hr class="w-64 h-px my-8 mx-auto bg-gray-200 border-0" />
      <transition
        enter-active-class="duration-300 ease-out"
        enter-from-class="transform opacity-0"
        enter-to-class="opacity-100"
        leave-active-class="duration-200 ease-in"
        leave-from-class="opacity-100"
        leave-to-class="transform opacity-0"
      >
        <div>
          <!-- nozzle feedback -->
          <dl class="mt-12 text-sm font-medium flex grid grid-cols-2 mb-6">
            <dt class="text-gray-800">
              <strong class="text-indigo-500">Hotend Nozzle</strong> <br />Was
              your hotend nozzle detected?
            </dt>
            <dd class="mt-2 text-indigo-600 flex grid grid-cols-3 gap-2">
              <button
                :class="[
                  store.demo.feedback_nozzle == api.DemoFeedbackEnum.Pass
                    ? 'bg-indigo-300 hover:bg-indigo-400'
                    : 'bg-gray-300 hover:bg-gray-400',
                  'h-12 hover:bg-gray-400 text-gray-800 font-bold py-2 px-4 rounded inline-flex items-center justify-center',
                ]"
                @click="
                  store.handleFeedback(
                    props.demoId,
                    'nozzle',
                    api.DemoFeedbackEnum.Pass
                  )
                "
              >
                <ThumbUpIconOutline class="w-6 h-6 mr-2" />
                <span>Yes</span>
              </button>
              <button
                :class="[
                  store.demo.feedback_nozzle == api.DemoFeedbackEnum.Fail
                    ? 'bg-indigo-300 hover:bg-indigo-400'
                    : 'bg-gray-300 hover:bg-gray-400',
                  'h-12 text-gray-800 font-bold py-2 px-4 rounded inline-flex items-center justify-center',
                ]"
                @click="
                  store.handleFeedback(
                    props.demoId,
                    'nozzle',
                    api.DemoFeedbackEnum.Fail
                  )
                "
              >
                <ThumbDownIconOutline class="w-6 h-6 mr-2" />
                <span>No</span>
              </button>
              <button
                :class="[
                  store.demo.feedback_nozzle == api.DemoFeedbackEnum.Na
                    ? 'bg-indigo-300 hover:bg-indigo-400'
                    : 'bg-gray-300 hover:bg-gray-400',
                  'h-12 text-gray-800 font-bold py-2 px-4 rounded inline-flex items-center justify-center',
                ]"
                @click="
                  store.handleFeedback(
                    props.demoId,
                    'nozzle',
                    api.DemoFeedbackEnum.Na
                  )
                "
              >
                <XIconOutline class="w-6 h-6 mr-2" />
                <span>N/A</span>
              </button>
            </dd>
          </dl>
          <!-- print feedback -->
          <dl class="mt-12 text-sm font-medium flex grid grid-cols-2 mb-6">
            <dt class="text-gray-800">
              <strong class="text-indigo-500">3D-Printed Object(s)</strong>
              <br />Was each 3D-printed object detected?
            </dt>
            <dd class="mt-2 text-indigo-600 flex grid grid-cols-3 gap-2">
              <button
                :class="[
                  store.demo.feedback_print == api.DemoFeedbackEnum.Pass
                    ? 'bg-indigo-300 hover:bg-indigo-400'
                    : 'bg-gray-300 hover:bg-gray-400',
                  'h-12 hover:bg-gray-400 text-gray-800 font-bold py-2 px-4 rounded inline-flex items-center justify-center',
                ]"
                @click="
                  store.handleFeedback(
                    props.demoId,
                    'print',
                    api.DemoFeedbackEnum.Pass
                  )
                "
              >
                <ThumbUpIconOutline class="w-6 h-6 mr-2" />
                <span>Yes</span>
              </button>
              <button
                :class="[
                  store.demo.feedback_print == api.DemoFeedbackEnum.Fail
                    ? 'bg-indigo-300 hover:bg-indigo-400'
                    : 'bg-gray-300 hover:bg-gray-400',
                  'h-12 text-gray-800 font-bold py-2 px-4 rounded inline-flex items-center justify-center',
                ]"
                @click="
                  store.handleFeedback(
                    props.demoId,
                    'print',
                    api.DemoFeedbackEnum.Fail
                  )
                "
              >
                <ThumbDownIconOutline class="w-6 h-6 mr-2" />
                <span>No</span>
              </button>
              <button
                :class="[
                  store.demo.feedback_print == api.DemoFeedbackEnum.Na
                    ? 'bg-indigo-300 hover:bg-indigo-400'
                    : 'bg-gray-300 hover:bg-gray-400',
                  'h-12 text-gray-800 font-bold py-2 px-4 rounded inline-flex items-center justify-center',
                ]"
                @click="
                  store.handleFeedback(
                    props.demoId,
                    'print',
                    api.DemoFeedbackEnum.Na
                  )
                "
              >
                <XIconOutline class="w-6 h-6 mr-2" />
                <span>N/A</span>
              </button>
            </dd>
          </dl>
          <!-- raft feedback -->
          <dl class="mt-12 text-sm font-medium flex grid grid-cols-2 mb-6">
            <dt class="text-gray-800">
              <strong class="text-indigo-500">Raft & Skirt</strong> <br />If
              there's a raft or skirt, did we detect it?
            </dt>
            <dd class="mt-2 text-indigo-600 flex grid grid-cols-3 gap-2">
              <button
                :class="[
                  store.demo.feedback_raft == api.DemoFeedbackEnum.Pass
                    ? 'bg-indigo-300 hover:bg-indigo-400'
                    : 'bg-gray-300 hover:bg-gray-400',
                  'h-12 hover:bg-gray-400 text-gray-800 font-bold py-2 px-4 rounded inline-flex items-center justify-center',
                ]"
                @click="
                  store.handleFeedback(
                    props.demoId,
                    'raft',
                    api.DemoFeedbackEnum.Pass
                  )
                "
              >
                <ThumbUpIconOutline class="w-6 h-6 mr-2" />
                <span>Yes</span>
              </button>
              <button
                :class="[
                  store.demo.feedback_raft == api.DemoFeedbackEnum.Fail
                    ? 'bg-indigo-300 hover:bg-indigo-400'
                    : 'bg-gray-300 hover:bg-gray-400',
                  'h-12 text-gray-800 font-bold py-2 px-4 rounded inline-flex items-center justify-center',
                ]"
                @click="
                  store.handleFeedback(
                    props.demoId,
                    'raft',
                    api.DemoFeedbackEnum.Fail
                  )
                "
              >
                <ThumbDownIconOutline class="w-6 h-6 mr-2" />
                <span>No</span>
              </button>
              <button
                :class="[
                  store.demo.feedback_raft == api.DemoFeedbackEnum.Na
                    ? 'bg-indigo-300 hover:bg-indigo-400'
                    : 'bg-gray-300 hover:bg-gray-400',
                  'h-12 text-gray-800 font-bold py-2 px-4 rounded inline-flex items-center justify-center',
                ]"
                @click="
                  store.handleFeedback(
                    props.demoId,
                    'raft',
                    api.DemoFeedbackEnum.Na
                  )
                "
              >
                <XIconOutline class="w-6 h-6 mr-2" />
                <span>N/A</span>
              </button>
            </dd>
          </dl>

          <!-- spaghetti feedback -->
          <dl class="mt-12 text-sm font-medium flex grid grid-cols-2 mb-6">
            <dt class="text-gray-800">
              <strong class="text-red-500">Defect: Spaghetti</strong> <br />If
              there's filament spaghetti, did we detect it?
            </dt>
            <dd class="mt-2 text-indigo-600 flex grid grid-cols-3 gap-2">
              <button
                :class="[
                  store.demo.feedback_spaghetti == api.DemoFeedbackEnum.Pass
                    ? 'bg-indigo-300 hover:bg-indigo-400'
                    : 'bg-gray-300 hover:bg-gray-400',
                  'h-12 hover:bg-gray-400 text-gray-800 font-bold py-2 px-4 rounded inline-flex items-center justify-center',
                ]"
                @click="
                  store.handleFeedback(
                    props.demoId,
                    'spaghetti',
                    api.DemoFeedbackEnum.Pass
                  )
                "
              >
                <ThumbUpIconOutline class="w-6 h-6 mr-2" />
                <span>Yes</span>
              </button>
              <button
                :class="[
                  store.demo.feedback_spaghetti == api.DemoFeedbackEnum.Fail
                    ? 'bg-indigo-300 hover:bg-indigo-400'
                    : 'bg-gray-300 hover:bg-gray-400',
                  'h-12 text-gray-800 font-bold py-2 px-4 rounded inline-flex items-center justify-center',
                ]"
                @click="
                  store.handleFeedback(
                    props.demoId,
                    'spaghetti',
                    api.DemoFeedbackEnum.Fail
                  )
                "
              >
                <ThumbDownIconOutline class="w-6 h-6 mr-2" />
                <span>No</span>
              </button>
              <button
                :class="[
                  store.demo.feedback_spaghetti == api.DemoFeedbackEnum.Na
                    ? 'bg-indigo-300 hover:bg-indigo-400'
                    : 'bg-gray-300 hover:bg-gray-400',
                  'h-12 text-gray-800 font-bold py-2 px-4 rounded inline-flex items-center justify-center',
                ]"
                @click="
                  store.handleFeedback(
                    props.demoId,
                    'spaghetti',
                    api.DemoFeedbackEnum.Na
                  )
                "
              >
                <XIconOutline class="w-6 h-6 mr-2" />
                <span>N/A</span>
              </button>
            </dd>
          </dl>

          <!-- adhesion feedback -->
          <dl class="mt-12 text-sm font-medium flex grid grid-cols-2 mb-6">
            <dt class="text-gray-800">
              <strong class="text-red-500"
                >Defect: Bed Adhesion & Warping</strong
              >
              <br />If the print warped or moved, did we detect it?
            </dt>
            <dd class="mt-2 text-indigo-600 flex grid grid-cols-3 gap-2">
              <button
                :class="[
                  store.demo.feedback_adhesion == api.DemoFeedbackEnum.Pass
                    ? 'bg-indigo-300 hover:bg-indigo-400'
                    : 'bg-gray-300 hover:bg-gray-400',
                  'h-12 hover:bg-gray-400 text-gray-800 font-bold py-2 px-4 rounded inline-flex items-center justify-center',
                ]"
                @click="
                  store.handleFeedback(
                    props.demoId,
                    'adhesion',
                    api.DemoFeedbackEnum.Pass
                  )
                "
              >
                <ThumbUpIconOutline class="w-6 h-6 mr-2" />
                <span>Yes</span>
              </button>
              <button
                :class="[
                  store.demo.feedback_adhesion == api.DemoFeedbackEnum.Fail
                    ? 'bg-indigo-300 hover:bg-indigo-400'
                    : 'bg-gray-300 hover:bg-gray-400',
                  'h-12 text-gray-800 font-bold py-2 px-4 rounded inline-flex items-center justify-center',
                ]"
                @click="
                  store.handleFeedback(
                    props.demoId,
                    'adhesion',
                    api.DemoFeedbackEnum.Fail
                  )
                "
              >
                <ThumbDownIconOutline class="w-6 h-6 mr-2" />
                <span>No</span>
              </button>
              <button
                :class="[
                  store.demo.feedback_adhesion == api.DemoFeedbackEnum.Na
                    ? 'bg-indigo-300 hover:bg-indigo-400'
                    : 'bg-gray-300 hover:bg-gray-400',
                  'h-12 text-gray-800 font-bold py-2 px-4 rounded inline-flex items-center justify-center',
                ]"
                @click="
                  store.handleFeedback(
                    props.demoId,
                    'adhesion',
                    api.DemoFeedbackEnum.Na
                  )
                "
              >
                <XIconOutline class="w-6 h-6 mr-2" />
                <span>N/A</span>
              </button>
            </dd>
          </dl>
          <transition
            enter-active-class="duration-1000 ease-out"
            enter-from-class="transform opacity-0"
            enter-to-class="opacity-100"
            leave-active-class="duration-700 ease-in"
            leave-from-class="opacity-100"
            leave-to-class="transform opacity-0"
          >
            <p
              v-if="store.saved"
              class="text-center m-auto text-sm text-gray-600 flex-start w-1/2"
            >
              ✔️ Saved
            </p>
            <TextSpinner
              v-else-if="store.loading"
              class="m-auto text-sm text-gray-800 justify-center flex-end"
              text="Saving..."
            />
          </transition>
          <hr class="w-64 h-px my-8 mx-auto bg-gray-200 border-0" />
        </div>
      </transition>
    </div>
  </div>
</template>
