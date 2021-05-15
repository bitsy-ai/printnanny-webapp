<script>
import DatePicker from 'vue2-datepicker'

import appConfig from '@src/app.config'
import Layout from '@layouts/main'

import Overview from './overview'
import Views from './views'
import Browser from './browser'
import System from './system'
import Channel from './channel'
import Media from './media'
import EngagementOverview from './engagement-overview'

/**
 * Dashboard-Analytics Component
 */
export default {
  page: {
    title: 'Analytics',
    meta: [{ name: 'description', content: appConfig.description }],
  },
  components: {
    DatePicker,
    Layout,
    Overview,
    Views,
    Browser,
    System,
    Channel,
    Media,
    EngagementOverview,
  },
  data() {
    return {
      state: {
        date: new Date(),
      },
    }
  },
}
</script>

<template>
  <Layout>
    <!-- start page title -->
    <div class="row">
      <div class="col-12">
        <div class="page-title-box">
          <div class="page-title-right">
            <form class="form-inline">
              <div class="form-group">
                <div class="input-group">
                  <date-picker
                    id="dash-daterange"
                    v-model="state.date"
                    :first-day-of-week="1"
                    lang="en"
                    format="MM/DD/YYYY"
                  ></date-picker>
                </div>
              </div>
              <a href="javascript: void(0);" class="btn btn-primary ml-2">
                <i class="mdi mdi-autorenew"></i>
              </a>
            </form>
          </div>
          <h4 class="page-title">Analytics</h4>
        </div>
      </div>
    </div>
    <!-- end page title -->

    <div class="row">
      <div class="col-xl-3 col-lg-4">
        <div class="card tilebox-one">
          <div class="card-body">
            <i class="uil uil-users-alt float-right"></i>
            <h6 class="text-uppercase mt-0">Active Users</h6>
            <h2 id="active-users-count" class="my-2">121</h2>
            <p class="mb-0 text-muted">
              <span class="text-success mr-2">
                <span class="mdi mdi-arrow-up-bold"></span> 5.27%
              </span>
              <span class="text-nowrap">Since last month</span>
            </p>
          </div>
          <!-- end card-body-->
        </div>
        <!--end card-->

        <div class="card tilebox-one">
          <div class="card-body">
            <i class="uil uil-window-restore float-right"></i>
            <h6 class="text-uppercase mt-0">Views per minute</h6>
            <h2 id="active-views-count" class="my-2">560</h2>
            <p class="mb-0 text-muted">
              <span class="text-danger mr-2">
                <span class="mdi mdi-arrow-down-bold"></span> 1.08%
              </span>
              <span class="text-nowrap">Since previous week</span>
            </p>
          </div>
          <!-- end card-body-->
        </div>
        <!--end card-->

        <div class="card cta-box overflow-hidden">
          <div class="card-body">
            <div class="media align-items-center">
              <div class="media-body">
                <h3 class="m-0 font-weight-normal cta-box-title">
                  Enhance your
                  <b>Campaign</b> for better outreach
                  <i class="mdi mdi-arrow-right"></i>
                </h3>
              </div>
              <img
                class="ml-3"
                src="@assets/images/email-campaign.svg"
                width="92"
                alt="Generic placeholder image"
              />
            </div>
          </div>
          <!-- end card-body -->
        </div>
      </div>
      <!-- end col -->

      <div class="col-xl-9 col-lg-8">
        <Overview />
      </div>
    </div>

    <div class="row">
      <div class="col-xl-4 col-lg-12">
        <Views />
      </div>
      <div class="col-xl-4 col-lg-6">
        <Browser />
      </div>
      <div class="col-xl-4 col-lg-6">
        <System />
      </div>
    </div>

    <div class="row">
      <div class="col-xl-4 col-lg-6">
        <Channel />
      </div>
      <div class="col-xl-4 col-lg-6">
        <Media />
      </div>
      <div class="col-xl-4 col-lg-6">
        <EngagementOverview />
      </div>
    </div>
  </Layout>
</template>