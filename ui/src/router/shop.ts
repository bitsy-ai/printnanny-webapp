import LandingLayout from "@/layouts/LandingLayout.vue";
import FoundingMembershipPage from "@/components/pages/FoundingMembershipPage.vue";

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
        ],
    },
]