<script>
import appConfig from '@src/app.config'
import Layout from '@layouts/main'
import PageHeader from '@components/page-header'

/**
 * Pie Charts component
 */
export default {
  page: {
    title: 'Pie Charts',
    meta: [{ name: 'description', content: appConfig.description }],
  },
  components: { Layout, PageHeader },
  data() {
    return {
      title: 'Pie Charts',
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
          text: 'Pie Charts',
          active: true,
        },
      ],
      pieChart: {
        series: [44, 55, 41, 17, 15],
        chartOptions: {
          labels: ['Series 1', 'Series 2', 'Series 3', 'Series 4', 'Series 5'],
          colors: ['#727cf5', '#6c757d', '#0acf97', '#fa5c7c', '#e3eaef'],
          legend: {
            show: true,
            position: 'bottom',
            horizontalAlign: 'center',
            verticalAlign: 'middle',
            floating: false,
            fontSize: '14px',
            offsetX: 0,
            offsetY: -10,
          },
          responsive: [
            {
              breakpoint: 600,
              options: {
                chart: {
                  height: 240,
                },
                legend: {
                  show: false,
                },
              },
            },
          ],
        },
      },
      donutChart: {
        series: [44, 55, 41, 17, 15],
        chartOptions: {
          legend: {
            show: true,
            position: 'bottom',
            horizontalAlign: 'center',
            verticalAlign: 'middle',
            floating: false,
            fontSize: '14px',
            offsetX: 0,
            offsetY: -10,
          },
          labels: ['Series 1', 'Series 2', 'Series 3', 'Series 4', 'Series 5'],
          colors: ['#39afd1', '#ffbc00', '#313a46', '#fa5c7c', '#0acf97'],
          responsive: [
            {
              breakpoint: 600,
              options: {
                chart: {
                  height: 240,
                },
                legend: {
                  show: false,
                },
              },
            },
          ],
        },
      },
    }
  },
}
</script>

<template>
  <Layout>
    <PageHeader :title="title" :items="items" />
    <div class="row">
      <div class="col-xl-6">
        <div class="card">
          <div class="card-body">
            <h4 class="header-title">Simple Pie Chart</h4>
            <!-- Simple Pie Chart -->
            <apexchart
              height="320"
              type="pie"
              class="apex-charts"
              :series="pieChart.series"
              :options="pieChart.chartOptions"
            ></apexchart>
          </div>
          <!-- end card body-->
        </div>
        <!-- end card -->
      </div>
      <!-- end col-->

      <div class="col-xl-6">
        <div class="card">
          <div class="card-body">
            <h4 class="header-title">Simple Donut Chart</h4>
            <!-- Simple Donut Chart -->
            <apexchart
              height="320"
              type="donut"
              class="apex-charts"
              :series="donutChart.series"
              :options="donutChart.chartOptions"
            ></apexchart>
          </div>
          <!-- end card body-->
        </div>
        <!-- end card -->
      </div>
      <!-- end col-->
    </div>
    <!-- end row-->
  </Layout>
</template>