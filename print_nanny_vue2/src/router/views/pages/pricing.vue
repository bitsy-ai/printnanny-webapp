<script>
import appConfig from '@src/app.config'
import Layout from '@layouts/main'
import PageHeader from '@components/page-header'

/**
 * Pricing component
 */
export default {
  page: {
    title: 'Pricing',
    meta: [{ name: 'description', content: appConfig.description }],
  },
  components: { Layout, PageHeader },
  data() {
    return {
      title: 'Pricing',
      items: [
        {
          text: 'Hyper',
          href: '/',
        },
        {
          text: 'Pages',
          href: '/',
        },
        {
          text: 'Pricing',
          active: true,
        },
      ],
      pricingData: [
        {
          title: 'Professional Pack',
          icon: 'dripicons-user',
          price: '$19',
          storage: 10,
          bandwidth: '500 GB',
          domain: 'No',
          user: '1',
        },
        {
          title: 'Business Pack',
          icon: 'dripicons-briefcase',
          price: '$29',
          storage: 50,
          bandwidth: '900 GB',
          domain: '2',
          user: '10',
        },
        {
          title: 'Enterprise Pack',
          icon: 'dripicons-store',
          price: '$39',
          storage: 100,
          bandwidth: 'Unlimited',
          domain: '10',
          user: 'Unlimited',
        },
      ],
    }
  },
}
</script>

<template>
  <Layout>
    <PageHeader :title="title" :items="items" />
    <div class="row justify-content-center">
      <div class="col-xl-10">
        <!-- Pricing Title-->
        <div class="text-center">
          <h3 class="mb-2">Our Plans and Pricing</h3>
          <p
            class="text-muted w-50 m-auto"
          >We have plans and prices that fit your business perfectly. Make your client site a success with our products.</p>
        </div>

        <!-- Plans -->
        <div class="row mt-sm-5 mt-3 mb-3">
          <div v-for="pricing of pricingData" :key="pricing.title" class="col-md-4">
            <div
              class="card card-pricing"
              :class=" { 'card-pricing-recommended': pricing.title === 'Business Pack' }"
            >
              <div class="card-body text-center">
                <div
                  v-if="pricing.title === 'Business Pack'"
                  class="card-pricing-plan-tag"
                >Recommended</div>
                <p
                  class="card-pricing-plan-name font-weight-bold text-uppercase"
                >{{ pricing.title }}</p>
                <i :class="`card-pricing-icon ${pricing.icon} text-primary`"></i>
                <h2 class="card-pricing-price">
                  {{pricing.price}}
                  <span>/ Month</span>
                </h2>
                <ul class="card-pricing-features">
                  <li>{{pricing.storage}} GB Storage</li>
                  <li>{{pricing.bandwidth}} Bandwidth</li>
                  <li>{{pricing.domain}} Domain</li>
                  <li>{{pricing.user}} User</li>
                  <li>Email Support</li>
                  <li>24x7 Support</li>
                </ul>
                <button class="btn btn-primary mt-4 mb-2 btn-rounded">Choose Plan</button>
              </div>
            </div>
            <!-- end Pricing_card -->
          </div>
          <!-- end col -->
        </div>
        <!-- end row -->
      </div>
      <!-- end col-->
    </div>
    <!-- end row -->
  </Layout>
</template>