<!-- left sidebar navigation -->
<template>
<nav class="px-3 mt-6">
    <div class="space-y-1">
    <router-link v-for="item in navigation" :key="item.name" :to="item.link" :class="[item.current ? 'bg-gray-200 text-gray-900' : 'text-gray-700 hover:text-gray-900 hover:bg-gray-50', 'group flex items-center px-2 py-2 text-sm font-medium rounded-md']" :aria-current="item.current ? 'page' : undefined">
        <component :is="item.icon" :class="[item.current ? 'text-gray-500' : 'text-gray-400 group-hover:text-gray-500', 'mr-3 flex-shrink-0 h-6 w-6']" aria-hidden="true" />
        {{ item.name }}
    </router-link>
    </div>
    <div class="mt-8">
    <!-- Secondary navigation -->
    <h3 class="px-3 text-xs font-semibold text-gray-500 uppercase tracking-wider" id="desktop-teams-headline">Teams</h3>
    <div class="mt-1 space-y-1" role="group" aria-labelledby="desktop-teams-headline">
        <a v-for="team in teams" :key="team.name" :href="team.href" class="group flex items-center px-3 py-2 text-sm font-medium text-gray-700 rounded-md hover:text-gray-900 hover:bg-gray-50">
        <span :class="[team.bgColorClass, 'w-2.5 h-2.5 mr-4 rounded-full']" aria-hidden="true" />
        <span class="truncate">
            {{ team.name }}
        </span>
        </a>
    </div>
    </div>
 </nav>
</template>
<script setup lang="ts">
import { ref } from 'vue';
import { RouterLink } from 'vue-router';
import { HomeIcon } from '@heroicons/vue/outline';

const navigation = [
  { name: 'Dashboard', link: {name: "dashboard" }, icon: HomeIcon, current: true },
//   { name: 'My tasks', href: '#', icon: ViewListIcon, current: false },
//   { name: 'Recent', href: '#', icon: ClockIcon, current: false },
]

const sidebarOpen = ref(false)
</script>