import LandingLayout from "@/layouts/LandingLayout.vue";
import FoundingMembershipPage from "@/components/pages/FoundingMembershipPage.vue";
import SDWirePage from "@/components/pages/SDWirePage.vue";
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
                meta: { title: "25% off launch price" },
            },
            {
                path: "sdwire",
                name: "sdwire",
                components: {
                    default: SDWirePage,
                },
                meta: { title: "Pre-order PrintNanny SDwore" },
            },
        ],
    },
]