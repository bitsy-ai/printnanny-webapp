/**
 * Alert or error message produced by front-end ui code
 */
// import type * as apiTypes from "printnanny-api-client";
import type { FunctionalComponent, HTMLAttributes, VNodeProps } from "vue";
import type { AnyObjectSchema } from "yup";
import type { RouteLocationRaw } from "vue-router";

export interface AlertAction {
  color: string;
  text: string;
}

export interface UiAlert {
  message: string;
  header: string;
  icon?: FunctionalComponent<HTMLAttributes & VNodeProps>;
  actions: Array<AlertAction>;
  error: Error | undefined;
}

// TODO union of | apiTypes.Alert
// export type Alert = UiAlert | UiAlert;

export type WizardButton = {
  text: string;
  link: () => RouteLocationRaw;
};

export type WizardStep = {
  key: string;
  component: FunctionalComponent<HTMLAttributes & VNodeProps>,
  validationSchema: AnyObjectSchema;
  nextButton: WizardButton | undefined;
  prevButton: WizardButton | undefined;
  onSubmit: (formData: any) => void;
};
