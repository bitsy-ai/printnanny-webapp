import LandingLayout from "@/layouts/LandingLayout.vue";
import FoundingMembershipPage from "@/components/pages/FoundingMembershipPage.vue";
import SDWirePage from "@/components/pages/SDWirePage.vue";
import SDWireSuccessPage from "@/components/pages/SDWireSuccessPage.vue";
import CheckoutPage from "@/components/pages/CheckoutPage.vue";

export default [
  {
    path: "/shop/",
    components: {
      default: LandingLayout,
    },
    children: [
      {
        path: "founding-membership",
        name: "founding-membership",
        components: {
          default: FoundingMembershipPage,
        },
        meta: { title: "50% off launch price" },
      },
      {
        path: "sdwire",
        name: "sdwire",
        components: {
          default: SDWirePage,
        },
        meta: { title: "Pre-order SDWire" },
      },
      {
        path: "sdwire/success/:sessionId",
        name: "sdwire-checkout-success",
        components: {
          default: SDWireSuccessPage,
        },
        props: { default: true },
        meta: { title: "Pre-order accepted" },
      },
      {
        path: "checkout",
        name: "checkout",
        components: {
          default: CheckoutPage,
        },
        meta: { title: "Checkout" },
      },
    ],
  },
];
