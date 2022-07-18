<script setup lang="ts">
import { useAlertStore } from "@/stores/alerts";
import { Field, ErrorMessage, Form } from "vee-validate";
import type * as apiTypes from "printnanny-api-client";

const alertStore = useAlertStore();
alertStore.fetchSettingsMetadata();
alertStore.fetchSettings();

function isOptionChecked(value, fieldName){
  return alertStore.settings[fieldName].includes(value)
}

</script>
<template>
  <form class="space-y-8 divide-y divide-gray-200" v-if="alertStore.settingsFormReady">
    <div class="space-y-8 divide-y divide-gray-200">
      <div>
        <div>
          <h3 class="text-lg leading-6 font-medium text-gray-900">Print Alert Settings</h3>
          <p class="mt-1 text-sm text-gray-500">These settings control the kind of notifications you will receive.</p>
        </div>

        <div class="mt-6 grid grid-cols-1 gap-y-6 gap-x-4 sm:grid-cols-6">
          <div class="sm:col-span-4">
            <label for="username" class="block text-sm font-medium text-gray-700"> Username </label>
            <div class="mt-1 flex rounded-md shadow-sm">
              <span class="inline-flex items-center px-3 rounded-l-md border border-r-0 border-gray-300 bg-gray-50 text-gray-500 sm:text-sm"> workcation.com/ </span>
              <input type="text" name="username" id="username" autocomplete="username" class="flex-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full min-w-0 rounded-none rounded-r-md sm:text-sm border-gray-300" />
            </div>
          </div>

          <div class="sm:col-span-6">
            <label for="about" class="block text-sm font-medium text-gray-700"> About </label>
            <div class="mt-1">
              <textarea id="about" name="about" rows="3" class="shadow-sm focus:ring-indigo-500 focus:border-indigo-500 block w-full sm:text-sm border border-gray-300 rounded-md" />
            </div>
            <p class="mt-2 text-sm text-gray-500">Write a few sentences about yourself.</p>
          </div>

          <div class="sm:col-span-6">
            <label for="photo" class="block text-sm font-medium text-gray-700"> Photo </label>
            <div class="mt-1 flex items-center">
              <span class="h-12 w-12 rounded-full overflow-hidden bg-gray-100">
                <svg class="h-full w-full text-gray-300" fill="currentColor" viewBox="0 0 24 24">
                  <path d="M24 20.993V24H0v-2.996A14.977 14.977 0 0112.004 15c4.904 0 9.26 2.354 11.996 5.993zM16.002 8.999a4 4 0 11-8 0 4 4 0 018 0z" />
                </svg>
              </span>
              <button type="button" class="ml-5 bg-white py-2 px-3 border border-gray-300 rounded-md shadow-sm text-sm leading-4 font-medium text-gray-700 hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">Change</button>
            </div>
          </div>

          <div class="sm:col-span-6">
            <label for="cover-photo" class="block text-sm font-medium text-gray-700"> Cover photo </label>
            <div class="mt-1 flex justify-center px-6 pt-5 pb-6 border-2 border-gray-300 border-dashed rounded-md">
              <div class="space-y-1 text-center">
                <svg class="mx-auto h-12 w-12 text-gray-400" stroke="currentColor" fill="none" viewBox="0 0 48 48" aria-hidden="true">
                  <path d="M28 8H12a4 4 0 00-4 4v20m32-12v8m0 0v8a4 4 0 01-4 4H12a4 4 0 01-4-4v-4m32-4l-3.172-3.172a4 4 0 00-5.656 0L28 28M8 32l9.172-9.172a4 4 0 015.656 0L28 28m0 0l4 4m4-24h8m-4-4v8m-12 4h.02" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
                </svg>
                <div class="flex text-sm text-gray-600">
                  <label for="file-upload" class="relative cursor-pointer bg-white rounded-md font-medium text-indigo-600 hover:text-indigo-500 focus-within:outline-none focus-within:ring-2 focus-within:ring-offset-2 focus-within:ring-indigo-500">
                    <span>Upload a file</span>
                    <input id="file-upload" name="file-upload" type="file" class="sr-only" />
                  </label>
                  <p class="pl-1">or drag and drop</p>
                </div>
                <p class="text-xs text-gray-500">PNG, JPG, GIF up to 10MB</p>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="pt-8">
        <div>
          <h3 class="text-lg leading-6 font-medium text-gray-900">Personal Information</h3>
          <p class="mt-1 text-sm text-gray-500">Use a permanent address where you can receive mail.</p>
        </div>
        <div class="mt-6 grid grid-cols-1 gap-y-6 gap-x-4 sm:grid-cols-6">
          <div class="sm:col-span-3">
            <label for="first-name" class="block text-sm font-medium text-gray-700"> First name </label>
            <div class="mt-1">
              <input type="text" name="first-name" id="first-name" autocomplete="given-name" class="shadow-sm focus:ring-indigo-500 focus:border-indigo-500 block w-full sm:text-sm border-gray-300 rounded-md" />
            </div>
          </div>

          <div class="sm:col-span-3">
            <label for="last-name" class="block text-sm font-medium text-gray-700"> Last name </label>
            <div class="mt-1">
              <input type="text" name="last-name" id="last-name" autocomplete="family-name" class="shadow-sm focus:ring-indigo-500 focus:border-indigo-500 block w-full sm:text-sm border-gray-300 rounded-md" />
            </div>
          </div>

          <div class="sm:col-span-4">
            <label for="email" class="block text-sm font-medium text-gray-700"> Email address </label>
            <div class="mt-1">
              <input id="email" name="email" type="email" autocomplete="email" class="shadow-sm focus:ring-indigo-500 focus:border-indigo-500 block w-full sm:text-sm border-gray-300 rounded-md" />
            </div>
          </div>

          <div class="sm:col-span-3">
            <label for="country" class="block text-sm font-medium text-gray-700"> Country </label>
            <div class="mt-1">
              <select id="country" name="country" autocomplete="country-name" class="shadow-sm focus:ring-indigo-500 focus:border-indigo-500 block w-full sm:text-sm border-gray-300 rounded-md">
                <option>United States</option>
                <option>Canada</option>
                <option>Mexico</option>
              </select>
            </div>
          </div>

          <div class="sm:col-span-6">
            <label for="street-address" class="block text-sm font-medium text-gray-700"> Street address </label>
            <div class="mt-1">
              <input type="text" name="street-address" id="street-address" autocomplete="street-address" class="shadow-sm focus:ring-indigo-500 focus:border-indigo-500 block w-full sm:text-sm border-gray-300 rounded-md" />
            </div>
          </div>

          <div class="sm:col-span-2">
            <label for="city" class="block text-sm font-medium text-gray-700"> City </label>
            <div class="mt-1">
              <input type="text" name="city" id="city" autocomplete="address-level2" class="shadow-sm focus:ring-indigo-500 focus:border-indigo-500 block w-full sm:text-sm border-gray-300 rounded-md" />
            </div>
          </div>

          <div class="sm:col-span-2">
            <label for="region" class="block text-sm font-medium text-gray-700"> State / Province </label>
            <div class="mt-1">
              <input type="text" name="region" id="region" autocomplete="address-level1" class="shadow-sm focus:ring-indigo-500 focus:border-indigo-500 block w-full sm:text-sm border-gray-300 rounded-md" />
            </div>
          </div>

          <div class="sm:col-span-2">
            <label for="postal-code" class="block text-sm font-medium text-gray-700"> ZIP / Postal code </label>
            <div class="mt-1">
              <input type="text" name="postal-code" id="postal-code" autocomplete="postal-code" class="shadow-sm focus:ring-indigo-500 focus:border-indigo-500 block w-full sm:text-sm border-gray-300 rounded-md" />
            </div>
          </div>
        </div>
      </div>

      <div class="pt-8">
        <div>
          <h3 class="text-lg leading-6 font-medium text-gray-900">Notifications</h3>
          <p class="mt-1 text-sm text-gray-500">Pick the notifications you want to receive.</p>
        </div>
        <div class="mt-6">
          <fieldset>
            <legend class="sr-only">Printer Alerts</legend>
            <div class="text-base font-medium text-gray-900" aria-hidden="true">Printer Alerts</div>
            <div class="mt-4 space-y-4">
              <div class="relative flex items-start" v-for="option in alertStore.alertSettingsFieldset.event_types.child.choices">
                <div class="flex items-center h-5">
                  <input id="comments" :checked="isOptionChecked(option.value, 'event_types')" value="{{ option.value}}" name="{{option.value}}" type="checkbox" class="focus:ring-indigo-500 h-4 w-4 text-indigo-600 border-gray-300 rounded" />
                </div>
                <div class="ml-3 text-sm">
                  <label for="{{option.value}}" class="font-medium text-gray-700">{{ option.display_name }}</label>
                </div>
              </div>
            </div>
            
          <div class="mt-6 grid grid-cols-1 gap-y-6 gap-x-4 sm:grid-cols-6">
            <div class="sm:col-span-3">
              <label for="print-progress" class="block text-sm font-medium text-gray-700">Print progress notification interval</label>
              <div class="mt-1">
                <input type="number" :value="alertStore.settings.print_progress_percent" name="print-progress"
                  class="shadow-sm focus:ring-indigo-500 focus:border-indigo-500 block w-full sm:text-sm border-gray-300 rounded-md" 
                />
                <small>Example: 25 will notify you at 25%, 50%, 75%, and 100% progress</small>

              </div>
            </div>
        </div>
          </fieldset>
        </div>
      </div>
    </div>

    <div class="pt-5">
      <div class="flex justify-end">
        <button type="button" class="bg-white py-2 px-4 border border-gray-300 rounded-md shadow-sm text-sm font-medium text-gray-700 hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">Cancel</button>
        <button type="submit" class="ml-3 inline-flex justify-center py-2 px-4 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">Save</button>
      </div>
    </div>
  </form>
  <!-- end alert settings form -->
</template>
