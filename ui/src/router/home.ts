import type { RouteRecordRaw } from "vue-router";
import { useAccountStore } from "@/stores/account";
import LandingLayout from "@/layouts/LandingLayout.vue";
import HomePage from "@/components/pages/HomePage.vue";

export default [
  {
    path: "/",
    components: {
      default: LandingLayout,
    },
    children: [
      {
        path: "",
        name: "home",
        components: {
          default: HomePage,
        },
        meta: { title: "Stop Babysitting Your 3D Printer" },
      },
      {
        path: "/account-confirm-email/:verificationKey",
        name: "account-confirm-email",
        props: { default: true },
        components: {
          default: () => import("@/views/EmailConfirmationView.vue"),
        },
      },
    ],
  },
  {
    path: "/login/",
    name: "login",
    component: () => import("@/views/LoginView.vue"),
  },
  {
    path: "/password-reset/",
    name: "reset-password",
    component: () => import("@/views/PasswordResetView.vue"),
  },
  {
    path: "/password-reset/confirm/:userId/:token/",
    name: "reset-password-confirm",
    props: { default: true },
    components: {
      default: () => import("@/views/PasswordResetConfirmView.vue"),
    },
  },
  {
    path: "/privacy/",
    name: "privacy",
    component: () => import("@/views/PrivacyView.vue"),
  },
  {
    path: "/terms/",
    name: "terms",
    component: () => import("@/views/TermsOfServiceView.vue"),
  },
  // clear account store data and direct to home
  {
    path: "/logout/",
    name: "logout",
    beforeEnter: async (_to: any, _from: any, next) => {
      const account = useAccountStore();
      await account.logout();
      next("/");
    },
  },
] as Array<RouteRecordRaw>;
