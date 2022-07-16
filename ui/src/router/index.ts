import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import LoginView from "../views/LoginView.vue";
import DashboardView from "../views/DashboardView.vue";
import { useAccountStore } from "@/stores/account";
import { useDeviceStore } from "@/stores/devices";
import { useBillingStore } from "@/stores/billing";


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,
    },
    {
      path: "/devices",
      name: "devices",
      component: DashboardView,
      beforeEnter: async (to, from) => {
        const devices = useDeviceStore();
        await devices.fetch();
      }
    },
    {
      path: "/login",
      name: "login",
      // route level code-splitting
      // this generates a separate chunk (Login.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      // redirect: to => {
      //   const account = useAccountStore();
      //   if (account.isAuthenticated) {
      //     return { path: '/dashboard' }
      //   }
      // },
      component: LoginView,
    },
    // clear account store data and direct to home
    {
      path: "/logout",
      name: "logout",
      redirect: { name: "home" },
      beforeEnter: async (to, from) => {
        const account = useAccountStore();
        await account.logout();
      }
    },
    {
      path: "/about",
      name: "about",
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import("@/views/AboutView.vue"),
    },
    // begin device routes
    { path: "/device/connect", name: "device-connect", component: () => import("@/views/DeviceCreateView.vue") },
    // end device routes

    // begin profile/settings/billings routers
    { path: "/settings", name: "settings", component: () => import("@/views/SettingsView.vue") },
    {
      path: "/billing",
      name: "billing",
      component: () => import("@/views/BillingView.vue"),
      beforeEnter: async (to, from) => {
        const billing = useBillingStore();
        await billing.fetch();
      }
    },
    {
      path: "/billing/cancel",
      name: "billing-cancel",
      component: () => import("@/views/BillingCancelView.vue"),
      beforeEnter: async (to, from) => {
        const billing = useBillingStore();
        await billing.fetch();
      }
    },
  ],
});

router.beforeEach(async (to, from) => {
  const account = useAccountStore();
  await account.fetchUser();
  if (
    // make sure the user is authenticated
    !account.isAuthenticated &&
    // ❗️ Avoid an infinite redirect
    to.name !== 'login' &&
    // ❗️ Login is not required for home view
    to.name !== 'home'
  ) {
    // redirect the user to the login page
    return { name: 'login' }
  }
})

export default router;
