<template>
  <div class="bg-white">
    <div
      class="mx-auto max-w-2xl py-16 px-4 sm:py-24 sm:px-6 lg:max-w-7xl lg:px-8"
    >
      <h2 class="sr-only">Products</h2>

      <div
        class="grid grid-cols-1 gap-y-4 sm:grid-cols-2 sm:gap-x-6 sm:gap-y-10 lg:grid-cols-3 lg:gap-x-8"
      >
        <div
          v-for="product in products"
          :key="product.id"
          class="group relative flex flex-col overflow-hidden rounded-lg border border-gray-200 bg-white"
        >
          <a :href="slugToProductPageUrl(product.slug)">
            <div
              class="aspect-w-3 aspect-h-4 bg-gray-200 group-hover:opacity-75 sm:aspect-none sm:h-96"
            >
              <img
                v-for="(image, index) in product.images"
                :key="index"
                :src="image"
                :alt="product.description"
                class="object-center sm:w-full"
              />
            </div>
          </a>
          <div class="flex flex-1 flex-col space-y-2 p-4">
            <h3 class="text-sm font-medium text-gray-900">
              <a :href="slugToProductPageUrl(product.slug)">
                <span aria-hidden="true" class="absolute inset-0" />
                {{ product.name }}
              </a>
            </h3>
            <p class="text-sm text-gray-500">{{ product.description }}</p>
            <div class="flex flex-1 flex-col justify-end">
              <p class="text-base font-medium text-gray-900">
                {{
                  product.prices[0].human_readable_price.replace(
                    "(one time)",
                    ""
                  )
                }}
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useShopStore } from "@/stores/shop";

const shopStore = useShopStore();
const products = await shopStore.fetchProducts();

function slugToProductPageUrl(slug: string) {
  return `/shop/${slug}/`;
}

// const products = [
//   {
//     id: 1,
//     name: 'Basic Tee 8-Pack',
//     href: '#',
//     price: '$256',
//     description: 'Get the full lineup of our Basic Tees. Have a fresh shirt all week, and an extra for laundry day.',
//     options: '8 colors',
//     imageSrc: 'https://tailwindui.com/img/ecommerce-images/category-page-02-image-card-01.jpg',
//     imageAlt: 'Eight shirts arranged on table in black, olive, grey, blue, white, red, mustard, and green.',
//   },
//   {
//     id: 2,
//     name: 'Basic Tee',
//     href: '#',
//     price: '$32',
//     description: 'Look like a visionary CEO and wear the same black t-shirt every day.',
//     options: 'Black',
//     imageSrc: 'https://tailwindui.com/img/ecommerce-images/category-page-02-image-card-02.jpg',
//     imageAlt: 'Front of plain black t-shirt.',
//   },
//   // More products...
// ]
</script>
