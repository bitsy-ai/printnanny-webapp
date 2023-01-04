<script setup lang="ts">
import moment from "moment";
import TableEmpty from "./TableEmpty.vue";
import DeviceActionMenu from "./DeviceActionMenu.vue";
import DeviceFavorites from "./DeviceFavorites.vue";
import { ExclamationIcon, SupportIcon} from "@heroicons/vue/outline";
import { ExternalLinkIcon, ChevronRightIcon} from "@heroicons/vue/solid";
import { useCrashReportStore } from "@/stores/crash-reports";

const store = useCrashReportStore();
const crashReports = await store.fetchCrashReports();
</script>

<template>
  <section>
    <div class="mt-10 sm:hidden">
      <div class="px-4 sm:px-6">
        <h2 class="text-gray-500 text-xs font-medium uppercase tracking-wide">
          Devices
        </h2>
      </div>
      <ul
        role="list"
        class="mt-3 border-t border-gray-200 divide-y divide-gray-100"
      >
        <li v-for="report in crashReports" :key="report.id">
          <a
            href="#"
            class="group flex items-center justify-between px-4 py-4 hover:bg-gray-50 sm:px-6"
          >
            <ChevronRightIcon
              class="ml-4 h-5 w-5 text-gray-400 group-hover:text-gray-500"
              aria-hidden="true"
            />
          </a>
        </li>
      </ul>
    </div>

    <!-- Devices table (small breakpoint and up) -->
    <div class="hidden mt-8 sm:block">
      <div
        class="align-middle inline-block min-w-full border-b border-gray-200"
      >
        <table class="min-w-full table-fixed">
          <thead>
            <tr class="border-t border-gray-200">
              <th
                class="px-6 py-3 border-b border-gray-200 bg-gray-50 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
                scope="col"
              >
                <span class="lg:pl-2">Report ID</span>
              </th>
              <th
                class="hidden md:table-cell px-6 py-3 border-b border-gray-200 bg-gray-50 text-right text-xs font-medium text-gray-500 uppercase tracking-wider"
                scope="col"
              >
                Updated
              </th>
              <th
                class="hidden md:table-cell px-6 py-3 border-b border-gray-200 bg-gray-50 text-right text-xs font-medium text-gray-500 uppercase tracking-wider"
                scope="col"
              >
                Status
              </th>
              <th
                class="px-6 py-3 border-b border-gray-200 bg-gray-50 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
                scope="col"
              >
                Actions & Quick Links
              </th>
            </tr>
          </thead>
          <tbody class="bg-white divide-y divide-gray-100">
            <TableEmpty v-if="store.showEmpty" :icon="SupportIcon" header="No crash reports found" />
            <tr
            v-for="report in crashReports" :key="report.id"
              v-show="!store.showEmpty"
              class="flex-row"
            >

            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </section>
</template>
