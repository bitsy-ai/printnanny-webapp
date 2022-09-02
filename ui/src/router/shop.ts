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
        meta: { title: "Shop" },
      },
      {
        path: "founding-membership",
        name: "shop-founding-membership",
        components: {
          default: FoundingMembershipPage,
        },
        meta: { title: "50% off launch price" },
      },
      {
        path: "sdwire",
        name: "shop-sdwire",
        components: {
          default: SDWirePage,
        },
        meta: { title: "Pre-order SDWire" },
      },
      {
        path: "sdwire/success/:sessionId",
        name: "sdwire-checkout-success",
        components: {
          default: CheckoutSuccessPage,
        },
        props: { default: true },
        meta: { title: "Pre-order accepted" },
      },
    ],
  },
];
