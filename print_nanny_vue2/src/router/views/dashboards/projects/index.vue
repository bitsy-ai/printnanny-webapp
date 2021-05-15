<script>
import appConfig from '@src/app.config'
import Layout from '@layouts/main'
import PageHeader from '@components/page-header'

import Stats from './stats'
import donutChart from './donut-chart'
import Tasks from './tasks'
import barChart from './bar-chart'
import Activity from './activity'
import Calendar from './calendar'

/**
 * Dashboard-Projects Component
 */
export default {
  page: {
    title: 'Projects',
    meta: [{ name: 'description', content: appConfig.description }],
  },
  components: {
    Layout,
    PageHeader,
    Stats,
    donutChart,
    Tasks,
    barChart,
    Activity,
    Calendar,
  },
  data() {
    return {
      title: 'Projects',
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
          text: 'Projects',
          active: true,
        },
      ],
    }
  },
}
</script>

<template>
  <Layout>
    <PageHeader :title="title" :items="items" />
    <div class="row">
      <div class="col-12">
        <Stats />
      </div>
    </div>
    <div class="row">
      <div class="col-lg-4">
        <div class="card">
          <div class="card-body">
            <div class="dropdown float-right">
              <b-dropdown toggle-class="arrow-none card-drop p-0" variant="black" right>
                <template v-slot:button-content>
                  <i class="mdi mdi-dots-vertical"></i>
                </template>
                <a href="javascript:void(0);" class="dropdown-item">Weekly Report</a>
                <!-- item-->
                <a href="javascript:void(0);" class="dropdown-item">Monthly Report</a>
                <!-- item-->
                <a href="javascript:void(0);" class="dropdown-item">Action</a>
                <!-- item-->
                <a href="javascript:void(0);" class="dropdown-item">Settings</a>
              </b-dropdown>
            </div>
            <h4 class="header-title mb-4">Project Status</h4>

            <div class="my-4 chartjs-chart" style="height: 202px;">
              <donutChart :height="170" />
            </div>

            <div class="row text-center mt-2 py-2">
              <div class="col-4">
                <i class="mdi mdi-trending-up text-success mt-3 h3"></i>
                <h3 class="font-weight-normal">
                  <span>64%</span>
                </h3>
                <p class="text-muted mb-0">Completed</p>
              </div>
              <div class="col-4">
                <i class="mdi mdi-trending-down text-primary mt-3 h3"></i>
                <h3 class="font-weight-normal">
                  <span>26%</span>
                </h3>
                <p class="text-muted mb-0">In-progress</p>
              </div>
              <div class="col-4">
                <i class="mdi mdi-trending-down text-danger mt-3 h3"></i>
                <h3 class="font-weight-normal">
                  <span>10%</span>
                </h3>
                <p class="text-muted mb-0">Behind</p>
              </div>
            </div>
            <!-- end row-->
          </div>
          <!-- end card body-->
        </div>
      </div>
      <div class="col-lg-8">
        <Tasks />
      </div>
    </div>

    <div class="row">
      <div class="col-12">
        <div class="card">
          <div class="card-body">
            <div class="dropdown float-right">
              <b-dropdown toggle-class="arrow-none card-drop p-0" variant="black" right>
                <template v-slot:button-content>
                  <i class="mdi mdi-dots-vertical"></i>
                </template>
                <a href="javascript:void(0);" class="dropdown-item">Weekly Report</a>
                <!-- item-->
                <a href="javascript:void(0);" class="dropdown-item">Monthly Report</a>
                <!-- item-->
                <a href="javascript:void(0);" class="dropdown-item">Action</a>
                <!-- item-->
                <a href="javascript:void(0);" class="dropdown-item">Settings</a>
              </b-dropdown>
            </div>
            <h4 class="header-title mb-4">Tasks Overview</h4>

            <div class="mt-3 chartjs-chart" style="height: 320px;">
              <barChart :height="320" />
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="row">
      <div class="col-xl-6">
        <Activity />
      </div>
      <div class="col-xl-6">
        <Calendar />
      </div>
    </div>
  </Layout>
</template>