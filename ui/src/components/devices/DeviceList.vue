<template>
  <section>
    <!-- Devices list (only on smallest breakpoint) -->
    <!-- Pinned devices -->
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
        <li v-for="device in deviceStore.devices" :key="device.id">
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
            <!-- No devices found -->
            <DeviceEmpty v-if="deviceStore.showEmpty" />
            <!-- device list -->
            <tr
              v-for="(device, index) in deviceStore.devices"
              v-show="!deviceStore.showEmpty"
              :key="index"
              class="flex-row"
            >
              <td
                class="px-6 py-3 max-w-0 whitespace-nowrap text-sm font-medium text-gray-900"
              >
                <div class="flex items-center space-x-3 lg:pl-2">
                  <div
                    v-if="!device.ws_connected"
                    class="bg-red-500 flex-shrink-0 w-2.5 h-2.5 rounded-full"
                    aria-hidden="true"
                  ></div>
                  <div
                    v-if="device.ws_connected"
                    class="bg-green-500 flex-shrink-0 w-2.5 h-2.5 rounded-full"
                    aria-hidden="true"
                  ></div>
                  <a href="#" class="truncate hover:text-gray-600">
                    <span>
                      {{ device.fqdn }}
                      {{ " " }}
                    </span>
                  </a>
                  <span
                    v-if="!device.ws_connected"
                    class="inline-flex items-center px-2.5 py-0.5 rounded-md text-sm font-medium bg-red-100 text-red-800"
                  >
                    <ExclamationIcon
                      v-if="!device.ws_connected"
                      class="bg-red-500"
                    />
                    Connection Issue
                  </span>
                </div>
              </td>
              <td
                class="hidden md:table-cell px-6 py-3 whitespace-nowrap text-sm text-gray-500 text-right"
              >
                {{ device.last_boot || "Waiting for first boot" }}
              </td>
              <td
                class="px-6 py-3 whitespace-nowrap text-sm font-medium text-right"
              >
                <DeviceActionMenu :device="device" :index="index" />
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </section>
</template>
<script setup lang="ts">
import { useDeviceStore } from "@/stores/devices";
import DeviceEmpty from "./DeviceEmpty.vue";
import DeviceActionMenu from "./DeviceActionMenu.vue";
import DeviceFavorites from "./DeviceFavorites.vue";
const deviceStore = useDeviceStore();
deviceStore.fetchDevices();
</script>
