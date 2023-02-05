<!-- Alerts Container (top-right corner )-->
<template>
  <!-- Global notification live region, render this permanently at the end of the document -->
  <div
    aria-live="assertive"
    class="fixed inset-0 flex items-end px-4 py-6 pointer-events-none sm:p-6 sm:items-start z-50"
  >
    <div class="w-full flex flex-col items-center space-y-4 sm:items-end">
      <!-- Notification panel, dynamically insert this into the live region when it needs to be displayed -->
      <SimpleAlert
        v-for="(alert, index) in alertStore.alerts"
        :key="index"
        :header="alert.header"
        :message="alert.message"
        :actions="alert.actions"
      >
        <template v-if="alert.error" #icon>
          <ExclamationTriangleIcon class="h-6 w-6 text-red-400" />
        </template>
      </SimpleAlert>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useAlertStore } from "@/stores/alerts";
import { ExclamationTriangleIcon } from "@heroicons/vue/24/outline";
import SimpleAlert from "./SimpleAlert.vue";

const alertStore = useAlertStore();
</script>
