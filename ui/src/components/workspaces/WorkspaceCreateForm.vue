<template>
  <Form
    v-slot="{ meta }"
    :validation-schema="schema"
    :initial-values="initialValues"
    @submit="onSubmit"
  >
    <div
      class="space-y-6 p-6 grid grid-cols-1 gap-x-8 gap-y-10 border-b border-gray-900/10 pb-12 md:grid-cols-3"
    >
      <div>
        <h2 class="text-base font-semibold leading-7 text-gray-900">
          Workspace Information
        </h2>
        <p class="mt-1 text-sm leading-6 text-gray-600">
          This will be displayed when you invite a team member to your
          workspace.
        </p>
      </div>

      <div
        class="grid max-w-2xl grid-cols-1 gap-x-6 sm:grid-cols-6 md:col-span-2"
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
                class="text-red-500 text-sm"
                name="name"
              ></error-message>
            </div>
          </div>

          <div class="sm:col-span-3 mt-2">
            <label
              for="slug"
              class="block text-sm font-medium leading-6 text-gray-900"
              >Workspace URL</label
            >
            <div class="mt-2">
              <Field
                id="slug"
                type="text"
                name="slug"
                :rules="{ regex: /^[A-Za-z0-9\-\_]+$/ }"
                class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
              />
              <error-message
                class="text-red-500 text-sm"
                name="slug"
              ></error-message>
              <p class="my-3 text-xs text-gray-400">
                Your workspace will be available at:<br />
                https://printnanny.ai/workspace/<span class="text-indigo-500"
                  >your-url-here</span
                >.
              </p>
            </div>
          </div>

          <div class="col-span-full">
            <label
              for="invites"
              class="block text-sm font-medium leading-6 text-gray-900"
              >Invite Team Members</label
            >
            <div class="mt-2">
              <Field
                id="invites"
                as="textarea"
                name="invites"
                rows="3"
                class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
              >
              </Field>
            </div>
            <p class="mt-3 text-sm leading-6 text-gray-600">
              Email addresses of team members you'd like to invite, one per
              line.
            </p>
          </div>
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
          :disabled="loading || !meta.valid"
          class="ml-3 rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-sm disabled:opacity-25 hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
        >
          Save
        </button>
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
    return "My Workspace"; // we should never return this, but...
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

function defaultWorkspaceSlug(email: undefined | string) {
  const domain = defaultWorkspaceName(email);
  // replace all non letter/number characters
  return domain.replace(/[^a-zA-Z0-9/-]+/, "-");
}

function defaultWorkspaceDescription(email: undefined | string){
  if (email) { return `A shared workspace owned by ${email}`}
  return "A personal workspace that can be shared amongst team members"
}

const initialValues = {
  name: defaultWorkspaceName(account.user?.email),
  slug: defaultWorkspaceSlug(account.user?.email),
  description: defaultWorkspaceDescription(account.user?.email)
};

const schema = yup.object({
  description: yup.string().required("You must provide a description of your workspace."),
  name: yup
    .string()
    .required("You must name your workspace")
    .default(defaultWorkspaceName(account.user?.email)),
  slug: yup
    .string()
    .matches(
      /^[A-Za-z0-9\-_]+$/,
      "Should contain only letters, numbers, hypens, and underscores."
    )
    .required("Your must provide a url for your workspace"),
  invites: yup.string(),
});

async function onSubmit(values: any) {
  loading.value = true;
  const name = values.name;
  const slug = values.slug;
  const description = values.description

  const workspace = await store.createWorkspace(name, slug, description);

  if (workspace && values.invites) {
    const invites = values.invites.trim().split("\n");
    for (const email of invites) {
      await store.inviteToWorkspace(email, workspace);
    }
  }

  loading.value = false;
  if (workspace){
    router.push({ name: "workspaceList" });

  }
}
</script>
