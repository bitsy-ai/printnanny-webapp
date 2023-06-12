<template>
  <main>
    <div class="bg-gray-900 lg:overflow-hidden">
      <div class="mx-auto">
        <div class="lg:grid lg:grid-cols-2 lg:gap-8">
          <div
            class="mx-auto max-w-md px-4 sm:max-w-2xl sm:px-6 sm:text-center lg:px-0 lg:text-left lg:flex lg:items-center"
          >
            <div class="lg:py-12">
              <h1
                class="col-span-3 tracking-tight font-extrabold text-white text-4xl xl:text-6xl"
              >
                <span
                  class="block pb-2 block bg-clip-text rounded-md shadow bg-gradient-to-r text-white sm:pb-2"
                  >Stop Babysitting</span
                >
                <span
                  class="pb-2 bg-clip-text rounded-md shadow bg-gradient-to-r text-white sm:pb-2"
                  >your 3D Print Farm</span
                >
              </h1>

              <p class="pt-6 max-w-prose mx-auto text-xl text-white">
                AI-powered monitoring and automation for 3D printers.
              </p>
              <router-link id="hero-pricing" :to="{ name: 'demo-submit' }">
                <button
                  class="transform md-shadow hover:scale-110 ease-in-out delay-150 duration-300 mt-6 block w-full sm:text-xl lg:text-lg xl:text-xl py-3 px-4 rounded-md shadow bg-gradient-to-r rounded-md shadow bg-gradient-to-r from-indigo-500 to-violet-600 text-white font-medium hover:from-indigo-600 hover:to-violet-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-cyan-400 focus:ring-offset-gray-900"
                >
                  Try a Risk-Free Demo
                </button>
              </router-link>
            </div>
          </div>

          <div class="mt-12 lg:m-0 lg:relative">
            <div
              class="mx-auto max-w-md px-4 sm:max-w-2xl sm:px-6 lg:max-w-none lg:px-0"
            >
              <video
                id="hero-video"
                muted="true"
                loop="true"
                controls="true"
                preload="metadata"
                autoplay="true"
                class="w-full lg:absolute lg:inset-y-0 lg:left-0 lg:h-full lg:w-auto lg:max-w-none drop-shadow-2xl"
                :poster="'/ui/images/placeholders/demo-video-placeholder-2.png'"
              >
                <source
                  src="https://cdn.printnanny.ai/www/demo-video-2.mp4"
                  type="video/mp4"
                />
              </video>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Feature section with quality control demo -->

    <div id="quality-control" class="relative bg-gray-50 pt-6 lg:pt-12">
      <div
        class="mx-auto max-w-md px-4 text-center sm:px-6 sm:max-w-3xl lg:px-8 lg:max-w-7xl"
      >
        <Transition
          enter-from-class="translate-x-[150%] opacity-0"
          enter-active-class="transition duration-300"
          appear
        >
          <div>
            <h1
              class="tracking-tight font-extrabold text-white text-4xl xl:text-6xl pt-8"
            >
              <span class="text-gray-900"
                >Quality Control that Never Sleeps</span
              >
            </h1>
            <p class="pt-6 max-w-prose mx-auto text-xl text-gray-500">
              Get notified or <strong>automatically pause</strong> if print job
              doesn't pass quality control.
            </p>
            <p class="pt-6 max-w-prose mx-auto text-xl text-gray-500">
              Tap/click videos 👇 to see PrintNanny in action.
            </p>
          </div>
        </Transition>
        <div class="mt-12">
          <DemoQualityAlert></DemoQualityAlert>
        </div>
        <router-link id="hero-pricing" :to="{ name: 'demo-submit' }">
          <button
            class="m-auto w-1/2 mb-2 transform md-shadow hover:scale-110 ease-in-out delay-150 duration-300 mt-6 block w-full sm:text-xl lg:text-lg xl:text-xl py-3 px-4 rounded-md shadow bg-gradient-to-r rounded-md shadow bg-gradient-to-r from-indigo-500 to-violet-600 text-white font-medium hover:from-indigo-600 hover:to-violet-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-cyan-400 focus:ring-offset-gray-900"
          >
            Try a Risk-Free Demo
          </button>
        </router-link>
      </div>
    </div>
    <!-- Feature section with toggle -->
    <div id="quality-control" class="relative bg-white pt-6 lg:pt-12">
      <div
        class="mx-auto max-w-md px-4 text-center sm:px-6 sm:max-w-3xl lg:px-8 lg:max-w-7xl"
      >
        <div>
          <h1
            class="tracking-tight font-extrabold text-white text-4xl xl:text-6xl pt-8"
          >
            <span class="text-gray-900">
              The Operating System for 3D Printing
            </span>
          </h1>
          <p
            class="text-base font-semibold tracking-wider text-indigo-600 uppercase mt-2"
          >
            Simple Install for Raspberry Pi
          </p>
          <p class="py-6 max-w-prose mx-auto text-xl text-gray-500">
            Mix & match your favorite 3D printing tools with PrintNanny OS:
          </p>
        </div>
        <div class="grid grid-cols-2 sm:grid-cols-3 gap-4 w-1/2 m-auto py-6">
          <img
            src="@/assets/images/addons/octoprint/octoprint_512x512.png"
            alt="OctoPrint"
          />
          <img
            src="@/assets/images/addons/mainsail/mainsail_512x512.png"
            alt="Mainsail"
          />
          <img
            src="@/assets/images/addons/klipper/klipper_512x512.png"
            alt="Klipper"
          />
          <img
            src="@/assets/images/addons/moonraker/moonraker_512x256.png"
            alt="Moonraker"
          />
          <img
            src="@/assets/images/addons/syncthing/syncthing_512x256.png"
            alt="Syncthing"
          />
          <img
            src="@/assets/images/addons/tailscale/tailscale_512x256.png"
            alt="Tailscale"
          />
        </div>
        <div class="mt-12">
          <div class="grid grid-cols-1">
            <p class="pb-6 max-w-prose mx-auto text-xl text-gray-500">
              Toggle between <strong>OctoPrint</strong> and
              <strong>Mainsail</strong> without re-imaging your SD card.
            </p>
            <img
              src="@/assets/images/toggle-mainsail-octoprint.gif"
              class="md:w-3/4 w-full m-auto"
            />
          </div>
        </div>
      </div>
    </div>

    <!-- OTA updates -->
    <div id="ota-updates" class="relative bg-gray-50 p-2 lg:py-12">
      <div
        class="mx-auto max-w-md px-4 text-center sm:max-w-3xl sm:px-6 lg:px-8 lg:max-w-7xl"
      >
        <h1
          class="tracking-tight font-extrabold text-white text-4xl xl:text-6xl pt-8"
        >
          <span class="text-gray-900">Over-the-air Updates</span>
        </h1>
        <p class="mt-5 max-w-prose mx-auto text-xl text-gray-500">
          <strong>Are you tired of re-imaging SD cards?</strong>
        </p>
        <p class="max-w-prose mx-auto text-xl text-gray-500 mb-8">
          PrintNanny OS keeps all your favorite tools up-to-date.
        </p>
        <div class="grid grid-cols-1 md:grid-cols-3 md:gap-4">
          <div class="col-span-2 space-y-6">
            <hr
              class="w-64 h-px my-8 mx-auto bg-gray-200 border-0 dark:bg-gray-700"
            />
            <p
              class="text-base font-semibold tracking-wider text-indigo-600 uppercase mt-5 mb-5"
            >
              Deploy rolling updates
            </p>
            <p class="mt-5 max-w-prose mx-auto text-xl text-gray-500">
              Upgrade a PrintNanny OS fleet from any browser.
            </p>
            <router-link id="ota-pricing-starter" :to="{ name: 'pricing' }">
              <button
                class="w-full md:w-3/4 m-auto transform md-shadow hover:scale-110 ease-in-out delay-150 duration-300 mt-6 block w-full sm:text-xl lg:text-lg xl:text-xl py-3 px-4 rounded-md shadow bg-gradient-to-r rounded-md shadow bg-gradient-to-r from-indigo-500 to-violet-600 text-white font-medium hover:from-indigo-600 hover:to-violet-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-cyan-400 focus:ring-offset-gray-900"
              >
                Get Started for $9.99/month
              </button>
            </router-link>
            <hr
              class="w-64 h-px my-8 mx-auto bg-gray-200 border-0 dark:bg-gray-700"
            />
            <p
              class="text-base font-semibold tracking-wider text-indigo-600 uppercase mt-5 mb-5"
            >
              Custom packages available for enterprise
            </p>
            <p class="mt-5 max-w-prose mx-auto text-xl text-gray-500">
              Distribute your own software packages and gcode macros.
            </p>
            <router-link
              id="hero-enterprise-quote"
              :to="{ name: 'pricing-enterprise' }"
            >
              <button
                class="w-full md:w-3/4 m-auto transform md-shadow hover:scale-110 ease-in-out delay-150 duration-300 mt-6 block w-full sm:text-xl lg:text-lg xl:text-xl py-3 px-4 rounded-md shadow bg-gradient-to-r rounded-md shadow bg-gradient-to-r from-indigo-500 to-violet-600 text-white font-medium hover:from-indigo-600 hover:to-violet-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-cyan-400 focus:ring-offset-gray-900"
              >
                Get a Quote for Enterprise OTA
              </button>
            </router-link>
          </div>
          <img
            :src="OTA_FEATURE_IMAGE"
            class="drop-shadow-xl w-full m-auto pt-6 md:pt-0 py-2 md:col-span-1 rounded-md"
          />
        </div>
      </div>
    </div>

    <!-- vcs settings -->
    <div id="vcs-settings" class="relative bg-white p-6 lg:py-12">
      <div
        class="mx-auto max-w-md px-4 text-center sm:max-w-3xl sm:px-6 lg:px-8 lg:max-w-7xl"
      >
        <h1
          class="tracking-tight font-extrabold text-white text-4xl xl:text-6xl pt-8"
        >
          <span class="text-gray-900">Settings & Macro Editor</span>
        </h1>
        <p class="mt-5 max-w-prose mx-auto text-xl text-gray-500">
          <strong>Tweak your settings without opening an SSH terminal.</strong>
        </p>
        <p class="mt-5 max-w-prose mx-auto text-xl text-gray-500">
          <strong>Easy sync for gcode macros.</strong>
        </p>
        <router-link id="settings-pricing-starter" :to="{ name: 'pricing' }">
          <button
            class="w-full md:w-1/3 m-auto transform md-shadow hover:scale-110 ease-in-out delay-150 duration-300 mt-6 block w-full sm:text-xl lg:text-lg xl:text-xl py-3 px-4 rounded-md shadow bg-gradient-to-r rounded-md shadow bg-gradient-to-r from-indigo-500 to-violet-600 text-white font-medium hover:from-indigo-600 hover:to-violet-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-cyan-400 focus:ring-offset-gray-900"
          >
            Get Started for $9.99/month
          </button>
        </router-link>
        <img
          :src="'/ui/images/demo/browser-edit-settings.png'"
          class="w-full rounded-md p-6"
        />
      </div>
    </div>

    <!-- past releases -->
    <div id="printnanny-os-releases" class="relative bg-gray-50 p-6 lg:py-12">
      <div
        class="mx-auto max-w-md px-4 text-center sm:max-w-3xl sm:px-6 lg:px-8 lg:max-w-7xl"
      >
        <img src="@/assets/logo/logo-rect-light.svg" class="m-auto h-36 mt-6" />
        <h2
          class="tracking-tight font-extrabold text-white text-4xl xl:text-6xl pt-8"
        >
          <span class="text-gray-900">Past Releases</span>
        </h2>
        <p class="my-5 mx-auto max-w-prose text-xl text-gray-500">
          Get development updates delivered to your inbox:
        </p>
        <WaitlistForm class="w-full md:w-1/2 m-auto"></WaitlistForm>
        <div
          class="mt-12 mx-auto max-w-md px-4 grid grid-cols-1 gap-8 sm:max-w-lg sm:px-6 lg:px-8 lg:grid-cols-4 lg:max-w-7xl"
        >
          <div
            v-for="(post, idx) in releases"
            :key="post.name"
            :class="[
              idx > 1 ? 'hidden md:flex md:flex-col' : 'flex flex-col',
              'rounded-lg shadow-lg overflow-hidden',
            ]"
          >
            <div class="flex-1 bg-gray-100 p-6 flex flex-col justify-between">
              <div class="flex-1">
                <p class="text-sm font-medium text-cyan-600">
                  <a :href="post.href" class="hover:underline">
                    {{ post.date }}
                  </a>
                </p>
                <a :href="post.href" class="block mt-2">
                  <p class="text-xl font-semibold text-gray-900">
                    {{ post.name }}
                  </p>
                  <p class="mt-3 text-base text-gray-500">
                    {{ post.description }}
                  </p>
                </a>
                <a
                  :href="post.href"
                  class="text-base text-indigo-700 hover:text-indigo-500 [text-decoration:none]"
                >
                  Release Notes &rarr;
                </a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="relative bg-gray-200 py-16">
      <div class="relative">
        <div id="waitlist" class="relative bg-gray-200">
          <div
            class="grid grid-cols-1 space-y-7 w-full md:w-3/4 lg:w-1/2 m-auto p-2 text-center"
          >
            <h2
              class="tracking-tight font-extrabold text-white text-4xl xl:text-6xl pt-8"
            >
              <span class="text-gray-900">Join the Community</span>
            </h2>
            <h2
              class="text-base font-semibold tracking-wider text-indigo-600 uppercase text-center mt-2"
            >
              Meetups, development updates, and cool Maker projects.
            </h2>

            <a
              href="https://discord.gg/sf23bk2hPr"
              target="_blank"
              class="w-full md:w-1/2 text-center m-auto transform md-shadow hover:scale-110 ease-in-out delay-150 duration-300 mt-6 block w-full sm:text-xl lg:text-lg xl:text-xl py-3 px-4 rounded-md shadow bg-gradient-to-r rounded-md shadow bg-gradient-to-r from-indigo-500 to-violet-600 text-white font-medium hover:from-indigo-600 hover:to-violet-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-cyan-400 focus:ring-offset-gray-900"
            >
              Join Discord
            </a>
            <p class="mt-5 mb-5 mx-auto max-w-prose text-xl text-gray-500">
              <a
                href="https://discord.gg/sf23bk2hPr"
                target="_blank"
                class="py-2"
              >
                <img
                  src="https://img.shields.io/discord/773452324692688956?color=%236366f1&label=discord&style=for-the-badge"
                  class="m-auto"
                />
              </a>
            </p>
          </div>
        </div>

        <div
          class="mt-12 mx-auto max-w-md px-4 grid gap-8 sm:max-w-lg sm:px-6 lg:px-8 lg:grid-cols-3 lg:max-w-7xl"
        >
          <div class="lg:col-span-3 grid space-y-7">
            <h3
              class="mt-2 text-3xl font-extrabold text-gray-900 tracking-tight sm:text-4xl text-center"
            >
              Events & Meetups
            </h3>
            <h2
              class="text-base font-semibold tracking-wider text-indigo-600 uppercase text-center mt-2"
            >
              Subscribe to 3D printing events & meetups in your area
            </h2>
            <WaitlistForm
              class="w-full md:w-1/2 m-auto"
              button-text="Subscribe"
            ></WaitlistForm>

            <h2
              class="text-base font-semibold tracking-wider text-indigo-600 uppercase text-center mt-2"
            >
              We proudly to sponsor Women in 3D Printing (WI3DP) Events
            </h2>
          </div>
          <div
            v-for="(post, idx) in eventPosts"
            :key="idx"
            :class="[
              post.upcoming
                ? 'border-t-8 border-indigo-700'
                : 'border-t-8 border-gray-300',
              'flex flex-col rounded-lg shadow-lg overflow-hidden',
            ]"
          >
            <div class="flex-shrink-0">
              <img
                class="h-48 w-full object-cover"
                :src="post.imageUrl"
                alt=""
              />
            </div>
            <div class="flex-1 bg-white p-6 flex flex-col justify-between">
              <div class="flex-1">
                <p class="text-sm font-medium text-cyan-600">
                  <a :href="post.category.href" class="hover:underline">
                    {{ post.category.name }}
                  </a>
                </p>
                <p class="text-sm font-medium text-gray-600">
                  {{ post.date }}
                  <span
                    v-if="post.upcoming"
                    class="bg-indigo-100 text-indigo-800 text-xs font-medium mr-2 px-2.5 py-0.5 rounded dark:bg-indigo-900 dark:text-indigo-300"
                    >Upcoming</span
                  >
                </p>
                <a :href="post.href" class="block mt-2">
                  <p class="text-xl font-semibold text-gray-900">
                    {{ post.name }}
                  </p>
                  <button
                    v-if="post.upcoming"
                    type="button"
                    class="mt-2 text-white bg-indigo-700 hover:bg-indigo-800 focus:ring-4 focus:outline-none focus:ring-blue-300 rounded-lg text-xl font-semibold px-5 py-2.5 text-center inline-flex items-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
                  >
                    RSVP
                    <svg
                      aria-hidden="true"
                      class="w-5 h-5 ml-2 -mr-1"
                      fill="currentColor"
                      viewBox="0 0 20 20"
                      xmlns="http://www.w3.org/2000/svg"
                    >
                      <path
                        fill-rule="evenodd"
                        d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z"
                        clip-rule="evenodd"
                      ></path>
                    </svg>
                  </button>
                </a>
              </div>
            </div>
          </div>
        </div>
        <div
          class="mt-12 mx-auto max-w-md px-4 grid gap-8 sm:max-w-lg sm:px-6 lg:px-8 lg:max-w-7xl"
        ></div>
        <div
          class="mt-12 mx-auto max-w-md px-4 grid gap-8 sm:max-w-lg sm:px-6 lg:px-8 lg:grid-cols-3 lg:max-w-7xl"
        >
          <div class="lg:col-span-3 grid space-y-7">
            <h3
              class="mt-2 text-3xl font-extrabold text-gray-900 tracking-tight sm:text-4xl text-center"
            >
              Development Blog
            </h3>
            <h2
              class="text-base font-semibold tracking-wider text-indigo-600 uppercase text-center mt-2"
            >
              Deep dive into the nitty-gritty of how PrintNanny works.
            </h2>
            <WaitlistForm class="w-full md:w-1/2 m-auto"></WaitlistForm>
          </div>
          <div
            v-for="post in blogPosts"
            :key="post.id"
            class="flex flex-col rounded-lg shadow-lg overflow-hidden"
          >
            <div class="flex-shrink-0">
              <img
                class="h-48 w-full object-cover"
                :src="post.imageUrl"
                alt=""
              />
            </div>
            <div class="flex-1 bg-white p-6 flex flex-col justify-between">
              <div class="flex-1">
                <p class="text-sm font-medium text-cyan-600">
                  <a :href="post.category.href" class="hover:underline">
                    {{ post.category.name }}
                  </a>
                </p>
                <a :href="post.href" class="block mt-2">
                  <p class="text-xl font-semibold text-gray-900">
                    {{ post.title }}
                  </p>
                  <p class="mt-3 text-base text-gray-500">
                    {{ post.preview }}
                  </p>
                </a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- CTA Section -->
  </main>
</template>
<script setup lang="ts">
import { onMounted } from "vue";
import {
  CogIcon,
  ArrowPathIcon,
  FolderOpenIcon,
  GlobeAltIcon,
  VideoCameraIcon,
  ComputerDesktopIcon,
} from "@heroicons/vue/24/outline";
import DemoQualityAlert from "@/components/demo/DemoQualityAlert.vue";

import googleIoImg from "@/assets/press/google-io.png";
import tfEverywhereImg from "@/assets/press/tensorflow-everywhere-na.png";
import WaitlistForm from "@/components/forms/WaitlistForm.vue";
import { LockOpenIcon } from "@heroicons/vue/24/solid";

onMounted(() => {
  const el = document.querySelector("video#hero-video") as HTMLVideoElement;
  el.playbackRate = 0.5;
  el.play();
});

const OTA_FEATURE_IMAGE = "/ui/images/landing/swupdate-messages-mobile.png";

const releases = [
  {
    date: "8 May, 2023",
    description: "Raspberry Pi Camera V3 Module.",
    name: "v0.7.0 (Garnet)",
    href: "https://printnanny.ai/docs/release-history/0.7.x-garnet-mickledore/",
    linkText: "Release Notes &rarr;",
  },
  {
    date: "23 Jan, 2023",
    description:
      "JPEG snapshots. Timelapse videos. Backup camera recordings to PrintNanny Cloud.",
    name: "v0.6.0 (Feldspar)",
    href: "https://printnanny.ai/docs/release-history/0.6.x-feldspar-langdale/",
    linkText: "Release Notes &rarr;",
  },
  {
    date: "27 Dec, 2022",
    description:
      "Tailscale add-on. Edit settings files in your browser. USB camera support.",
    name: "v0.5.0 (Emerald)",
    href: "https://printnanny.ai/docs/release-history/0.5.x-emerald-langdale/",
    linkText: "Release Notes &rarr;",
  },
  {
    date: "27 Oct, 2022",
    description:
      "Mainsail and Syncthing GA. New device dashboard. PrintNanny monitoring works without an internet connection.",
    name: "v0.4.0 (Dunite)",
    href: "https://printnanny.ai/docs/release-history/0.4.x-dunite-langdale/",
  },
  // {
  //   date: "28 Aug, 2022",
  //   description:
  //     "PrintNanny Cam available from mobile/cellular network. Swagger and Redoc API docs. Cloud UI theme",
  //   name: "v0.3.0 (Cinnabar)",
  //   href: "https://printnanny.ai/docs/release-history/0.3.x-cinnabar-kirkstone/",
  // },
];

const eventPosts = [
  {
    date: "Jul 19, 2023",
    name: "Happy Hour @ Trumpf",
    href: "https://www.eventbrite.com/e/women-in-3d-printing-silicon-valley-happy-hour-tickets-639824059987",
    category: {
      name: "Women in 3D Printing - Silicon Valley",
      href: "https://www.eventbrite.com/o/women-in-3d-printing-wi3dp-silicon-valley-57083828133",
    },
    imageUrl: "/ui/images/landing/wi3dp/wi3dp_trumpf.jpeg",
    upcoming: true,
  },
  {
    date: "April 26, 2023",
    name: "Happy Hour @ Gener8",
    href: "https://www.eventbrite.com/e/women-in-3d-printing-silicon-valley-happy-hour-tickets-606042327917",
    imageUrl: "/ui/images/landing/wi3dp/wi3dp_gener8.jpeg",
    category: {
      name: "Women in 3D Printing - Silicon Valley",
      href: "https://www.eventbrite.com/o/women-in-3d-printing-wi3dp-silicon-valley-57083828133",
    },
    upcoming: false,
  },
  {
    date: "Jan 11, 2023",
    name: "Happy Hour @ Blue River Technology",
    href: "https://www.eventbrite.com/e/women-in-3d-printing-silicon-valley-happy-hour-tickets-471462215177",
    imageUrl: "/ui/images/landing/wi3dp/wi3dp_bluerivertechnology.jpeg",
    category: {
      name: "Women in 3D Printing - Silicon Valley",
      href: "https://www.eventbrite.com/o/women-in-3d-printing-wi3dp-silicon-valley-57083828133",
    },
    upcoming: false,
  },
];

const features = [
  {
    name: "Easy Install",
    description:
      "Get started by installing PrintNanny OS to a Raspberry Pi in less than 5 minutes.",
    icon: ComputerDesktopIcon,
  },
  {
    name: "Cloud File Sync",
    description: "Sync gcode and 3D model files across your 3D printer fleet",
    icon: FolderOpenIcon,
  },
  // TODO
  // {
  //   name: "Simple Queues",
  //   description:
  //     "Keep track of finished inventory. Re-queue failed jobs on the next available printer.",
  //   icon: ArrowPathIcon,
  // },
  {
    name: "Live Camera Feed",
    description:
      "AI-powered monitoring that runs on your Pi, 24/7. No metered usage or hidden costs.",
    icon: VideoCameraIcon,
  },
  {
    name: "Powerful API",
    description:
      "Build your own automation with API clients available for Rust, Typescript, and Python.",
    icon: CogIcon,
  },
  {
    name: "Access from Anywhere",
    description:
      "Connect to a secure Tailscale VPN to control your PrintNanny devices from anywhere.",
    icon: GlobeAltIcon,
  },
  {
    name: "100% Open Source",
    description:
      "Every line of code released under AGPLv3. Contributions back to OctoPrint, AsyncAPI, and Mainsail ecosystems.",
    icon: LockOpenIcon,
  },
];
const blogPosts = [
  {
    id: 4,
    title: "I needed a sold-out SDWire board, so I learned how to fab PCBs",
    date: "Nov 16, 2022",
    dateTime: "2022-11-16",
    category: {
      name: "PrintNanny Blog",
      href: "https://bitsy.ai/tag/printnanny/",
    },
    href: "https://bitsy.ai/preorder-printnanny-sdwire/",
    imageUrl:
      "https://bitsy.ai/content/images/size/w1000/2022/08/SDWire-3D-front-v1.4-r1-2.jpg",
    preview:
      "I desperately needed a Tizen SDWire board to automate smoke tests for PrintNanny OS, but couldn't buy one due to supply shortages. So I learned how to fab PCBs with components made in the USA.",
    readingLength: "4 min",
  },
  {
    id: 2,
    title: "Launching an AI/ML Product as a Solo Founder",
    href: "https://towardsdatascience.com/soft-launching-an-ai-ml-product-as-a-solo-founder-87ee81bbe6f6",
    date: "Apr 19, 2021",
    datetime: "2021-04-19",
    category: {
      name: "Featured in Towards Data Science",
      href: "https://towardsdatascience.com/soft-launching-an-ai-ml-product-as-a-solo-founder-87ee81bbe6f6",
    },
    imageUrl: "https://miro.medium.com/proxy/0*1zq-gwSYQip4eoid",
    preview:
      "The origin story of PrintNanny, plus a technical deep dive into one of the early prototypes.",
    readingLength: "20 min read",
  },
  {
    id: 1,
    title: "PrintNanny @ TensorFlow Everywhere North America",
    href: "https://www.youtube.com/watch?v=eJqV5nPjOZQ&t=8559s",
    date: "Feb 27, 2021",
    datetime: "2021-02-27",
    category: {
      name: "Video",
      href: "https://www.youtube.com/watch?v=eJqV5nPjOZQ&t=8559",
    },
    imageUrl: tfEverywhereImg,
    preview: "How PrintNanny's ensemble detection algorithm works.",
    readingLength: "60 min",
  },
  {
    id: 3,
    title: "PrintNanny @ Google I/O",
    href: "https://bit.ly/google-io-21-print-nanny",
    date: "Feb 12, 2021",
    datetime: "2021-02-12",
    category: {
      name: "Slide Deck",
      href: "https://bit.ly/google-io-21-print-nanny",
    },
    imageUrl: googleIoImg,
    preview: "Training & evaluating PrintNanny's first detection model",
    readingLength: "10 min",
  },
  {
    id: 5,
    title: "Automate Image Annotation",
    href: "https://bitsy.ai/automate-bounding-box-annotation-with-tensorflow-and-automl/",
    date: "Nov 2, 2020",
    datetime: "2020-11-02",
    category: {
      name: "Bitsy.ai Blog",
      href: "https://bitsy.ai/tag/printnanny/",
    },
    imageUrl:
      "https://bitsy.ai/content/images/size/w2000/2021/05/microsoft-vott-custom-tensorflow-js-model.resized-1--1--1.gif",
    preview:
      "How I used TensorFlow.js and Automated Machine Learning (AutoML) to increase the efficiency of manual data labeling.",
    readingLength: "10 min",
  },
  {
    id: 5,
    title: "Real-time object tracking",
    href: "https://bitsy.ai/real-time-object-tracking-with-tensorflow--raspberry-pi--and-pan-tilt-hat/",
    date: "Nov 2, 2020",
    datetime: "2020-11-02",
    category: {
      name: "Bitsy.ai Blog",
      href: "https://bitsy.ai/tag/printnanny/",
    },
    imageUrl:
      "https://bitsy.ai/content/images/2021/05/1-xAs0SJR4gvvgcuuySdfmAw.jpeg",
    preview:
      "Detect and track an object in real-time using a Raspberry Pi, Pan-Tilt HAT, and TensorFlow. Perfect for hobbyists curious about computer vision & machine learning.",
    readingLength: "12 min",
  },
];
</script>
