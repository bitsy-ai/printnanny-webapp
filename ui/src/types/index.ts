/**
 * Alert or error message produced by front-end ui code
 */
// import type * as apiTypes from "printnanny-api-client";
import type { FunctionalComponent, HTMLAttributes, VNodeProps } from "vue";

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
