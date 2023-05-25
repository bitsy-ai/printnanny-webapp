<template>
  <transition
    enter-active-class="transform ease-out duration-300 transition"
    enter-from-class="translate-y-2 opacity-0 sm:translate-y-0 sm:translate-x-2"
    enter-to-class="translate-y-0 opacity-100 sm:translate-x-0"
    leave-active-class="transition ease-in duration-100"
    leave-from-class="opacity-100"
    leave-to-class="opacity-0"
  >
    <div
      v-if="store.workspaces.length > 0"
      class="space-y-6 mt-2 mx-2 md:mt-6 md:mx-6"
    >
      <!-- workspaces table -->
      <div
        v-for="workspace in store.workspaces"
        :key="workspace.id"
        class="p-4 sm:p-6 lg:p-8 bg-gray-50 rounded-md"
      >
        <div class="sm:flex sm:items-center">
          <div class="sm:flex-auto">
            <h1 class="font-semibold text-2xl text-gray-900">
              {{ workspace.name }}
            </h1>
          </div>
          <div class="mt-4 sm:ml-16 sm:mt-0 sm:flex-none">
            <router-link
              :to="{
                name: 'workspaceInvite',
                params: { slug: workspace.slug },
              }"
            >
              <button
                type="button"
                class="block rounded-md bg-indigo-600 px-3 py-2 text-center text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
              >
                Invite Team Member
              </button>
            </router-link>
          </div>
        </div>
        <div class="mt-8 flow-root">
          <h2 class="font-semibold text-md text-gray-900">Workspace Members</h2>
          <p class="mt-2 text-sm text-gray-700">
            Invite a team member to give them access to
            <strong>{{ workspace.name }}</strong> workspace.
          </p>
          <div class="-mx-4 -my-2 overflow-x-auto sm:-mx-6 lg:-mx-8">
            <div
              class="inline-block min-w-full py-2 align-middle sm:px-6 lg:px-8"
            >
              <table class="min-w-full divide-y divide-gray-300">
                <thead>
                  <tr>
                    <th
                      scope="col"
                      class="px-3 py-3.5 text-left text-sm font-semibold text-gray-900"
                    >
                      Email
                    </th>
                    <th
                      scope="col"
                      class="px-3 py-3.5 text-left text-sm font-semibold text-gray-900"
                    >
                      Info
                    </th>
                    <th scope="col" class="relative py-3.5 pl-3 pr-4 sm:pr-0">
                      <span class="sr-only">Remove</span>
                    </th>
                  </tr>
                </thead>
                <tbody class="divide-y divide-gray-200">
                  <tr v-for="person in workspace.users" :key="person.email">
                    <td
                      class="whitespace-nowrap px-3 py-4 text-sm text-gray-500"
                    >
                      {{ person.email }}
                    </td>
                    <td
                      class="whitespace-nowrap px-3 py-4 text-sm text-gray-500"
                    >
                      <span
                        v-if="isOwner(person, workspace)"
                        class="inline-flex items-center rounded-md bg-green-50 px-2 py-1 text-xs font-medium text-green-700 ring-1 ring-inset ring-green-600/20"
                        >Owner</span
                      >
                    </td>
                    <td
                      class="relative whitespace-nowrap py-4 pl-3 pr-4 text-right text-sm font-medium sm:pr-0"
                    >
                      <a
                        v-if="!isOwner(person, workspace)"
                        href="#"
                        class="text-indigo-600 hover:text-indigo-900"
                        >Remove<span class="sr-only"
                          >, {{ person.email }}</span
                        ></a
                      >
                    </td>
                  </tr>
                  <tr
                    v-for="person in workspace.pending_invites"
                    :key="person.invitee_identifier"
                  >
                    <td
                      class="whitespace-nowrap px-3 py-4 text-sm text-gray-500"
                    >
                      {{ person.invitee_identifier }}
                    </td>
                    <td
                      class="whitespace-nowrap px-3 py-4 text-sm text-gray-500"
                    >
                      <span
                        class="inline-flex items-center rounded-md bg-amber-50 px-2 py-1 text-xs font-medium text-amber-700 ring-1 ring-inset ring-amber-600/20"
                        >Pending</span
                      >
                    </td>
                    <td
                      class="relative whitespace-nowrap py-4 pl-3 pr-4 text-right text-sm font-medium sm:pr-0"
                    >
                      <a
                        class="text-indigo-600 hover:text-indigo-900"
                        @click="store.resendInvite(person.id)"
                        >Resend<span class="sr-only"></span
                      ></a>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div v-else class="w-full space-y-4">
      <table-empty
        :icon="UserPlusIcon"
        header="No shared workspaces found"
        body="Create a shared workspace to get started"
      >
        <router-link :to="{ name: 'workspaceCreate' }">
          <button
            type="button"
            class="inline-flex items-center px-4 py-2 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
          >
            <UserPlusIcon class="-ml-1 mr-2 h-5 w-5" aria-hidden="true" />
            Create Shared Workspace
          </button>
        </router-link>
      </table-empty>
    </div>
  </transition>
</template>
<script setup lang="ts">
import { RouterLink } from "vue-router";
import { useWorkspaceStore } from "@/stores/workspaces";
import TableEmpty from "@/components/devices/TableEmpty.vue";
import type * as api from "printnanny-api-client";
import { UserPlusIcon, PlusIcon } from "@heroicons/vue/24/solid";

const formUrl = import.meta.env.VITE_WORKSPACE_ALPHA_FORM;

const store = useWorkspaceStore();
await store.fetchWorkspaces();

function isOwner(user: api.User, workspace: api.Workspace) {
  return workspace.owner.organization_user.user.id === user.id;
}
</script>
