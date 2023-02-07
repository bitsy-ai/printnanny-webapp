<template>
  <Popover v-slot="{ open }" class="py-4 md:py-0 text-center">
    <PopoverButton
      :class="[
        open ? 'text-white' : 'text-white',
        'group inline-flex items-center w-full rounded-md text-lg font-medium hover:text-indigo-300 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2 py-2 px-4 md:p-0',
      ]"
    >
      <span>{{ menuText }}</span>
      <ChevronDownIcon
        :class="[
          open ? 'text-gray-600' : 'text-gray-400',
          'ml-2 h-5 w-5 group-hover:text-gray-500',
        ]"
        aria-hidden="true"
      />
    </PopoverButton>

    <transition
      enter-active-class="transition ease-out duration-200"
      enter-from-class="opacity-0 -translate-y-1"
      enter-to-class="opacity-100 translate-y-0"
      leave-active-class="transition ease-in duration-150"
      leave-from-class="opacity-100 translate-y-0"
      leave-to-class="opacity-0 -translate-y-1"
    >
      <PopoverPanel class="pt-4 absolute inset-x-0 z-10 transform shadow-lg">
        <div class="bg-white md:py-4">
          <div
            class="mx-auto grid max-w-7xl gap-y-6 p-6 sm:grid-cols-2 sm:gap-8 sm:py-8 lg:grid-cols-4 lg:px-8 lg:py-12 xl:py-16"
          >
            <a
              v-for="item in links"
              :key="item.name"
              :href="item.href"
              class="-m-3 flex flex-col justify-around rounded-lg p-3 transition duration-150 ease-in-out hover:bg-gray-50"
            >
              <div class="flex md:h-full lg:flex-col">
                <div class="flex-shrink-0">
                  <div
                    class="inline-flex h-10 w-10 items-center justify-center rounded-md bg-indigo-500 text-white sm:h-12 sm:w-12"
                  >
                    <component
                      :is="item.icon"
                      class="h-6 w-6"
                      aria-hidden="true"
                    />
                  </div>
                </div>
                <div
                  class="ml-4 md:flex md:flex-1 md:flex-col md:justify-around lg:ml-0 lg:mt-4"
                >
                  <div>
                    <p class="text-base font-medium text-gray-900">
                      {{ item.name }}
                    </p>
                    <p
                      class="mt-1 text-sm text-gray-500"
                      style="white-space: pre-wrap"
                    >
                      {{ item.description }}
                    </p>
                  </div>
                  <p class="mt-2 text-sm font-medium text-indigo-600 lg:mt-4">
                    {{ item.cta }}
                    <span aria-hidden="true"> &rarr;</span>
                  </p>
                </div>
              </div>
            </a>
            <div class="grid grid-cols-2 sm:grid-cols-3 gap-4 m-auto py-6">
              <h2
                class="col-span-3 font-extrabold text-gray-900 tracking-tight sm:text-2xl"
              >
                Mix & Match
              </h2>
              <img
                src="@/assets/images/addons/octoprint/octoprint_512x512.png"
              />
              <img src="@/assets/images/addons/mainsail/mainsail_512x512.png" />
              <img src="@/assets/images/addons/klipper/klipper_512x512.png" />
              <img
                src="@/assets/images/addons/moonraker/moonraker_512x256.png"
              />
              <img
                src="@/assets/images/addons/syncthing/syncthing_512x256.png"
              />
              <img
                src="@/assets/images/addons/tailscale/tailscale_512x256.png"
              />
            </div>
          </div>
        </div>
        <div class="bg-gray-50">
          <div
            class="mx-auto max-w-7xl space-y-6 px-6 py-5 sm:flex sm:space-y-0 sm:space-x-10 lg:px-8"
          >
            <div v-for="item in footer" :key="item.name" class="flow-root">
              <a
                :href="item.href"
                class="-m-3 bg-gray-100 flex items-center rounded-md p-3 text-base font-medium text-gray-900 transition duration-150 ease-in-out hover:bg-gray-200"
              >
                <component
                  :is="item.icon"
                  class="h-6 w-6 flex-shrink-0 text-gray-400"
                  aria-hidden="true"
                />
                <span class="ml-3">{{ item.name }}</span>
              </a>
            </div>
          </div>
        </div>
      </PopoverPanel>
    </transition>
  </Popover>
</template>

<script setup lang="ts">
import type { PropType } from "vue";

import { Popover, PopoverButton, PopoverPanel } from "@headlessui/vue";
import { ChevronDownIcon } from "@heroicons/vue/20/solid";
import {
  ChartBarIcon,
  CheckCircleIcon,
  CursorArrowRaysIcon,
  PhoneIcon,
  PlayIcon,
  ShieldCheckIcon,
  Squares2X2Icon,
} from "@heroicons/vue/24/outline";
import type {
  FullWidthFlyoutMenuLink,
  FullWidthFlyoutMenuFooterLink,
} from "@/types/links";

const props = defineProps({
  menuText: {
    type: String,
    default: "Learn More",
  },
  links: {
    type: Object as PropType<Array<FullWidthFlyoutMenuLink>>,
    required: true,
  },
  footer: {
    type: Object as PropType<Array<FullWidthFlyoutMenuFooterLink>>,
    required: true,
  },
});

const solutions = [
  {
    name: "Analytics",
    description:
      "Get a better understanding of where your traffic is coming from.",
    href: "#",
    icon: ChartBarIcon,
  },
  {
    name: "Engagement",
    description: "Speak directly to your customers in a more meaningful way.",
    href: "#",
    icon: CursorArrowRaysIcon,
  },
  {
    name: "Security",
    description: "Your customers' data will be safe and secure.",
    href: "#",
    icon: ShieldCheckIcon,
  },
  {
    name: "Integrations",
    description: "Connect with third-party tools that you're already using.",
    href: "#",
    icon: Squares2X2Icon,
  },
];
const callsToAction = [
  { name: "Watch Demo", href: "#", icon: PlayIcon },
  { name: "View All Products", href: "#", icon: CheckCircleIcon },
  { name: "Contact Sales", href: "#", icon: PhoneIcon },
];
</script>
