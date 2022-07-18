<script setup lang="ts">
import { useAlertStore } from "@/stores/alerts";
import { Field, ErrorMessage, Form } from "vee-validate";
import type * as apiTypes from "printnanny-api-client";

const alertStore = useAlertStore();
alertStore.fetchSettingsMetadata();
</script>
<template>
<div class="p-12">
          <h2 class="text-2xl font-bold">Notification Settings</h2>
          <div class="mt-8 max-w-md">
            <div class="grid grid-cols-1 gap-6">
              <label class="block">
                <span class="text-gray-700">Full name</span>
                <input type="text" class="
                    mt-1
                    block
                    w-full
                    rounded-md
                    border-gray-300
                    shadow-sm
                    focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50
                  " placeholder="">
              </label>
              <label class="block">
                <span class="text-gray-700">Email address</span>
                <input type="email" class="
                    mt-1
                    block
                    w-full
                    rounded-md
                    border-gray-300
                    shadow-sm
                    focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50
                  " placeholder="john@example.com">
              </label>
              <label class="block">
                <span class="text-gray-700">When is your event?</span>
                <input type="date" class="
                    mt-1
                    block
                    w-full
                    rounded-md
                    border-gray-300
                    shadow-sm
                    focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50
                  ">
              </label>
              <fieldset class="block">
              <legend class="text-gray-700">What kind of notifications do you want to receive?</legend>
              <div class="mt-2">
                <div>
                  <label class="inline-flex items-center">
                    <input class="form-checkbox" type="checkbox" checked="">
                    <span class="ml-2">Option 1</span>
                  </label>
                </div>
                <div>
                  <label class="inline-flex items-center">
                    <input class="form-checkbox" type="checkbox">
                    <span class="ml-2">Option 2</span>
                  </label>
                </div>
                <div>
                  <label class="inline-flex items-center">
                    <input class="form-checkbox" type="checkbox">
                    <span class="ml-2">Option 3</span>
                  </label>
                </div>
              </div>
            </fieldset>
              <label class="block">
                <span class="text-gray-700">What kind of notifications do you want to receive?</span>
                <select class="
                    block
                    w-full
                    mt-1
                    rounded-md
                    border-gray-300
                    shadow-sm
                    focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50
                  ">
                  <option>Corporate event</option>
                  <option>Wedding</option>
                  <option>Birthday</option>
                  <option>Other</option>
                </select>
              </label>
              <label class="block">
                <span class="text-gray-700">Additional details</span>
                <textarea class="
                    mt-1
                    block
                    w-full
                    rounded-md
                    border-gray-300
                    shadow-sm
                    focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50
                  " rows="3"></textarea>
              </label>
              <div class="block">
                <div class="mt-2">
                  <div>
                    <label class="inline-flex items-center">
                      <input type="checkbox" class="
                          rounded
                          border-gray-300
                          text-indigo-600
                          shadow-sm
                          focus:border-indigo-300
                          focus:ring
                          focus:ring-offset-0
                          focus:ring-indigo-200
                          focus:ring-opacity-50
                        " checked="">
                      <span class="ml-2">Email me news and special offers</span>
                    </label>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

</template>
