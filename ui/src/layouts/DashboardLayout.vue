<template>
  <div class="flex flex-col h-screen justify-between">
    <div class="min-h-full">
      <!-- alerts component -->
      <StickyAlerts />
      <TransitionRoot as="template" :show="sidebarOpen">
        <Dialog
          as="div"
          class="relative z-40 lg:hidden"
          @close="sidebarOpen = false"
        >
          <TransitionChild
            as="template"
            enter="transition-opacity ease-linear duration-300"
            enter-from="opacity-0"
            enter-to="opacity-100"
            leave="transition-opacity ease-linear duration-300"
            leave-from="opacity-100"
            leave-to="opacity-0"
          >
            <div class="fixed inset-0 bg-gray-600 bg-opacity-75" />
          </TransitionChild>

          <div class="fixed inset-0 flex z-40">
            <TransitionChild
              as="template"
              enter="transition ease-in-out duration-300 transform"
              enter-from="-translate-x-full"
              enter-to="translate-x-0"
              leave="transition ease-in-out duration-300 transform"
              leave-from="translate-x-0"
              leave-to="-translate-x-full"
            >
              <DialogPanel
                class="relative flex-1 flex flex-col max-w-xs w-full pt-5 pb-4 bg-white"
              >
                <TransitionChild
                  as="template"
                  enter="ease-in-out duration-300"
                  enter-from="opacity-0"
                  enter-to="opacity-100"
                  leave="ease-in-out duration-300"
                  leave-from="opacity-100"
                  leave-to="opacity-0"
                >
                  <div class="absolute top-0 right-0 -mr-12 pt-2">
                    <button
                      type="button"
                      class="ml-1 flex items-center justify-center h-10 w-10 rounded-full focus:outline-none focus:ring-2 focus:ring-inset focus:ring-white"
                      @click="sidebarOpen = false"
                    >
                      <span class="sr-only">Close sidebar</span>
                      <XIcon class="h-6 w-6 text-white" aria-hidden="true" />
                    </button>
                  </div>
                </TransitionChild>
                <MobileSidebarNav />
              </DialogPanel>
            </TransitionChild>
            <div class="flex-shrink-0 w-14" aria-hidden="true">
              <!-- Dummy element to force sidebar to shrink to fit close icon -->
            </div>
          </div>
        </Dialog>
      </TransitionRoot>

      <!-- Static sidebar for desktop -->
      <div
        class="hidden lg:flex lg:flex-col lg:w-64 lg:fixed lg:inset-y-0 lg:border-r lg:border-gray-200 lg:pt-1 lg:pb-4 lg:bg-gray-100"
      >
        <div class="flex items-center flex-shrink-0 px-6">
          <img
            class="h-auto w-full"
            src="@/assets/logo/logo-rect-light.svg"
            alt="PrintNanny"
          />
        </div>
        <!-- Sidebar component, swap this element with another sidebar if you like -->
        <div class="pt-6 h-0 flex-1 flex flex-col overflow-y-auto">
          <!-- User account dropdown -->
          <ProfileMenu />
          <!-- TODO Sidebar Search -->

          <!-- Sidebar Navigation -->
          <SidebarNav />
        </div>
      </div>
      <!-- Main column -->
      <div class="lg:pl-64 flex flex-col">
        <!-- Search header -->
        <div
          class="sticky top-0 z-10 flex-shrink-0 flex h-16 bg-white border-b border-gray-200 lg:hidden"
        >
          <button
            type="button"
            class="px-4 border-r border-gray-200 text-gray-500 focus:outline-none focus:ring-2 focus:ring-inset focus:ring-purple-500 lg:hidden"
            @click="sidebarOpen = true"
          >
            <span class="sr-only">Open sidebar</span>
            <MenuAlt1Icon class="h-6 w-6" aria-hidden="true" />
          </button>
          <div class="flex-1 flex justify-between px-4 sm:px-6 lg:px-8">
            <div class="flex-1 flex">
              <!-- todo mobile search form -->
            </div>
            <div class="flex items-center">
              <!-- Profile dropdown -->
              <MobileProfileMenu />
            </div>
          </div>
        </div>
        <main class="flex-1">
          <!-- Page title & actions -->
          <div
            class="border-b border-gray-200 px-4 py-4 sm:flex sm:items-center sm:justify-between sm:px-6 lg:px-8"
          >
            <div class="flex-1 min-w-0">
              <router-view name="TopBar"> </router-view>
            </div>
            <div class="mt-4 flex sm:mt-0 sm:ml-4">
              <!-- top right section (content-specific action buttons) -->
              <router-view name="TopRight"> </router-view>
            </div>
          </div>
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
        </main>
      </div>
      <BuildInfoFooter />
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";
import {
  Dialog,
  DialogPanel,
  TransitionChild,
  TransitionRoot,
} from "@headlessui/vue";
import { MenuAlt1Icon, XIcon } from "@heroicons/vue/outline";
import ProfileMenu from "@/components/nav/ProfileMenu.vue";
import SidebarNav from "@/components/nav/SidebarNav.vue";
import MobileProfileMenu from "@/components/nav/MobileProfileMenu.vue";
import MobileSidebarNav from "@/components/nav/MobileSidebarNav.vue";
import BuildInfoFooter from "@/components/footer/BuildInfoFooter.vue";
import StickyAlerts from "@/components/alerts/StickyAlerts.vue";
const sidebarOpen = ref(false);
</script>
