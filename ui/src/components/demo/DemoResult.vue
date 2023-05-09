<script setup lang="ts">
import { RouterLink, useRouter } from "vue-router";
import { useAccountStore } from "@/stores/account";
import { handleApiError } from "@//utils/api";
import { HandThumbUpIcon as ThumbUpIconSolid, HandThumbDownIcon as ThumbDownIconSolid, XMarkIcon as XIconSolid } from "@heroicons/vue/24/solid";
import { HandThumbUpIcon as ThumbUpIconOutline, HandThumbDownIcon as ThumbDownIconOutline, XMarkIcon as XIconOutline } from "@heroicons/vue/24/outline";

const account = useAccountStore();
const props = defineProps({
    demoId: {
        type: String,
        required: true
    }
});

const demo = (await account.demosApi.demosRetrieve(props.demoId).catch(handleApiError)).data;
console.log("Loaded demo", demo)

</script>
<template>
  <div
    class="flex-1 flex items-center justify-center p-12 px-4 sm:px-6 lg:px-8 bg-indigo-20 md:w-3/4 m:0 md:mx-auto rounded bg-white shadow-md"
  >
    <div class="max-w-2xl w-full space-y-8">
      <img
        class="mx-auto h-30 w-auto"
        src="@/assets/logo/logo-rect-light.svg"
        alt="PrintNanny"
      />
      <h2 class="my-6 text-center text-3xl font-extrabold text-gray-900">
        Your results are in! 🔮
      </h2>
      <p class="mt-5 max-w-prose mx-auto text-xl text-gray-500 text-center">
        How'd we do? <br> Your feedback helps PrintNanny learn.
      </p>
      <hr class="w-64 h-px my-8 mx-auto bg-gray-200 border-0" />

      <transition
        enter-active-class="transition ease-out duration-100"
        enter-from-class="transform opacity-0 scale-95"
        enter-to-class="transform opacity-100 scale-100"
        leave-active-class="transition ease-in duration-75"
        leave-from-class="transform opacity-100 scale-100"
        leave-to-class="transform opacity-0 scale-95"
      >
      <div>
        <dl class="mt-12 text-sm font-medium flex grid grid-cols-3">
            <dt class="text-gray-900"><strong>Nozzle</strong> <br>Was your hotend nozzle detected?</dt>
            <dd class="mt-2 text-indigo-600 flex grid grid-cols-3 gap-2 col-span-2">
                <button 
                  :class="[
                    demo.feedback_nozzle === true ? 'bg-indigo-500' : '',
                    'bg-gray-300 h-12 hover:bg-gray-400 text-gray-800 font-bold py-2 px-4 rounded inline-flex items-center justify-center']">
                    <ThumbUpIconOutline class="w-6 h-6 mr-2" />
                    <span>Yes</span>
                    </button>
                <button :class="[
                    demo.feedback_nozzle === false ? 'bg-indigo-500' : '',
                    'bg-gray-300 h-12 hover:bg-gray-400 text-gray-800 font-bold py-2 px-4 rounded inline-flex items-center justify-center']">
                    <ThumbDownIconOutline class="w-6 h-6 mr-2" />
                    <span>No</span>
                </button>
                <button :class="[
                    demo.feedback_nozzle === null ? 'bg-indigo-500' : '',
                    'bg-gray-300 h-12 hover:bg-gray-400 text-gray-800 font-bold py-2 px-4 rounded inline-flex items-center justify-center']">
                    <XIconOutline class="w-6 h-6 mr-2"/>
                    <span>N/A</span>
                </button>
            </dd>
        </dl>
        <hr class="w-64 h-px my-8 mx-auto bg-gray-200 border-0" />

        <img :src="demo.result" v-if="demo" class="m-auto"/>
        </div>
      </transition>
    </div>
  </div>
</template>