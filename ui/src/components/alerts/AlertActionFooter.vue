<!-- Alert with one or two action -->
<template>
    <div class="mt-3 flex space-x-7">
        <button v-for="action in actions" type="button" :class="colorClassNames(action.color)" class="bg-white rounded-md text-sm font-medium focus:outline-none focus:ring-2 focus:ring-offset-2">
        {{ action.text }}
        </button>
    </div>
</template>
<script setup lang="ts">
import { XIcon } from '@heroicons/vue/solid'
import { ref } from 'vue'
const props = defineProps({
  actions: {
    /**
     * [AlertAction]
     */
    type: Array
  }
});
function colorClassNames(color: string) {
    return `text-${color}-600 hover:text-${color}-500 focus:ring-${color}-500 bg-${color}`
}

const show = ref(true)
</script>