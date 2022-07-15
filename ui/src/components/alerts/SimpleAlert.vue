<!-- Simple text-only dismissable alert with customizable background and actions -->

<template>
<transition enter-active-class="transform ease-out duration-300 transition" enter-from-class="translate-y-2 opacity-0 sm:translate-y-0 sm:translate-x-2" enter-to-class="translate-y-0 opacity-100 sm:translate-x-0" leave-active-class="transition ease-in duration-100" leave-from-class="opacity-100" leave-to-class="opacity-0">

<div v-if="show" class="max-w-sm w-full shadow-lg rounded-lg pointer-events-auto ring-1 ring-black ring-opacity-5 overflow-hidden" :class="bgColor">
    <div class="p-4">
    <div class="flex items-start">
        <div class="flex-shrink-0">
        <slot name="icon"></slot> <!-- icon slot -->
        </div>
        <div class="ml-3 w-0 flex-1 pt-0.5">
        <p class="text-sm font-medium text-gray-900">
            {{ header }}
        </p>
        <p class="mt-1 text-sm text-gray-500">
            {{ message }}       
        </p>
        <AlertActionFooter vf-if="actions.length" :actions="actions"/>
        </div>
        <div class="ml-4 flex-shrink-0 flex">
        <button type="button" @click="show = false" class="bg-white rounded-md inline-flex text-gray-400 hover:text-gray-500 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
            <span class="sr-only">Dismiss</span>
            <XIcon class="h-5 w-5" aria-hidden="true" />
        </button>
        </div>
    </div>
    </div>
</div>
</transition>
</template>
<script setup lang="ts">
import { XIcon } from '@heroicons/vue/solid'
import { ref } from 'vue'
import AlertActionFooter from './AlertActionFooter.vue'
import type { AlertAction } from '@/types';
const props = defineProps({
  message: String,
  header: String,
  bgColor: {
    type: String,
    required: false,
    default: "bg-white"
  },
  actions: {
    /**
     * [AlertAction]
     */
    type: Array
  }
});

const show = ref(true)
</script>