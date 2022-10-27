<script setup lang="ts">
import { RouterLink, useRouter } from "vue-router";
import { useAccountStore } from "@/stores/account";
import { useAchievementsStore } from "@/stores/achievements";
import {
  HomeIcon,
  QuestionMarkCircleIcon,
  DocumentDownloadIcon,
  ExclamationIcon,
  ChatIcon,
  MapIcon,
  CogIcon,
} from "@heroicons/vue/outline";

const router = useRouter();

const achievementStore = useAchievementsStore();
const accountStore = useAccountStore();
// app-based navigiation links
const app_nav = [
  {
    name: "My Network",
    link: { name: "devices" },
    icon: HomeIcon,
    current: router.currentRoute.value.name == "devices",
  },
  {
    name: "Settings",
    link: { name: "alertSettings" },
    icon: CogIcon,
    current: router.currentRoute.value.path.includes("settings"),
  },
];

// external hrefs
const help_nav = [
  {
    name: "Quick Start",
    href: "https://docs.printnanny.ai/docs/category/quick-start/",
    icon: QuestionMarkCircleIcon,
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
    href: "https://docs.printnanny.ai/docs/release-history/0.2.0-beryl-kirkstone/",
    icon: DocumentDownloadIcon,
  },
  {
    name: "In Development",
    href: "https://github.com/bitsy-ai/printnanny-os/milestones",
    icon: MapIcon,
  },
];
</script>
<template>
  <div class="mt-5 flex-1 h-0 overflow-y-auto">
    <nav class="px-2">
      <div class="space-y-1">
        <router-link
          v-for="item in app_nav"
          :key="item.name"
          :to="item.link"
          :class="[
            item.current
              ? 'bg-gray-100 text-gray-900'
              : 'text-gray-600 hover:text-gray-900 hover:bg-gray-50',
            'group flex items-center px-2 py-2 text-base leading-5 font-medium rounded-md',
          ]"
          :aria-current="item.current ? 'page' : undefined"
        >
          <component
            :is="item.icon"
            :class="[
              item.current
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
        <h3
          id="mobile-teams-headline"
          class="px-3 text-xs font-semibold text-gray-500 uppercase tracking-wider"
        >
          Help & Support
        </h3>
        <div
          class="mt-1 space-y-1"
          role="group"
          aria-labelledby="mobile-teams-headline"
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
      </div>
      <div class="mt-8">
        <h3
          id="mobile-teams-headline"
          class="px-3 text-xs font-semibold text-gray-500 uppercase tracking-wider"
        >
          Roadmap
        </h3>
        <div
          class="mt-1 space-y-1"
          role="group"
          aria-labelledby="mobile-teams-headline"
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
    </nav>
  </div>
  <div class="flex-shrink-0 flex items-center px-4">
    <img
      class="w-full"
      src="@/assets/logo/logo-rect-light.svg"
      alt="PrintNanny"
    />
  </div>
</template>
