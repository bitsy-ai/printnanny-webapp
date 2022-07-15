<!-- Alerts Container (top-right corner )-->
<template>
  <!-- Global notification live region, render this permanently at the end of the document -->
  <div aria-live="assertive" class="fixed inset-0 flex items-end px-4 py-6 pointer-events-none sm:p-6 sm:items-start">
    <div class="w-full flex flex-col items-center space-y-4 sm:items-end">
      <!-- Notification panel, dynamically insert this into the live region when it needs to be displayed -->
        <SimpleAlert v-for="alert in alertStore.alerts" :key="alert.id" :header="alert.header" :message="alert.message" >

        </SimpleAlert>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useAlertStore } from '@/stores/alerts';
import {  XIcon} from '@heroicons/vue/outline'
import SimpleAlert from './SimpleAlert.vue'

const alertStore = useAlertStore();
</script>