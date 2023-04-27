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

            <p class="space-y-6 text-gray-500 text-sm">
              Please allow up to 4 weeks lead time.
            </p>
            <p class="space-y-6 text-gray-500 text-sm">
              Shipping available to United States & U.S. territories.
            </p>
            <Form
              class="mt-6 flex flex-col justify-evenly space-y-6"
              :validation-schema="schema"
              @submit="onClick"
            >
              <div class="w-full">
                <label for="email" class="text-sm font-medium"
                  >Enter your email address to begin:</label
                >
                <Field
                  id="email"
                  name="email"
                  type="email"
                  autocomplete="email"
                  class="border block w-full px-4 py-3 rounded-md text-base text-gray-900 placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-cyan-400 focus:ring-offset-gray-900"
                  placeholder="Email address"
                  rules="required"
                />
                <error-message
                  class="text-red-500 text-sm font-medium"
                  name="email"
                ></error-message>
              </div>
              <div class="w-full">
                <button
                  id="checkout-submit"
                  type="submit"
                  class="block w-full py-3 px-4 rounded-md shadow bg-gradient-to-r from-indigo-500 to-violet-600 text-white text-2xl font-bold tracking-tight text-white text-center hover:from-indigo-600 hover:to-violet-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-cyan-400 focus:ring-offset-gray-900"
                >
                  <CustomSpinner
                    v-if="shop.loading"
                    color="indigo"
                    class="mr-2"
                  ></CustomSpinner>
                  <span v-if="!shop.loading"> Checkout with Stripe </span>
                  <span v-if="shop.loading">
                    Redirecting to Stripe Checkout
                  </span>
                </button>
              </div>
            </Form>
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
import CustomSpinner from "@/components/util/CustomSpinner.vue";
import { Field, ErrorMessage, Form } from "vee-validate";

const sku = "rpi4b-4gb-kit";

const shop = useShopStore();

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
      name: "What's included?",
      defaultOpen: true,
      items: [
        "Raspberry Pi 4B (4GB)",
        "Raspberry Pi Camera Module 3",
        "Official Raspberry Pi 15W Power Supply, US",
        "Aluminum heatsinks (3-pack)",
        "32 GB SD Card pre-loaded with PrintNanny OS",
        "6 months of PrintNanny Cloud ($60 value, included for FREE)",
      ],
    },
    {
      name: "What comes pre-installed?",
      defaultOpen: true,
      items: [
        "OctoPrint",
        "Mainsail / Moonraker / Klipper",
        "Syncthing (like having a personal Dropbox server)",
        "Tailscale VPN (easy remote access)",
        "Compatible with Marlin and Klipper firmware",
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
  const productData = await shop.getProductBySku(sku);
  if (productData === undefined) {
    new Error("Failed to fetch Stripe product data");
  }
  // get the price matching selecting billing frequency (monthly or annual)
  console.log("form submitted", values, productData);
  if (values && values.email !== undefined && productData !== undefined) {
    await shop.createCheckoutSession(values.email, [
      { product: productData.id, price: productData.prices[0].id },
    ] as Array<api.OrderItemRequest>);
  }
}
</script>
