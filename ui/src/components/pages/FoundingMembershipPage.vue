<template>
  <div class="bg-white">
    <div
      class="mx-auto max-w-2xl py-16 px-4 sm:py-24 sm:px-6 lg:max-w-7xl lg:px-8"
    >
      <div class="lg:grid lg:grid-cols-2 lg:items-start lg:gap-x-8">
        <!-- Image gallery -->
        <div>
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

          <div
            class="mx-auto mt-16 w-full max-w-2xl lg:col-span-4 lg:mt-0 lg:max-w-none"
          >
            <TabGroup as="div">
              <div class="border-b border-gray-200">
                <TabList class="-mb-px flex space-x-8">
                  <Tab v-slot="{ selected }" as="template">
                    <button
                      :class="[
                        selected
                          ? 'border-indigo-600 text-indigo-600'
                          : 'border-transparent text-gray-700 hover:text-gray-800 hover:border-gray-300',
                        'whitespace-nowrap border-b-2 py-6 text-sm font-medium focus:outline-none',
                      ]"
                    >
                      FAQ
                    </button>
                  </Tab>
                  <Tab v-slot="{ selected }" as="template">
                    <button
                      :class="[
                        selected
                          ? 'border-indigo-600 text-indigo-600'
                          : 'border-transparent text-gray-700 hover:text-gray-800 hover:border-gray-300',
                        'whitespace-nowrap border-b-2 py-6 text-sm font-medium focus:outline-none',
                      ]"
                    >
                      Release History
                    </button>
                  </Tab>
                </TabList>
              </div>
              <TabPanels as="template">
                <TabPanel class="text-sm text-gray-500">
                  <h3 class="sr-only">Frequently Asked Questions</h3>

                  <dl>
                    <template v-for="faq in faqs" :key="faq.question">
                      <dt class="mt-10 font-medium text-gray-900">
                        {{ faq.question }}
                      </dt>
                      <dd class="prose prose-sm mt-2 max-w-none text-gray-500">
                        <div v-html="faq.answer"></div>
                      </dd>
                    </template>
                  </dl>
                </TabPanel>

                <TabPanel class="pt-10">
                  <h3 class="sr-only">Timeline</h3>

                  <div
                    class="prose prose-sm max-w-none text-gray-500"
                    v-html="timeline.content"
                  />
                </TabPanel>
              </TabPanels>
            </TabGroup>
          </div>
        </div>

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
              <span class="text-red-500 ml-2">{{ product.price }}</span>
            </p>
            <p class="text-xl tracking-tight mt-2">50% off launch price</p>
          </div>

          <div class="mt-6">
            <h3 class="sr-only">Description</h3>

            <div
              class="space-y-6 text-base text-gray-700"
              v-html="product.description"
            />
          </div>

          <!-- prompt for email address if user is not logged in -->
          <div v-if="!accountStore.isAuthenticated" class="mt-10">
            <p class="text-sm my-2">
              Enter your email address or
              <a href="/login" class="text-indigo-500 hover:text-indigo-600"
                >log in to an existing account.</a
              >
            </p>
            <Form
              class="sm:max-w-xl sm:mx-auto lg:mx-0"
              :validation-schema="schema"
              @submit="onClick"
            >
              <div class="sm:flex">
                <div class="min-w-0 flex-1">
                  <label for="email" class="sr-only">Email address</label>
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
                    class="text-red-500"
                    name="email"
                  ></error-message>
                </div>
                <div class="mt-3 sm:mt-0 sm:ml-3">
                  <button
                    type="submit"
                    class="block w-full py-3 px-4 rounded-md shadow bg-gradient-to-r from-indigo-500 to-violet-600 text-white font-medium hover:from-indigo-600 hover:to-violet-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-cyan-400 focus:ring-offset-gray-900"
                  >
                    <CustomSpinner
                      v-if="shopStore.loading"
                      color="indigo"
                      class="mr-2"
                    ></CustomSpinner>
                    <span v-if="!shopStore.loading">
                      Pre-order with Stripe
                    </span>
                    <span v-if="shopStore.loading">
                      Redirecting to Stripe Checkout
                    </span>
                  </button>
                </div>
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

<script setup lang="ts">
import { ref } from "vue";
import * as yup from "yup";
import { Field, ErrorMessage, Form } from "vee-validate";

import {
  Disclosure,
  DisclosureButton,
  DisclosurePanel,
  Tab,
  TabGroup,
  TabList,
  TabPanel,
  TabPanels,
} from "@headlessui/vue";
import { HeartIcon, MinusIcon, PlusIcon } from "@heroicons/vue/outline";
import { useAccountStore } from "@/stores/account";
import { useShopStore } from "@/stores/shop";
import CustomSpinner from "@/components/util/CustomSpinner.vue";

import coaster1Url from "@/assets/images/founding-swag/coasters-1.jpeg";
import coaster2Url from "@/assets/images/founding-swag/coasters-2.jpeg";
import caseUrl from "@/assets/images/founding-swag/case-3.jpeg";

// define a validation schema
const schema = yup.object({
  email: yup.string().required().email(),
});

const accountStore = useAccountStore();
const shopStore = useShopStore();

const products = await shopStore.fetchProducts();
const productData = products?.find((p) => p.slug == "founding-membership");

async function onClick(values: any) {
  if (values && values.email !== undefined && productData !== undefined) {
    await shopStore.createCheckoutSession(values.email, [
      productData.id,
    ] as Array<string>);
  } else if (
    accountStore.isAuthenticated &&
    accountStore.user !== undefined &&
    productData !== undefined
  ) {
    await shopStore.createCheckoutSession(accountStore.user?.email, [
      productData.id,
    ] as Array<string>);
  }
}

const timeline = {
  content: ``,
};

const faqs = [
  {
    question: "Does the Founding Membership include hardware?",
    answer: `You must supply your own hardware to participate in the Founding Member program. 
    <br><a href="https://docs.printnanny.ai/docs/quick-start/hardware/" class="text-indigo-500 hover:text-indigo-600" target="_blank">
      Learn more about required hardware.</a>`,
  },
  {
    question: "Which boards are supported?",
    answer: `PrintNanny's early access program requires a Raspberry Pi 4 (2GB+). Subscribe to the following Github issues to track support for other boards:
      <br><a href="https://github.com/bitsy-ai/printnanny-os/issues/16" class="text-indigo-500 hover:text-indigo-600" target="_blank">Raspberry Pi 3</a>
      <br><a href="https://github.com/bitsy-ai/printnanny-os/issues/37" class="text-indigo-500 hover:text-indigo-600" target="_blank">Rock Pi 4</a>
    `,
  },
  {
    question: "What is PrintNanny OS?",
    answer: `PrintNanny OS is a Linux distribution based on the <a href="https://www.yoctoproject.org/" class="text-indigo-500 hover:text-indigo-600" target="_blank">Yocto Project</a>, designed to let you focus on the fun parts of 3D printing. 
      Compared to general-purpose Linux distributions like Raspberry Pi OS (Raspbian), PrintNanny OS is highly optimized for 3D printer controllers and computer vision tasks. 

      PrintNanny OS can receive over-the-air updates and is upgradable via web ui. Your settings are automatically kept in sync with PrintNanny Cloud.
    <br>`,
  },
  {
    question: "How to I install PrintNanny OS?",
    answer: `Check out the <a href="https://docs.printnanny.ai/docs/category/quick-start/" class="text-indigo-500 hover:text-indigo-600" target="_blank">Quick Start guide</a>.</a>`,
  },
  {
    question: "How to I update PrintNanny OS?",
    answer: `Follow the steps in <a href="https://docs.printnanny.ai/docs/update-printnanny-os/"  class="text-indigo-500 hover:text-indigo-600" target="_blank">Update PrintNanny OS</a>.`,
  },
];

const product = ref({
  name: "Founding Membership",
  price: "$149 / year",
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
  description: `<p>Skip the waitlist by by joining the early access Founding Member program.</p>
    <p>Founding Members enjoy unlimited use, special perks, and drive the roadmap.</p>
  `,
  details: [
    {
      name: "Founding Member Perks",
      open: true,
      items: [
        "No metered usage. No monthly addons.",
        "Connect unlimited printers for one flat rate.",
        "Get access to private #members-only Discord channel.",
        "Exclusive 3D-printable swag (set of 6 two-tone coasters, Raspberry Pi case)",
      ],
      extra:
        "Money-back guarantee. If you're not 100% satisfied with PrintNanny, email support@printnanny.ai for a full refund.",
    },
    {
      name: "Hardware Requirements",
      extra: "",
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
</script>
