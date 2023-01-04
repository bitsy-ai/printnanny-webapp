<script setup lang="ts">
import moment from "moment";
import { useDeviceStore, buildDeviceActions } from "@/stores/devices";
import {
  ChevronDownIcon,
  ChevronRightIcon,
  HeartIcon,
  TrashIcon,
  ExternalLinkIcon,
} from "@heroicons/vue/solid";
import TableEmpty from "./TableEmpty.vue";
import DeviceActionMenu from "./DeviceActionMenu.vue";
import DeviceFavorites from "./DeviceFavorites.vue";
import { ExclamationIcon } from "@heroicons/vue/outline";
import type { Pi, PatchedPiRequest } from "printnanny-api-client";

const deviceStore = useDeviceStore();
const pis = await deviceStore.fetchDevices();


</script>

<template>
  <section>
    <!-- Devices list (only on smallest breakpoint) -->
    <!-- Pinned pis -->
    <DeviceFavorites />
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
        <li v-for="pi in pis" :key="pi.id">
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
                <span class="lg:pl-2">Connection Status</span>
              </th>
              <th
                class="hidden md:table-cell px-6 py-3 border-b border-gray-200 bg-gray-50 text-right text-xs font-medium text-gray-500 uppercase tracking-wider"
                scope="col"
              >
                Last Sync
              </th>
              <th
                class="hidden md:table-cell px-6 py-3 border-b border-gray-200 bg-gray-50 text-right text-xs font-medium text-gray-500 uppercase tracking-wider"
                scope="col"
              >
                Disk Available
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
            <!-- No pis found -->
            <TableEmpty v-if="deviceStore.showEmpty" />
            <!-- pi list -->
            <tr
              v-for="(pi, index) in pis"
              v-show="!deviceStore.showEmpty"
              :key="index"
              class="flex-row"
            >
              <td
                class="px-6 py-3 max-w-0 whitespace-nowrap text-sm font-medium text-gray-900"
              >
                <div class="flex items-center space-x-3 lg:pl-2">
                  <div
                    v-if="!pi.setup_finished"
                    class="bg-yellow-500 flex-shrink-0 w-2.5 h-2.5 rounded-full"
                    aria-hidden="true"
                  ></div>
                  <div
                    v-if="pi.setup_finished"
                    class="bg-green-500 flex-shrink-0 w-2.5 h-2.5 rounded-full"
                    aria-hidden="true"
                  ></div>
                  <a href="#" class="truncate hover:text-gray-600">
                    <span>
                      {{ pi.fqdn }}
                      {{ " " }}
                    </span>
                  </a>
                  <!-- TODO add a failed badge indicator  -->
                  <!--
                  <router-link
                    v-if="!pi.setup_finished"
                    :to="{
                      name: wizardSteps[2].routeName,
                      params: {
                        piId: pi.id,
                      },
                    }"
                  >
                    <span
                      class="inline-flex items-center px-2.5 py-0.5 rounded-md text-sm font-medium bg-yellow-100 text-yellow-800 hover:bg-yellow-200"
                    >
                      <ExclamationIcon
                        class="mr-1 w-5 h-5 text-yellow-800 text-yellow-800"
                      />
                      Finish Setup
                    </span>
                  </router-link>
                  <a v-else :href="pi.urls.mission_control" target="_blank">
                    <span
                      class="inline-flex items-center px-2.5 py-0.5 rounded-md text-sm font-medium bg-emerald-100 text-emerald-800 hover:bg-emerald-200"
                    >
                      <ExternalLinkIcon
                        class="mr-1 w-5 h-5 text-emerald-800 text-emerald-800"
                      />
                      PrintNanny OS
                    </span>
                  </a>
                  -->
                </div>
              </td>
              <td
                class="hidden md:table-cell px-6 py-3 whitespace-nowrap text-sm text-gray-500 text-right"
              >
                {{
                  pi.last_boot
                    ? moment(pi.last_boot).fromNow()
                    : "Waiting for first boot"
                }}
              </td>
              <td
                class="hidden md:table-cell px-6 py-3 whitespace-nowrap text-sm text-gray-500 text-right"
              >
                {{
                  pi.system_info ? pi.system_info.datafs_available_pretty : ""
                }}
              </td>
              <td
                class="px-6 py-3 whitespace-nowrap text-sm font-medium text-right"
              >
              <DeviceActionMenu :pi="pi" :index="index" />
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </section>
</template>
