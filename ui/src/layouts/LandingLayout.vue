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
              class="relative w-full flex items-center justify-items-center px-4 sm:px-6 lg:px-24"
              aria-label="Global"
            >
              <div class="flex items-center flex-1">
                <div
                  class="grid grid-cols-2 lg:grid-cols-1 items-center justify-items-center w-full lg:w-auto"
                >
                  <a href="/" class="justify-self-start">
                    <span class="sr-only">Workflow</span>
                    <img
                      class="h-8 w-auto sm:h-10"
                      src="@/assets/logo/logo-text-rect-white.svg"
                      alt="PrintNanny"
                    />
                  </a>
                  <div
                    class="-mr-2 flex lg:hidden align-self-end justify-self-end"
                  >
                    <PopoverButton
                      class="bg-gray-900 rounded-md p-2 inline-flex items-center justify-center text-gray-400 hover:bg-gray-800 focus:outline-none focus:ring-2 focus-ring-inset focus:ring-white"
                    >
                      <span class="sr-only">Open main menu</span>
                      <Bars3Icon class="h-6 w-6" aria-hidden="true" />
                    </PopoverButton>
                  </div>
                </div>
                <div class="hidden space-x-8 lg:flex md:ml-10">
                  <FullWidthFlyoutMenu
                    id="products-flyout"
                    :links="productLinks"
                    :footer="productFooterLinks"
                    menu-text="Products & Pricing"
                  />
                  <FullWidthFlyoutMenu
                    id="services-flyout"
                    :links="serviceLinks"
                    :footer="productFooterLinks"
                    menu-text="Services"
                  />
                  <SimpleFlyoutMenu
                    id="learn-more-flyout"
                    :links="learnMoreLinks"
                    menu-text="Learn More"
                  />
                  <SimpleFlyoutMenu
                    id="community-flyout"
                    :links="communityLinks"
                    menu-text="Join the Community"
                  />
                </div>
              </div>
              <LoginNav />
            </nav>
          </div>
          <MobileLoginNav
            :product-links="productLinks"
            :service-links="serviceLinks"
            :product-footer-links="productFooterLinks"
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
import {
  Bars3Icon,
  CloudIcon,
  CpuChipIcon,
  BoltIcon,
  FaceSmileIcon,
  WrenchScrewdriverIcon,
  AcademicCapIcon,
  CubeTransparentIcon,
} from "@heroicons/vue/24/outline";
import LoginNav from "@/components/nav/LoginNav.vue";
import { Popover, PopoverButton } from "@headlessui/vue";
import SimpleFlyoutMenu from "@/components/nav/SimpleFlyoutMenu.vue";
import FullWidthFlyoutMenu from "@/components/nav/FullWidthFlyoutMenu.vue";
import StickyAlerts from "../components/alerts/StickyAlerts.vue";
import FooterNav from "@/components/nav/FooterNav.vue";
import MobileLoginNav from "@/components/nav/MobileLoginNav.vue";

import type {
  SimpleFlyoutMenuLink,
  FullWidthFlyoutMenuLink,
  FullWidthFlyoutMenuFooterLink,
} from "@/types/links";

const productLinks = [
  {
    name: "PrintNanny Cloud",
    id: "nav-cloud-pricing-flyout",
    href: "/pricing",
    description:
      "Manage your 3D printer from anywhere. \n Live monitoring and email alerts. \n Flexible plans with no hidden costs.",
    cta: "Get started",
    icon: CloudIcon,
  } as FullWidthFlyoutMenuLink,
  {
    name: "Raspberry Pi 4 Kit",
    id: "nav-os-flyout",
    href: "/shop/raspberry-pi-4-kit",
    description:
      "Everything you need to get started: \n Raspberry Pi 4, power supply, camera, and pre-loaded SD card.",
    cta: "Learn more",
    icon: CpuChipIcon,
  } as FullWidthFlyoutMenuLink,
  {
    name: "PrintNanny SDWire",
    id: "nav-sdwire-flyout",
    href: "/shop/sdwire",
    description:
      "10x faster gcode transfer to SD cards. \n Compatible with OctoPrint-SDWire plugin.",
    cta: "Learn more",
    icon: BoltIcon,
  } as FullWidthFlyoutMenuLink,
];

const serviceLinks = [
  {
    name: "OEM",
    id: "nav-custom-oem-solutions",
    href: import.meta.env.VITE_OEM_QUOTE_FORM,
    description:
      "Custom development and hardware kit services for original 3D printer equipment manufacturers.",
    cta: "Request a quote",
    icon: CubeTransparentIcon,
  } as FullWidthFlyoutMenuLink,
  {
    name: "On-demand Manufacturing",
    id: "nav-custom-on-demand-solutions",
    href: import.meta.env.VITE_ENTERPRISE_CLOUD_QUOTE_FORM,
    description:
      "Custom development and solutions for your on-demand manufacturing operation.",
    cta: "Request a quote",
    icon: WrenchScrewdriverIcon,
  } as FullWidthFlyoutMenuLink,
  {
    name: "K-12 & Higher Education",
    id: "nav-custom-edu-solutions",
    href: import.meta.env.VITE_EDU_QUOTE_FORM,
    description:
      "Custom solutions for schools, libraries, research lkabs, and makerspaces.",
    cta: "Request a quote",
    icon: AcademicCapIcon,
  } as FullWidthFlyoutMenuLink,
];

const productFooterLinks = [
  {
    name: "Flexible Plans for Hobbyists",
    href: "/pricing",
    icon: FaceSmileIcon,
  },
  {
    name: "Custom Software for OEM & Enterprise",
    href: "/pricing/enterprise",
    icon: WrenchScrewdriverIcon,
  },
  {
    name: "K-12 & Higher Education",
    href: "/pricing/enterprise",
    icon: AcademicCapIcon,
  },
] as Array<FullWidthFlyoutMenuFooterLink>;

const communityLinks = [
  {
    name: "Discord",
    description:
      "Share your latest project. Hang out with friendly makers from around the world.",
    href: "https://discord.gg/sf23bk2hPr",
    blank: true,
  } as SimpleFlyoutMenuLink,
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
  } as SimpleFlyoutMenuLink,
  {
    name: "How do I update PrintNanny?",
    description:
      "No-hassle updates with a web UI. Automated backup & recovery mode.",
    href: "https://printnanny.ai/docs/update-printnanny-os/",
    blank: true,
  } as SimpleFlyoutMenuLink,
  {
    name: "Roadmap & Milestones",
    description: "See what's in store for upcoming PrintNanny OS releases",
    href: "https://github.com/bitsy-ai/printnanny-os/milestones",
    blank: true,
  } as SimpleFlyoutMenuLink,

  {
    name: "API Documentation",
    description:
      "Customize your workflow. Clients available in Typescript, Python, and Rust.",
    href: "/api/schema/redoc/",
  } as SimpleFlyoutMenuLink,
];
</script>
