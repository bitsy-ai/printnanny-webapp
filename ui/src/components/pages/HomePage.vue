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
                Get an AI-powered personal assistant <br />to automate the
                tedious parts of 3D printing.
              </p>
              <div class="mt-10 sm:mt-12">
                <WaitlistForm />
              </div>
              <router-link
                id="skip-the-waitlist"
                :to="{ name: 'shop-founding-membership' }"
              >
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
            <img
              src="@/assets/logo/logo-rect-light.svg"
              class="m-auto h-36 py-2"
            />
            <h2
              class="tracking-tight font-extrabold text-white text-4xl xl:text-6xl pt-8"
            >
              <span class="text-gray-900"
                >Quality Control that Never Sleeps</span
              >
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
            Simple Install for Raspberry Pi
          </p>
          <p class="py-6 max-w-prose mx-auto text-xl text-gray-500">
            PrintNanny OS makes it easy to install your favorite 3D printing
            tools.
          </p>
        </div>
        <div class="grid grid-cols-2 sm:grid-cols-3 gap-4 w-1/2 m-auto py-6">
          <img src="@/assets/images/addons/octoprint/octoprint_512x512.png" />
          <img src="@/assets/images/addons/mainsail/mainsail_512x512.png" />
          <img src="@/assets/images/addons/klipper/klipper_512x512.png" />
          <img src="@/assets/images/addons/moonraker/moonraker_512x256.png" />
          <img src="@/assets/images/addons/syncthing/syncthing_512x256.png" />
          <img src="@/assets/images/addons/tailscale/tailscale_512x256.png" />
        </div>
        <div class="mt-12">
          <div class="grid grid-cols-1">
            <img
              src="@/assets/images/toggle-mainsail-octoprint.gif"
              class="md:w-3/4 w-full m-auto"
            />
            <p class="pb-6 max-w-prose mx-auto text-xl text-gray-500">
              Toggle between <strong>OctoPrint</strong> and
              <strong>Mainsail</strong> without re-imaging your SD card.
            </p>
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
    <div class="relative bg-white p-2 lg:py-6">
      <img
        src="@/assets/images/swupdate-messages.png"
        class="drop-shadow-xl w-full md:w-3/4 lg:w-1/2 m-auto py-6"
      />
    </div>
    <!-- Feature section with grid -->
    <div id="printnanny-os" class="relative bg-white py-4 sm:py-8">
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

          <a href="https://discord.gg/sf23bk2hPr" target="_blank">
            <img
              src="https://img.shields.io/discord/773452324692688956?color=%236366f1&label=discord&style=for-the-badge"
              class="m-auto"
            />
          </a>
          <a
            href="https://discord.gg/sf23bk2hPr"
            target="_blank"
            class="my-12 text-white text-3xl font-extrabold tracking-tight sm:text-4xl bg-indigo-500 w-full m-auto md:w-1/2 block hover:bg-blue-700 text-white py-2 px-4 rounded mt-4 transform md-shadow hover:scale-110 ease-in-out delay-150 duration-300"
          >
            Join Discord
          </a>
          <a
            href="https://printnanny.ai/docs/faq/founding-membership/"
            target="_blank"
            class="my-12 text-white text-3xl font-extrabold tracking-tight sm:text-4xl bg-indigo-500 w-full m-auto md:w-1/2 block hover:bg-blue-700 text-white py-2 px-4 rounded mt-4 transform md-shadow hover:scale-110 ease-in-out delay-150 duration-300"
          >
            Founding Member FAQ
          </a>
        </div>

        <h2
          class="mt-2 text-3xl font-extrabold text-gray-900 tracking-tight sm:text-4xl text-center mt-24"
        >
          Development Blog
        </h2>
        <h2
          class="text-base font-semibold tracking-wider text-indigo-600 uppercase text-center mt-2"
        >
          Deep dive into the nitty-gritty of how PrintNanny works.
        </h2>
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

const releases = [
  {
    date: "Upcoming",
    description: "See what's on the roadmap for January/February 2023.",
    name: "v0.6.0 (January 2023)",
    href: "https://github.com/bitsy-ai/printnanny-os/milestone/6",
    linkText: "Roadmap &rarr;",
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
  {
    date: "28 Aug, 2022",
    description:
      "PrintNanny Cam available from mobile/cellular network. Swagger and Redoc API docs. Cloud UI theme",
    name: "v0.3.0 (Cinnabar)",
    href: "https://printnanny.ai/docs/release-history/0.3.x-cinnabar-kirkstone/",
  },
];

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
      name: "PrintNanny Blog",
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
    title: "Automate Image Annotation",
    href: "https://bitsy.ai/real-time-object-tracking-with-tensorflow--raspberry-pi--and-pan-tilt-hat/",
    date: "Nov 2, 2020",
    datetime: "2020-11-02",
    category: {
      name: "PrintNanny Blog",
      href: "https://bitsy.ai/tag/printnanny/",
    },
    imageUrl:
      "https://bitsy.ai/content/images/2021/05/1-xAs0SJR4gvvgcuuySdfmAw.jpeg",
    preview:
      "etect and track an object in real-time using a Raspberry Pi, Pan-Tilt HAT, and TensorFlow. Perfect for hobbyists curious about computer vision & machine learning.",
    readingLength: "12 min",
  },
];
</script>
