<script setup land="ts">
import { RouterLink, RouterView } from "vue-router";
</script>

<template>
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
            src="https://tailwindui.com/img/logos/workflow-mark-teal-200-cyan-400.svg"
            alt=""
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
          class="text-base font-medium text-white hover:text-gray-300"
          >{{ item.name }}</a
        >
      </div>
    </div>
    <div class="hidden md:flex md:items-center md:space-x-6">
      <a href="#" class="text-base font-medium text-white hover:text-gray-300">
        Log in
      </a>
      <a
        href="#"
        class="inline-flex items-center px-4 py-2 border border-transparent text-base font-medium rounded-md text-white bg-gray-600 hover:bg-gray-700"
      >
        Start free trial
      </a>
    </div>
  </nav>
</template>
