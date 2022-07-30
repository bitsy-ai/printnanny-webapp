<template>
  <div>
    <h1>Multi-step Form Wizard</h1>
    <p>
      This example uses a the composition API to create a multi-step form with
      next/previous controls and validation before moving to the next step.
      There are infinite ways you could implement this, this is just one of
      them. You could throw in a form generator to make this even easier.
    </p>

    <FormWizard :validation-schema="validationSchema" @submit="onSubmit">
      <FormStep>
        <Field name="fullName" type="text" placeholder="Type your Full name" />
        <ErrorMessage name="fullName" />

        <Field name="email" type="email" placeholder="Type your email" />
        <ErrorMessage name="email" />
      </FormStep>

      <FormStep>
        <Field
          name="password"
          type="password"
          placeholder="Type a strong one"
        />
        <ErrorMessage name="password" />

        <Field
          name="confirmPass"
          type="password"
          placeholder="Confirm your password"
        />
        <ErrorMessage name="confirmPass" />
      </FormStep>

      <FormStep>
        <Field name="favoriteDrink" as="select">
          <option>Select a drink</option>
          <option value="coffee">Coffee</option>
          <option value="tea">Tea</option>
          <option value="soda">Soda</option>
        </Field>
        <ErrorMessage name="favoriteDrink" />
      </FormStep>
    </FormWizard>
  </div>
</template>

<script setup lang="ts">
import { Field, ErrorMessage } from "vee-validate";
import * as yup from "yup";
import FormWizard from "@/components/forms/FormWizard.vue";
import FormStep from "@/components/forms/FormStep.vue";

// break down the validation steps into multiple schemas
const validationSchema = [
    yup.object({
    fullName: yup.string().required().label("Full Name"),
    email: yup.string().required().email().label("Email Address"),
    }),
    yup.object({
    password: yup.string().min(8).required(),
    confirmPass: yup
        .string()
        .required()
        .oneOf([yup.ref("password")], "Passwords must match"),
    }),
    yup.object({
    favoriteDrink: yup
        .string()
        .required()
        .oneOf(["coffee", "tea", "soda"], "Choose a drink"),
    }),
];

/**
 * Only Called when the last step is submitted
 */
function onSubmit(formData) {
    console.log(JSON.stringify(formData, null, 2));
}
</script>