<!-- This example requires Tailwind CSS v2.0+ -->
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
      enter-from-class="opacity-0 translate-y-1"
      enter-to-class="opacity-100 translate-y-0"
      leave-active-class="transition ease-in duration-150"
      leave-from-class="opacity-100 translate-y-0"
      leave-to-class="opacity-0 translate-y-1"
    >
      <PopoverPanel
        class="absolute z-10 mt-3 w-screen max-w-xs -translate-x-1/3 transform px-2 sm:px-0"
      >
        <div
          class="overflow-hidden rounded-lg shadow-lg ring-1 ring-black ring-opacity-5"
        >
          <div
            class="relative grid gap-6 bg-gray-900 px-5 py-6 sm:gap-8 sm:p-8"
          >
            <span
              v-for="item in links"
              :key="item.name"
              class="-m-3 block rounded-md p-3 transition duration-150 ease-in-out hover:bg-gray-800"
            >
              <a v-if="item.href && !item.blank" :href="item.href">
                <p class="text-base font-medium text-white">{{ item.name }}</p>
                <p class="mt-1 text-sm text-gray-500">{{ item.description }}</p>
              </a>
              <a
                v-else-if="item.href && item.blank"
                :href="item.href"
                target="_blank"
              >
                <p class="text-base font-medium text-white">{{ item.name }}</p>
                <p class="mt-1 text-sm text-gray-500">{{ item.description }}</p>
              </a>
              <router-link v-else-if="item.routerLink" :to="item.routerLink">
                <p class="text-base font-medium text-white">{{ item.name }}</p>
                <p class="mt-1 text-sm text-gray-500">{{ item.description }}</p>
              </router-link>
            </span>
          </div>
        </div>
      </PopoverPanel>
    </transition>
  </Popover>
</template>

<script setup lang="ts">
import { Popover, PopoverButton, PopoverPanel } from "@headlessui/vue";
import { ChevronDownIcon } from "@heroicons/vue/24/solid";
import type { PropType } from "vue";
import { RouterLink } from "vue-router";
import type { SimpleFlyoutMenuLink } from "@/types/links";

defineProps({
  menuText: {
    type: String,
    default: "Learn More",
  },
  links: {
    type: Object as PropType<Array<SimpleFlyoutMenuLink>>,
    required: true,
  },
});
</script>
