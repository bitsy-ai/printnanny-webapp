<!--
  This example requires some changes to your config:
  
  ```
  // tailwind.config.js
  module.exports = {
    // ...
    plugins: [
      // ...
      require('@tailwindcss/typography'),
      require('@tailwindcss/aspect-ratio'),
    ],
  }
  ```
-->
<template>
  <div class="bg-white">
    <div
      class="mx-auto max-w-2xl px-4 py-16 sm:px-6 sm:py-24 lg:max-w-7xl lg:px-8"
    >
      <div class="lg:grid lg:grid-cols-2 lg:items-start lg:gap-x-8">
        <!-- Image gallery -->
        <TabGroup as="div" class="flex flex-col-reverse">
          <!-- Image selector -->
          <div
            class="mx-auto mt-6 hidden w-full max-w-2xl sm:block lg:max-w-none"
          >
            <TabList class="grid grid-cols-4 gap-6">
              <Tab
                v-for="image in product.images"
                :key="image.id"
                v-slot="{ selected }"
                class="relative flex h-24 cursor-pointer items-center justify-center rounded-md bg-white text-sm font-medium uppercase text-gray-900 hover:bg-gray-50 focus:outline-none focus:ring focus:ring-opacity-50 focus:ring-offset-4"
              >
                <span class="sr-only">{{ image.name }}</span>
                <span class="absolute inset-0 overflow-hidden rounded-md">
                  <img
                    :src="image.src"
                    alt=""
                    class="h-full w-full object-cover object-center"
                  />
                </span>
                <span
                  :class="[
                    selected ? 'ring-indigo-500' : 'ring-transparent',
                    'pointer-events-none absolute inset-0 rounded-md ring-2 ring-offset-2',
                  ]"
                  aria-hidden="true"
                />
              </Tab>
            </TabList>
          </div>

          <TabPanels class="aspect-h-1 aspect-w-1 w-full">
            <TabPanel v-for="image in product.images" :key="image.id">
              <img
                :src="image.src"
                :alt="image.alt"
                class="h-full w-full object-cover object-center sm:rounded-lg"
              />
            </TabPanel>
          </TabPanels>
        </TabGroup>

        <!-- Product info -->
        <div class="mt-10 px-4 sm:mt-16 sm:px-0 lg:mt-0">
          <h1 class="text-3xl font-bold tracking-tight text-gray-900">
            {{ product.name }}
          </h1>

          <div class="mt-3">
            <h2 class="sr-only">Product information</h2>
            <p class="text-3xl tracking-tight text-gray-900">
              {{ product.price }} USD
            </p>
          </div>

          <div class="mt-6">
            <h3 class="sr-only">Description</h3>

            <div
              class="space-y-6 text-base text-gray-700"
              v-html="product.description"
            />
            <div class="mt-10 grid grid-cols-1">
              <WaitlistForm
                class="p-4 my-4 bg-gray-100 rounded w-full"
                button-text="Notify Me"
                :interest="api.InterestEnum.Sdwire"
              >
                <p class="mb-2 text-gray-500">
                  Get notified when kits become available:
                </p>
              </WaitlistForm>

              <p class="text-sm">
                Already have all the hardware? Follow the
                <a
                  href="https://printnanny.ai/docs/category/quick-start/"
                  class="text-indigo-500 hover:text-indigo-700"
                  >quick start</a
                >
                to install PrintNanny OS.
              </p>
            </div>
          </div>

          <section aria-labelledby="details-heading" class="mt-12">
            <h2 id="details-heading" class="sr-only">Additional details</h2>

            <div class="divide-y divide-gray-200 border-t">
              <Disclosure
                v-for="detail in product.details"
                :key="detail.name"
                v-slot="{ open }"
                as="div"
                :default-open="detail.defaultOpen"
              >
                <h3>
                  <DisclosureButton
                    class="group relative flex w-full items-center justify-between py-6 text-left"
                  >
                    <span
                      :class="[
                        open ? 'text-indigo-600' : 'text-gray-900',
                        'text-sm font-medium',
                      ]"
                      >{{ detail.name }}</span
                    >
                    <span class="ml-6 flex items-center">
                      <PlusIcon
                        v-if="!open"
                        class="block h-6 w-6 text-gray-400 group-hover:text-gray-500"
                        aria-hidden="true"
                      />
                      <MinusIcon
                        v-else
                        class="block h-6 w-6 text-indigo-400 group-hover:text-indigo-500"
                        aria-hidden="true"
                      />
                    </span>
                  </DisclosureButton>
                </h3>
                <DisclosurePanel as="div" class="prose prose-sm pb-6">
                  <ul role="list">
                    <li v-for="item in detail.items" :key="item">{{ item }}</li>
                  </ul>
                </DisclosurePanel>
              </Disclosure>
            </div>
          </section>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import * as yup from "yup";
import * as api from "printnanny-api-client";
import {
  Tab,
  TabGroup,
  TabList,
  TabPanel,
  TabPanels,
  Disclosure,
  DisclosureButton,
  DisclosurePanel,
} from "@headlessui/vue";
import { useShopStore } from "@/stores/shop";
import { useAlertStore } from "@/stores/alerts";
import type { UiAlert, AlertAction } from "@/types/alerts";
import WaitlistForm from "@/components/forms/WaitlistForm.vue";
import {
  HeartIcon,
  MinusIcon,
  PlusIcon,
  StarIcon,
} from "@heroicons/vue/24/outline";

const imgUrl = new URL("./img.png", import.meta.url).href;

const alertStore = useAlertStore();
const shopStore = useShopStore();

const products = await shopStore.fetchProducts();
const productData = products?.find((p) => p.slug == "sdwire");

// define a validation schema
const schema = yup.object({
  email: yup.string().required().email(),
});

// TODO: load products via API instead of hard-coding

const product = {
  name: "Raspberry Pi 4 Kit (4GB)",
  price: "$199",
  description: "Can't find a Raspberry Pi 4 in stock? We've got you covered.",
  highlights: [
    "Raspberry Pi 4 (4GB)",
    "Raspberry Pi Camera Module 3",
    "Official Raspberry Pi 15W Power Supply, US",
    "Aluminum heatsinks (3-pack)",
  ],
  images: [
    {
      id: 1,
      name: "Raspberry Pi 4B (4GB)",
      alt: "Raspberry Pi 4B (4GB)",
      src: "/ui/images/rpi4-kit/rpi4.svg",
    },
    {
      id: 2,
      name: "Raspberry Pi Camera Module 3",
      alt: "Raspberry Pi Camera Module 3",
      src: "/ui/images/rpi4-kit/camera.svg",
    },
    {
      id: 3,
      name: "Official Raspberry Pi 4 14W Power Supply",
      alt: "Official Raspberry Pi 4 14W Power Supply",
      src: "/ui/images/rpi4-kit/power-supply.svg",
    },

    {
      id: 4,
      name: "Aluminum heat sinks (3-pack)",
      alt: "Aluminum heat sinks (3-pack)",
      src: "/ui/images/rpi4-kit/heatsinks.svg",
    },
  ],
  details: [
    {
      name: "What's included? (hardware)",
      defaultOpen: true,
      items: [
        "Raspberry Pi 4B (4GB)",
        "Raspberry Pi Camera Module 3",
        "Official Raspberry Pi 15W Power Supply, US",
        "Aluminum heatsinks (3-pack)",
        "32 GB SD Card pre-loaded with PrintNanny OS",
      ],
    },
    {
      name: "What's included? (software)",
      defaultOpen: true,
      items: [
        "OctoPrint",
        "Mainsail / Moonraker / Klipper toolchain",
        "Syncthing (like having a personal Dropbox server)",
        "Tailscale VPN (easy remote access)",
      ],
    },
    {
      name: "Shipping, Returns & Refunds",
      defaultOpen: false,
      items: [
        "Flat-rate shipping to all U.S. states and territories.",
        "International shipping available for bulk (10+) orders, please email support@printnanny.ai for details.",
        "90-day money-back guarantee.",
      ],
    },
  ],
};

async function onClick(values: any) {
  if (productData == undefined) {
    const actions = [
      {
        color: "red",
        text: "Refresh",
        onClick: () => {
          window.location.reload();
        },
      },
    ] as Array<AlertAction>;
    const alert: UiAlert = {
      header: "Oops, something went wrong",
      message: "Failed to get product information from Stripe.",
      actions: actions,
      error: "Failed to get product information from Stripe.",
    };
    alertStore.push(alert);
  }
  new Error("SDWire checkout is not implemetned for checkout system v2");
  // if (values && values.email !== undefined && productData !== undefined) {
  //   await shopStore.createCheckoutSession(values.email, [
  //     productData.id,
  //   ] as Array<string>);
  // } else if (
  //   accountStore.isAuthenticated &&
  //   accountStore.user !== undefined &&
  //   productData !== undefined
  // ) {
  //   await shopStore.createCheckoutSession(accountStore.user?.email, [
  //     productData.id,
  //   ] as Array<string>);
  // }
}
</script>
