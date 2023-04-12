<template>
  <div class="bg-gray-50 lg:min-h-100">
    <div class="relative shadow bg-gradient-to-r from-indigo-500 to-violet-600">
      <!-- Overlapping background -->

      <div
        class="relative mx-auto max-w-2xl px-6 pt-16 text-center sm:pt-32 lg:max-w-7xl lg:px-8"
      >
        <h1 class="text-4xl font-bold tracking-tight text-white sm:text-6xl">
          <span class="block lg:inline">Simple pricing, </span>
          <span class="block lg:inline">no hidden costs</span>
        </h1>
        <p class="mt-4 text-xl text-indigo-100">
          Flexible pay-as-you-go monthly plans.
        </p>
        <p class="mt-4 text-xl text-indigo-100">
          Unlimited annual plans for rapid-scaling businesses.
        </p>
      </div>
      <!-- Cards -->
      <div
        class="relative mx-auto mt-8 max-w-2xl px-6 pb-8 sm:mt-12 lg:max-w-6xl lg:px-8 lg:pb-4"
      >
        <!-- Decorative background -->
        <div
          aria-hidden="true"
          class="absolute inset-0 top-4 bottom-6 left-8 right-8 hidden rounded-tl-lg rounded-tr-lg bg-indigo-800 lg:block"
        />
        <!-- monthly / annual billing tiers -->
        <div class="relative space-y-6 lg:grid lg:grid-cols-2 lg:space-y-0">
          <div
            :class="[
              plan?.featured
                ? 'bg-white ring-2 ring-indigo-700 shadow-md'
                : 'bg-indigo-700 lg:bg-transparent',
              'pt-6 px-6 pb-3 rounded-lg lg:px-8 lg:pt-12',
            ]"
          >
            <div>
              <h3
                :class="[
                  plan?.featured ? 'text-indigo-600' : 'text-white',
                  'text-base font-semibold',
                ]"
              >
                {{ plan?.title }}
              </h3>
              <div
                class="flex flex-col items-start sm:flex-row sm:items-center sm:justify-between lg:flex-col lg:items-start"
              >
                <div v-if="price == 'monthly'" class="mt-3 flex items-center">
                  <p
                    :class="[
                      plan?.featured ? 'text-indigo-600' : 'text-white',
                      'text-4xl font-bold tracking-tight',
                    ]"
                  >
                    ${{ plan?.priceMonthly }}
                  </p>
                  <div class="ml-4">
                    <p
                      :class="[
                        plan?.featured ? 'text-gray-700' : 'text-white',
                        'text-sm',
                      ]"
                    >
                      USD / mo
                    </p>
                    <p
                      :class="[
                        plan?.featured ? 'text-gray-500' : 'text-indigo-200',
                        'text-sm',
                      ]"
                    >
                      Billed monthly
                    </p>
                  </div>
                </div>
                <div v-else class="mt-3 flex items-center">
                  <p
                    :class="[
                      plan?.featured ? 'text-indigo-600' : 'text-white',
                      'text-4xl font-bold tracking-tight',
                    ]"
                  >
                    ${{
                      Math.round(parseFloat(plan?.priceYearly as string) / 12)
                    }}
                  </p>
                  <div class="ml-4">
                    <p
                      :class="[
                        plan?.featured ? 'text-gray-700' : 'text-white',
                        'text-sm',
                      ]"
                    >
                      USD / mo
                    </p>
                    <p
                      :class="[
                        plan?.featured ? 'text-gray-500' : 'text-indigo-200',
                        'text-sm',
                      ]"
                    >
                      Billed yearly (${{ plan?.priceYearly }})
                    </p>
                  </div>
                </div>
              </div>
            </div>
            <h4 class="sr-only">Features</h4>
            <ul
              role="list"
              :class="[
                plan?.featured
                  ? 'border-gray-200 divide-gray-200'
                  : 'border-indigo-500 divide-indigo-500 divide-opacity-75',
                'mt-7 border-t divide-y lg:border-t-0',
              ]"
            >
              <li
                v-for="mainFeature in plan?.mainFeatures"
                :key="mainFeature.id"
                class="flex items-center py-3"
              >
                <CheckIcon
                  :class="[
                    plan?.featured ? 'text-indigo-500' : 'text-indigo-200',
                    'w-5 h-5 flex-shrink-0',
                  ]"
                  aria-hidden="true"
                />
                <span
                  :class="[
                    plan?.featured ? 'text-gray-600' : 'text-white',
                    'ml-3 text-sm font-medium',
                  ]"
                  >{{ mainFeature.value }}</span
                >
              </li>
            </ul>
          </div>

          <div
            :class="[
              'bg-indigo-700 lg:bg-transparent flex flex-col justify-around space-y-6',
              'pt-6 px-6 pb-3 rounded-lg lg:px-8 lg:pt-12',
            ]"
          >
            <Form
              class="flex flex-col justify-evenly space-y-6"
              :validation-schema="schema"
              @submit="onClick"
            >
              <h1
                class="text-2xl font-bold tracking-tight text-white text-center"
              >
                <span class="block lg:inline">Enter your email addrees</span>
              </h1>
              <div class="w-full">
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
                  class="text-white text-sm font-medium"
                  name="email"
                ></error-message>
              </div>
              <div class="">
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
        </div>
      </div>
    </div>
  </div>
</template>
<script setup lang="ts">
import { onMounted } from "vue";
import { useShopStore } from "@/stores/shop";
import * as yup from "yup";
import type * as api from "printnanny-api-client";
import { Field, ErrorMessage, Form } from "vee-validate";
import { CheckIcon, XMarkIcon } from "@heroicons/vue/24/solid";

import CustomSpinner from "@/components/util/CustomSpinner.vue";

const props = defineProps({
  sku: {
    type: String,
    required: true,
  },
  price: {
    type: String,
    required: true,
  },
});

const plans = [
  {
    cta: "Try Starter Risk-Free",
    title: "Starter",
    sku: "cloud-starter-plan",
    priceId: `starter_${props.price}`,
    featured: true,
    description: "Perfect for hobbyists and makers.",
    priceMonthly: "9.99",
    priceYearly: "99.99",
    mainFeatures: [
      { id: 1, value: "Up to 3 active printers" },
      { id: 2, value: "10 GB cloud storage" },
      { id: 3, value: "Email alerts" },
      { id: 4, value: "Money-back guarantee" },
    ],
  },
  {
    title: "Scale",
    cta: "Try Scale Risk-Free",
    sku: "cloud-scaler-plan",
    priceId: `scaler_${props.price}`,
    featured: true,
    description: "The best tools to scale a 3D printing business.",
    priceMonthly: "19.99",
    priceYearly: "199.99",
    mainFeatures: [
      { id: 1, value: "No active printer limit" },
      { id: 2, value: "Unlimited cloud storage" },
      { id: 3, value: "API Access" },
      // { id: 4, value: 'Alpha access to e-commerce integrations' },
      { id: 5, value: "Money-back guarantee" },
    ],
  },
];

const plan = plans.find((v) => v.sku === props.sku);

onMounted(async () => {
  await shop.fetchCloudPlans();
});

// define a validation schema
const schema = yup.object({
  email: yup.string().required().email(),
});

const shop = useShopStore();

async function onClick(values: any) {
  const productData = shop.getCloudPlanBySku(props.sku);
  if (productData === undefined) {
    new Error("Failed to fetch Stripe product data");
  }
  const priceData = shop.getCloudPlanPriceByFreq(
    productData as api.Product,
    props.price
  );

  // get the price matching selecting billing frequency (monthly or annual)
  console.log("form submitted", values, productData);

  if (values && values.email !== undefined && productData !== undefined) {
    await shop.createCheckoutSession(values.email, [
      { product: productData.id, price: priceData?.id },
    ] as Array<api.OrderItemRequest>);
  }
}
</script>
