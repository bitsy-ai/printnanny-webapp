<template>
  <div class="bg-white min-h-screen items-stretch flex flex-col">
    <div class="flex-1 flex flex-col">
      <Transition
        enter-active-class="duration-300 ease-out"
        enter-from-class="transform opacity-0"
        enter-to-class="opacity-100"
        leave-active-class="duration-200 ease-in"
        leave-from-class="opacity-100"
        leave-to-class="transform opacity-0"
        appear
      >
        <Popover as="header" class="relative">
          <div class="bg-gray-900 py-6">
            <nav
              class="relative max-w-7xl mx-auto flex items-center justify-between px-4 sm:px-6"
              aria-label="Global"
            >
              <div class="flex items-center flex-1">
                <div class="flex items-center justify-between w-full md:w-auto">
                  <a href="/">
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
                      <Bars3Icon class="h-6 w-6" aria-hidden="true" />
                    </PopoverButton>
                  </div>
                </div>
                <div class="hidden space-x-8 md:flex md:ml-10">
                  <FlyoutMenu
                    id="learn-more-flyout"
                    :links="learnMoreLinks"
                    menu-text="Learn More"
                  />
                  <FlyoutMenu
                    id="community-flyout"
                    :links="communityLinks"
                    menu-text="Join the Community"
                  />
                  <FlyoutMenu
                    id="shop-flyout"
                    :links="shopLinks"
                    menu-text="Shop"
                  />
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
      </Transition>
      <StickyAlerts />

      <!-- Main content area -->
      <div class="flex-1 flex flex-col justify-center shadow bg-white">
        <RouterView v-slot="{ Component }">
          <template v-if="Component">
            <Transition
              enter-active-class="duration-300 ease-out"
              enter-from-class="transform opacity-0"
              enter-to-class="opacity-100"
              leave-active-class="duration-200 ease-in"
              leave-from-class="opacity-100"
              leave-to-class="transform opacity-0"
              appear
            >
              <KeepAlive>
                <Suspense>
                  <!-- main content -->
                  <component :is="Component"></component>

                  <!-- loading state -->
                  <template #fallback>
                    <p class="text-center font-medium text-lg">Loading ...</p>
                  </template>
                </Suspense>
              </KeepAlive>
            </Transition>
          </template>
        </RouterView>
      </div>

      <FooterNav />
    </div>
  </div>
</template>
<script setup lang="ts">
import { Bars3Icon } from "@heroicons/vue/24/outline";
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
    routerLink: { name: "shop-founding-membership" },
    description: "Get early access to PrintNanny",
  } as FlyoutMenuLink,
  {
    name: "PrintNanny SDWire",
    routerLink: { name: "shop-sdwire" },
    description: "Compatible with OctoPrint-SDWire",
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
    href: "https://printnanny.ai/docs/category/quick-start/",
    blank: true,
  } as FlyoutMenuLink,
  {
    name: "Founding Member FAQ",
    description:
      "Founding Members get unlimited access to PrintNanny at a flat rate.",
    href: "https://printnanny.ai/docs/faq/founding-membership/",
    blank: true,
  } as FlyoutMenuLink,
  {
    name: "How do I update PrintNanny?",
    description:
      "No-hassle updates with a web UI. Automated backup & recovery mode.",
    href: "https://printnanny.ai/docs/update-printnanny-os/",
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
