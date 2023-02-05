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
          class="absolute inset-0 top-4 bottom-6 left-8 right-8 hidden rounded-tl-lg rounded-tr-lg bg-indigo-700 lg:block"
        />
        <!-- monthly / annual billing tiers -->
        <div
          v-if="showBilling == 'monthly' || showBilling == 'yearly'"
          class="relative space-y-6 lg:grid lg:grid-cols-2 lg:space-y-0"
        >
          <div
            v-for="plan in plans.slice(0, 2)"
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
                <div
                  v-else-if="showBilling == 'monthly'"
                  class="mt-3 flex items-center"
                >
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
                  :href="plan.href"
                  :id="`${plan.sku}-${showBilling}`"
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

        <!-- main features -->
        <div
          v-else
          class="relative space-y-6 lg:grid lg:grid-cols-3 lg:space-y-0"
        >
          <div
            v-for="plan in plans.slice(2)"
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

    <!-- Toggle -->
    <h2 class="sr-only">Plans</h2>
    <div class="relative mt-12 flex justify-center sm:mt-16">
      <div class="flex rounded-lg bg-indigo-700 p-0.5">
        <button
          type="button"
          id="pricing-yearly-toggle"
          :class="[
            showBilling == 'yearly'
              ? 'text-indigo-700 bg-white border-indigo-700 hover:bg-indigo-50 focus:z-10 focus:outline-none focus:ring-2 focus:ring-white focus:ring-offset-2 focus:ring-offset-indigo-700'
              : 'text-indigo-200 hover:bg-indigo-800 focus:z-10 focus:outline-none focus:ring-2 focus:ring-white focus:ring-offset-2 focus:ring-offset-indigo-700',
          ]"
          class="relative whitespace-nowrap rounded-md py-2 px-6 text-sm font-medium shadow-sm"
          @click="() => (showBilling = 'yearly')"
        >
          Yearly billing
        </button>
        <button
          id="pricing-monthly-toggle"

          :class="[
            showBilling == 'monthly'
              ? 'text-indigo-700 bg-white hover:bg-indigo-50 focus:z-10 focus:outline-none focus:ring-2 focus:ring-white focus:ring-offset-2 focus:ring-offset-indigo-700'
              : 'text-indigo-200 hover:bg-indigo-800 focus:z-10 focus:outline-none focus:ring-2 focus:ring-white focus:ring-offset-2 focus:ring-offset-indigo-700',
          ]"
          type="button"
          class="relative ml-0.5 whitespace-nowrap rounded-md border border-transparent py-2 px-6 text-sm font-medium"
          @click="() => (showBilling = 'monthly')"
        >
          Monthly billing
        </button>
        <button
            id="pricing-invoice-toggle"

          :class="[
            showBilling == 'invoice'
              ? 'text-indigo-700 bg-white hover:bg-indigo-50 focus:z-10 focus:outline-none focus:ring-2 focus:ring-white focus:ring-offset-2 focus:ring-offset-indigo-700'
              : 'text-indigo-200 hover:bg-indigo-800 focus:z-10 focus:outline-none focus:ring-2 focus:ring-white focus:ring-offset-2 focus:ring-offset-indigo-700',
          ]"
          type="button"
          class="relative ml-0.5 whitespace-nowrap rounded-md border border-transparent py-2 px-6 text-sm font-medium"
          @click="() => (showBilling = 'invoice')"
        >
          Invoice billing
        </button>
      </div>
    </div>

    <!-- Feature comparison (up to lg) -->
    <section aria-labelledby="mobile-comparison-heading" class="lg:hidden">
      <h1 class="text-4xl font-bold tracking-tight text-gray-800 sm:text-6xl">
        <span class="block lg:inline">Money-back guarantee</span>
        <span class="block lg:inline">no hidden fees</span>
      </h1>
      <h2 id="mobile-comparison-heading" class="sr-only">Feature comparison</h2>

      <div class="mx-auto max-w-2xl space-y-16 py-16 px-6">
        <div
          v-for="(plan, mobilePlanIndex) in simplePlans"
          :key="mobilePlanIndex"
          class="border-t border-gray-200"
        >
          <div
            :class="[
              plan.featured ? 'border-indigo-600' : 'border-transparent',
              '-mt-px pt-6 border-t-2 sm:w-1/2',
            ]"
          >
            <h3
              :class="[
                plan.featured ? 'text-indigo-600' : 'text-gray-900',
                'text-sm font-bold',
              ]"
            >
              {{ plan.title }}
            </h3>
            <p class="mt-2 text-sm text-gray-500">{{ plan.description }}</p>
          </div>
          <h4 class="mt-10 text-sm font-bold text-gray-900">
            Automation for everyone
          </h4>

          <div class="relative mt-6">
            <!-- Fake card background -->
            <div
              aria-hidden="true"
              class="pointer-events-none absolute inset-0 hidden sm:block"
            >
              <div
                :class="[
                  plan.featured ? 'shadow-md' : 'shadow',
                  'absolute right-0 w-1/2 h-full bg-white rounded-lg',
                ]"
              />
            </div>

            <div
              :class="[
                plan.featured
                  ? 'ring-2 ring-indigo-600 shadow-md'
                  : 'ring-1 ring-black ring-opacity-5 shadow',
                'relative py-3 px-4 bg-white rounded-lg sm:p-0 sm:bg-transparent sm:rounded-none sm:ring-0 sm:shadow-none',
              ]"
            >
              <dl class="divide-y divide-gray-200">
                <div
                  v-for="feature in features"
                  :key="feature.title"
                  class="flex items-center justify-between py-3 sm:grid sm:grid-cols-2"
                >
                  <dt class="pr-4 text-sm font-medium text-gray-600">
                    {{ feature.title }}
                  </dt>
                  <dd
                    class="flex items-center justify-end sm:justify-center sm:px-4"
                  >
                    <span
                      v-if="
                        typeof feature.tiers[mobilePlanIndex].value === 'string'
                      "
                      :class="[
                        feature.tiers[mobilePlanIndex].featured
                          ? 'text-indigo-600'
                          : 'text-gray-900',
                        'text-sm font-medium',
                      ]"
                      >{{ feature.tiers[mobilePlanIndex].value }}</span
                    >
                    <template v-else>
                      <CheckIcon
                        v-if="feature.tiers[mobilePlanIndex].value === true"
                        class="mx-auto h-5 w-5 text-indigo-600"
                        aria-hidden="true"
                      />
                      <XMarkIcon
                        v-else
                        class="mx-auto h-5 w-5 text-gray-400"
                        aria-hidden="true"
                      />
                      <span class="sr-only">{{
                        feature.tiers[mobilePlanIndex].value === true
                          ? "Yes"
                          : "No"
                      }}</span>
                    </template>
                  </dd>
                </div>
              </dl>
            </div>

            <!-- Fake card border -->
            <div
              aria-hidden="true"
              class="pointer-events-none absolute inset-0 hidden sm:block"
            >
              <div
                :class="[
                  plan.featured
                    ? 'ring-2 ring-indigo-600'
                    : 'ring-1 ring-black ring-opacity-5',
                  'absolute right-0 w-1/2 h-full rounded-lg',
                ]"
              />
            </div>
          </div>

          <!-- hardware / software -->
          <h4 class="mt-10 text-sm font-bold text-gray-900">
            Included hardware & software
          </h4>

          <div class="relative mt-6">
            <!-- Fake card background -->
            <div
              aria-hidden="true"
              class="pointer-events-none absolute inset-0 hidden sm:block"
            >
              <div
                :class="[
                  plan.featured ? 'shadow-md' : 'shadow',
                  'absolute right-0 w-1/2 h-full bg-white rounded-lg',
                ]"
              />
            </div>

            <div
              :class="[
                plan.featured
                  ? 'ring-2 ring-indigo-600 shadow-md'
                  : 'ring-1 ring-black ring-opacity-5 shadow',
                'relative py-3 px-4 bg-white rounded-lg sm:p-0 sm:bg-transparent sm:rounded-none sm:ring-0 sm:shadow-none',
              ]"
            >
              <dl class="divide-y divide-gray-200">
                <div
                  v-for="item in hardwareAndSoftware"
                  :key="item.title"
                  class="flex justify-between py-3 sm:grid sm:grid-cols-2"
                >
                  <dt class="text-sm font-medium text-gray-600 sm:pr-4">
                    {{ item.title }}
                  </dt>
                  <dd class="text-center sm:px-4">
                    <CheckIcon
                      v-if="item.tiers[mobilePlanIndex].value === true"
                      class="mx-auto h-5 w-5 text-indigo-600"
                      aria-hidden="true"
                    />
                    <XMarkIcon
                      v-else
                      class="mx-auto h-5 w-5 text-gray-400"
                      aria-hidden="true"
                    />
                    <span class="sr-only">{{
                      item.tiers[mobilePlanIndex].value === true ? "Yes" : "No"
                    }}</span>
                  </dd>
                </div>
              </dl>
            </div>

            <!-- Fake card border -->
            <div
              aria-hidden="true"
              class="pointer-events-none absolute inset-0 hidden sm:block"
            >
              <div
                :class="[
                  plan.featured
                    ? 'ring-2 ring-indigo-600'
                    : 'ring-1 ring-black ring-opacity-5',
                  'absolute right-0 w-1/2 h-full rounded-lg',
                ]"
              />
            </div>
          </div>

          <!-- enterprise plus -->

          <h4 class="mt-10 text-sm font-bold text-gray-900">
            Enterprise features
          </h4>

          <div class="relative mt-6">
            <!-- Fake card background -->
            <div
              aria-hidden="true"
              class="pointer-events-none absolute inset-0 hidden sm:block"
            >
              <div
                :class="[
                  plan.featured ? 'shadow-md' : 'shadow',
                  'absolute right-0 w-1/2 h-full bg-white rounded-lg',
                ]"
              />
            </div>

            <div
              :class="[
                plan.featured
                  ? 'ring-2 ring-indigo-600 shadow-md'
                  : 'ring-1 ring-black ring-opacity-5 shadow',
                'relative py-3 px-4 bg-white rounded-lg sm:p-0 sm:bg-transparent sm:rounded-none sm:ring-0 sm:shadow-none',
              ]"
            >
              <dl class="divide-y divide-gray-200">
                <div
                  v-for="item in hardwareAndSoftware"
                  :key="item.title"
                  class="flex justify-between py-3 sm:grid sm:grid-cols-2"
                >
                  <dt class="text-sm font-medium text-gray-600 sm:pr-4">
                    {{ item.title }}
                  </dt>
                  <dd class="text-center sm:px-4">
                    <CheckIcon
                      v-if="item.tiers[mobilePlanIndex].value === true"
                      class="mx-auto h-5 w-5 text-indigo-600"
                      aria-hidden="true"
                    />
                    <XMarkIcon
                      v-else
                      class="mx-auto h-5 w-5 text-gray-400"
                      aria-hidden="true"
                    />
                    <span class="sr-only">{{
                      item.tiers[mobilePlanIndex].value === true ? "Yes" : "No"
                    }}</span>
                  </dd>
                </div>
              </dl>
            </div>

            <!-- Fake card border -->
            <div
              aria-hidden="true"
              class="pointer-events-none absolute inset-0 hidden sm:block"
            >
              <div
                :class="[
                  plan.featured
                    ? 'ring-2 ring-indigo-600'
                    : 'ring-1 ring-black ring-opacity-5',
                  'absolute right-0 w-1/2 h-full rounded-lg',
                ]"
              />
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Feature comparison (lg+) -->
    <section aria-labelledby="comparison-heading" class="hidden lg:block">
      <h2 id="comparison-heading" class="sr-only">Feature comparison</h2>

      <div class="mx-auto max-w-8xl py-16 px-8">
        <div class="flex w-full items-stretch border-t border-gray-200">
          <div class="-mt-px flex w-1/4 items-end py-6 pr-4">
            <h3 class="mt-auto text-sm font-bold text-gray-900">
              Automation for everyone
            </h3>
          </div>
          <div
            v-for="(plan, planIdx) in simplePlans"
            :key="plan.title"
            aria-hidden="true"
            :class="[
              planIdx === plans.length - 1 ? '' : 'pr-4',
              '-mt-px pl-4 w-1/4',
            ]"
          >
            <div
              :class="[
                plan.featured ? 'border-indigo-600' : 'border-transparent',
                'py-6 border-t-2',
              ]"
            >
              <p
                :class="[
                  plan.featured ? 'text-indigo-600' : 'text-gray-900',
                  'text-sm font-bold',
                ]"
              >
                {{ plan.title }}
              </p>
              <p class="mt-2 text-sm text-gray-500">{{ plan.description }}</p>
            </div>
          </div>
        </div>

        <div class="relative">
          <!-- Fake card backgrounds -->
          <div
            class="pointer-events-none absolute inset-0 flex items-stretch"
            aria-hidden="true"
          >
            <div class="w-1/4 pr-4" />
            <div class="w-1/4 px-4">
              <div class="h-full w-full rounded-lg bg-white shadow" />
            </div>
            <div class="w-1/4 px-4">
              <div class="h-full w-full rounded-lg bg-white shadow-md" />
            </div>
            <div class="w-1/4 px-4">
              <div class="h-full w-full rounded-lg bg-white shadow-md" />
            </div>
          </div>

          <table class="relative w-full">
            <caption class="sr-only">
              Business feature comparison
            </caption>
            <thead>
              <tr class="text-left">
                <th scope="col">
                  <span class="sr-only">Feature</span>
                </th>
                <th v-for="plan in simplePlans" :key="plan.title" scope="col">
                  <span class="sr-only">{{ plan.title }} plan</span>
                </th>
              </tr>
            </thead>
            <tbody class="divide-y divide-gray-100">
              <tr v-for="feature in features" :key="feature.title">
                <th
                  scope="row"
                  class="w-1/4 py-3 pr-4 text-left text-sm font-medium text-gray-600"
                >
                  {{ feature.title }}
                </th>
                <td
                  v-for="(tier, tierIdx) in feature.tiers"
                  :key="tier.title"
                  :class="[
                    tierIdx === feature.tiers.length - 1 ? 'pl-4' : 'px-4',
                    'relative w-1/4 py-0 text-center',
                  ]"
                >
                  <span class="relative h-full w-full py-3">
                    <span
                      v-if="typeof tier.value === 'string'"
                      :class="[
                        tier.featured ? 'text-indigo-600' : 'text-gray-900',
                        'text-sm font-medium',
                      ]"
                      >{{ tier.value }}</span
                    >
                    <template v-else>
                      <CheckIcon
                        v-if="tier.value === true"
                        :class="[
                          tier.featured ? 'text-indigo-600' : 'text-gray-900',
                          'mx-auto h-5 w-5',
                        ]"
                        aria-hidden="true"
                      />
                      <XMarkIcon
                        v-else
                        class="mx-auto h-5 w-5 text-gray-400"
                        aria-hidden="true"
                      />
                      <span class="sr-only">{{
                        tier.value === true ? "Yes" : "No"
                      }}</span>
                    </template>
                  </span>
                </td>
              </tr>
            </tbody>
          </table>

          <!-- Fake card borders -->
          <div
            class="pointer-events-none absolute inset-0 flex items-stretch"
            aria-hidden="true"
          >
            <div class="w-1/4 pr-4" />
            <div
              v-for="plan in simplePlans"
              :key="plan.title"
              class="w-1/4 px-4"
            >
              <div
                :class="[
                  plan.featured
                    ? 'ring-2 ring-indigo-600 ring-opacity-100'
                    : 'ring-1 ring-black ring-opacity-5',
                  'h-full w-full rounded-lg ',
                ]"
                class="ring-1 ring-black ring-opacity-5"
              />
            </div>
          </div>
        </div>

        <h3 class="mt-10 text-sm font-bold text-gray-900">
          Included hardware & software
        </h3>

        <div class="relative mt-6">
          <!-- Fake card backgrounds -->
          <div
            class="pointer-events-none absolute inset-0 flex items-stretch"
            aria-hidden="true"
          >
            <div class="w-1/4 pr-4" />
            <div class="w-1/4 px-4">
              <div class="h-full w-full rounded-lg bg-white shadow" />
            </div>
            <div class="w-1/4 px-4">
              <div class="h-full w-full rounded-lg bg-white shadow-md" />
            </div>
            <div class="w-1/4 pl-4">
              <div class="h-full w-full rounded-lg bg-white shadow" />
            </div>
          </div>

          <table class="relative w-full">
            <caption class="sr-only">
              Hardware and software comparison
            </caption>
            <thead>
              <tr class="text-left">
                <th scope="col">
                  <span class="sr-only">Perk</span>
                </th>
                <th v-for="plan in simplePlans" :key="plan.title" scope="col">
                  <span class="sr-only">{{ plan.title }} plan</span>
                </th>
              </tr>
            </thead>
            <tbody class="divide-y divide-gray-100">
              <tr v-for="item in hardwareAndSoftware" :key="item.title">
                <th
                  scope="row"
                  class="w-1/4 py-3 pr-4 text-left text-sm font-medium text-gray-600"
                >
                  {{ item.title }}
                </th>
                <td
                  v-for="(tier, tierIdx) in item.tiers"
                  :key="tier.title"
                  :class="[
                    tierIdx === item.tiers.length - 1 ? 'pl-4' : 'px-4',
                    'relative w-1/4 py-0 text-center',
                  ]"
                >
                  <span class="relative h-full w-full py-3">
                    <span
                      v-if="typeof tier.value === 'string'"
                      :class="[
                        tier.featured ? 'text-indigo-600' : 'text-gray-900',
                        'text-sm font-medium',
                      ]"
                      >{{ tier.value }}</span
                    >
                    <template v-else>
                      <CheckIcon
                        v-if="tier.value === true"
                        class="mx-auto h-5 w-5 text-indigo-600"
                        aria-hidden="true"
                      />
                      <XMarkIcon
                        v-else
                        class="mx-auto h-5 w-5 text-gray-400"
                        aria-hidden="true"
                      />
                      <span class="sr-only">{{
                        tier.value === true ? "Yes" : "No"
                      }}</span>
                    </template>
                  </span>
                </td>
              </tr>
            </tbody>
          </table>

          <!-- Fake card borders -->
          <div
            class="pointer-events-none absolute inset-0 flex items-stretch"
            aria-hidden="true"
          >
            <div class="w-1/4 pr-4" />
            <div
              v-for="plan in simplePlans"
              :key="plan.title"
              class="w-1/4 px-4"
            >
              <div
                :class="[
                  plan.featured
                    ? 'ring-2 ring-indigo-600 ring-opacity-100'
                    : 'ring-1 ring-black ring-opacity-5',
                  'h-full w-full rounded-lg ',
                ]"
                class="ring-1 ring-black ring-opacity-5"
              />
            </div>
          </div>
        </div>

        <h3 class="mt-10 text-sm font-bold text-gray-900">
          Business & Enterprise
        </h3>

        <div class="relative mt-6">
          <!-- Fake card backgrounds -->
          <div
            class="pointer-events-none absolute inset-0 flex items-stretch"
            aria-hidden="true"
          >
            <div class="w-1/4 pr-4" />
            <div class="w-1/4 px-4">
              <div class="h-full w-full rounded-lg bg-white shadow" />
            </div>
            <div class="w-1/4 px-4">
              <div class="h-full w-full rounded-lg bg-white shadow-md" />
            </div>
            <div class="w-1/4 pl-4">
              <div class="h-full w-full rounded-lg bg-white shadow" />
            </div>
          </div>

          <table class="relative w-full">
            <caption class="sr-only">
              Enterprise feature comparison
            </caption>
            <thead>
              <tr class="text-left">
                <th scope="col">
                  <span class="sr-only">Perk</span>
                </th>
                <th v-for="plan in plans" :key="plan.title" scope="col">
                  <span class="sr-only">{{ plan.title }} plan</span>
                </th>
              </tr>
            </thead>
            <tbody class="divide-y divide-gray-100">
              <tr v-for="item in enterprisePlus" :key="item.title">
                <th
                  scope="row"
                  class="w-1/4 py-3 pr-4 text-left text-sm font-medium text-gray-600"
                >
                  {{ item.title }}
                </th>
                <td
                  v-for="(tier, tierIdx) in item.tiers"
                  :key="tier.title"
                  :class="[
                    tierIdx === item.tiers.length - 1 ? 'pl-4' : 'px-4',
                    'relative w-1/4 py-0 text-center',
                  ]"
                >
                  <span class="relative h-full w-full py-3">
                    <span
                      v-if="typeof tier.value === 'string'"
                      :class="[
                        tier.featured ? 'text-indigo-600' : 'text-gray-900',
                        'text-sm font-medium',
                      ]"
                      >{{ tier.value }}</span
                    >
                    <template v-else>
                      <CheckIcon
                        v-if="tier.value === true"
                        class="mx-auto h-5 w-5 text-indigo-600"
                        aria-hidden="true"
                      />
                      <XMarkIcon
                        v-else
                        class="mx-auto h-5 w-5 text-gray-400"
                        aria-hidden="true"
                      />
                      <span class="sr-only">{{
                        tier.value === true ? "Yes" : "No"
                      }}</span>
                    </template>
                  </span>
                </td>
              </tr>
            </tbody>
          </table>

          <!-- Fake card borders -->
          <div
            class="pointer-events-none absolute inset-0 flex items-stretch"
            aria-hidden="true"
          >
            <div class="w-1/4 pr-4" />
            <div
              v-for="plan in simplePlans"
              :key="plan.title"
              class="w-1/4 px-4"
            >
              <div
                :class="[
                  plan.featured
                    ? 'ring-2 ring-indigo-600 ring-opacity-100'
                    : 'ring-1 ring-black ring-opacity-5',
                  'h-full w-full rounded-lg ',
                ]"
                class="ring-1 ring-black ring-opacity-5"
              />
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from "vue";
import { CheckIcon, XMarkIcon } from "@heroicons/vue/24/solid";
import { useShopStore } from "@/stores/shop";

const showBilling = ref("yearly");
const shop = useShopStore();

onMounted(async () =>{
    await shop.fetchCloudPlans();
})

const plans = ref([
  {
    href: computed(() => "/shop/checkout/cloud-starter-plan/" + showBilling.value),
    cta: "Try Starter Risk-Free",
    title: "Starter",
    sku: "cloud-starter-plan",
    featured: false,
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
    href: computed(() => "/shop/checkout/cloud-starter-plan/" + showBilling.value),
    featured: computed(() => showBilling.value !== "invoice"),
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
  {
    title: "Enterprise",
    href: "",
    cta: "Get a Quote",
    featured: computed(() => showBilling.value === "invoice"),
    description:
      "Customized for additive manufacturing operations and digital warehouses.",
    priceOnRequest:
      "Customized for additive manufacturing operations and digital warehouses.",
    //   priceMonthly: 12,
    //   priceYearly: 140,
    mainFeatures: [
      { id: 1, value: "Custom software integrations" },
      { id: 2, value: "Single Sign-on" },
      { id: 3, value: "Audit trail" },
      { id: 4, value: "On-prem installation option" },
      // { id: 3, value: 'Additional support for Rock Pi, Orange Pi' },
    ],
  },
  {
    title: "OEM",
    href: "",
    cta: "Get a Quote",
    featured: false,
    description: "Customized for manufacturers of 3D printers.",
    priceOnRequest: "Customized for manufacturers of 3d printers.",
    //   priceMonthly: 12,
    //   priceYearly: 140,
    mainFeatures: [
      { id: 1, value: "Large-format 3D printers" },
      { id: 2, value: "Customized for your product line" },
      { id: 3, value: "White-labeled branding" },
      { id: 4, value: "On-prem installation option" },

      // { id: 3, value: 'Additional support for Rock Pi, Orange Pi' },
    ],
  },
  {
    title: "Education",
    href: "",
    cta: "Get a Quote",
    featured: false,
    description: "Schools, libraries, research labs, and makerspaces.",
    priceOnRequest: "Schools, libraries, research labs, and makerspaces.",
    //   priceMonthly: 12,
    //   priceYearly: 140,
    mainFeatures: [
      { id: 1, value: "Permission controls" },
      { id: 2, value: "Single Sign-on" },
      { id: 3, value: "K-12 and Higher Education" },
      { id: 4, value: "On-prem installation option" },
    ],
  },
]);

const simplePlans = ref(
  plans.value.slice(0, 2).concat({
    title: "Enterprise, OEM, Education",
    href: "",
    cta: "Get a Quote",
    featured: computed(() => showBilling.value === "invoice"),
    description:
      "Invoice billing available for enterprise, OEM manufacturers, and K-12/higher education.",
    priceOnRequest: "",
    mainFeatures: [
      { id: 1, value: "Permission controls" },
      { id: 2, value: "Single Sign-on" },
      { id: 3, value: "K-12 and Higher Education" },
      { id: 4, value: "On-prem installation option" },
    ],
  })
);

const features = ref([
  {
    title: "AI-powered quality monitoring",
    tiers: [
      { title: "starter", value: true },
      {
        title: "popular",
        featured: computed(() => showBilling.value != "invoice"),
        value: true,
      },
      {
        title: "enterprise",
        featured: computed(() => showBilling.value === "invoice"),
        value: true,
      },
    ],
  },
  {
    title: "High-quality camera stream",
    tiers: [
      { title: "starter", value: true },
      {
        title: "popular",
        featured: computed(() => showBilling.value != "invoice"),
        value: true,
      },
      {
        title: "enterprise",
        featured: computed(() => showBilling.value === "invoice"),
        value: true,
      },
    ],
  },
  {
    title: "Remote Access (Tailscale VPN)",
    tiers: [
      { title: "starter", value: true },
      {
        title: "popular",
        featured: computed(() => showBilling.value != "invoice"),
        value: true,
      },
      {
        title: "enterprise",
        featured: computed(() => showBilling.value === "invoice"),
        value: true,
      },
    ],
  },

  {
    title: "Cloud Storage",
    tiers: [
      { title: "starter", value: "10 GB" },
      {
        title: "popular",
        featured: computed(() => showBilling.value != "invoice"),
        value: "Unlimited Storage",
      },
      {
        title: "enterprise",
        featured: computed(() => showBilling.value === "invoice"),
        value: "Unlimited Storage",
      },
    ],
  },
  {
    title: "Number of Printers",
    tiers: [
      { title: "starter", value: "Up to 3 printers" },
      {
        title: "popular",
        featured: computed(() => showBilling.value != "invoice"),
        value: "Unlimited Printers",
      },
      {
        title: "enterprise",
        featured: computed(() => showBilling.value === "invoice"),
        value: "Unlimited Printers",
      },
    ],
  },
  {
    title: "Email notifications",
    tiers: [
      { title: "starter", value: true },
      { title: "popular", featured: true, value: true },
      { title: "enterprise", value: true },
    ],
  },
]);

const hardwareAndSoftware = ref([
  {
    title: "Supported hardware",
    tiers: [
      { title: "starter", value: "Raspberry Pi 4" },
      {
        title: "popular",
        featured: computed(() => showBilling.value != "invoice"),
        value: "Raspberry Pi 4",
      },
      {
        title: "enterprise",
        featured: computed(() => showBilling.value === "invoice"),
        value: "Raspberry Pi 4, Rock Pi, Orange Pi",
      },
    ],
  },
  {
    title: "Over-the-air updates",
    tiers: [
      { title: "starter", value: true },
      {
        title: "popular",
        featured: computed(() => showBilling.value != "invoice"),
        value: true,
      },
      {
        title: "enterprise",
        featured: computed(() => showBilling.value === "invoice"),
        value: true,
      },
    ],
  },
  {
    title: "OctoPrint",
    tiers: [
      { title: "starter", value: true },
      {
        title: "popular",
        featured: computed(() => showBilling.value != "invoice"),
        value: true,
      },
      {
        title: "enterprise",
        featured: computed(() => showBilling.value === "invoice"),
        value: true,
      },
    ],
  },
  {
    title: "Mainsail / Klipper / Moonraker",
    tiers: [
      { title: "starter", value: true },
      {
        title: "popular",
        featured: computed(() => showBilling.value != "invoice"),
        value: true,
      },
      {
        title: "enterprise",
        featured: computed(() => showBilling.value === "invoice"),
        value: true,
      },
    ],
  },
  {
    title: "Hardware included",
    tiers: [
      { title: "starter", value: false },
      {
        title: "popular",
        featured: computed(() => showBilling.value != "invoice"),
        value: false,
      },
      {
        title: "enterprise",
        featured: computed(() => showBilling.value === "invoice"),
        value: true,
      },
    ],
  },
]);

const enterprisePlus = ref([
  {
    title: "Multi-accounts",
    tiers: [
      { title: "starter", value: "1 account" },
      {
        title: "popular",
        featured: computed(() => showBilling.value != "invoice"),
        value: "Up to 10 accounts",
      },
      {
        title: "enterprise",
        featured: computed(() => showBilling.value === "invoice"),
        value: "Unlimited accounts",
      },
    ],
  },
  {
    title: "Permission Controls",
    tiers: [
      { title: "starter", value: false },
      {
        title: "popular",
        featured: computed(() => showBilling.value != "invoice"),
        value: false,
      },
      {
        title: "enterprise",
        featured: computed(() => showBilling.value === "invoice"),
        value: "Role-based access-control",
      },
    ],
  },
  {
    title: "Custom OS Image",
    tiers: [
      { title: "starter", value: false },
      {
        title: "popular",
        featured: computed(() => showBilling.value != "invoice"),
        value: false,
      },
      {
        title: "enterprise",
        featured: computed(() => showBilling.value === "invoice"),
        value: true,
      },
    ],
  },
  {
    title: "Custom Software Integrations",
    tiers: [
      { title: "starter", value: false },
      {
        title: "popular",
        featured: computed(() => showBilling.value != "invoice"),
        value: false,
      },
      {
        title: "enterprise",
        featured: computed(() => showBilling.value === "invoice"),
        value: true,
      },
    ],
  },
]);
</script>
