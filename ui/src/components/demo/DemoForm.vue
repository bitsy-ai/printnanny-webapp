<script setup lang="ts">
import { ref, reactive } from "vue";
import { RouterLink, useRouter } from "vue-router";
import { LockClosedIcon, ArrowPathIcon } from "@heroicons/vue/24/solid";
import { Field, ErrorMessage, Form } from "vee-validate";
import { Disclosure, DisclosureButton, DisclosurePanel } from "@headlessui/vue";
import { MinusSmallIcon, PlusSmallIcon } from "@heroicons/vue/24/outline";
import * as yup from "yup";
import type * as apiTypes from "printnanny-api-client";
import { useDemoStore } from "@/stores/demo";
import { error } from "@/stores/alerts";

const router = useRouter();
const loading = ref(false);
const submitted = ref(false);

const file = ref(undefined as undefined | string);
const store = useDemoStore();

const state = reactive({
  loading,
});

// define a validation schema
const schema = yup.object({
  email: yup.string().required().email(),
});

async function onSubmit(values: any) {
  state.loading = true;
  if (file.value === undefined) {
    return error(
      "Select a PNG or JPEG photo",
      "You must select a photo to try PrintNanny. Use the 'Choose File' button to select a file, then submit your test. PrintNanny will email you when your results are available."
    );
  }
  await store.submit(values.email, file.value as string);
  state.loading = false;
}

function onChangeFile(e: any) {
  console.log("Selected file", e);
  const files = e.target.files || e.dataTransfer.files;
  if (!files.length) return;
  file.value = files[0];
}

const faqs = [
  {
    question: "How does PrintNanny work?",
    answer:
      "PrintNanny watches a camera feed, continuously scanning for 3D printed objects, a variety of defects, and 3D printer components (like the hotend nozzle). ",
    defaultOpen: true,
  },
  {
    question: "What kinds of defects are detected?",
    answer:
      "We currently detect filament spaghetti, bed adhesion issues, and layer warping.",
    defaultOpen: true,
  },
  {
    question: "Should I test other kinds of defects?",
    answer:
      "Yes, please do! PrintNanny is constantly learning. With your help, we'll be able to spot a wider variety of issues in the future.",
    defaultOpen: true,
  },
  {
    question: "What kind of 3D printers are supported?",
    answer:
      "Any desktop FDM/FFA printer should work with PrintNanny. Prusa and Ender are the most popular brands we see.",
    defaultOpen: true,
  },
  {
    question: "I have another question",
    answer:
      "Join our Discord server or email support@printnanny.ai. We're happy to chat more!",
    defaultOpen: true,
  },
];

const examples = [
  {
    header: "Example #1: spaghetti detected in Ultimaker 2+",
    description: [
    "The Ultimaker 2+ is a machine popular with educators, labs, and businesses looking for a solution that 'just works' in the $2,500 - $3,000 price range.",
    "Like any FDM/FFA 3D printer, the Ultimaker 2+ can produce defective prints.",
    "In this example, PrintNanny initially detects a healthy 3D-print object with a skirt/raft.",
    "Later on, the print object collapses and shifts outside of the skirt/raft. When subsequent layers fail to adhere to the 3D-printed object, PrintNanny sees filament spaghetti."
    ],
    images: [
      "/ui/images/demo/printnanny-ultimaker-healthy-1.png",
      "/ui/images/demo/printnanny-ultimaker-fail-1.png",
    ],
    defaultOpen: true,
  },
  {
    header: "Example #2: adhesion issues leading to spaghetti",
    description: [
    "Common sense tells us 'where there's smoke, there's fire!' The same holds true in 3D printing: subtle ealy adhesion issues inevitably lead to catastrophic failures later on.",
    "As a first line of defense, PrintNanny monitors for bed and layer adhesion problems. That's why we taught PrintNanny how to spot a raft/skirt.",
    "As a result, PrintNanny can spot subtle shifts in orientation relative to the raft."
    ],
    images: [
      "/ui/images/demo/printnanny-skull-ok.png",
      "/ui/images/demo/printnanny-skull-adhesion-problems.png",
      "/ui/images/demo/printnanny-skull-spaghetti.png",
    ],
    defaultOpen: true,
  },
  {
    header: "Example #3: first layer adhesion issues in Ultimaker 2+",
    description: [
    "In this example, PrintNanny is monitoring from a top-down view. Our goal is to provide best-in-class quality control from any angle, under any lighting conditions, on any FDM/FFA machine.",
    "PrintNanny detects that early layers have failed to adhere, dooming the print job to failure."
    ],
    images: [
      "/ui/images/demo/printnanny-ultimaker-fail-2.png",
      "/ui/images/demo/printnanny-ultimaker-fail-3.png",

    ],
    defaultOpen: true,
  },
];
</script>
<template>
  <div class="grid grid-cols-1 lg:grid-cols-4 p-12 md:p-24">
    <div class="lg:col-span-2 max-w-md m-auto w-full space-y-8">
      <img
        class="mx-auto h-30 w-auto mt-8"
        src="@/assets/logo/logo-rect-light.svg"
        alt="PrintNanny"
      />
      <h1 class="my-6 text-center text-4xl font-extrabold text-gray-900">
        Try PrintNanny Risk-free
      </h1>
      <p class="mt-5 max-w-prose mx-auto text-xl text-gray-500 text-center">
        Upload your gnarliest FDM/FFA 3D print failures to test our detection
        system.
      </p>

      <hr class="w-64 h-px my-8 mx-auto bg-gray-200 border-0" />

      <transition
        enter-active-class="transition ease-out duration-100"
        enter-from-class="transform opacity-0 scale-95"
        enter-to-class="transform opacity-100 scale-100"
        leave-active-class="transition ease-in duration-75"
        leave-from-class="transform opacity-100 scale-100"
        leave-to-class="transform opacity-0 scale-95"
      >
        <Form v-slot="{ meta }" :validation-schema="schema" @submit="onSubmit">
          <label class="block text-sm text-gray-900" for="file_input"
            >Select a photo of a 3D print job:</label
          >
          <input
            id="file_input"
            class="p-1 mt-1 block w-full text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-200 focus:outline-none"
            aria-describedby="file_input_help"
            type="file"
            accept="image/png, image/jpeg"
            @change="onChangeFile"
          />
          <hr class="w-64 h-px my-8 mx-auto bg-gray-200 border-0" />
          <label for="email" class="block text-sm text-gray-900"
            >We'll email your test results:</label
          >
          <Field
            id="email"
            name="email"
            type="email"
            autocomplete="email"
            class="appearance-none mt-1 relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"
            placeholder="Email address"
            rules="required"
          />
          <error-message
            class="text-red-500 text-sm"
            name="email"
          ></error-message>

          <button
            id="email-submit"
            :disabled="state.loading || !meta.valid || file === undefined"
            type="submit"
            class="group mt-2 relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 disabled:opacity-25"
          >
            <span class="absolute left-0 inset-y-0 flex items-center pl-3">
              <ArrowPathIcon
                v-if="state.loading"
                class="animate-spin h-5 w-5 text-white"
                aria-hidden="true"
              />
            </span>
            Get Results
          </button>
        </Form>
      </transition>
    </div>
    <div class="lg:col-span-2 w-3/4 mx-auto px-4 py-4">
      <div class="mx-auto divide-y divide-gray-900/10">
        <h2 class="text-4xl font-extrabold text-gray-900">
          Frequently asked questions
        </h2>
        <dl class="mt-10 space-y-6 divide-y divide-gray-900/10">
          <Disclosure
            v-for="faq in faqs"
            :key="faq.question"
            v-slot="{ open }"
            as="div"
            class="pt-6"
            :default-open="faq.defaultOpen"
          >
            <dt>
              <DisclosureButton
                class="flex w-full items-start justify-between text-left text-gray-900"
              >
                <span class="text-base font-semibold leading-7">{{
                  faq.question
                }}</span>
                <span class="ml-6 flex h-7 items-center">
                  <PlusSmallIcon
                    v-if="!open"
                    class="h-6 w-6"
                    aria-hidden="true"
                  />
                  <MinusSmallIcon v-else class="h-6 w-6" aria-hidden="true" />
                </span>
              </DisclosureButton>
            </dt>
            <DisclosurePanel as="dd" class="mt-2 pr-12">
              <p class="text-base leading-7 text-gray-600">{{ faq.answer }}</p>
            </DisclosurePanel>
          </Disclosure>
        </dl>
      </div>
      <a
        href="https://discord.gg/sf23bk2hPr"
        target="_blank"
        class="text-center w-full m-auto transform md-shadow hover:scale-110 ease-in-out delay-150 duration-300 mt-6 block w-full sm:text-xl lg:text-lg xl:text-xl py-3 px-4 rounded-md shadow bg-gradient-to-r rounded-md shadow bg-gradient-to-r from-indigo-500 to-violet-600 text-white font-medium hover:from-indigo-600 hover:to-violet-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-cyan-400 focus:ring-offset-gray-900"
      >
        Join Discord
      </a>
    </div>
    <div class="lg:col-span-4 mx-auto px-6 lg:px-8">
      <hr class="w-64 h-px my-8 mx-auto bg-gray-200 border-0" />

      <h2 class="my-6 text-center text-4xl font-extrabold text-gray-900">
        Examples
      </h2>
      <p class="text-center text-base leading-7 text-gray-600">
        Use the -/+ icons on the right to collapse/expand each example.
      </p>

      <div class="mx-auto divide-y divide-gray-900/10">
        <dl class="mt-10 space-y-6 divide-y divide-gray-900/10">
          <Disclosure
            v-for="example in examples"
            :key="example.header"
            v-slot="{ open }"
            as="div"
            class="pt-6"
            :default-open="example.defaultOpen"
          >
            <dt>
              <DisclosureButton
                class="flex w-full items-start justify-between text-left text-gray-900"
              >
                <span class="text-2xl font-semibold leading-7">{{
                  example.header
                }}</span>
                <span class="ml-6 flex h-7 items-center">
                  <PlusSmallIcon
                    v-if="!open"
                    class="h-6 w-6"
                    aria-hidden="true"
                  />
                  <MinusSmallIcon v-else class="h-6 w-6" aria-hidden="true" />
                </span>
              </DisclosureButton>
            </dt>
            <DisclosurePanel as="dd" class="mt-2 pr-12 space-y-2">
              <p class="text-base leading-7 text-gray-600" v-for="description in example.description" :key="description">
                {{ description }}
              </p>
              <div :class="['grid gap-4', `grid-cols-1 lg:grid-cols-${example.images.length}`]">
                <img v-for="img in example.images" :src="img" :key="img" class="w-full h-auto"/>
              </div>
            </DisclosurePanel>
          </Disclosure>
        </dl>
      </div>
    </div>
  </div>
</template>
