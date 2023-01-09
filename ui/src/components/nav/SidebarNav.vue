<!-- left sidebar navigation -->
<template>
  <nav class="px-3 mt-6">
    <div class="space-y-1">
      <!-- Primary app navigation -->

      <router-link
        v-for="item in app_nav"
        :key="item.name"
        :to="item.link"
        :class="[
          item.current()
            ? 'bg-gray-200 text-gray-900'
            : 'text-gray-700 hover:text-gray-900 hover:bg-gray-50',
          'group flex items-center px-2 py-2 text-sm font-medium rounded-md',
        ]"
        :aria-current="item.current() ? 'page' : undefined"
      >
        <component
          :is="item.icon"
          :class="[
            item.current()
              ? 'text-gray-500'
              : 'text-gray-400 group-hover:text-gray-500',
            'mr-3 flex-shrink-0 h-6 w-6',
          ]"
          aria-hidden="true"
        />
        {{ item.name }}
      </router-link>
    </div>
    <div class="mt-8">
      <!-- help/support navigation -->
      <h3
        id="desktop-teams-headline"
        class="px-3 text-xs font-semibold text-gray-500 uppercase tracking-wider"
      >
        Help & Support
      </h3>
      <div
        class="mt-1 space-y-1"
        role="group"
        aria-labelledby="desktop-teams-headline"
      >
        <a
          v-for="item in help_nav"
          :key="item.name"
          target="_blank"
          :href="item.href"
          class="group flex items-center px-3 py-2 text-sm font-medium text-gray-700 rounded-md hover:text-gray-900 hover:bg-gray-50"
        >
          <component
            :is="item.icon"
            class="text-gray-400 group-hover:text-gray-500 mr-3 flex-shrink-0 h-6 w-6"
            aria-hidden="true"
          />
          {{ item.name }}
        </a>
      </div>
      <!-- milestones/roadmap/other info -->
      <h3
        id="roadmap-headline"
        class="pt-4 px-3 text-xs font-semibold text-gray-500 uppercase tracking-wider"
      >
        Roadmap
      </h3>
      <div
        class="mt-1 space-y-1"
        role="group"
        aria-labelledby="roadmap-headline"
      >
        <a
          v-for="item in misc_nav"
          :key="item.name"
          target="_blank"
          :href="item.href"
          class="group flex items-center px-3 py-2 text-sm font-medium text-gray-700 rounded-md hover:text-gray-900 hover:bg-gray-50"
        >
          <component
            :is="item.icon"
            class="text-gray-400 group-hover:text-gray-500 mr-3 flex-shrink-0 h-6 w-6"
            aria-hidden="true"
          />
          {{ item.name }}
        </a>
      </div>

      <h3
        id="badges-headline"
        class="pt-4 px-3 text-xs font-semibold text-gray-500 uppercase tracking-wider"
      >
        Achievements
      </h3>
      <div
        class="mt-1 space-y-1"
        role="group"
        aria-labelledby="badges-headline"
      >
        <span
          v-for="item in achievementStore.achievements"
          :key="item.type"
          class="pn-achievement-badge mt-2 inline-flex items-center px-3 py-0.5 rounded-full text-sm font-medium bg-indigo-100 text-indigo-800"
        >
          {{ item.type }}
        </span>
      </div>
    </div>
  </nav>
</template>
<script setup lang="ts">
import { RouterLink, useRouter } from "vue-router";
import {
  HomeIcon,
  QuestionMarkCircleIcon,
  DocumentDownloadIcon,
  ExclamationIcon,
  ChatIcon,
  MapIcon,
  CogIcon,
  SparklesIcon,
  CodeIcon,
  TerminalIcon,
  SupportIcon,
} from "@heroicons/vue/outline";
import { useAchievementsStore } from "@/stores/achievements";

const achievementStore = useAchievementsStore();
achievementStore.fetchAchievements();

const router = useRouter();
// app-based navigiation links
const app_nav = [
  {
    name: "My Network",
    link: { name: "devices" },
    icon: HomeIcon,
    current: () => router.currentRoute.value.name == "devices",
  },
  {
    name: "Crash Reports",
    link: { name: "crash-reports" },
    icon: SupportIcon,
    current: () => router.currentRoute.value.name == "crash-reports",
  },
  {
    name: "Member Swag",
    link: { name: "swag" },
    icon: SparklesIcon,
    current: () => router.currentRoute.value.path.includes("swag"),
  },
  {
    name: "Settings",
    link: { name: "networkSettings" },
    icon: CogIcon,
    current: () => router.currentRoute.value.path.includes("settings"),
  },
];

// external hrefs
const help_nav = [
  {
    name: "Quick Start",
    href: "https://printnanny.ai/docs/category/quick-start/",
    icon: QuestionMarkCircleIcon,
  },
  {
    name: "API Docs",
    href: import.meta.env.VITE_PRINTNANNY_API_REDOCS_URL,
    icon: CodeIcon,
  },
  {
    name: "Report Issue",
    href: "https://github.com/bitsy-ai/printnanny-os/issues/new/choose",
    icon: ExclamationIcon,
  },
  {
    name: "Join Discord",
    href: "https://discord.gg/sf23bk2hPr",
    icon: ChatIcon,
  },
];

const misc_nav = [
  {
    name: "Latest Release",
    href: "https://printnanny.ai/docs/release-history/0.2.0-beryl-kirkstone/",
    icon: DocumentDownloadIcon,
  },
  {
    name: "In Development",
    href: "https://github.com/bitsy-ai/printnanny-os/milestones",
    icon: MapIcon,
  },
];
</script>
