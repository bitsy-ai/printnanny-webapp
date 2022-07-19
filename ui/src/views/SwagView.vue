<script setup lang="ts">
import HomePage from "@/components/pages/HomePage.vue";
import FooterNav from "@/components/nav/FooterNav.vue";
import StickyAlerts from "../components/alerts/StickyAlerts.vue";
import DashboardPage from "../components/pages/DashboardPage.vue";
import { ModelStl } from 'vue-3d-model';

import { ref, reactive } from 'vue'
import { StarIcon } from '@heroicons/vue/solid'
import { RadioGroup, RadioGroupLabel, RadioGroupOption } from '@headlessui/vue'
import { CurrencyDollarIcon, GlobeIcon } from '@heroicons/vue/outline'

const downloadUrl = "https://cdn.printnanny.ai/www/logostl/printnanny-logos.zip"
const product = {
  name: 'PrintNanny Coasters (Set of 6)',
  price: 'FREE SWAG',
  rating: 3.9,
  reviewCount: 512,
  href: '#',
  breadcrumbs: [
    { id: 1, name: 'Women', href: '#' },
    { id: 2, name: 'Clothing', href: '#' },
  ],
  stl: [
    {
      id: 1,
      src: 'https://cdn.printnanny.ai/www/logostl/logo_circle.stl',
      primary: true,
    },
    {
      id: 2,
      src: 'https://cdn.printnanny.ai/www/logostl/sleeping.stl',
      primary: false,
    },
    {
      id: 3,
      src: 'https://cdn.printnanny.ai/www/logostl/love.stl',
      primary: false,
    },
    {
      id: 4,
      src: 'https://cdn.printnanny.ai/www/logostl/confused.stl',
      primary: false,
    },
    {
      id: 5,
      src: 'https://cdn.printnanny.ai/www/logostl/crying.stl',
      primary: false,
    },
    {
      id: 6,
      src: 'https://cdn.printnanny.ai/www/logostl/surprised.stl',
      primary: false,
    },
  ],
  img: [],
  colors: [
    { name: 'Black', bgColor: 'bg-gray-900', selectedColor: 'ring-gray-900' },
    { name: 'Heather Grey', bgColor: 'bg-gray-400', selectedColor: 'ring-gray-400' },
  ],
  sizes: [
    { name: 'XXS', inStock: true },
    { name: 'XS', inStock: true },
    { name: 'S', inStock: true },
    { name: 'M', inStock: true },
    { name: 'L', inStock: true },
    { name: 'XL', inStock: false },
  ],
  description: `
    <p>Thank you for support PrintNanny's development through the Founding Member program! 💜</p>
    <p>I hope you enjoy this adorable set of coasters.</p>
    <p>For a polished result, print with two colors and sand any rough edges.</p>
  `,
  recommendedSettings: [
    "0.15mm layer height",
    "15% infill",
    "No supports needed",
  ],
}
const policies = [
  { name: 'International delivery', icon: GlobeIcon, description: 'Get your order in 2 years' },
  { name: 'Loyalty rewards', icon: CurrencyDollarIcon, description: "Don't look at other tees" },
]

const selectedColor = ref(product.colors[0]);
const selectedSize = ref(product.sizes[2]);

const rotation = {
                    x: 0,
                    y: -0.1,
                    z: 0,
                    };
</script>

<template>
  <main>
    <StickyAlerts />
    <DashboardPage >
        <template #content>

  <div class="bg-white">
    <div class="pt-6 pb-16 sm:pb-24">
      <div class="mt-8 max-w-2xl mx-auto px-4 sm:px-6 lg:max-w-7xl lg:px-8">
        <div class="lg:grid lg:grid-cols-12 lg:auto-rows-min lg:gap-x-8">
          <div class="lg:col-start-8 lg:col-span-5">
            <div class="flex justify-between">
              <h1 class="text-xl font-medium text-gray-900">
                {{ product.name }}
              </h1>
              <p class="text-xl font-medium text-gray-900">
                {{ product.price }}
              </p>
            </div>
          </div>

          <!-- Image gallery -->
          <div class="mt-8 lg:mt-0 lg:col-start-1 lg:col-span-7 lg:row-start-1 lg:row-span-3">
            <h2 class="sr-only">Images</h2>

            <div class="grid grid-cols-1 lg:grid-cols-2 lg:grid-rows-3 lg:gap-8">
              <model-stl 
                  :rotation="rotation"
                background-color="#1e1e1e"  crossOrigin="anonymous" v-for="stl in product.stl.filter((v) => v.primary)" :key="stl.id" :src="stl.src" :class="[stl.primary ? 'lg:col-span-2 lg:row-span-2' : 'hidden lg:block', 'rounded-lg']">
                </model-stl>
              <model-stl background-color="#1e1e1e"  crossOrigin="anonymous" v-for="stl in product.stl.filter((v) => !v.primary)" :key="stl.id" :src="stl.src" :class="[stl.primary ? 'lg:col-span-2 lg:row-span-2' : 'hidden lg:block', 'rounded-lg']"></model-stl>
            </div>
          </div>

          <div class="mt-8 lg:col-span-5">
            <a :href="downloadUrl">
                <button class="mt-8 w-full bg-indigo-600 border border-transparent rounded-md py-3 px-8 flex items-center justify-center text-base font-medium text-white hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">Download .zip</button>
            </a>

            <!-- Product details -->
            <div class="mt-10">

              <h2 class="text-sm font-medium text-gray-900">Click to drag model preview</h2>

              <div class="mt-4 prose prose-sm text-gray-500" v-html="product.description" />
            </div>

            <div class="mt-8 border-t border-gray-200 pt-8">
              <h2 class="text-sm font-medium text-gray-900">Recommended Settings</h2>

              <div class="mt-4 prose prose-sm text-gray-500">
                <ul role="list">
                  <li v-for="item in product.recommendedSettings" :key="item">{{ item }}</li>
                </ul>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
        </template>
    </DashboardPage>
  </main>
</template>