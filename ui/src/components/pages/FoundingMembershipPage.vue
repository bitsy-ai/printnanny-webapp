<!--
  This example requires Tailwind CSS v2.0+ 
  
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
      class="mx-auto max-w-2xl py-16 px-4 sm:py-24 sm:px-6 lg:max-w-7xl lg:px-8"
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
                <span class="sr-only"> {{ image.name }} </span>
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

          <TabPanels class="aspect-w-1 aspect-h-1 w-full">
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
            <p class="text-3xl tracking-tight">
              <span class="text-grey-900"
                ><s>{{ product.fullPrice }}</s></span
              >
              <span class="text-red-500">{{ product.price }}</span>
            </p>
            <p class="text-xl tracking-tight mt-2">50% off launch price</p>
          </div>

          <!-- TODO Reviews 
          <div class="mt-3">
            <h3 class="sr-only">Reviews</h3>
            <div class="flex items-center">
              <div class="flex items-center">
                <StarIcon v-for="rating in [0, 1, 2, 3, 4]" :key="rating" :class="[product.rating > rating ? 'text-indigo-500' : 'text-gray-300', 'h-5 w-5 flex-shrink-0']" aria-hidden="true" />
              </div>
              <p class="sr-only">{{ product.rating }} out of 5 stars</p>
            </div>
          </div>
            -->

          <div class="mt-6">
            <h3 class="sr-only">Description</h3>

            <div
              class="space-y-6 text-base text-gray-700"
              v-html="product.description"
            />
          </div>

          <form class="mt-6">
            <div class="sm:flex-col1 mt-10 flex">
              <button
                type="submit"
                class="flex max-w-xs flex-1 items-center justify-center rounded-md border border-transparent bg-indigo-600 py-3 px-8 text-base font-medium text-white hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2 focus:ring-offset-gray-50 sm:w-full"
              >
                Become a Founding Member
              </button>

              <button
                type="button"
                class="ml-4 flex items-center justify-center rounded-md py-3 px-3 text-gray-400 hover:bg-gray-100 hover:text-gray-500"
              >
                <HeartIcon class="h-6 w-6 flex-shrink-0" aria-hidden="true" />
                <span class="sr-only">Add to favorites</span>
              </button>
            </div>
          </form>

          <section aria-labelledby="details-heading" class="mt-12">
            <h2 id="details-heading" class="sr-only">Additional details</h2>

            <div class="divide-y divide-gray-200 border-t">
              <Disclosure
                v-for="detail in product.details"
                :key="detail.name"
                v-slot="{ open }"
                as="div"
                :default-open="true"
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
                    <li
                      v-for="item in detail.items"
                      :key="item"
                      v-html="item"
                    ></li>
                  </ul>
                  <p>{{ detail.extra }}</p>
                </DisclosurePanel>
              </Disclosure>
            </div>
          </section>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from "vue";
import {
  Disclosure,
  DisclosureButton,
  DisclosurePanel,
  RadioGroup,
  RadioGroupLabel,
  RadioGroupOption,
  Tab,
  TabGroup,
  TabList,
  TabPanel,
  TabPanels,
  TransitionRoot,
  TransitionChild,
} from "@headlessui/vue";
import { StarIcon } from "@heroicons/vue/solid";
import { HeartIcon, MinusIcon, PlusIcon } from "@heroicons/vue/outline";

import coaster1Url from "@/assets/images/founding-swag/coasters-1.jpeg";
import coaster2Url from "@/assets/images/founding-swag/coasters-2.jpeg";
import caseUrl from "@/assets/images/founding-swag/case-3.jpeg";

const product = ref({
  name: "Founding Membership",
  price: "$99 / year",
  fullPrice: "$199 / year",
  highlights: [
    "200+ SVG icons in 3 unique styles",
    "Compatible with Figma, Sketch, and Adobe XD",
    "Drawn on 24 x 24 pixel grid",
  ],
  images: [
    {
      src: coaster1Url,
      active: true,
      alt: "Two-tone PrintNanny coaster printed with purple and blue filament",
    },
    {
      src: coaster2Url,
      active: false,
      alt: "Two-tone PrintNanny coaster printed with purple and green filament",
    },
    {
      src: caseUrl,
      active: false,
      alt: "Raspberry Pi case with PrintNanny logo cutout, printed with purple filament",
    },
  ],
  description: `<p>Skip the waitlist by by joining the early access Founding Member program</p>
    <p>Founding Members enjoy unlimited use, special perks, and drive the roadmap.</p>
  `,
  details: [
    {
      name: "Perks",
      open: true,
      items: [
        "Money-back guarantee.",
        "No metered usage. No monthly addons.",
        "Connect unlimited printers for one flat rate.",
        "Get access to private #members-only Discord channel.",
        "Exclusive 3D-printable swag (set of 6 two-tone coasters, Raspberry Pi case)",
      ],
      extra:
        "If you're not 100% satisfied with PrintNanny, email leigh@printnanny.ai for a full refund.",
    },
    {
      name: "Hardware Requirements",
      extra:
        "Founding Members must supply their own hardware. Pre-built kits will be available at launch.",
      open: true,
      items: [
        `<a href="https://docs.printnanny.ai/docs/quick-start/hardware/" class="text-indigo-500 hover:text-indigo-600" target="_blank">Read more about required hardware</a>`,
        "Raspberry Pi 4",
        "Raspberry Pi Camera",
        "5.1v / 3.0A DC power supply",
        "Micro SD card",
        "Heatsinks",
      ],
    },
    // More sections...
  ],
});

const activeImage = computed(() => {
  return product.value.images.filter((i) => i.active == true)[0];
});

// const product = {
//   name: 'Zip Tote Basket',
//   price: '$140',
//   rating: 4,
//   images: [
//     {
//       id: 1,
//       name: 'Angled view',
//       src: 'https://tailwindui.com/img/ecommerce-images/product-page-03-product-01.jpg',
//       alt: 'Angled front view with bag zipped and handles upright.',
//     },
//     // More images...
//   ],
//   colors: [
//     { name: 'Washed Black', bgColor: 'bg-gray-700', selectedColor: 'ring-gray-700' },
//     { name: 'White', bgColor: 'bg-white', selectedColor: 'ring-gray-400' },
//     { name: 'Washed Gray', bgColor: 'bg-gray-500', selectedColor: 'ring-gray-500' },
//   ],
//   description: `
//     <p>The Zip Tote Basket is the perfect midpoint between shopping tote and comfy backpack. With convertible straps, you can hand carry, should sling, or backpack this convenient and spacious bag. The zip top and durable canvas construction keeps your goods protected for all-day use.</p>
//   `,
//   details: [
//     {
//       name: 'Features',
//       items: [
//         'Multiple strap configurations',
//         'Spacious interior with top zip',
//         'Leather handle and tabs',
//         'Interior dividers',
//         'Stainless strap loops',
//         'Double stitched construction',
//         'Water-resistant',
//       ],
//     },
//     // More sections...
//   ],
// }
</script>
