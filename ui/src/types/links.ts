import type { RouteLocationRaw } from "vue-router";

export type FlyoutMenuLink = {
  name: string;
  description: string;
  blank?: boolean;
  href?: string;
  routerLocation?: RouteLocationRaw;
};
