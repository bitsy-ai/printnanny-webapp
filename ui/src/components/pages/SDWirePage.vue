<template>
  <div class="bg-white">
    <div class="mx-auto py-16 px-4 sm:py-24 sm:px-6 lg:max-w-7xl lg:px-8">
      <!-- Product -->
      <div
        class="lg:grid lg:grid-cols-7 lg:grid-rows-1 lg:gap-x-8 lg:gap-y-10 xl:gap-x-16"
      >
        <!-- Product image -->
        <div class="lg:col-span-4 lg:row-end-1">
          <div
            class="aspect-w-4 aspect-h-3 overflow-hidden rounded-lg bg-gray-100"
          >
            <img
              src="/images/sdwire/SDWire-3D-front-v1.4-r1.jpg"
              :alt="product.imageAlt"
              class="object-cover object-center"
            />
          </div>
        </div>

        <!-- Product details -->
        <div
          class="mx-auto mt-14 max-w-2xl sm:mt-16 lg:col-span-3 lg:row-span-2 lg:row-end-2 lg:mt-0 lg:max-w-none"
        >
          <div class="flex flex-col-reverse">
            <div class="mt-4">
              <h1
                class="text-2xl font-bold tracking-tight text-gray-900 sm:text-3xl"
              >
                {{ product.name }}
              </h1>
              <h2
                class="text-xl font-bold tracking-tight text-gray-900 sm:text-2xl"
              >
                {{ product.price }}
                <span class="font-medium text-sm"
                  >plus shipping & handling</span
                >
              </h2>
              <h2 id="information-heading" class="sr-only">
                Product information
              </h2>
              <p class="mt-2 text-sm text-gray-500">
                Version {{ product.version.name }} (Updated
                <time :datetime="product.version.datetime">{{
                  product.version.date
                }}</time
                >)
              </p>
            </div>
            <!-- TODO reviews
            <div>
              <h3 class="sr-only">Reviews</h3>
              <div class="flex items-center">
                <StarIcon v-for="rating in [0, 1, 2, 3, 4]" :key="rating" :class="[reviews.average > rating ? 'text-yellow-400' : 'text-gray-300', 'h-5 w-5 flex-shrink-0']" aria-hidden="true" />
              </div>
              <p class="sr-only">{{ reviews.average }} out of 5 stars</p>
            </div>
            -->
          </div>

          <p class="mt-6 text-gray-500">{{ product.description }}</p>
          <div class="mt-10">
            <button
              type="button"
              disabled
              class="flex w-full items-center block justify-center rounded-md border border-transparent bg-indigo-600 py-3 px-8 text-base font-medium text-white focus:outline-none disabled:opacity-25"
              @click="onClick"
            >
              Sold Out
            </button>
          </div>
          <!-- prompt for email address if user is not logged in -->
          <!-- DISABLED SDWIRE, SOLD OUT
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

          <div v-else class="mt-10">
            <button
              type="button"
              class="flex w-full items-center block justify-center rounded-md border border-transparent bg-indigo-600 py-3 px-8 text-base font-medium text-white hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2 focus:ring-offset-gray-50"
              @click="onClick"
            >
              <CustomSpinner
                v-if="shopStore.loading"
                color="indigo"
                class="mr-2"
              ></CustomSpinner>
              <span v-if="!shopStore.loading"> Pre-order with Stripe </span>
              <span v-if="shopStore.loading">
                Redirecting to Stripe Checkout
              </span>
            </button>
          </div>
          -->

          <div class="mt-10 border-t border-gray-200 pt-10">
            <h3 class="text-sm font-medium text-gray-900">Highlights</h3>
            <div class="prose prose-sm mt-4 text-gray-500">
              <ul role="list">
                <li v-for="highlight in product.highlights" :key="highlight">
                  {{ highlight }}
                </li>
              </ul>
            </div>
          </div>

          <div class="mt-10 border-t border-gray-200 pt-10">
            <h3 class="text-sm font-medium text-gray-900">License</h3>
            <p class="mt-4 text-sm text-gray-500">
              {{ license.summary }} <br /><a
                :href="license.href"
                class="font-medium text-indigo-600 hover:text-indigo-500"
                >Read the wiki</a
              >
            </p>
          </div>

          <div class="mt-10 border-t border-gray-200 pt-10">
            <h3 class="text-sm font-medium text-gray-900">Support</h3>
            <p class="text-gray-500 text-sm">
              Email questions to support@printnanny.ai or
              <a
                href="https://github.com/bitsy-ai/printnanny-sdwire"
                class="text-indigo-500 hover:text-indigo-600"
                >open a Github issue.</a
              >
            </p>
          </div>
        </div>

        <div
          class="mx-auto mt-16 w-full max-w-2xl lg:col-span-4 lg:mt-0 lg:max-w-none"
        >
          <TabGroup as="div">
            <div class="border-b border-gray-200">
              <TabList class="-mb-px flex space-x-8">
                <!-- TODO reviews
                <Tab as="template" v-slot="{ selected }">
                  <button :class="[selected ? 'border-indigo-600 text-indigo-600' : 'border-transparent text-gray-700 hover:text-gray-800 hover:border-gray-300', 'whitespace-nowrap border-b-2 py-6 text-sm font-medium']">Customer Reviews</button>
                </Tab>
                -->
                <Tab v-slot="{ selected }" as="template">
                  <button
                    :class="[
                      selected
                        ? 'border-indigo-600 text-indigo-600'
                        : 'border-transparent text-gray-700 hover:text-gray-800 hover:border-gray-300',
                      'whitespace-nowrap border-b-2 py-6 text-sm font-medium',
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
                      'whitespace-nowrap border-b-2 py-6 text-sm font-medium',
                    ]"
                  >
                    Timeline
                  </button>
                </Tab>
              </TabList>
            </div>
            <TabPanels as="template">
              <!-- TODO reviews
              <TabPanel class="-mb-10">
                <h3 class="sr-only">Customer Reviews</h3>

                <div v-for="(review, reviewIdx) in reviews.featured" :key="review.id" class="flex space-x-4 text-sm text-gray-500">
                  <div class="flex-none py-10">
                    <img :src="review.avatarSrc" alt="" class="h-10 w-10 rounded-full bg-gray-100" />
                  </div>
                  <div :class="[reviewIdx === 0 ? '' : 'border-t border-gray-200', 'py-10']">
                    <h3 class="font-medium text-gray-900">{{ review.author }}</h3>
                    <p>
                      <time :datetime="review.datetime">{{ review.date }}</time>
                    </p>

                    <div class="mt-4 flex items-center">
                      <StarIcon v-for="rating in [0, 1, 2, 3, 4]" :key="rating" :class="[review.rating > rating ? 'text-yellow-400' : 'text-gray-300', 'h-5 w-5 flex-shrink-0']" aria-hidden="true" />
                    </div>
                    <p class="sr-only">{{ review.rating }} out of 5 stars</p>

                    <div class="prose prose-sm mt-4 max-w-none text-gray-500" v-html="review.content" />
                  </div>
                </div>
              </TabPanel>
            -->

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
    </div>
  </div>
</template>

<script setup lang="ts">
import * as yup from "yup";
import { Field, ErrorMessage, Form } from "vee-validate";

import CustomSpinner from "@/components/util/CustomSpinner.vue";
import { Tab, TabGroup, TabList, TabPanel, TabPanels } from "@headlessui/vue";
import { useShopStore } from "@/stores/shop";
import { useAccountStore } from "@/stores/account";
import { useAlertStore } from "@/stores/alerts";
import type { UiAlert, AlertAction } from "@/types/alerts";

const accountStore = useAccountStore();
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
  name: "PrintNanny SDWire",
  version: {
    name: "1.4 revision 1",
    date: "August 30, 2022",
    datetime: "2022-08-30",
  },
  price: "$89",
  description:
    "SDWire connects a device-under-test to a host computer, enabling flashing/re-imaging an SD card with no moving parts. SDWire functions as an SD card reader and SD card mux.",
  highlights: [
    "Fits Micro SD card slot or SD Card slot with adaptor",
    "Compatible with Raspberry Pi and Rock Pi",
    "Compatible with OctoPrint-SDWire",

    "Fabulous purple PCB design 💜",
    "Gold-finished contacts",
    "48.4mm x 21.6mm x 0.8mm",
  ],
  imageSrc: "@/assets/images/sdwire/SDWire-3D-front-v1.4-r1.jpg",
  imageAlt: "3D rendering of PrintNanny SDWire board (front view)",
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
const faqs = [
  {
    question: "What can an SDWire be used for?",
    answer: `<p>SDWire is designed to make life easier for embedded software engineers and single-board computer enthusiasts. The SDWire board allows you to automate the transfer of SD card data, while the card is connected to a host (personal computer) and device-under-test (DUT) that boots from an SD card.</p> 
      <p>Anyone who has spent lots of time removing, re-imaging, re-inserting, SD cards will appreciate the quality-of-life improvements provided by SDWire.</p>
      <p>The 3D printing community uses SDWire to transfer gcode files to a printer's SD card reader. See <a href="https://github.com/arekm/OctoPrint-Sdwire" class="text-indigo-500 hover:text-indigo-600" target="_blank">OctoPrint-SDwire</a> for an example.</p>
      `,
  },
  {
    question:
      "What is the difference between Tizen SDWire and PrintNanny SDWire?",
    answer:
      "PrintNanny SDWire is based on the open-source SDWire design by Tizen, with revisions to replace unavailable components with parts that are easy to source in the US.",
  },
  {
    question: "Can you ship to my country?",
    answer:
      "If you do not see a shipping option available for your country, email support@printnanny.ai with your country, postal code, and order quantity. Please keep in mind that shipping outside of the US/Canada may be prohibitely expensive for small orders. If you would like to place a bulk order and re-distribute PrintNanny SDWire, get in touch for a quote.",
  },
  {
    question: "When will I receive my order?",
    answer:
      "The first batch of units will ship in October-November 2022. We assemble and ship pre-orders in the order they're received. You'll receive an email confirmation when your order is ready to ship, to make sure we have the correct address on file.",
  },
  {
    question: "When does my payment method get charged?",
    answer:
      "Your payment will be charged when you place your pre-order. If you cancel your pre-order, your payment method will be refunded.",
  },
  {
    question: "Can I cancel my pre-order?",
    answer:
      "Yes, as long as your order hasn't shipped. Please send an email to support@printnanny.ai to cancel your pre-order and receive a refund.",
  },
  {
    question: "What is your return policy?",
    answer: `If you receive a board that doesn't work, get in touch immediately! 
      We happily accept returns within 30 days of delivery. Please send an email support@printanny.ai to start the return process.
    `,
  },
  {
    question: "Do you offer a bulk discount?",
    answer:
      "For orders of 5+ boards, email support@printnanny.ai with your country, zip code, and desired quantity.",
  },
  {
    question: "Is PrintNanny SDWire open source?",
    answer: `Yes! The <a href="https://github.com/bitsy-ai/PrintNanny-SDwire" class="text-indigo-500 hover:text-indigo-600">KiCAD project</a> is available on Github.`,
  },
  {
    question:
      "Where can I learn more about the development and production process?",
    answer: `Check out the <a href="https://bitsy.ai/" class="text-indigo-500 hover:text-indigo-600">Bitsy AI blog</a> to learn how PrintNanny SDWire was created. If you have questions about the development process, subscribe to the Bitsy AI newsletter. We'll send out an "Ask the Electrical Engineer" form to collect your questions and answer them in an upcoming blog post!`,
  },
];
const license = {
  href: "https://wiki.tizen.org/SDWire",
  summary: "Based on Tizen SDWire",
};

const timeline = {
  content: `
    <h4>October-November, 2022</h4>
    <ul role="list">
      <li>Production Batch 1</li>
    </ul>
    <h4>September 5, 2022</h4>
      <ul role="list">
      <li>PrintNanny SDWire is available for pre-order.</li>
      <li>Units ordered in September are expected to ship with Production Batch 1, October-November 2022</li>
      </ul>

    <h4>August 28, 2022</h4>
        
    <ul role="list">
    <li>Published PrintNanny SDWire v1.4-r1 </li>
    <li>Test Batch 1 (10 units)</li>
    </ul>
    
  `,
};
</script>
