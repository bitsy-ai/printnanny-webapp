<template>
  <div class="bg-white">
    <div class="relative overflow-hidden">
      <Popover as="header" class="relative">
        <div class="bg-gray-900 pt-6">
          <nav
            class="relative max-w-7xl mx-auto flex items-center justify-between px-4 sm:px-6"
            aria-label="Global"
          >
            <div class="flex items-center flex-1">
              <div class="flex items-center justify-between w-full md:w-auto">
                <a href="#">
                  <span class="sr-only">Workflow</span>
                  <img
                    class="h-8 w-auto sm:h-10"
                    src="@/assets/logo/logo-text-rect-white.svg"
                    alt="PrintNanny"
                  />
                </a>
                <div class="-mr-2 flex items-center md:hidden">
                  <PopoverButton
                    class="bg-gray-900 rounded-md p-2 inline-flex items-center justify-center text-gray-400 hover:bg-gray-800 focus:outline-none focus:ring-2 focus-ring-inset focus:ring-white"
                  >
                    <span class="sr-only">Open main menu</span>
                    <MenuIcon class="h-6 w-6" aria-hidden="true" />
                  </PopoverButton>
                </div>
              </div>
              <div class="hidden space-x-8 md:flex md:ml-10">
                <a
                  v-for="item in navigation"
                  :key="item.name"
                  :href="item.href"
                  :target="item.external ? '_blank' : ''"
                  class="text-base font-medium text-white hover:text-gray-300"
                >
                  {{ item.name }}
                </a>
                <FlyoutMenu :links="learnMoreLinks" menuText="Learn More"/>
                <FlyoutMenu :links="communityLinks" menuText="Join the Community"/>

              </div>
            </div>
            <LoginNav />
          </nav>
        </div>

        <transition
          enter-active-class="duration-150 ease-out"
          enter-from-class="opacity-0 scale-95"
          enter-to-class="opacity-100 scale-100"
          leave-active-class="duration-100 ease-in"
          leave-from-class="opacity-100 scale-100"
          leave-to-class="opacity-0 scale-95"
        >
          <PopoverPanel
            focus
            class="absolute top-0 inset-x-0 p-2 transition transform origin-top md:hidden"
          >
            <div
              class="rounded-lg shadow-md bg-white ring-1 ring-black ring-opacity-5 overflow-hidden"
            >
              <div class="px-5 pt-4 flex items-center justify-between">
                <div>
                  <img
                    class="h-8 w-auto"
                    src="@/assets/logo/logo-text-rect-white.svg"
                    alt="PrintNanny"
                  />
                </div>
                <div class="-mr-2">
                  <PopoverButton
                    class="bg-white rounded-md p-2 inline-flex items-center justify-center text-gray-400 hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-inset focus:ring-cyan-600"
                  >
                    <span class="sr-only">Close menu</span>
                    <XIcon class="h-6 w-6" aria-hidden="true" />
                  </PopoverButton>
                </div>
              </div>
              <div class="pt-5 pb-6">
                <div class="px-2 space-y-1">
                  <a
                    v-for="item in navigation"
                    :key="item.name"
                    :href="item.href"
                    class="block px-3 py-2 rounded-md text-base font-medium text-gray-900 hover:bg-gray-50"
                    >{{ item.name }}</a
                  >
                </div>
                <MobileLoginNav />
              </div>
            </div>
          </PopoverPanel>
        </transition>
      </Popover>


      <StickyAlerts />

        <!-- Main content area -->
        <RouterView v-slot="{ Component }">
            <template v-if="Component">
            <Transition mode="out-in" name="fade">
                <KeepAlive>
                <Suspense>
                    <!-- main content -->
                    <component :is="Component"></component>

                    <!-- loading state -->
                    <template #fallback>
                    <p>Loading ...</p>
                    </template>
                </Suspense>
                </KeepAlive>
            </Transition>
            </template>
        </RouterView>
      <FooterNav />

    </div>
</div>
</template>
<script setup lang="ts">
import {
  MenuIcon,
  XIcon,
} from "@heroicons/vue/outline";
import LoginNav from "@/components/nav/LoginNav.vue";
import { Popover, PopoverButton, PopoverPanel} from "@headlessui/vue";
import FlyoutMenu from "@/components/nav/FlyoutMenu.vue";
import StickyAlerts from "../components/alerts/StickyAlerts.vue";
import FooterNav from "@/components/nav/FooterNav.vue";
import ProfileMenu from "@/components/nav/ProfileMenu.vue";
import SidebarNav from "@/components/nav/SidebarNav.vue";
import MobileProfileMenu from "@/components/nav/MobileProfileMenu.vue";
import MobileSidebarNav from "@/components/nav/MobileSidebarNav.vue";
import MobileLoginNav from "@/components/nav/MobileLoginNav.vue";

import type { FlyoutMenuLink } from "@/types/links";

const navigation = [
  { name: "Quality Control", href: "#quality-control" },
  { name: "PrintNanny OS", href: "#printnanny-os" },
];

const communityLinks = [
    { name: "Discord", description: "Share your latest project. Hang out with friendly makers from around the world.", href: "https://discord.gg/sf23bk2hPr", blank: true} as FlyoutMenuLink,
    { name: "Star the Github project", description: "Show your support. 🌟", href: "https://github.com/bitsy-ai/printnanny-os", blank: true},
    { name: "Follow the Founder", description: "@grepLeigh is an indie hacker building PrintNanny in public.", href: "https://twitter.com/grepLeigh", blank: true}
]

const learnMoreLinks = [
  { name: "Quick Start", description: "Setup PrintNanny OS in 15 minutes.", href: "https://docs.printnanny.ai/docs/category/quick-start/", blank: true} as FlyoutMenuLink,
  { name: "What's inside PrintNanny?", description: "Designed to let you focus on the fun parts of 3D printing.", href: "https://docs.printnanny.ai/docs/category/whats-inside-printnanny/", blank: true} as FlyoutMenuLink,
  { name: "How do I update PrintNanny?", description: "No-hassle updates with a web UI. Automated backup & recovery mode.", href: "https://docs.printnanny.ai/docs/update-printnanny-os/", blank: true} as FlyoutMenuLink,
  { name: "Roadmap & Milestones", description: "See what's in store for upcoming PrintNanny OS releases", href: "https://github.com/bitsy-ai/printnanny-os/milestones", blank: true} as FlyoutMenuLink,

  { name: "API Documentation", description: "Customize your workflow. Clients available in Typescript, Python, and Rust.", href: "/api/schema/redoc/" } as FlyoutMenuLink,
]
</script>