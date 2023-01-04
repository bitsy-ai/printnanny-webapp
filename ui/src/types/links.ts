import type { RouteLocationRaw } from "vue-router";
import type { FunctionalComponent, HTMLAttributes, VNodeProps } from "vue";

export type FlyoutMenuLink = {
  name: string;
  description: string;
  blank?: boolean;
  href?: string;
  routerLink?: RouteLocationRaw;
};

export type TableActionLink = {
  name: string;
  icon?: FunctionalComponent<HTMLAttributes & VNodeProps>;
  click?: Function;
  href?: string;
  routerLink?: RouteLocationRaw;
  slot?: FunctionalComponent<HTMLAttributes & VNodeProps>;
};
