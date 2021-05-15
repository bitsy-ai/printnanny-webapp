<script>
import appConfig from '@src/app.config'
import Layout from '@layouts/main'
import PageHeader from '@components/page-header'

import Stats from './stats'
import Campaign from './campaign'
import Revenue from './revenue'
import Performing from './performing'
import Leads from './leads'
import Todo from './todo'

/**
 * Dashboard-CRM Component
 */
export default {
  page: {
    title: 'CRM',
    meta: [{ name: 'description', content: appConfig.description }],
  },
  components: {
    Layout,
    PageHeader,
    Stats,
    Campaign,
    Revenue,
    Performing,
    Leads,
    Todo,
  },
  data() {
    return {
      title: 'CRM',
      items: [
        {
          text: 'Hyper',
          href: '/',
        },
        {
          text: 'Dashboard',
          href: '/',
        },
        {
          text: 'CRM',
          active: true,
        },
      ],
    }
  },
}
</script>

<template>
  <Layout>
    <PageHeader
      :title="title"
      :items="items"
    />
    <div>
      <Stats />
    </div>
    <div class="row">
      <div class="col-lg-5">
        <Campaign />
      </div>
      <!-- end col -->
      <div class="col-lg-7">
        <Revenue />
      </div>
      <!-- end col -->
    </div>
    <!-- end row -->

    <div class="row">
      <div class="col-xl-4 col-lg-12">
        <Performing />
      </div>
      <!-- end col -->
      <div class="col-xl-4 col-lg-6">
        <Leads />
      </div>
      <!-- end col -->

      <div class="col-xl-4 col-lg-6">
        <div class="card cta-box bg-primary text-white">
          <div class="card-body">
            <div class="media align-items-center">
              <div class="media-body">
                <h2 class="mt-0">
                  <i class="mdi mdi-bullhorn-outline"></i>&nbsp;
                </h2>
                <h3 class="m-0 font-weight-normal cta-box-title">
                  Enhance your
                  <b>Campaign</b> for better outreach
                  <i class="mdi mdi-arrow-right"></i>
                </h3>
              </div>
              <img
                class="ml-3"
                src="@assets/images/email-campaign.svg"
                width="120"
                alt="Generic placeholder image"
              />
            </div>
          </div>
          <!-- end card-body -->
        </div>
        <!-- end card-->

        <!-- Todo-->
        <Todo />
        <!-- end -->
      </div>
      <!-- end col -->
    </div>
    <!-- end row -->
  </Layout>
</template>
