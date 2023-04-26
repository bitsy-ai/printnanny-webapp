import LandingLayout from "@/layouts/LandingLayout.vue";
import FoundingMembershipPage from "@/components/pages/FoundingMembershipPage.vue";
import SDWirePage from "@/components/pages/SDWirePage.vue";
import CheckoutSuccessPage from "@/components/pages/CheckoutSuccessPage.vue";
import ShopProductsListPage from "@/components/pages/ShopProductsListPage.vue";
export default [
  {
    path: "/shop/",
    components: {
      default: LandingLayout,
    },
    children: [
      {
        path: "",
        name: "shop-products-list",
        components: {
          default: ShopProductsListPage,
        },
        meta: { title: "PrintNanny: Shop" },
      },
      {
        path: "checkout/:sku/:price",
        name: "checkout-v2",
        components: {
          default: () =>
            import("@/components/shop/PriceTableCheckoutSession.vue"),
        },
        meta: { title: "PrintNanny: Checkout" },
        props: { default: true },
      },
      {
        path: "sdwire",
        name: "shop-sdwire",
        components: {
          default: () => import("@/components/pages/SDWirePage.vue"),
        },
        meta: {
          title:
            "PrintNanny SDWire: 10x faster gcode transfer to SD cards. Compatible with OctoPrint-SDWire plugin.",
        },
      },
      {
        path: "raspberry-pi-4-kit",
        name: "shop-rpi4kit",
        components: {
          default: () => import("@/components/pages/Rpi4KitPage.vue"),
        },
        meta: {
          title:
            "PrintNanny Raspberry Pi 4 kit: everything you need to get started.",
        },
      },
      {
        path: "thank-you/:sessionId",
        name: "shop-checkout-success",
        components: {
          default: CheckoutSuccessPage,
        },
        props: { default: true },
        meta: { title: "PrintNanny: Thank you!" },
      },
    ],
  },
];
