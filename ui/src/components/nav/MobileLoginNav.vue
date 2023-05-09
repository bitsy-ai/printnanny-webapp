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
      class="z-20 absolute top-0 inset-x-0 transition transform origin-top lg:hidden"
    >
      <div
        class="h-screen p-4 rounded-lg shadow-md bg-gray-900 ring-1 ring-black ring-opacity-5 overflow-hidden"
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
              <XMarkIcon class="h-6 w-6" aria-hidden="true" />
            </PopoverButton>
          </div>
        </div>
        <div class="pt-5 pb-6">
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
import type {
  SimpleFlyoutMenuLink,
  FullWidthFlyoutMenuLink,
  FullWidthFlyoutMenuFooterLink,
} from "@/types/links";
import type { PropType } from "vue";
import { PopoverButton, PopoverPanel } from "@headlessui/vue";
import { XMarkIcon } from "@heroicons/vue/24/outline";
import FullWidthFlyoutMenu from "@/components/nav/FullWidthFlyoutMenu.vue";
import SimpleFlyoutMenu from "@/components/nav/SimpleFlyoutMenu.vue";

defineProps({
  productLinks: {
    type: Object as PropType<Array<FullWidthFlyoutMenuLink>>,
    required: true,
  },
  serviceLinks: {
    type: Object as PropType<Array<FullWidthFlyoutMenuLink>>,
    required: true,
  },
  productFooterLinks: {
    type: Object as PropType<Array<FullWidthFlyoutMenuFooterLink>>,
    required: true,
  },
  communityLinks: {
    type: Object as PropType<Array<SimpleFlyoutMenuLink>>,
    required: true,
  },
  learnMoreLinks: {
    type: Object as PropType<Array<SimpleFlyoutMenuLink>>,
    required: true,
  },
});
</script>
