<template>
    <div class="bg-gray-50">
      <div class="relative bg-indigo-600">
        <!-- Overlapping background -->
        <div aria-hidden="true" class="absolute bottom-0 hidden h-6 w-full bg-gray-50 lg:block" />
  
        <div class="relative mx-auto max-w-2xl px-6 pt-16 text-center sm:pt-32 lg:max-w-7xl lg:px-8">
          <h1 class="text-4xl font-bold tracking-tight text-white sm:text-6xl">
            <span class="block lg:inline">Simple pricing,</span>
            <span class="block lg:inline">no hidden fees</span>
          </h1>
          <p class="mt-4 text-xl text-indigo-100">Everything you need, nothing you don't. Pick a plan that best suits your business.</p>
        </div>
  
        <h2 class="sr-only">Plans</h2>
  
        <!-- Toggle -->
        <div class="relative mt-12 flex justify-center sm:mt-16">
          <div class="flex rounded-lg bg-indigo-700 p-0.5">
            <button type="button" class="relative whitespace-nowrap rounded-md border-indigo-700 bg-white py-2 px-6 text-sm font-medium text-indigo-700 shadow-sm hover:bg-indigo-50 focus:z-10 focus:outline-none focus:ring-2 focus:ring-white focus:ring-offset-2 focus:ring-offset-indigo-700">Monthly billing</button>
            <button type="button" class="relative ml-0.5 whitespace-nowrap rounded-md border border-transparent py-2 px-6 text-sm font-medium text-indigo-200 hover:bg-indigo-800 focus:z-10 focus:outline-none focus:ring-2 focus:ring-white focus:ring-offset-2 focus:ring-offset-indigo-700">Yearly billing</button>
          </div>
        </div>
  
        <!-- Cards -->
        <div class="relative mx-auto mt-8 max-w-2xl px-6 pb-8 sm:mt-12 lg:max-w-7xl lg:px-8 lg:pb-0">
          <!-- Decorative background -->
          <div aria-hidden="true" class="absolute inset-0 top-4 bottom-6 left-8 right-8 hidden rounded-tl-lg rounded-tr-lg bg-indigo-700 lg:block" />
  
          <div class="relative space-y-6 lg:grid lg:grid-cols-3 lg:space-y-0">
            <div v-for="plan in plans" :key="plan.title" :class="[plan.featured ? 'bg-white ring-2 ring-indigo-700 shadow-md' : 'bg-indigo-700 lg:bg-transparent', 'pt-6 px-6 pb-3 rounded-lg lg:px-8 lg:pt-12']">
              <div>
                <h3 :class="[plan.featured ? 'text-indigo-600' : 'text-white', 'text-base font-semibold']">{{ plan.title }}</h3>
                <div class="flex flex-col items-start sm:flex-row sm:items-center sm:justify-between lg:flex-col lg:items-start">
                  <div class="mt-3 flex items-center">
                    <p :class="[plan.featured ? 'text-indigo-600' : 'text-white', 'text-4xl font-bold tracking-tight']">${{ plan.priceMonthly }}</p>
                    <div class="ml-4">
                      <p :class="[plan.featured ? 'text-gray-700' : 'text-white', 'text-sm']">USD / mo</p>
                      <p :class="[plan.featured ? 'text-gray-500' : 'text-indigo-200', 'text-sm']">Billed yearly (${{ plan.priceYearly }})</p>
                    </div>
                  </div>
                  <a href="#" :class="[plan.featured ? 'bg-indigo-600 text-white hover:bg-indigo-700' : 'bg-white text-indigo-600 hover:bg-indigo-50', 'mt-6 w-full inline-block py-2 px-8 border border-transparent rounded-md shadow-sm text-center text-sm font-medium sm:mt-0 sm:w-auto lg:mt-6 lg:w-full']">Buy {{ plan.title }}</a>
                </div>
              </div>
              <h4 class="sr-only">Features</h4>
              <ul role="list" :class="[plan.featured ? 'border-gray-200 divide-gray-200' : 'border-indigo-500 divide-indigo-500 divide-opacity-75', 'mt-7 border-t divide-y lg:border-t-0']">
                <li v-for="mainFeature in plan.mainFeatures" :key="mainFeature.id" class="flex items-center py-3">
                  <CheckIcon :class="[plan.featured ? 'text-indigo-500' : 'text-indigo-200', 'w-5 h-5 flex-shrink-0']" aria-hidden="true" />
                  <span :class="[plan.featured ? 'text-gray-600' : 'text-white', 'ml-3 text-sm font-medium']">{{ mainFeature.value }}</span>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>
  
      <!-- Feature comparison (up to lg) -->
      <section aria-labelledby="mobile-comparison-heading" class="lg:hidden">
        <h2 id="mobile-comparison-heading" class="sr-only">Feature comparison</h2>
  
        <div class="mx-auto max-w-2xl space-y-16 py-16 px-6">
          <div v-for="(plan, mobilePlanIndex) in plans" :key="mobilePlanIndex" class="border-t border-gray-200">
            <div :class="[plan.featured ? 'border-indigo-600' : 'border-transparent', '-mt-px pt-6 border-t-2 sm:w-1/2']">
              <h3 :class="[plan.featured ? 'text-indigo-600' : 'text-gray-900', 'text-sm font-bold']">{{ plan.title }}</h3>
              <p class="mt-2 text-sm text-gray-500">{{ plan.description }}</p>
            </div>
            <h4 class="mt-10 text-sm font-bold text-gray-900">Catered for business</h4>
  
            <div class="relative mt-6">
              <!-- Fake card background -->
              <div aria-hidden="true" class="pointer-events-none absolute inset-0 hidden sm:block">
                <div :class="[plan.featured ? 'shadow-md' : 'shadow', 'absolute right-0 w-1/2 h-full bg-white rounded-lg']" />
              </div>
  
              <div :class="[plan.featured ? 'ring-2 ring-indigo-600 shadow-md' : 'ring-1 ring-black ring-opacity-5 shadow', 'relative py-3 px-4 bg-white rounded-lg sm:p-0 sm:bg-transparent sm:rounded-none sm:ring-0 sm:shadow-none']">
                <dl class="divide-y divide-gray-200">
                  <div v-for="feature in features" :key="feature.title" class="flex items-center justify-between py-3 sm:grid sm:grid-cols-2">
                    <dt class="pr-4 text-sm font-medium text-gray-600">{{ feature.title }}</dt>
                    <dd class="flex items-center justify-end sm:justify-center sm:px-4">
                      <span v-if="typeof feature.tiers[mobilePlanIndex].value === 'string'" :class="[feature.tiers[mobilePlanIndex].featured ? 'text-indigo-600' : 'text-gray-900', 'text-sm font-medium']">{{ feature.tiers[mobilePlanIndex].value }}</span>
                      <template v-else>
                        <CheckIcon v-if="feature.tiers[mobilePlanIndex].value === true" class="mx-auto h-5 w-5 text-indigo-600" aria-hidden="true" />
                        <XMarkIcon v-else class="mx-auto h-5 w-5 text-gray-400" aria-hidden="true" />
                        <span class="sr-only">{{ feature.tiers[mobilePlanIndex].value === true ? 'Yes' : 'No' }}</span>
                      </template>
                    </dd>
                  </div>
                </dl>
              </div>
  
              <!-- Fake card border -->
              <div aria-hidden="true" class="pointer-events-none absolute inset-0 hidden sm:block">
                <div :class="[plan.featured ? 'ring-2 ring-indigo-600' : 'ring-1 ring-black ring-opacity-5', 'absolute right-0 w-1/2 h-full rounded-lg']" />
              </div>
            </div>
  
            <h4 class="mt-10 text-sm font-bold text-gray-900">Other perks</h4>
  
            <div class="relative mt-6">
              <!-- Fake card background -->
              <div aria-hidden="true" class="pointer-events-none absolute inset-0 hidden sm:block">
                <div :class="[plan.featured ? 'shadow-md' : 'shadow', 'absolute right-0 w-1/2 h-full bg-white rounded-lg']" />
              </div>
  
              <div :class="[plan.featured ? 'ring-2 ring-indigo-600 shadow-md' : 'ring-1 ring-black ring-opacity-5 shadow', 'relative py-3 px-4 bg-white rounded-lg sm:p-0 sm:bg-transparent sm:rounded-none sm:ring-0 sm:shadow-none']">
                <dl class="divide-y divide-gray-200">
                  <div v-for="perk in perks" :key="perk.title" class="flex justify-between py-3 sm:grid sm:grid-cols-2">
                    <dt class="text-sm font-medium text-gray-600 sm:pr-4">{{ perk.title }}</dt>
                    <dd class="text-center sm:px-4">
                      <CheckIcon v-if="perk.tiers[mobilePlanIndex].value === true" class="mx-auto h-5 w-5 text-indigo-600" aria-hidden="true" />
                      <XMarkIcon v-else class="mx-auto h-5 w-5 text-gray-400" aria-hidden="true" />
                      <span class="sr-only">{{ perk.tiers[mobilePlanIndex].value === true ? 'Yes' : 'No' }}</span>
                    </dd>
                  </div>
                </dl>
              </div>
  
              <!-- Fake card border -->
              <div aria-hidden="true" class="pointer-events-none absolute inset-0 hidden sm:block">
                <div :class="[plan.featured ? 'ring-2 ring-indigo-600' : 'ring-1 ring-black ring-opacity-5', 'absolute right-0 w-1/2 h-full rounded-lg']" />
              </div>
            </div>
          </div>
        </div>
      </section>
  
      <!-- Feature comparison (lg+) -->
      <section aria-labelledby="comparison-heading" class="hidden lg:block">
        <h2 id="comparison-heading" class="sr-only">Feature comparison</h2>
  
        <div class="mx-auto max-w-7xl py-24 px-8">
          <div class="flex w-full items-stretch border-t border-gray-200">
            <div class="-mt-px flex w-1/4 items-end py-6 pr-4">
              <h3 class="mt-auto text-sm font-bold text-gray-900">Catered for business</h3>
            </div>
            <div v-for="(plan, planIdx) in plans" :key="plan.title" aria-hidden="true" :class="[planIdx === plans.length - 1 ? '' : 'pr-4', '-mt-px pl-4 w-1/4']">
              <div :class="[plan.featured ? 'border-indigo-600' : 'border-transparent', 'py-6 border-t-2']">
                <p :class="[plan.featured ? 'text-indigo-600' : 'text-gray-900', 'text-sm font-bold']">{{ plan.title }}</p>
                <p class="mt-2 text-sm text-gray-500">{{ plan.description }}</p>
              </div>
            </div>
          </div>
  
          <div class="relative">
            <!-- Fake card backgrounds -->
            <div class="pointer-events-none absolute inset-0 flex items-stretch" aria-hidden="true">
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
                Business feature comparison
              </caption>
              <thead>
                <tr class="text-left">
                  <th scope="col">
                    <span class="sr-only">Feature</span>
                  </th>
                  <th v-for="plan in plans" :key="plan.title" scope="col">
                    <span class="sr-only">{{ plan.title }} plan</span>
                  </th>
                </tr>
              </thead>
              <tbody class="divide-y divide-gray-100">
                <tr v-for="feature in features" :key="feature.title">
                  <th scope="row" class="w-1/4 py-3 pr-4 text-left text-sm font-medium text-gray-600">{{ feature.title }}</th>
                  <td v-for="(tier, tierIdx) in feature.tiers" :key="tier.title" :class="[tierIdx === feature.tiers.length - 1 ? 'pl-4' : 'px-4', 'relative w-1/4 py-0 text-center']">
                    <span class="relative h-full w-full py-3">
                      <span v-if="typeof tier.value === 'string'" :class="[tier.featured ? 'text-indigo-600' : 'text-gray-900', 'text-sm font-medium']">{{ tier.value }}</span>
                      <template v-else>
                        <CheckIcon v-if="tier.value === true" class="mx-auto h-5 w-5 text-indigo-600" aria-hidden="true" />
                        <XMarkIcon v-else class="mx-auto h-5 w-5 text-gray-400" aria-hidden="true" />
                        <span class="sr-only">{{ tier.value === true ? 'Yes' : 'No' }}</span>
                      </template>
                    </span>
                  </td>
                </tr>
              </tbody>
            </table>
  
            <!-- Fake card borders -->
            <div class="pointer-events-none absolute inset-0 flex items-stretch" aria-hidden="true">
              <div class="w-1/4 pr-4" />
              <div class="w-1/4 px-4">
                <div class="h-full w-full rounded-lg ring-1 ring-black ring-opacity-5" />
              </div>
              <div class="w-1/4 px-4">
                <div class="h-full w-full rounded-lg ring-2 ring-indigo-600 ring-opacity-100" />
              </div>
              <div class="w-1/4 pl-4">
                <div class="h-full w-full rounded-lg ring-1 ring-black ring-opacity-5" />
              </div>
            </div>
          </div>
  
          <h3 class="mt-10 text-sm font-bold text-gray-900">Other perks</h3>
  
          <div class="relative mt-6">
            <!-- Fake card backgrounds -->
            <div class="pointer-events-none absolute inset-0 flex items-stretch" aria-hidden="true">
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
                Perk comparison
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
                <tr v-for="perk in perks" :key="perk.title">
                  <th scope="row" class="w-1/4 py-3 pr-4 text-left text-sm font-medium text-gray-600">{{ perk.title }}</th>
                  <td v-for="(tier, tierIdx) in perk.tiers" :key="tier.title" :class="[tierIdx === perk.tiers.length - 1 ? 'pl-4' : 'px-4', 'relative w-1/4 py-0 text-center']">
                    <span class="relative h-full w-full py-3">
                      <CheckIcon v-if="tier.value === true" class="mx-auto h-5 w-5 text-indigo-600" aria-hidden="true" />
                      <XMarkIcon v-else class="mx-auto h-5 w-5 text-gray-400" aria-hidden="true" />
                      <span class="sr-only">{{ tier.value === true ? 'Yes' : 'No' }}</span>
                    </span>
                  </td>
                </tr>
              </tbody>
            </table>
  
            <!-- Fake card borders -->
            <div class="pointer-events-none absolute inset-0 flex items-stretch" aria-hidden="true">
              <div class="w-1/4 pr-4" />
              <div class="w-1/4 px-4">
                <div class="h-full w-full rounded-lg ring-1 ring-black ring-opacity-5" />
              </div>
              <div class="w-1/4 px-4">
                <div class="h-full w-full rounded-lg ring-2 ring-indigo-600 ring-opacity-100" />
              </div>
              <div class="w-1/4 pl-4">
                <div class="h-full w-full rounded-lg ring-1 ring-black ring-opacity-5" />
              </div>
            </div>
          </div>
        </div>
      </section>
    </div>
  </template>
  
  <script setup>
  import { CheckIcon, XMarkIcon } from '@heroicons/vue/24/solid'
  
  const plans = [
    {
      title: 'Starter',
      featured: false,
      description: 'All your essential business finances, taken care of.',
      priceMonthly: 5,
      priceYearly: 56,
      mainFeatures: [
        { id: 1, value: 'Basic invoicing' },
        { id: 2, value: 'Easy to use accounting' },
        { id: 3, value: 'Mutli-accounts' },
      ],
    },
    {
      title: 'Scale',
      featured: true,
      description: 'The best financial services for your thriving business.',
      priceMonthly: 19,
      priceYearly: 220,
      mainFeatures: [
        { id: 1, value: 'Advanced invoicing' },
        { id: 2, value: 'Easy to use accounting' },
        { id: 3, value: 'Mutli-accounts' },
        { id: 4, value: 'Tax planning toolkit' },
        { id: 5, value: 'VAT & VATMOSS filing' },
        { id: 6, value: 'Free bank transfers' },
      ],
    },
    {
      title: 'Growth',
      featured: false,
      description: 'Convenient features to take your business to the next level.',
      priceMonthly: 12,
      priceYearly: 140,
      mainFeatures: [
        { id: 1, value: 'Basic invoicing' },
        { id: 2, value: 'Easy to use accounting' },
        { id: 3, value: 'Mutli-accounts' },
        { id: 4, value: 'Tax planning toolkit' },
      ],
    },
  ]
  const features = [
    {
      title: 'Tax Savings',
      tiers: [
        { title: 'starter', value: true },
        { title: 'popular', featured: true, value: true },
        { title: 'intermediate', value: true },
      ],
    },
    {
      title: 'Easy to use accounting',
      tiers: [
        { title: 'starter', value: true },
        { title: 'popular', featured: true, value: true },
        { title: 'intermediate', value: true },
      ],
    },
    {
      title: 'Multi-accounts',
      tiers: [
        { title: 'starter', value: '3 accounts' },
        { title: 'popular', featured: true, value: 'Unlimited accounts' },
        { title: 'intermediate', value: '7 accounts' },
      ],
    },
    {
      title: 'Invoicing',
      tiers: [
        { title: 'starter', value: '3 invoices' },
        { title: 'popular', featured: true, value: 'Unlimited invoices' },
        { title: 'intermediate', value: '10 invoices' },
      ],
    },
    {
      title: 'Exclusive offers',
      tiers: [
        { title: 'starter', value: false },
        { title: 'popular', featured: true, value: true },
        { title: 'intermediate', value: true },
      ],
    },
    {
      title: '6 months free advisor',
      tiers: [
        { title: 'starter', value: false },
        { title: 'popular', featured: true, value: true },
        { title: 'intermediate', value: true },
      ],
    },
    {
      title: 'Mobile and web access',
      tiers: [
        { title: 'starter', value: false },
        { title: 'popular', featured: true, value: true },
        { title: 'intermediate', value: false },
      ],
    },
  ]
  const perks = [
    {
      title: '24/7 customer support',
      tiers: [
        { title: 'starter', value: true },
        { title: 'popular', featured: true, value: true },
        { title: 'intermediate', value: true },
      ],
    },
    {
      title: 'Instant notifications',
      tiers: [
        { title: 'starter', value: true },
        { title: 'popular', featured: true, value: true },
        { title: 'intermediate', value: true },
      ],
    },
    {
      title: 'Budgeting tools',
      tiers: [
        { title: 'starter', value: true },
        { title: 'popular', featured: true, value: true },
        { title: 'intermediate', value: true },
      ],
    },
    {
      title: 'Digital receipts',
      tiers: [
        { title: 'starter', value: true },
        { title: 'popular', featured: true, value: true },
        { title: 'intermediate', value: true },
      ],
    },
    {
      title: 'Pots to separate money',
      tiers: [
        { title: 'starter', value: false },
        { title: 'popular', featured: true, value: true },
        { title: 'intermediate', value: true },
      ],
    },
    {
      title: 'Free bank transfers',
      tiers: [
        { title: 'starter', value: false },
        { title: 'popular', featured: true, value: true },
        { title: 'intermediate', value: false },
      ],
    },
    {
      title: 'Business debit card',
      tiers: [
        { title: 'starter', value: false },
        { title: 'popular', featured: true, value: true },
        { title: 'intermediate', value: false },
      ],
    },
  ]
  </script>