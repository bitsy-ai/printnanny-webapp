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
        meta: {
          title: "PrintNanny: Stop Babysitting Your 3D Printer",
          requiresAuth: false,
        },
      },
      {
        path: "register",
        name: "register",
        components: {
          default: () => import("@/views/RegisterAccountView.vue"),
        },
        meta: { title: "Create Account", requiresAuth: false },
      },
      {
        path: "pricing",
        name: "pricing",
        components: {
          default: () => import("@/components/shop/PriceTable.vue"),
        },
        meta: { title: "PrintNanny: Plans & Pricing", requiresAuth: false },
      },
      {
        path: "pricing/enterprise",
        name: "pricing-enterprise",
        components: {
          default: () => import("@/components/shop/PriceTableEnterprise.vue"),
        },
        meta: {
          title: "PrintNanny: Enterprise, Education, OEM Plans",
          requiresAuth: false,
        },
      },
      {
        path: "account-verify-email",
        name: "account-verify-email",
        components: {
          default: () => import("@/components/forms/EmailVerificationForm.vue"),
        },
        meta: { requiresAuth: false },
      },
      {
        path: "account-confirm-email/:verificationKey",
        name: "account-confirm-email",
        props: { default: true },
        components: {
          default: () => import("@/views/EmailConfirmationView.vue"),
        },
        meta: { requiresAuth: false },
      },
      {
        path: "login",
        name: "login",
        components: {
          default: () => import("@/components/forms/MagicLinkLoginForm.vue"),
        },
        meta: { requiresAuth: false },
      },
      {
        path: "login/confirm/:email/:token?",
        name: "login-confirm",
        props: { default: true },
        meta: { requiresAuth: false },
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
        meta: { requiresAuth: false },
      },
      {
        path: "password-reset/confirm/:userId/:token",
        name: "reset-password-confirm",
        props: { default: true },
        components: {
          default: () =>
            import("@/components/forms/PasswordResetConfirmForm.vue"),
        },
        meta: { requiresAuth: false },
      },
      {
        path: "demo",
        name: "demo-submit",
        components: {
          default: () => import("@/components/demo/DemoForm.vue"),
        },
        meta: { title: "PrintNanny: Try Risk-free", requiresAuth: false },
      },
      {
        path: "demo/:demoId",
        name: "demo-result",
        props: { default: true },
        components: {
          default: () => import("@/components/demo/DemoResult.vue"),
        },
        meta: { title: "PrintNanny: Your Results", requiresAuth: false },
      },
      {
        path: "workspaces/register/:token/:email",
        name: "workspace-register",
        components: {
          default: () =>
            import("@/components/workspaces/WorkspaceRegistrationForm.vue"),
        },
        props: { default: true },
        meta: { title: "Create your account", requiresAuth: false },
      },
    ],
  },
  {
    path: "/privacy/",
    name: "privacy",
    component: () => import("@/views/PrivacyView.vue"),
    meta: { title: "Privacy Policy", requiresAuth: false },
  },
  {
    path: "/terms/",
    name: "terms",
    component: () => import("@/views/TermsOfServiceView.vue"),
    meta: { title: "Terms of Service", requiresAuth: false },
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
    meta: { title: "Logout", requiresAuth: true },
  },
] as Array<RouteRecordRaw>;
