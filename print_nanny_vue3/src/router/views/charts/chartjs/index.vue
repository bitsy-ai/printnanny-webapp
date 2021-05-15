<script>
import appConfig from '@src/app.config'
import Layout from '@layouts/main'
import PageHeader from '@components/page-header'

import lineChart from './line-chart'
import barChart from './bar-chart'
import donutChart from './donut-chart'
import radarChart from './radar-chart'

/**
 * Chartjs Charts component
 */
export default {
  page: {
    title: 'Chartjs Charts',
    meta: [{ name: 'description', content: appConfig.description }],
  },
  components: {
    Layout,
    PageHeader,
    lineChart,
    barChart,
    donutChart,
    radarChart,
  },
  data() {
    return {
      title: 'Chartjs',
      items: [
        {
          text: 'Hyper',
          href: '/',
        },
        {
          text: 'Apex',
          href: '/',
        },
        {
          text: 'Chartjs',
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
      <div class="col-lg-6">
        <div class="card">
          <div class="card-body">
            <h4 class="header-title mb-4">Line Chart</h4>
            <!-- Line Chart -->
            <lineChart :height="350" />
          </div>
        </div>
      </div>
      <div class="col-lg-6">
        <div class="card">
          <div class="card-body">
            <h4 class="header-title mb-4">Bar Chart</h4>
            <!-- Bar chart -->
            <barChart :height="350" />
          </div>
        </div>
      </div>
    </div>
    <div class="row">
      <div class="col-lg-6">
        <div class="card">
          <div class="card-body">
            <h4 class="header-title mb-4">Donut Chart</h4>
            <!-- Donut Chart -->
            <donutChart :height="170" />
          </div>
        </div>
      </div>
      <div class="col-lg-6">
        <div class="card">
          <div class="card-body">
            <h4 class="header-title mb-4">Radar Chart</h4>
            <!-- Radar Chart -->
            <radarChart :height="170" />
          </div>
        </div>
      </div>
    </div>
  </Layout>
</template>