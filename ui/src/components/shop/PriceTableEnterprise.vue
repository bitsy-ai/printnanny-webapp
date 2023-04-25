<template>
  <div class="bg-gray-50">
    <div class="relative shadow bg-gradient-to-r from-indigo-500 to-violet-600">
      <!-- Overlapping background -->
      <div
        aria-hidden="true"
        class="absolute bottom-0 hidden h-6 w-full bg-gray-50 lg:block"
      />

      <div
        class="relative mx-auto max-w-2xl px-6 pt-16 text-center sm:pt-32 lg:max-w-7xl lg:px-8"
      >
        <h1 class="text-4xl font-bold tracking-tight text-white sm:text-6xl">
          <span class="block lg:inline">Enterprise Plans</span>
        </h1>
        <p class="mt-4 text-xl text-indigo-100">
          Get white-glove onboarding and integration with your existing
          hardware/software ecosystem.
        </p>
        <img
          src="@/assets/logo/logo-square-white.svg"
          class="h-40 hidden md:flex m-auto mt-4"
        />
      </div>
      <!-- Cards -->
      <div
        class="relative mx-auto mt-8 max-w-2xl px-6 pb-8 sm:mt-12 lg:max-w-6xl lg:px-8 lg:pb-4"
      >
        <!-- Decorative background -->
        <div
          aria-hidden="true"
          class="absolute inset-0 top-4 bottom-6 left-8 right-8 hidden rounded-tl-lg rounded-tr-lg bg-indigo-700 lg:block"
        />

        <!-- main features -->
        <div class="relative space-y-6 lg:grid lg:grid-cols-3 lg:space-y-0">
          <div
            v-for="plan in plans"
            :key="plan.title"
            :class="[
              plan.featured
                ? 'bg-white ring-2 ring-indigo-700 shadow-md'
                : 'bg-indigo-700 lg:bg-transparent',
              'pt-6 px-6 pb-3 rounded-lg lg:px-8 lg:pt-12',
            ]"
          >
            <div>
              <h3
                :class="[
                  plan.featured ? 'text-indigo-600' : 'text-white',
                  'text-base font-semibold',
                ]"
              >
                {{ plan.title }}
              </h3>
              <div
                class="flex flex-col items-start sm:flex-row sm:items-center sm:justify-between lg:flex-col lg:items-start"
              >
                <div v-if="plan.priceOnRequest" class="mt-3 flex items-center">
                  <p
                    :class="[
                      plan.featured ? 'text-gray-500' : 'text-indigo-200',
                      'text-sm',
                    ]"
                  >
                    {{ plan.priceOnRequest }}
                  </p>
                </div>
                <div v-else-if="showMonthly" class="mt-3 flex items-center">
                  <p
                    :class="[
                      plan.featured ? 'text-indigo-600' : 'text-white',
                      'text-4xl font-bold tracking-tight',
                    ]"
                  >
                    ${{ plan.priceMonthly }}
                  </p>
                  <div class="ml-4">
                    <p
                      :class="[
                        plan.featured ? 'text-gray-700' : 'text-white',
                        'text-sm',
                      ]"
                    >
                      USD / mo
                    </p>
                    <p
                      :class="[
                        plan.featured ? 'text-gray-500' : 'text-indigo-200',
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
                      plan.featured ? 'text-indigo-600' : 'text-white',
                      'text-4xl font-bold tracking-tight',
                    ]"
                  >
                    ${{ Math.round(plan.priceYearly / 12) }}
                  </p>
                  <div class="ml-4">
                    <p
                      :class="[
                        plan.featured ? 'text-gray-700' : 'text-white',
                        'text-sm',
                      ]"
                    >
                      USD / mo
                    </p>
                    <p
                      :class="[
                        plan.featured ? 'text-gray-500' : 'text-indigo-200',
                        'text-sm',
                      ]"
                    >
                      Billed yearly (${{ plan.priceYearly }})
                    </p>
                  </div>
                </div>
                <a
                  :id="`${plan.sku}-${showBilling}`"
                  :href="plan.href"
                  :class="[
                    plan.featured
                      ? 'bg-indigo-600 text-white hover:bg-indigo-700'
                      : 'bg-white text-indigo-600 hover:bg-indigo-50',
                    'mt-6 w-full inline-block py-2 px-8 border border-transparent rounded-md shadow-sm text-center text-sm font-medium sm:mt-0 sm:w-auto lg:mt-6 lg:w-full',
                  ]"
                  >{{ plan.cta }}</a
                >
              </div>
            </div>
            <h4 class="sr-only">Features</h4>
            <ul
              role="list"
              :class="[
                plan.featured
                  ? 'border-gray-200 divide-gray-200'
                  : 'border-indigo-500 divide-indigo-500 divide-opacity-75',
                'mt-7 border-t divide-y lg:border-t-0',
              ]"
            >
              <li
                v-for="mainFeature in plan.mainFeatures"
                :key="mainFeature.id"
                class="flex items-center py-3"
              >
                <CheckIcon
                  :class="[
                    plan.featured ? 'text-indigo-500' : 'text-indigo-200',
                    'w-5 h-5 flex-shrink-0',
                  ]"
                  aria-hidden="true"
                />
                <span
                  :class="[
                    plan.featured ? 'text-gray-600' : 'text-white',
                    'ml-3 text-sm font-medium',
                  ]"
                  >{{ mainFeature.value }}</span
                >
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>

    <h1
      class="text-2xl font-bold tracking-tight text-gray-900 sm:text-3xl text-center my-8"
    >
      <span class="block lg:inline">Itching to get started today?</span>
      <router-link id="enterprise-to-basic-pricing" :to="{ name: 'pricing' }">
        <button
          class="w-full md:w-1/3 m-auto transform md-shadow hover:scale-110 ease-in-out delay-150 duration-300 mt-6 block w-full sm:text-xl lg:text-lg xl:text-xl py-3 px-4 rounded-md shadow bg-gradient-to-r rounded-md shadow bg-gradient-to-r from-indigo-500 to-violet-600 text-white font-medium hover:from-indigo-600 hover:to-violet-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-cyan-400 focus:ring-offset-gray-900"
        >
          Try the Starter Plah
        </button>
      </router-link>
    </h1>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from "vue";
import { CheckIcon, XMarkIcon } from "@heroicons/vue/24/solid";
import { useShopStore } from "@/stores/shop";

const shop = useShopStore();

const showBilling = ref();

onMounted(async () => {
  await shop.fetchCloudPlans();
});

const plans = ref([
  {
    title: "Enterprise",
    href: import.meta.env.VITE_ENTERPRISE_CLOUD_QUOTE_FORM,
    cta: "Get a Quote",
    featured: computed(() => showBilling.value === "invoice"),
    description:
      "Customized for additive manufacturing operations and digital warehouses.",
    priceOnRequest:
      "Customized for additive manufacturing operations and digital warehouses.",
    mainFeatures: [
      { id: 1, value: "Custom software integrations" },
      { id: 2, value: "Single Sign-on" },
      { id: 3, value: "Audit trail" },
      { id: 4, value: "On-prem installation" },
      // { id: 3, value: 'Additional support for Rock Pi, Orange Pi' },
    ],
  },
  {
    title: "OEM",
    href: import.meta.env.VITE_OEM_QUOTE_FORM,
    cta: "Get a Quote",
    featured: false,
    description: "Customized for original 3D printer equipment manufacturers",
    priceOnRequest:
      "Customized for original 3D printer equipment manufacturers",
    mainFeatures: [
      { id: 1, value: "Large-format 3D printers" },
      { id: 2, value: "Customized for your product line" },
      { id: 3, value: "White-labeled branding" },
      { id: 4, value: "On-prem installation" },

      // { id: 3, value: 'Additional support for Rock Pi, Orange Pi' },
    ],
  },
  {
    title: "Education",
    href: import.meta.env.VITE_EDU_QUOTE_FORM,
    cta: "Get a Quote",
    featured: false,
    description: "Schools, libraries, research labs, and makerspaces.",
    priceOnRequest: "Schools, libraries, research labs, and makerspaces.",
    mainFeatures: [
      { id: 1, value: "Permission controls" },
      { id: 2, value: "Single Sign-on" },
      { id: 3, value: "K-12 and Higher Education" },
      { id: 4, value: "On-prem installation option" },
    ],
  },
]);
</script>
