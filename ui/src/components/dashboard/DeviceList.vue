<template>
<section>
    <!-- Devices list (only on smallest breakpoint) -->
    <div class="mt-10 sm:hidden">
        <div class="px-4 sm:px-6">
        <h2 class="text-gray-500 text-xs font-medium uppercase tracking-wide">Devices</h2>
        </div>
        <ul role="list" class="mt-3 border-t border-gray-200 divide-y divide-gray-100">
        <li v-for="device in deviceStore.devices" :key="device.id">
            <a href="#" class="group flex items-center justify-between px-4 py-4 hover:bg-gray-50 sm:px-6">
            <span class="flex items-center truncate space-x-3">
                <span :class="[device.bgColorClass, 'w-2.5 h-2.5 flex-shrink-0 rounded-full']" aria-hidden="true" />
                <span class="font-medium truncate text-sm leading-6">
                {{ device.title }}
                {{ ' ' }}
                <span class="truncate font-normal text-gray-500">in {{ device.team }}</span>
                </span>
            </span>
            <ChevronRightIcon class="ml-4 h-5 w-5 text-gray-400 group-hover:text-gray-500" aria-hidden="true" />
            </a>
        </li>
        </ul>
    </div>

    <!-- Devices table (small breakpoint and up) -->
    <div class="hidden mt-8 sm:block">
        <div class="align-middle inline-block min-w-full border-b border-gray-200">
        <table class="min-w-full">
            <thead>
            <tr class="border-t border-gray-200">
                <th class="px-6 py-3 border-b border-gray-200 bg-gray-50 text-left text-xs font-medium text-gray-500 uppercase tracking-wider" scope="col">
                <span class="lg:pl-2">Hostname</span>
                </th>
                <th class="px-6 py-3 border-b border-gray-200 bg-gray-50 text-left text-xs font-medium text-gray-500 uppercase tracking-wider" scope="col">
                <span class="lg:pl-2">Installed Software</span>
                </th>
                <th class="px-6 py-3 border-b border-gray-200 bg-gray-50 text-left text-xs font-medium text-gray-500 uppercase tracking-wider" scope="col">Members</th>
                <th class="hidden md:table-cell px-6 py-3 border-b border-gray-200 bg-gray-50 text-right text-xs font-medium text-gray-500 uppercase tracking-wider" scope="col">Last updated</th>
                <th class="pr-6 py-3 border-b border-gray-200 bg-gray-50 text-right text-xs font-medium text-gray-500 uppercase tracking-wider" scope="col" />
            </tr>
            </thead>
            <tbody class="bg-white divide-y divide-gray-100">
                <!-- No devices found -->
                <DeviceEmpty v-if="deviceStore.devices.length == 0" />
                <!-- device list -->
                <tr v-for="device in deviceStore.devices" :key="device.id" v-if="deviceStore.devices.length > 0">
                    <td class="px-6 py-3 max-w-0 w-full whitespace-nowrap text-sm font-medium text-gray-900">
                    <div class="flex items-center space-x-3 lg:pl-2">
                        <div :class="[device.bgColorClass, 'flex-shrink-0 w-2.5 h-2.5 rounded-full']" aria-hidden="true" />
                        <a href="#" class="truncate hover:text-gray-600">
                        <span>
                            {{ device.title }}
                            {{ ' ' }}
                            <span class="text-gray-500 font-normal">in {{ device.team }}</span>
                        </span>
                        </a>
                    </div>
                    </td>
                    <td class="px-6 py-3 text-sm text-gray-500 font-medium">
                    members
                    </td>
                    <td class="hidden md:table-cell px-6 py-3 whitespace-nowrap text-sm text-gray-500 text-right">
                    {{ device.lastUpdated }}
                    </td>
                    <td class="px-6 py-3 whitespace-nowrap text-right text-sm font-medium">
                    <a href="#" class="text-indigo-600 hover:text-indigo-900">Edit</a>
                    </td>
                </tr>
            </tbody>
        </table>
        </div>
    </div>
</section>
</template>
<script setup lang="ts">
import { useDeviceStore } from '@/stores/devices';
import DeviceEmpty from './DeviceEmpty.vue';
const deviceStore = useDeviceStore();
</script>