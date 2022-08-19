
import type { FunctionalComponent, HTMLAttributes, VNodeProps } from "vue";


export interface AlertAction {
  color: string;
  text: string;
  onClick: Function;
}

export interface UiAlert {
  message: string;
  header: string;
  icon?: FunctionalComponent<HTMLAttributes & VNodeProps>;
  actions: Array<AlertAction>;
  error: Error | undefined;
}