import HomeView from "@/views/HomeView.vue";
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
    redirect: { name: "home" },
    beforeEnter: async (_to, _from) => {
      const account = useAccountStore();
      await account.logout();
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
]