<!-- left sidebar navigation -->
<template>
<nav class="px-3 mt-6">
    <div class="space-y-1">
    <!-- Primary app navigation -->

    <router-link v-for="item in app_nav" :key="item.name" :to="item.link" :class="[item.current ? 'bg-gray-200 text-gray-900' : 'text-gray-700 hover:text-gray-900 hover:bg-gray-50', 'group flex items-center px-2 py-2 text-sm font-medium rounded-md']" :aria-current="item.current ? 'page' : undefined">
        <component :is="item.icon" :class="[item.current ? 'text-gray-500' : 'text-gray-400 group-hover:text-gray-500', 'mr-3 flex-shrink-0 h-6 w-6']" aria-hidden="true" />
        {{ item.name }}
    </router-link>
    </div>
    <div class="mt-8">
    <!-- Secondary navigation -->
    <h3 class="px-3 text-xs font-semibold text-gray-500 uppercase tracking-wider" id="desktop-teams-headline">Links</h3>
    <div class="mt-1 space-y-1" role="group" aria-labelledby="desktop-teams-headline">
        <a v-for="item in link_nav" :key="item.name" target="_blank" :href="item.href" class="group flex items-center px-3 py-2 text-sm font-medium text-gray-700 rounded-md hover:text-gray-900 hover:bg-gray-50">
            <component :is="item.icon" class="text-gray-400 group-hover:text-gray-500 mr-3 flex-shrink-0 h-6 w-6" aria-hidden="true" />
            {{ item.name }}
        </a>
    </div>
    </div>
 </nav>
</template>
<script setup lang="ts">
import { ref } from 'vue';
import { RouterLink, useRouter } from 'vue-router';
import { HomeIcon, QuestionMarkCircleIcon,  DocumentDownloadIcon, ExclamationIcon, ChatIcon, VideoCameraIcon } from '@heroicons/vue/outline';

const router = useRouter();
// app-based navigiation links
const app_nav = [
  { name: 'My Network', link: {name: "devices" }, icon: HomeIcon, current: router.currentRoute.value.name == "devices"},
//   { name: 'My Cameras', link: {name: "cameras" }, icon: VideoCameraIcon, current: router.currentRoute.value.name == "cameras"},
//   { name: 'My tasks', href: '#', icon: ViewListIcon, current: false },
//   { name: 'Recent', href: '#', icon: ClockIcon, current: false },
]

// external hrefs
const link_nav = [
  { name: 'Quick Start', href: "https://docs.printnanny.ai/docs/category/quick-start/", icon: QuestionMarkCircleIcon},
  { name: 'Latest Release', href: "https://docs.printnanny.ai/docs/release-history/0.2.0-beryl-kirkstone/", icon: DocumentDownloadIcon },
  { name: 'Report Issue', href: "https://github.com/bitsy-ai/printnanny-os/issues/new/choose", icon: ExclamationIcon },
  { name: 'Join Discord', href: "https://discord.gg/sf23bk2hPr", icon: ChatIcon }

]

const sidebarOpen = ref(false)
</script>