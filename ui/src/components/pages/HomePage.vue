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
                class="text-4xl tracking-tight font-extrabold text-white sm:text-6xl xl:text-6xl"
              >
                <span
                  class="block pb-3 block bg-clip-text text-transparent bg-gradient-to-r from-indigo-300 to-violet-500 sm:pb-5"
                  >Stop babysitting</span
                >
                <span
                  class="pb-3 bg-clip-text text-transparent bg-gradient-to-r from-indigo-200 to-violet-400 sm:pb-5"
                  >your 3D printer</span
                >
                👀
              </h1>
              <h2 class="sm:text-xl md:text-3xl text-white mt-4 mb-4">
                Get a personal assistant for your 3D printer.
              </h2>
              <p
                class="mt-4 text-base text-white sm:text-md lg:text-lg xl:text-lg"
              >
                Quality control alerts. Live print progress.
              </p>
              <p
                class="mt-4 text-base text-white sm:text-md lg:text-lg xl:text-lg"
              >
                Keep files and 3D model revisions in sync.
              </p>
              <p
                class="mt-4 text-base text-white sm:text-md lg:text-lg xl:text-lg"
              >
                15 minute install. Works with OctoPrint, Mainsail + Moonraker +
                Klipper.
              </p>
              <div class="mt-10 sm:mt-12">
                <WaitlistForm />
              </div>
              <router-link :to="{ name: 'founding-membership' }">
                <button
                  class="mt-6 block w-full sm:text-xl lg:text-lg xl:text-xl py-3 px-4 rounded-md shadow bg-gradient-to-r from-red-500 to-violet-600 text-white font-medium hover:from-indigo-600 hover:to-violet-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-cyan-400 focus:ring-offset-gray-900"
                >
                  Skip the waitlist!<br />
                  Founding Members get early access
                </button>
              </router-link>
            </div>
          </div>

          <div class="mt-12 lg:m-0 lg:relative">
            <div
              class="mx-auto max-w-md px-4 sm:max-w-2xl sm:px-6 lg:max-w-none lg:px-0"
            >
              <video
                autoplay="true"
                muted="true"
                loop="true"
                controls="true"
                class="w-full lg:absolute lg:inset-y-0 lg:left-0 lg:h-full lg:w-auto lg:max-w-none"
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
        <div>
          <h2
            class="mt-2 text-3xl font-extrabold text-gray-900 tracking-tight sm:text-4xl"
          >
            Quality Control that Never Sleeps
          </h2>
          <p class="py-6 max-w-prose mx-auto text-xl text-gray-500">
            Get notified or automatically pause if print doesn't pass quality
            standards.
          </p>
          <p
            class="text-base font-semibold tracking-wider text-indigo-600 uppercase mt-2"
          >
            Works with no/low bandwidth
          </p>
          <p
            class="text-base font-semibold tracking-wider text-indigo-600 uppercase mt-2"
          >
            Designed with privacy in mind
          </p>
        </div>
        <div class="mt-12">
          <DemoQualityAlert></DemoQualityAlert>
        </div>
      </div>
    </div>

    <!-- Feature section with grid -->
    <div id="printnanny-os" class="relative bg-white py-16 sm:py-24 lg:py-32">
      <div
        class="mx-auto max-w-md px-4 text-center sm:max-w-3xl sm:px-6 lg:px-8 lg:max-w-7xl"
      >
        <a href="#founding-membership">
          <button
            class="mb-3 inline-flex justify-center rounded-lg font-semibold py-3 px-4 bg-slate-900 text-white hover:bg-slate-700 sm:text-xl bg-gradient-to-r from-red-500 to-violet-600 rounded-md shadow-lg"
          >
            Become a Founding Member
          </button>
        </a>
        <p
          class="mt-2 text-3xl font-extrabold text-gray-900 tracking-tight sm:text-4xl"
        >
          The Operating System for your 3D Printer Farm
        </p>
        <p class="mt-5 max-w-prose mx-auto text-xl text-gray-500">
          PrintNanny OS lets you mix/match OctoPrint + Moonraker + Mainsail +
          Klipper.
        </p>
        <h2
          class="text-base font-semibold tracking-wider text-indigo-600 uppercase mt-2"
        >
          PrintNanny OS
        </h2>
        <div class="mt-12">
          <div class="grid grid-cols-1 gap-8 sm:grid-cols-2 lg:grid-cols-3">
            <div v-for="feature in features" :key="feature.name" class="pt-6">
              <div class="flow-root bg-gray-50 rounded-lg px-6 pb-8">
                <div class="-mt-6">
                  <div>
                    <span
                      class="inline-flex items-center justify-center p-3 bg-gradient-to-r from-indigo-500 to-violet-600 rounded-md shadow-lg"
                    >
                      <component
                        :is="feature.icon"
                        class="h-6 w-6 text-white"
                        aria-hidden="true"
                      />
                    </span>
                  </div>
                  <h3
                    class="mt-8 text-lg font-medium text-gray-900 tracking-tight"
                  >
                    {{ feature.name }}
                  </h3>
                  <p class="mt-5 text-base text-gray-500">
                    {{ feature.description }}
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="mt-12 flex grid grid-cols-1 md:grid-cols-2 gap-4">
          <div class="flex-1">
            <p
              class="mt-2 text-3xl font-extrabold text-gray-900 tracking-tight sm:text-4xl"
            >
              Easy Configuration
              <br />+ <br />Over-the-Air Updates
            </p>
            <p class="mt-5 max-w-prose mx-auto text-xl text-gray-500">
              Tired of burning SD cards? <br />
              Are you still manually configuring your Raspberry Pis?
            </p>
            <p
              class="text-base font-semibold tracking-wider text-indigo-600 uppercase mt-5 mb-5"
            >
              Install once
            </p>
            <p
              class="text-base font-semibold tracking-wider text-indigo-600 uppercase mt-5 mb-5"
            >
              Easy customization Powered by cloud-init
            </p>
            <p
              class="text-base font-semibold tracking-wider text-indigo-600 uppercase mt-5 mb-5"
            >
              Configure hostname, wifi, locale, ssh
            </p>
            <p
              class="text-base font-semibold tracking-wider text-indigo-600 uppercase mt-5 mb-5"
            >
              Apply updates with web ui
            </p>
          </div>
          <div class="flex-1 hidden md:show">
            <img src="@/assets/images/swupdate-messages.png" />
          </div>
        </div>
      </div>
    </div>

    <!-- founding member offer section -->
    <section
      id="founding-membership"
      aria-labelledby="sale-heading"
      class="relative mx-auto flex max-w-7xl flex-col items-center px-4 sm:py-24 lg:py-32 text-center sm:px-6 lg:px-8 rounded-md shadow bg-gradient-to-r from-red-500 to-indigo-600 py-16 sm:py-24 lg:py-32"
    >
      <div class="mx-auto max-w-2xl lg:max-w-none">
        <h2
          id="sale-heading"
          class="text-4xl font-bold tracking-tight text-gray-900 sm:text-5xl lg:text-6xl"
        >
          <span class="text-white">Founding Members</span> enjoy early access
        </h2>
        <p class="mx-auto mt-4 max-w-xl text-xl text-white">
          <strong
            >No metered usage. <br />No monthly addons. <br /><span
              class="text-gray-900 text-sm"
              >24/7 printer monitoring with no hidden costs.</span
            >
          </strong>
        </p>
        <p class="mx-auto mt-4 max-w-xl text-xl text-white">
          <strong
            >#members-only Discord channel. <br /><span
              class="text-gray-900 text-sm"
              >Drive PrintNanny's roadmap.</span
            >
          </strong>
        </p>
        <p class="mx-auto mt-4 max-w-xl text-xl text-white">
          <strong
            >$99 / year early access price<br />
            <s class="text-gray-900 text-sm">$199 / year public launch price</s>
          </strong>
        </p>
        <a
          href="/shop/founding-membership"
          class="mt-6 sm:text-3xl inline-block w-full rounded-md border border-transparent bg-gray-900 py-3 px-8 font-medium text-white hover:bg-gray-800 sm:w-auto"
          >Get Early Access Now</a
        >
        <p class="mx-auto mt-4 max-w-xl text-xl text-white">
          <strong
            >Money-back Guarantee.<br /><span class="text-gray-900 text-sm"
              >If you're not 100% satisfied with PrintNanny, email
              leigh@printnanny.ai for a full refund.</span
            ></strong
          >
        </p>
      </div>
    </section>
    <!-- end founding member offer section -->

    <!-- Blog section -->
    <div class="relative bg-gray-50 py-16 sm:py-24 lg:py-32">
      <div class="relative">
        <div
          class="text-center mx-auto max-w-md px-4 sm:max-w-3xl sm:px-6 lg:px-8 lg:max-w-7xl"
        >
          <h2
            class="text-base font-semibold tracking-wider text-indigo-600 uppercase"
          >
            Join the Community
          </h2>
          <p
            class="mt-2 text-3xl font-extrabold text-gray-900 tracking-tight sm:text-4xl"
          >
            Learn More
          </p>
          <p class="mt-5 mb-5 mx-auto max-w-prose text-xl text-gray-500">
            Learn more about PrintNanny's development, roadmap, and join an
            amazing community.
          </p>
          <p>
            <a
              href="https://discord.gg/sf23bk2hPr"
              target="_blank"
              class="bg-indigo-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded mt-4"
            >
              Join Discord
            </a>
          </p>
        </div>
        <div
          class="mt-12 mx-auto max-w-md px-4 grid gap-8 sm:max-w-lg sm:px-6 lg:px-8 lg:grid-cols-3 lg:max-w-7xl"
        >
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
import {
  CogIcon,
  RefreshIcon,
  FolderOpenIcon,
  GlobeIcon,
  VideoCameraIcon,
  DesktopComputerIcon,
} from "@heroicons/vue/outline";
import DemoQualityAlert from "@/components/demo/DemoQualityAlert.vue";

import googleIoImg from "@/assets/press/google-io.png";
import tfEverywhereImg from "@/assets/press/tensorflow-everywhere-na.png";
import WaitlistForm from "@/components/forms/WaitlistForm.vue";

const features = [
  {
    name: "One Install to Rule them All",
    description:
      "Raspberry Pi 4 is fully supported, with Raspberry Pi 3 and Rock Pi in development.",
    icon: DesktopComputerIcon,
  },
  {
    name: "Cloud File Sync",
    description:
      "Like DropBox, but focused on taming model revisions, slicer settings, and gcode macros. Powered by SyncThing.",
    icon: FolderOpenIcon,
  },
  {
    name: "Simple Queues",
    description:
      "Keep track of finished inventory. Re-queue failed jobs on the next available printer.",
    icon: RefreshIcon,
  },
  {
    name: "Share Camera Feed",
    description:
      "Securely share live camera stream with employees, friends, and family.",
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
      "Connect to a secure Wireguard VPN to control your PrintNanny devices from anywhere.",
    icon: GlobeIcon,
  },
];
const blogPosts = [
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
];
</script>
