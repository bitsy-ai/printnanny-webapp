<template>
  <div class="bg-white">
    <div class="relative overflow-hidden">
      <Popover as="header" class="relative">
        <div class="bg-gray-900 pt-6">
          <nav
            class="
              relative
              max-w-7xl
              mx-auto
              flex
              items-center
              justify-between
              px-4
              sm:px-6
            "
            aria-label="Global"
          >
            <div class="flex items-center flex-1">
              <div class="flex items-center justify-between w-full md:w-auto">
                <a href="#">
                  <span class="sr-only">Workflow</span>
                  <img
                    class="h-8 w-auto sm:h-10"
                    src="@/assets/logo/logo-text-rect-white.svg"
                    alt="PrintNanny"
                  />
                </a>
                <div class="-mr-2 flex items-center md:hidden">
                  <PopoverButton
                    class="
                      bg-gray-900
                      rounded-md
                      p-2
                      inline-flex
                      items-center
                      justify-center
                      text-gray-400
                      hover:bg-gray-800
                      focus:outline-none
                      focus:ring-2
                      focus-ring-inset
                      focus:ring-white
                    "
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
              <a
                href="/accounts/login"
                class="text-base font-medium text-white hover:text-gray-300"
              >
                Log in
              </a>
              <a
                href="/request-invite"
                class="
                  inline-flex
                  items-center
                  px-4
                  py-2
                  border border-transparent
                  text-base
                  font-medium
                  rounded-md
                  text-white
                  bg-gray-600
                  hover:bg-gray-700
                "
              >
                Request Access
              </a>
            </div>
          </nav>
        </div>

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
            class="
              absolute
              top-0
              inset-x-0
              p-2
              transition
              transform
              origin-top
              md:hidden
            "
          >
            <div
              class="
                rounded-lg
                shadow-md
                bg-white
                ring-1 ring-black ring-opacity-5
                overflow-hidden
              "
            >
              <div class="px-5 pt-4 flex items-center justify-between">
                <div>
                  <img
                    class="h-8 w-auto"
                    src="@/assets/logo.svg"
                    alt="PrintNanny"
                  />
                </div>
                <div class="-mr-2">
                  <PopoverButton
                    class="
                      bg-white
                      rounded-md
                      p-2
                      inline-flex
                      items-center
                      justify-center
                      text-gray-400
                      hover:bg-gray-100
                      focus:outline-none
                      focus:ring-2
                      focus:ring-inset
                      focus:ring-cyan-600
                    "
                  >
                    <span class="sr-only">Close menu</span>
                    <XIcon class="h-6 w-6" aria-hidden="true" />
                  </PopoverButton>
                </div>
              </div>
              <div class="pt-5 pb-6">
                <div class="px-2 space-y-1">
                  <a
                    v-for="item in navigation"
                    :key="item.name"
                    :href="item.href"
                    class="
                      block
                      px-3
                      py-2
                      rounded-md
                      text-base
                      font-medium
                      text-gray-900
                      hover:bg-gray-50
                    "
                    >{{ item.name }}</a
                  >
                </div>
                <div class="mt-6 px-5">
                  <a
                    href="#"
                    class="
                      block
                      text-center
                      w-full
                      py-3
                      px-4
                      rounded-md
                      shadow
                      bg-gradient-to-r
                      from-indigo-300
                      to-cyan-600
                      text-white
                      font-medium
                      hover:from-teal-600 hover:to-cyan-700
                    "
                    >Request Acesss</a
                  >
                </div>
                <div class="mt-6 px-5">
                  <p class="text-center text-base font-medium text-gray-500">
                    Existing customer?
                    <a href="#" class="text-gray-900 hover:underline">Login</a>
                  </p>
                </div>
              </div>
            </div>
          </PopoverPanel>
        </transition>
      </Popover>
      <main>
        <div
          class="pt-10 bg-gray-900 sm:pt-16 lg:pt-8 lg:pb-14 lg:overflow-hidden"
        >
          <div class="mx-auto">
            <div class="lg:grid lg:grid-cols-2 lg:gap-8">
              <div
                class="
                  mx-auto
                  max-w-md
                  px-4
                  sm:max-w-2xl sm:px-6 sm:text-center
                  lg:px-0 lg:text-left lg:flex lg:items-center
                "
              >
                <div class="lg:py-24">
                  <!-- <a
                    href="#"
                    class="
                      inline-flex
                      items-center
                      text-white
                      bg-black
                      rounded-full
                      p-1
                      pr-2
                      sm:text-base
                      lg:text-sm
                      xl:text-base
                      hover:text-gray-200
                    "
                  >
                    <span
                      class="
                        px-3
                        py-0.5
                        text-white text-xs
                        font-semibold
                        leading-5
                        uppercase
                        tracking-wide
                        bg-gradient-to-r
                        from-teal-500
                        to-cyan-600
                        rounded-full
                      "
                      >New Docs</span
                    >
                    <span class="ml-4 text-sm">Visit our careers page</span>
                    <ChevronRightIcon
                      class="ml-2 w-5 h-5 text-gray-500"
                      aria-hidden="true"
                    />
                  </a> -->
                  <h1
                    class="
                      mt-4
                      text-4xl
                      tracking-tight
                      font-extrabold
                      text-white
                      sm:mt-5 sm:text-6xl
                      lg:mt-6
                      xl:text-6xl
                    "
                  >
                    <span
                      class="
                        block
                        pb-3
                        block
                        bg-clip-text
                        text-transparent
                        bg-gradient-to-r
                        from-indigo-300
                        to-violet-500
                        sm:pb-5
                      "
                      >Stop babysitting</span
                    >
                    <span
                      class="
                        pb-3
                        bg-clip-text
                        text-transparent
                        bg-gradient-to-r
                        from-indigo-200
                        to-violet-400
                        sm:pb-5
                      "
                      >your 3D printer</span
                    >
                    👀
                  </h1>
                  <p
                    class="
                      mt-4
                      text-base text-gray-300
                      sm:text-xl
                      lg:text-lg
                      xl:text-xl
                    "
                  >
                    Receive quality control alerts and live job progress.
                  </p>
                  <p
                    class="
                      mt-4
                      text-base text-gray-300
                      sm:text-xl
                      lg:text-lg
                      xl:text-xl
                    "
                  >
                    Control your printer from anywhere in the world.
                  </p>
                  <p
                    class="
                      mt-4
                      text-base text-gray-300
                      sm:text-xl
                      lg:text-lg
                      xl:text-xl
                    "
                  >
                    Settings and file revisions automatically synced across your
                    devices.
                  </p>
                  <div class="mt-10 sm:mt-12">
                    <form action="#" class="sm:max-w-xl sm:mx-auto lg:mx-0">
                      <div class="sm:flex">
                        <div class="min-w-0 flex-1">
                          <label for="email" class="sr-only"
                            >Email address</label
                          >
                          <input
                            id="email"
                            type="email"
                            placeholder="Enter your email"
                            class="
                              block
                              w-full
                              px-4
                              py-3
                              rounded-md
                              border-0
                              text-base text-gray-900
                              placeholder-gray-500
                              focus:outline-none
                              focus:ring-2
                              focus:ring-offset-2
                              focus:ring-cyan-400
                              focus:ring-offset-gray-900
                            "
                          />
                        </div>
                        <div class="mt-3 sm:mt-0 sm:ml-3">
                          <button
                            type="submit"
                            class="
                              block
                              w-full
                              py-3
                              px-4
                              rounded-md
                              shadow
                              bg-gradient-to-r
                              from-indigo-500
                              to-violet-600
                              text-white
                              font-medium
                              hover:from-indigo-600 hover:to-violet-700
                              focus:outline-none
                              focus:ring-2
                              focus:ring-offset-2
                              focus:ring-cyan-400
                              focus:ring-offset-gray-900
                            "
                          >
                            Request Access
                          </button>
                        </div>
                      </div>
                      <p class="mt-3 text-sm text-gray-300 sm:mt-4">
                        <!-- By providing your email, you agree to our
                        <a href="#" class="font-medium text-white"
                          >terms of service</a
                        >. -->
                      </p>
                    </form>
                  </div>
                </div>
              </div>
              <div class="mt-12 -mb-16 sm:-mb-48 lg:m-0 lg:relative">
                <div
                  class="
                    mx-auto
                    max-w-md
                    px-4
                    sm:max-w-2xl sm:px-6
                    lg:max-w-none lg:px-0
                  "
                >
                  <video
                    autoplay=""
                    muted=""
                    loop=""
                    controls=""
                    class="
                      w-full
                      lg:absolute
                      lg:inset-y-0
                      lg:left-0
                      lg:h-full
                      lg:w-auto
                      lg:max-w-none
                    "
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
        <div class="relative bg-gray-50 pt-16 sm:pt-24 lg:pt-32" id="quality-control">
          <div
            class="
              mx-auto
              max-w-md
              px-4
              text-center
              sm:px-6 sm:max-w-3xl
              lg:px-8 lg:max-w-7xl
            "
          >
            <div>
              <h2
                class="
                  text-base
                  font-semibold
                  tracking-wider
                  text-indigo-600
                  uppercase
                "
              >
                PrintNanny QC
              </h2>
              <p
                class="
                  mt-2
                  text-3xl
                  font-extrabold
                  text-gray-900
                  tracking-tight
                  sm:text-4xl
                "
              >
                🔮 Quality Control that Never Sleeps
              </p>
              <p class="mt-5 max-w-prose mx-auto text-xl text-gray-500">
                Get notified or automatically pause if print doesn't pass quality standards.
              </p>
            </div>
            <div class="mt-12">
              <DemoQualityAlert></DemoQualityAlert>
            </div>
          </div>
        </div>

        <!-- Feature section with grid -->
        <div class="relative bg-white py-16 sm:py-24 lg:py-32" id="printnanny-os">
          <div
            class="
              mx-auto
              max-w-md
              px-4
              text-center
              sm:max-w-3xl sm:px-6
              lg:px-8 lg:max-w-7xl
            "
          >
            <h2
              class="
                text-base
                font-semibold
                tracking-wider
                text-indigo-600
                uppercase
              "
            >
              PrintNanny OS
            </h2>
            <p
              class="
                mt-2
                text-3xl
                font-extrabold
                text-gray-900
                tracking-tight
                sm:text-4xl
              "
            >
              Tame your menagerie of devices
            </p>
            <p class="mt-5 max-w-prose mx-auto text-xl text-gray-500">
              Tired of re-imaging your printer controllers? <br>Mix and match OctoPrint, Repetier, and Mainsail with PrintNanny OS.
            </p>
            <div class="mt-12">
              <div class="grid grid-cols-1 gap-8 sm:grid-cols-2 lg:grid-cols-3">
                <div
                  v-for="feature in features"
                  :key="feature.name"
                  class="pt-6"
                >
                  <div class="flow-root bg-gray-50 rounded-lg px-6 pb-8">
                    <div class="-mt-6">
                      <div>
                        <span
                          class="
                            inline-flex
                            items-center
                            justify-center
                            p-3
                            bg-gradient-to-r
                            from-indigo-500
                            to-violet-600
                            rounded-md
                            shadow-lg
                          "
                        >
                          <component
                            :is="feature.icon"
                            class="h-6 w-6 text-white"
                            aria-hidden="true"
                          />
                        </span>
                      </div>
                      <h3
                        class="
                          mt-8
                          text-lg
                          font-medium
                          text-gray-900
                          tracking-tight
                        "
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

        <!-- Testimonial section -->

        <!-- Blog section -->
        <div class="relative bg-gray-50 py-16 sm:py-24 lg:py-32">
          <div class="relative">
            <div
              class="
                text-center
                mx-auto
                max-w-md
                px-4
                sm:max-w-3xl sm:px-6
                lg:px-8 lg:max-w-7xl
              "
            >
              <h2
                class="
                  text-base
                  font-semibold
                  tracking-wider
                  text-indigo-600
                  uppercase
                "
              >
                Join the Community
              </h2>
              <p
                class="
                  mt-2
                  text-3xl
                  font-extrabold
                  text-gray-900
                  tracking-tight
                  sm:text-4xl
                "
              >
                Learn More
              </p>
              <p class="mt-5 mb-5 mx-auto max-w-prose text-xl text-gray-500">
                Learn more about PrintNanny's development, roadmap, and join an amazing community.
              </p>
              <p>
              <a href="https://discord.gg/sf23bk2hPr" target="_blank" class="bg-indigo-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded mt-4">
                  Join Discord
              </a>
              </p>
            </div>
            <div
              class="
                mt-12
                mx-auto
                max-w-md
                px-4
                grid
                gap-8
                sm:max-w-lg sm:px-6
                lg:px-8 lg:grid-cols-3 lg:max-w-7xl
              "
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
      <footer class="bg-gray-900" aria-labelledby="footer-heading">
        <h2 id="footer-heading" class="sr-only">Footer</h2>
        <div
          class="
            max-w-md
            mx-auto
            pt-12
            px-4
            sm:max-w-7xl sm:px-6
            lg:pt-16 lg:px-8
          "
        >
          <div class="xl:grid xl:grid-cols-3 xl:gap-8">
            <div class="space-y-8 xl:col-span-1">
              <img
                class="h-10"
                src="@/assets/logo/logo-text-rect-white.svg"
                alt="Company name"
              />
              <p class="text-gray-500 text-base">
                Your personal 3D printing assistant.
              </p>
              <div class="flex space-x-6">
                <a
                  v-for="item in footerNavigation.social"
                  :key="item.name"
                  :href="item.href"
                  class="text-gray-400 hover:text-gray-500"
                >
                  <span class="sr-only">{{ item.name }}</span>
                  <component
                    :is="item.icon"
                    class="h-6 w-6"
                    aria-hidden="true"
                  />
                </a>
              </div>
            </div>
            <div class="mt-12 grid grid-cols-2 gap-8 xl:mt-0 xl:col-span-2">
              <div class="md:grid md:grid-cols-2 md:gap-8">
                <div>
                  <h3
                    class="
                      text-sm
                      font-semibold
                      text-gray-400
                      tracking-wider
                      uppercase
                    "
                  >
                    PrintNanny OS
                  </h3>
                  <ul role="list" class="mt-4 space-y-4">
                    <li
                      v-for="item in footerNavigation.printnannyos"
                      :key="item.name"
                    >
                      <a
                        :href="item.href"
                        class="text-base text-gray-500 hover:text-white"
                      >
                        {{ item.name }}
                      </a>
                    </li>
                  </ul>
                </div>
                <div class="mt-12 md:mt-0">
                  <h3
                    class="
                      text-sm
                      font-semibold
                      text-gray-400
                      tracking-wider
                      uppercase
                    "
                  >
                    Support
                  </h3>
                  <ul role="list" class="mt-4 space-y-4">
                    <li
                      v-for="item in footerNavigation.documentation"
                      :key="item.name"
                    >
                      <a
                        :href="item.href"
                        class="text-base text-gray-500 hover:text-white"
                      >
                        {{ item.name }}
                      </a>
                    </li>
                  </ul>
                </div>
              </div>
            </div>
          </div>
          <div class="mt-12 border-t border-gray-200 py-8">
            <p class="text-base text-gray-400 xl:text-center">
              &copy; 2022 Bitsy AI Labs, LLC. All rights reserved.
            </p>
          </div>
        </div>
      </footer>
    </div>
  </div>
</template>
<script setup lang="ts">
import { defineComponent, h } from "vue";
import { Popover, PopoverButton, PopoverPanel } from "@headlessui/vue";
import {
  CloudUploadIcon,
  CogIcon,
  LockClosedIcon,
  MenuIcon,
  RefreshIcon,
  ServerIcon,
  ShieldCheckIcon,
  XIcon,
  FolderOpenIcon,
  GlobeIcon,
  VideoCameraIcon,
  DesktopComputerIcon
} from "@heroicons/vue/outline";
import { ChevronRightIcon, ExternalLinkIcon } from "@heroicons/vue/solid";
import DemoQualityAlert from "@/components/demo/DemoQualityAlert.vue";
import googleIoImg from "@/assets/press/google-io.png";
import tfEverywhereImg from "@/assets/press/tensorflow-everywhere-na.png";

const navigation = [
  { name: "Quality Control", href: "#quality-control" },
  { name: "PrintNanny OS", href: "#printnanny-os" },
  { name: "Join Discord", href: "https://discord.gg/sf23bk2hPr" },
  { name: "Quick Start", href: "https://docs.printnanny.ai/docs/category/quick-start/" },
];
const features = [
  {
    name: "One Install to Rule them All",
    description:
      "Raspberry Pi 4 is fully supported, with Raspberry Pi 3 and Rock Pi in development.",
    icon: DesktopComputerIcon,
  },
  {
    name: "Sync & Backup Files",
    description:
      "Tame your model revisions and gcode with SyncThing, built with privacy in mind.",
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
    icon: GlobeIcon ,
  },
];
const blogPosts = [
  {
    id: 2,
    title: "Launching an AI/ML Product as a Solo Founder",
    href: "https://towardsdatascience.com/soft-launching-an-ai-ml-product-as-a-solo-founder-87ee81bbe6f6",
    date: "Apr 19, 2021",
    datetime: "2021-04-19",
    category: { name: "Featured in Towards Data Science", href: "https://towardsdatascience.com/soft-launching-an-ai-ml-product-as-a-solo-founder-87ee81bbe6f6" },
    imageUrl:
      "https://miro.medium.com/proxy/0*1zq-gwSYQip4eoid",
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
    category: { name: "Video", href: "https://www.youtube.com/watch?v=eJqV5nPjOZQ&t=8559" },
    imageUrl:  tfEverywhereImg,
    preview:
      "How PrintNanny's ensemble detection algorithm works.",
    readingLength: "60 min",
  },
  {
    id: 3,
    title: "PrintNanny @ Google I/O",
    href: "https://bit.ly/google-io-21-print-nanny",
    date: "Feb 12, 2021",
    datetime: "2021-02-12",
    category: { name: "Slide Deck", href: "https://bit.ly/google-io-21-print-nanny" },
    imageUrl: googleIoImg,
    preview:
      "Training & evaluating PrintNanny's first detection model",
    readingLength: "10 min",
  },
];
const footerNavigation = {
  printnannyos: [
    { name: "Roadmap & Milestones", href: "https://github.com/bitsy-ai/printnanny-os/milestones" },
    { name: "Search Open Issues", href: "https://github.com/bitsy-ai/printnanny-os/issues" },
    { name: "Create New Issue", href: "https://github.com/bitsy-ai/printnanny-os/issues/new/choose" },
  ],
  documentation: [
    { name: "Quick Start", href: "https://docs.printnanny.ai/docs/category/quick-start/" },
    { name: "Release History", href: "https://docs.printnanny.ai/docs/release-history/" },
    { name: "API Status", href: "/health" },
  ],
  company: [
    { name: "About", href: "#" },
    { name: "Blog", href: "#" },
    { name: "Jobs", href: "#" },
    { name: "Press", href: "#" },
    { name: "Partners", href: "#" },
  ],
  legal: [
    { name: "Claim", href: "#" },
    { name: "Privacy", href: "#" },
    { name: "Terms", href: "#" },
  ],
  social: [

    {
      name: "Twitter",
      href: "https://twitter.com/grepLeigh",
      icon: defineComponent({
        render: () =>
          h("svg", { fill: "currentColor", viewBox: "0 0 24 24" }, [
            h("path", {
              d: "M8.29 20.251c7.547 0 11.675-6.253 11.675-11.675 0-.178 0-.355-.012-.53A8.348 8.348 0 0022 5.92a8.19 8.19 0 01-2.357.646 4.118 4.118 0 001.804-2.27 8.224 8.224 0 01-2.605.996 4.107 4.107 0 00-6.993 3.743 11.65 11.65 0 01-8.457-4.287 4.106 4.106 0 001.27 5.477A4.072 4.072 0 012.8 9.713v.052a4.105 4.105 0 003.292 4.022 4.095 4.095 0 01-1.853.07 4.108 4.108 0 003.834 2.85A8.233 8.233 0 012 18.407a11.616 11.616 0 006.29 1.84",
            }),
          ]),
      }),
    },
    {
      name: "GitHub",
      href: "https://github.com/bitsy-ai/printnanny-os",
      icon: defineComponent({
        render: () =>
          h("svg", { fill: "currentColor", viewBox: "0 0 24 24" }, [
            h("path", {
              "fill-rule": "evenodd",
              d: "M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.531 1.032 1.531 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z",
              "clip-rule": "evenodd",
            }),
          ]),
      }),
    },
  ],
};
</script>
