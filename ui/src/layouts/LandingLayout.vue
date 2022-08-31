<template>
  <div class="bg-white">
    <div class="relative overflow-hidden">
      <Popover as="header" class="relative">
        <div class="bg-gray-900 py-6">
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
                <FlyoutMenu :links="learnMoreLinks" menu-text="Learn More" />
                <FlyoutMenu
                  :links="communityLinks"
                  menu-text="Join the Community"
                />
                <FlyoutMenu :links="shopLinks" menu-text="Shop" />
              </div>
            </div>
            <LoginNav />
          </nav>
        </div>
        <MobileLoginNav
          :shop-links="shopLinks"
          :community-links="communityLinks"
          :learn-more-links="learnMoreLinks"
        />
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
import { MenuIcon } from "@heroicons/vue/outline";
import LoginNav from "@/components/nav/LoginNav.vue";
import { Popover, PopoverButton } from "@headlessui/vue";
import FlyoutMenu from "@/components/nav/FlyoutMenu.vue";
import StickyAlerts from "../components/alerts/StickyAlerts.vue";
import FooterNav from "@/components/nav/FooterNav.vue";
import MobileLoginNav from "@/components/nav/MobileLoginNav.vue";

import type { FlyoutMenuLink } from "@/types/links";

const shopLinks = [
  {
    name: "Founding Membership",
    routerLink: { name: "founding-membership" },
    description: "Get early access to PrintNanny",
  } as FlyoutMenuLink,
  {
    name: "PrintNanny SDWire",
    routerLink: { name: "sdwire" },
    description: "Compatible with OctoPrint-SDWire plugin.",
  } as FlyoutMenuLink,
];

const communityLinks = [
  {
    name: "Discord",
    description:
      "Share your latest project. Hang out with friendly makers from around the world.",
    href: "https://discord.gg/sf23bk2hPr",
    blank: true,
  } as FlyoutMenuLink,
  {
    name: "Star the Github project",
    description: "Show your support. 🌟",
    href: "https://github.com/bitsy-ai/printnanny-os",
    blank: true,
  },
  {
    name: "Follow the Founder",
    description: "@grepLeigh is an indie hacker building PrintNanny in public.",
    href: "https://twitter.com/grepLeigh",
    blank: true,
  },
];

const learnMoreLinks = [
  {
    name: "Quick Start",
    description: "Setup PrintNanny OS in 15 minutes.",
    href: "https://docs.printnanny.ai/docs/category/quick-start/",
    blank: true,
  } as FlyoutMenuLink,
  {
    name: "What's inside PrintNanny?",
    description: "Designed to let you focus on the fun parts of 3D printing.",
    href: "https://docs.printnanny.ai/docs/category/whats-inside-printnanny/",
    blank: true,
  } as FlyoutMenuLink,
  {
    name: "How do I update PrintNanny?",
    description:
      "No-hassle updates with a web UI. Automated backup & recovery mode.",
    href: "https://docs.printnanny.ai/docs/update-printnanny-os/",
    blank: true,
  } as FlyoutMenuLink,
  {
    name: "Roadmap & Milestones",
    description: "See what's in store for upcoming PrintNanny OS releases",
    href: "https://github.com/bitsy-ai/printnanny-os/milestones",
    blank: true,
  } as FlyoutMenuLink,

  {
    name: "API Documentation",
    description:
      "Customize your workflow. Clients available in Typescript, Python, and Rust.",
    href: "/api/schema/redoc/",
  } as FlyoutMenuLink,
];
</script>