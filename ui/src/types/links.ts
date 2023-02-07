import type { RouteLocationRaw } from "vue-router";
import type { FunctionalComponent, HTMLAttributes, VNodeProps } from "vue";

export type SimpleFlyoutMenuLink = {
  name: string;
  description: string;
  blank?: boolean;
  href?: string;
  routerLink?: RouteLocationRaw;
};

export type FullWidthFlyoutMenuLink = {
  id: string;
  name: string;
  description: string;
  cta: string;
  blank?: boolean;
  href?: string;
  routerLink?: RouteLocationRaw;
  icon: FunctionalComponent<HTMLAttributes & VNodeProps>;
};

export type FullWidthFlyoutMenuFooterLink = {
  name: string;
  href: string;
  icon: FunctionalComponent<HTMLAttributes & VNodeProps>;
};

export type TableActionLink = {
  name: string;
  click?: () => void;
  href?: string;
  routerLink?: RouteLocationRaw;
  slot?: FunctionalComponent<HTMLAttributes & VNodeProps>;
  icon: FunctionalComponent<HTMLAttributes & VNodeProps>;
};
