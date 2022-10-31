<template>
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
        class="rounded-lg shadow-md bg-gradient-to-r from-gray-800 to-gray-900 ring-1 ring-black ring-opacity-5 overflow-hidden"
      >
        <div class="px-5 pt-4 flex items-center justify-between">
            <img
              class="h-8 w-auto"
              src="@/assets/logo/logo-text-rect-white.svg"
              alt="PrintNanny"
            />
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
          <span class="text-white font-medium text-base px-4">Tap to expand sections 👇</span>
          <FlyoutMenu :links="learnMoreLinks" menu-text="Learn More" />
          <FlyoutMenu :links="communityLinks" menu-text="Join the Community" />
          <FlyoutMenu :links="shopLinks" menu-text="Shop" />
          <div class="mt-6 px-5">
            <p
              class="text-center text-base font-medium md:text-gray-500 text-white"
            >
              Existing customer?
              <a
                href="/login"
                class="text-indigo-500 md:text-gray-900 hover:underline"
                >Login</a
              >
            </p>
          </div>
        </div>
      </div>
    </PopoverPanel>
  </transition>
</template>

<script setup lang="ts">
import type { FlyoutMenuLink } from "@/types/links";
import type { PropType } from "vue";
import { PopoverButton, PopoverPanel } from "@headlessui/vue";
import { XIcon } from "@heroicons/vue/outline";

import FlyoutMenu from "@/components/nav/FlyoutMenu.vue";

defineProps({
  shopLinks: {
    type: Object as PropType<Array<FlyoutMenuLink>>,
    required: true,
  },
  communityLinks: {
    type: Object as PropType<Array<FlyoutMenuLink>>,
    required: true,
  },
  learnMoreLinks: {
    type: Object as PropType<Array<FlyoutMenuLink>>,
    required: true,
  },
});
</script>
