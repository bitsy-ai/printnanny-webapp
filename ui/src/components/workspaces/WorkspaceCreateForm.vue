<template>
  <Form
    :validation-schema="schema"
    :initial-values="initialValues"
    @submit="onSubmit"
  >
    <div
      class="space-y-12 p-6 grid grid-cols-1 gap-x-8 gap-y-10 border-b border-gray-900/10 pb-12 md:grid-cols-3"
    >
      <div>
        <h2 class="text-base font-semibold leading-7 text-gray-900"></h2>
        <p class="mt-1 text-sm leading-6 text-gray-600">
          This information will be displayed when you invite a team member to
          your workspace.
        </p>
      </div>

      <div
        class="grid max-w-2xl grid-cols-1 gap-x-6 gap-y-8 sm:grid-cols-6 md:col-span-2"
      >
        <div class="md:col-span-4">
          <div class="sm:col-span-3">
            <label
              for="name"
              class="block text-sm font-medium leading-6 text-gray-900"
              >Workspace Name</label
            >
            <div class="mt-2">
              <Field
                id="name"
                type="text"
                name="name"
                class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
              />
              <error-message
                class-name="text-red-500"
                name="name"
              ></error-message>
            </div>
          </div>

          <div class="col-span-full">
            <label
              for="invites"
              class="block text-sm font-medium leading-6 text-gray-900"
              >Invite Team Members</label
            >
            <div class="mt-2">
              <Field v-slot="{ field, errors }" name="invites">
                <textarea
                  id="invites"
                  v-bind="field"
                  name="invites"
                  rows="3"
                  class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
                />
              </Field>
            </div>
            <p class="mt-3 text-sm leading-6 text-gray-600">
              Email addresses of team members you'd like to invite, one per
              line.
            </p>
          </div>
        </div>

        <div class="col-span-2 flex items-center justify-end">
          <TextSpinner
            v-if="loading"
            height="h-6"
            width="w-6"
            text="Saving..."
          ></TextSpinner>
          <button
            type="submit"
            :disabled="loading"
            class="ml-3 rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-sm disabled:opacity-25 hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
          >
            Save
          </button>
        </div>
      </div>
    </div>
  </Form>
</template>
<script setup lang="ts">
import { ref } from "vue";
import * as yup from "yup";
import { useRouter } from "vue-router";
import { Field, ErrorMessage, Form } from "vee-validate";
import { useAccountStore } from "@/stores/account";
import TextSpinner from "../util/TextSpinner.vue";
import { useWorkspaceStore } from "@/stores/workspaces";
import { success } from "@/stores/alerts";

const router = useRouter();

const loading = ref(false);
const account = useAccountStore();
const store = useWorkspaceStore();
function defaultWorkspaceName(email: undefined | string) {
  if (email === undefined) {
    return "My Shared Workspace"; // we should never return this, but...
  }
  // split on the @ sign in email
  const split = email.split("@");
  const domain = split[split.length - 1];

  switch (domain) {
    case "gmail.com":
    case "yahoo.com":
    case "outlook.com":
    case "hotmail.com":
    case "icloud.com":
      return `${split[0]}'s workspace'`;
    default:
      return domain;
  }
}

const initialValues = { name: defaultWorkspaceName(account.user?.email) };

const schema = yup.object({
  name: yup
    .string()
    .required("Workspace name is required")
    .default(defaultWorkspaceName(account.user?.email)),
  invites: yup.string(),
});

async function onSubmit(values: any) {
  loading.value = true;
  const name = values.name;
  const invites = values.invites.trim().split("\n");

  const workspace = await store.createWorkspace(name);

  if (workspace) {
    for (const email of invites) {
      await store.inviteToWorkspace(email, workspace.id);
    }
  }

  loading.value = false;
  router.push({ name: "workspaceList" });
}
</script>
