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
                class="tracking-tight font-extrabold text-white text-4xl xl:text-6xl"
              >
                <span
                  class="block pb-2 block bg-clip-text text-transparent rounded-md shadow bg-gradient-to-r from-indigo-400 to-violet-500 sm:pb-2"
                  >Stop Babysitting</span
                >
                <span
                  class="pb-2 bg-clip-text text-transparent rounded-md shadow bg-gradient-to-r from-indigo-400 to-violet-500 sm:pb-2"
                  >your 3D Printer</span
                >
                👀
              </h1>
              <p class="pt-6 max-w-prose mx-auto text-xl text-white">
                Get an AI-powered personal assistant <br>to automate the tedious parts of 3D printing.
              </p>
              <div class="mt-10 sm:mt-12">
                <WaitlistForm />
              </div>
              <router-link :to="{ name: 'shop-founding-membership' }">
                <button
                  class="transform md-shadow hover:scale-110 ease-in-out delay-150 duration-300 mt-6 block w-full sm:text-xl lg:text-lg xl:text-xl py-3 px-4 rounded-md shadow bg-gradient-to-r from-red-500 to-violet-600 text-white font-medium hover:from-red-600 hover:to-violet-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-cyan-400 focus:ring-offset-gray-900"
                >
                  Want to skip the waitlist?<br />
                  Founding Members get early access.
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
                class="w-full lg:absolute lg:inset-y-0 lg:left-0 lg:h-full lg:w-auto lg:max-w-none drop-shadow-2xl"
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
            <img src="@/assets/logo/logo-rect-light.svg" class="m-auto h-36 py-2"/>
            <h2
              class="tracking-tight font-extrabold text-white text-4xl xl:text-6xl pt-8"
            >
              <span class="text-gray-900">Quality Control that Never Sleeps</span>
            </h2>
            <p class="pt-6 max-w-prose mx-auto text-xl text-gray-500">
              Get notified or <strong>automatically pause</strong> if print job
              doesn't pass quality control.
            </p>
          </div>
        </Transition>
        <div class="mt-12">
          <DemoQualityAlert></DemoQualityAlert>
        </div>
        <router-link :to="{ name: 'shop-founding-membership' }">
              <button
                class="text-white text-3xl font-extrabold tracking-tight sm:text-4xl inline-flex justify-center transform md-shadow hover:scale-110 ease-in-out delay-150 duration-300 mt-6 block py-3 px-4 rounded-md shadow bg-gradient-to-r from-red-500 to-violet-600 hover:from-red-600 hover:to-violet-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-cyan-400 focus:ring-offset-gray-900"
              >
                Get Access Now
              </button>
      </router-link>
      </div>
    </div>

    <!-- Feature section with toggle -->
    <div id="quality-control" class="relative bg-gray-50 pt-6 lg:pt-12">
      <div
        class="mx-auto max-w-md px-4 text-center sm:px-6 sm:max-w-3xl lg:px-8 lg:max-w-7xl"
      >
        <div>
          <h2
            class="mt-2 text-3xl font-extrabold text-gray-900 tracking-tight sm:text-4xl"
          >
            Mix & Match Your Favorite Software
          </h2>
          <p
            class="text-base font-semibold tracking-wider text-indigo-600 uppercase mt-2"
          >
            PrintNanny OS + Raspberry Pi
          </p>
          <p class="py-6 max-w-prose mx-auto text-xl text-gray-500">
            Toggle between <strong>OctoPrint</strong> and
            <strong>Mainsail</strong> with PrintNanny OS.
          </p>
        </div>
        <div class="mt-12">
          <div class="grid grid-cols-1">
            <img
              src="@/assets/images/toggle-mainsail-octoprint.gif"
              class="md:w-3/4 w-full m-auto"
            />
          </div>
        </div>
      </div>
    </div>

    <!-- OTA updates -->
    <div id="printnanny-os" class="relative bg-white p-6 lg:py-12">
      <div
        class="mx-auto max-w-md px-4 text-center sm:max-w-3xl sm:px-6 lg:px-8 lg:max-w-7xl"
      >
        <div class="flex-1">
          <h2
            class="mt-2 text-3xl font-extrabold text-gray-900 tracking-tight sm:text-4xl"
          >
            Over-the-air Updates
          </h2>
          <p class="mt-5 max-w-prose mx-auto text-xl text-gray-500">
            <strong>Are you tired of re-imaging SD cards?</strong>
          </p>
          <p
            class="text-base font-semibold tracking-wider text-indigo-600 uppercase mt-5 mb-5"
          >
            Seamless A/B System Updates
          </p>
        </div>
        <div class="flex grid grid-cols-1 md:grid-cols-2 gap-4">
          <div class="flex grid grid-cols-2 gap-2">
            <p
              class="mt-2 text-3xl font-extrabold text-gray-900 tracking-tight sm:text-4xl col-span-2"
            >
              Release History
            </p>
            <div
              class="p-6 rounded-lg shadow-sm bg-gray-50 border border-gray-200"
            >
              <p class="m-0 mb-1 text-sm text-slate-500">27 Dec, 2022</p>
              <h2 class="m-0 mb-6 text-2xl leading-6 text-slate-500">v0.5.0</h2>
              <p class="m-0 mb-6 text-base text-slate-700">
                Tailscale add-on. Edit settings files in your browser. USB
                camera support.
              </p>
              <a
                href="https://printnanny.ai/docs/release-history/0.5.x-emerald-langdale/"
                class="text-base text-indigo-700 hover:text-indigo-500 [text-decoration:none]"
              >
                Release Notes &rarr;
              </a>
            </div>
            <div
              class="p-6 rounded-lg shadow-sm bg-gray-50 border border-gray-200"
            >
              <p class="m-0 mb-1 text-sm text-slate-500">27 Oct, 2022</p>
              <h2 class="m-0 mb-6 text-2xl leading-6 text-slate-500">v0.4.0</h2>
              <p class="m-0 mb-6 text-base text-slate-700">
                Mainsail and Syncthing GA. PrintNanny monitoring works without
                an internet connection.
              </p>
              <a
                href="https://printnanny.ai/docs/release-history/0.4.x-dunite-langdale/"
                class="text-base text-indigo-700 hover:text-indigo-500 [text-decoration:none]"
              >
                Release Notes &rarr;
              </a>
            </div>
          </div>
          <img
            src="@/assets/images/swupdate-messages.png"
            class="drop-shadow-2xl"
          />
        </div>
      </div>
    </div>

    <!-- Feature section with grid -->
    <div id="printnanny-os" class="relative bg-white py-16 sm:py-16">
      <div
        class="mx-auto max-w-md px-4 text-center sm:max-w-3xl sm:px-6 lg:px-8 lg:max-w-7xl"
      >
        <h2
          class="mt-2 text-3xl font-extrabold text-gray-900 tracking-tight sm:text-4xl"
        >
          Ready to get started?
        </h2>
        <router-link :to="{ name: 'shop-founding-membership' }">
          <button
            class="text-white text-3xl font-extrabold tracking-tight sm:text-4xl inline-flex justify-center transform md-shadow hover:scale-110 ease-in-out delay-150 duration-300 mt-6 block py-3 px-4 rounded-md shadow bg-gradient-to-r from-red-500 to-violet-600 hover:from-red-600 hover:to-violet-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-cyan-400 focus:ring-offset-gray-900"
          >
            Become a Founding Member
          </button>
        </router-link>

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
      </div>
    </div>

    <!-- founding member offer section -->
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
            Join an amazing community of entrepreneurs and makers.
          </p>
          <a
            href="https://discord.gg/sf23bk2hPr"
            target="_blank"
            class="text-white text-3xl font-extrabold tracking-tight sm:text-4xl bg-indigo-500 w-full m-auto md:w-1/2 block hover:bg-blue-700 text-white py-2 px-4 rounded mt-4 transform md-shadow hover:scale-110 ease-in-out delay-150 duration-300"
          >
            Join Discord
          </a>
          <a
            href="https://printnanny.ai/docs/faq/founding-membership/"
            target="_blank"
            class="text-white text-3xl font-extrabold tracking-tight sm:text-4xl bg-indigo-500 w-full m-auto md:w-1/2 block hover:bg-blue-700 text-white py-2 px-4 rounded mt-4 transform md-shadow hover:scale-110 ease-in-out delay-150 duration-300"
          >
            Founding Member FAQ
          </a>
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
    name: "Raspberry Pi",
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
      "Connect to a secure Tailscale VPN to control your PrintNanny devices from anywhere.",
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
