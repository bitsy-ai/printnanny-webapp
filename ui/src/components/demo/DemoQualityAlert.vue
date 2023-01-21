<script setup lang="ts">
import { onMounted, ref } from "vue";

const show = ref(true);
onMounted(() => {
  const el1 = document.querySelector("video#demo-video-1") as HTMLVideoElement;
  el1.playbackRate = 0.5;
  const el2 = document.querySelector("video#demo-video-2") as HTMLVideoElement;
  el2.playbackRate = 0.5;
});
</script>
<!-- This example requires Tailwind CSS v2.0+ -->
<template>
  <div class="grid grid-cols-1 md:grid-cols-2">
    <section>
      <div
        v-if="show"
        class="mx-auto max-w-md w-full bg-white shadow-lg rounded-lg pointer-events-auto flex ring-1 ring-black ring-opacity-5 divide-x divide-gray-200"
      >
        <div class="w-0 flex-1 flex items-center p-4">
          <div class="w-full">
            <p class="text-sm font-medium text-gray-900">Quality Alert!</p>
            <p class="mt-1 text-sm text-gray-500">
              Detected <strong>collapsed overhangs</strong> and
              <strong>spaghetti</strong>. Job automatically paused.
            </p>
          </div>
        </div>
        <div class="flex">
          <div class="flex flex-col divide-y divide-gray-200">
            <div class="h-0 flex-1 flex">
              <button
                type="button"
                class="w-full border border-transparent rounded-none rounded-tr-lg px-4 py-3 flex items-center justify-center text-sm font-medium text-indigo-600 hover:text-indigo-500 focus:outline-none focus:z-10 focus:ring-2 focus:ring-indigo-500"
              >
                Resume Job
              </button>
            </div>
            <div class="h-0 flex-1 flex">
              <button
                type="button"
                class="w-full border border-transparent rounded-none rounded-br-lg px-4 py-3 flex items-center justify-center text-sm font-medium text-gray-700 hover:text-gray-500 focus:outline-none focus:ring-2 focus:ring-indigo-500"
                @click="show = false"
              >
                Dismiss
              </button>
            </div>
          </div>
        </div>
      </div>
      <div class="px-4 py-5 sm:p-6">
        <video
          id="demo-video-1"
          muted="true"
          loop="true"
          controls="true"
          class="w-full"
          preload="metadata"
        >
          <source
            src="https://cdn.printnanny.ai/www/demo-video-1.mp4"
            type="video/mp4"
          />
        </video>
      </div>
    </section>
    <section>
      <div
        v-if="show"
        class="mx-auto max-w-md w-full bg-white shadow-lg rounded-lg pointer-events-auto flex ring-1 ring-black ring-opacity-5 divide-x divide-gray-200"
      >
        <div class="w-0 flex-1 flex items-center p-4">
          <div class="w-full">
            <p class="text-sm font-medium text-gray-900">Quality Alert!</p>
            <p class="mt-1 text-sm text-gray-500">
              Detected <strong>layer warping</strong>. Should I pause the active
              job?
            </p>
          </div>
        </div>
        <div class="flex">
          <div class="flex flex-col divide-y divide-gray-200">
            <div class="h-0 flex-1 flex">
              <button
                type="button"
                class="w-full border border-transparent rounded-none rounded-tr-lg px-4 py-3 flex items-center justify-center text-sm font-medium text-red-600 hover:text-red-500 focus:outline-none focus:z-10 focus:ring-2 focus:ring-red-500"
              >
                Pause Job
              </button>
            </div>
            <div class="h-0 flex-1 flex">
              <button
                type="button"
                class="w-full border border-transparent rounded-none rounded-br-lg px-4 py-3 flex items-center justify-center text-sm font-medium text-gray-700 hover:text-gray-500 focus:outline-none focus:ring-2 focus:ring-indigo-500"
                @click="show = false"
              >
                Dismiss
              </button>
            </div>
          </div>
        </div>
      </div>
      <div class="px-4 py-5 sm:p-6">
        <video
          id="demo-video-2"
          muted="true"
          loop="true"
          controls="true"
          class="w-full"
          preload="metadata"
        >
          <source
            src="https://cdn.printnanny.ai/www/demo-video-3.mp4"
            type="video/mp4"
          />
        </video>
      </div>
    </section>
  </div>
</template>
