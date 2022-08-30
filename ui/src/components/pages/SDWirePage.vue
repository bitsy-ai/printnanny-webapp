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
    <div class="mx-auto py-16 px-4 sm:py-24 sm:px-6 lg:max-w-7xl lg:px-8">
      <!-- Product -->
      <div class="lg:grid lg:grid-cols-7 lg:grid-rows-1 lg:gap-x-8 lg:gap-y-10 xl:gap-x-16">
        <!-- Product image -->
        <div class="lg:col-span-4 lg:row-end-1">
          <div class="aspect-w-4 aspect-h-3 overflow-hidden rounded-lg bg-gray-100">
            <img src="@/assets/images/sdwire/SDWire-3D-front-v1.4-r1.jpg" :alt="product.imageAlt" class="object-cover object-center" />
          </div>
        </div>

        <!-- Product details -->
        <div class="mx-auto mt-14 max-w-2xl sm:mt-16 lg:col-span-3 lg:row-span-2 lg:row-end-2 lg:mt-0 lg:max-w-none">
          <div class="flex flex-col-reverse">
            <div class="mt-4">
              <h1 class="text-2xl font-bold tracking-tight text-gray-900 sm:text-3xl">{{ product.name }}</h1>

              <h2 id="information-heading" class="sr-only">Product information</h2>
              <p class="mt-2 text-sm text-gray-500">
                Version {{ product.version.name }} (Updated <time :datetime="product.version.datetime">{{ product.version.date }}</time
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

          <div class="mt-10 grid grid-cols-1 gap-x-6 gap-y-4 sm:grid-cols-2">
            <button type="button" class="flex w-full items-center justify-center rounded-md border border-transparent bg-indigo-600 py-3 px-8 text-base font-medium text-white hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2 focus:ring-offset-gray-50">Pre-order for {{ product.price }}</button>
            <i>Shipping & handling calculated at checkout</i>
          </div>

          <div class="mt-10 border-t border-gray-200 pt-10">
            <h3 class="text-sm font-medium text-gray-900">Highlights</h3>
            <div class="prose prose-sm mt-4 text-gray-500">
              <ul role="list">
                <li v-for="highlight in product.highlights" :key="highlight">{{ highlight }}</li>
              </ul>
            </div>
          </div>

          <div class="mt-10 border-t border-gray-200 pt-10">
            <h3 class="text-sm font-medium text-gray-900">License</h3>
            <p class="mt-4 text-sm text-gray-500">{{ license.summary }} <br><a :href="license.href" class="font-medium text-indigo-600 hover:text-indigo-500">Read the wiki</a></p>
          </div>

          <div class="mt-10 border-t border-gray-200 pt-10">
            <h3 class="text-sm font-medium text-gray-900">Support</h3>
            <p class="text-gray-500 text-sm">Email questions to leigh@printnanny.ai or <a href="https://github.com/bitsy-ai/printnanny-sdwire" class="text-indigo-500 hover:text-indigo-600">open a Github issue.</a></p>

          </div>
        </div>

        <div class="mx-auto mt-16 w-full max-w-2xl lg:col-span-4 lg:mt-0 lg:max-w-none">
          <TabGroup as="div">
            <div class="border-b border-gray-200">
              <TabList class="-mb-px flex space-x-8">
                <!-- TODO reviews
                <Tab as="template" v-slot="{ selected }">
                  <button :class="[selected ? 'border-indigo-600 text-indigo-600' : 'border-transparent text-gray-700 hover:text-gray-800 hover:border-gray-300', 'whitespace-nowrap border-b-2 py-6 text-sm font-medium']">Customer Reviews</button>
                </Tab>
                -->
                <Tab as="template" v-slot="{ selected }">
                  <button :class="[selected ? 'border-indigo-600 text-indigo-600' : 'border-transparent text-gray-700 hover:text-gray-800 hover:border-gray-300', 'whitespace-nowrap border-b-2 py-6 text-sm font-medium']">FAQ</button>
                </Tab>
                <Tab as="template" v-slot="{ selected }">
                  <button :class="[selected ? 'border-indigo-600 text-indigo-600' : 'border-transparent text-gray-700 hover:text-gray-800 hover:border-gray-300', 'whitespace-nowrap border-b-2 py-6 text-sm font-medium']">Timeline</button>
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
                    <dt class="mt-10 font-medium text-gray-900">{{ faq.question }}</dt>
                    <dd class="prose prose-sm mt-2 max-w-none text-gray-500">
                      <div v-html="faq.answer"></div>
                    </dd>
                  </template>
                </dl>
              </TabPanel>

              <TabPanel class="pt-10">
                <h3 class="sr-only">Timeline</h3>

                <div class="prose prose-sm max-w-none text-gray-500" v-html="timeline.content" />
              </TabPanel>
            </TabPanels>
          </TabGroup>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { StarIcon } from '@heroicons/vue/solid'
import { Tab, TabGroup, TabList, TabPanel, TabPanels } from '@headlessui/vue'

const product = {
  name: 'PrintNanny SDWire',
  version: { name: '1.4 revision 1', date: 'August 30, 2022', datetime: '2022-08-30' },
  price: '$89',
  description:
    'SDWire connects a device-under-test to a host computer, enabling flashing/re-imaging an SD card with no moving parts. SDWire functions as an SD card reader and SD card mux.',
  highlights: [
    'Fits Micro SD card slot or SD Card slot with adaptor',
    'Compatible with Raspberry Pi and Rock Pi',
    'Compatible with OctoPrint-SDWire',

    'Fabulous purple PCB design 💜',
    'Gold-finished contacts',
    '48.4mm x 21.6mm x 0.8mm'
  ],
  imageSrc: '@/assets/images/sdwire/SDWire-3D-front-v1.4-r1.jpg',
  imageAlt: '3D rendering of PrintNanny SDWire board (front view)',
}

// TODO prompt for review on delivery
// const reviews = {
//   average: 4,
//   featured: [
//     {
//       id: 1,
//       rating: 5,
//       content: `
//         <p>This icon pack is just what I need for my latest project. There's an icon for just about anything I could ever need. Love the playful look!</p>
//       `,
//       date: 'July 16, 2021',
//       datetime: '2021-07-16',
//       author: 'Emily Selman',
//       avatarSrc:
//         'https://images.unsplash.com/photo-1502685104226-ee32379fefbe?ixlib=rb-=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=8&w=256&h=256&q=80',
//     },
//     {
//       id: 2,
//       rating: 5,
//       content: `
//         <p>Blown away by how polished this icon pack is. Everything looks so consistent and each SVG is optimized out of the box so I can use it directly with confidence. It would take me several hours to create a single icon this good, so it's a steal at this price.</p>
//       `,
//       date: 'July 12, 2021',
//       datetime: '2021-07-12',
//       author: 'Hector Gibbons',
//       avatarSrc:
//         'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?ixlib=rb-=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=8&w=256&h=256&q=80',
//     },
//     // More reviews...
//   ],
// }
const faqs = [
  {
    question: "When will I receive my order?",
    answer: "The first batch of units will ship in October 2022."
  },
  {
    question: "When will I be charged for my order?",
    answer: "You will not be charged for your pre-order until the unit is ready to ship. When the unit is about to ship, we'll send you a confirmation email to make sure the shipping address and amount are correct."
  },
  {
    question: 'What can an SDWire be used for?',
    answer:
      `<p>SDWire is designed to make life easier for embedded software engineers and single-board computer enthusiasts. The SDWire board allows you to automate the transfer of SD card data, while the card is connected to a host (personal computer) and device-under-test (DUT) that boots from an SD card.</p> 
      <p>Anyone who has spent lots of time removing, re-imaging, re-inserting, SD cards will appreciate the quality-of-life improvements provided by SDWire.</p>
      <p>SDWire is an SD card mux, which allows you to transfer data to any device that reads from an SD card. The 3D printing community has discovered a clever application for SDWire, such as <a href="https://github.com/arekm/OctoPrint-Sdwire">OctoPrint-SDwire</a>.</p>


      `
  },
  {
    question: 'What is the difference between Tizen SDWire and PrintNanny SDWire?',
    answer:
      "PrintNanny SDWire is based on the open-source SDWire design by Tizen, with revisions to replace unavailable components with parts that are easy to source in the US.",
  },
  {
    question: "Is PrintNanny SDWire open source?",
    answer: `Yes! The KiCAD project will be available on Github. Watch <a href="https://github.com/bitsy-ai/PrintNanny SDwire" class="text-indigo-500 hover:text-indigo-600">this repo</a> to get notified of updates.`
  }
  // More FAQs...
]
const license = {
  href: 'https://wiki.tizen.org/SDWire',
  summary:
    'Based on Tizen SDWire',
}

const timeline = {
  content: `
    <h4>August 30, 2022</h4>
      <ul role="list">
      <li>PrintNanny SDWire is available for pre-order.</li>
      <li>Units ordered in September are expected to ship in October</li>
      </ul>

    <h4>August 28, 2022</h4>
        
    <ul role="list">
    <li>PCB revision 1 sent to manufacturer.</li>
    <li>20 units expected with 2-3 weeks lead time.</li>
    </ul>
    
  `,
}
</script>