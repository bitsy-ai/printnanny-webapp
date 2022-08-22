import HomeView from "@/views/HomeView.vue";
import type { RouteRecordRaw } from "vue-router";
import { useAccountStore } from "@/stores/account";

export default [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/login/",
    name: "login",
    component: () => import("@/views/LoginView.vue"),
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
  {
    path: "/about/",
    name: "about",
    // route level code-splitting
    // this generates a separate chunk (About.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import("@/views/AboutView.vue"),
  },
] as Array<RouteRecordRaw>;
