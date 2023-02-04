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
        path: "register",
        name: "register",
        components: {
          default: () => import("@/views/RegisterAccountView.vue"),
        },
      },
      {
        path: "pricing",
        name: "pricing",
        components: {
          default: () => import("@/components/shop/PriceTable.vue"),
        },
      },
      {
        path: "account-verify-email",
        name: "account-verify-email",
        components: {
          default: () => import("@/components/forms/EmailVerificationForm.vue"),
        },
      },
      {
        path: "account-confirm-email/:verificationKey",
        name: "account-confirm-email",
        props: { default: true },
        components: {
          default: () => import("@/views/EmailConfirmationView.vue"),
        },
      },
      {
        path: "login",
        name: "login",
        components: {
          default: () => import("@/components/forms/MagicLinkLoginForm.vue"),
        },
      },
      {
        path: "login/confirm/:email/:token?",
        name: "login-confirm",
        props: { default: true },
        components: {
          default: () => import("@/components/forms/MagicLinkConfirmForm.vue"),
        },
      },
      {
        path: "password-reset",
        name: "reset-password",
        components: {
          default: () => import("@/components/forms/PasswordResetForm.vue"),
        },
      },
      {
        path: "password-reset/confirm/:userId/:token",
        name: "reset-password-confirm",
        props: { default: true },
        components: {
          default: () =>
            import("@/components/forms/PasswordResetConfirmForm.vue"),
        },
      },
    ],
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
