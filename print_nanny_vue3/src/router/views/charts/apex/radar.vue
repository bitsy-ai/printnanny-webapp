<script>
import appConfig from '@src/app.config'
import Layout from '@layouts/main'
import PageHeader from '@components/page-header'

/**
 * Radar Charts component
 */
export default {
  page: {
    title: 'Radar Charts',
    meta: [{ name: 'description', content: appConfig.description }],
  },
  components: { Layout, PageHeader },
  data() {
    return {
      title: 'Radar Charts',
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
          text: 'Radar Charts',
          active: true,
        },
      ],
      polygonRadarChart: {
        series: [
          {
            name: 'Series 1',
            data: [20, 100, 40, 30, 50, 80, 33],
          },
        ],
        chartOptions: {
          colors: ['#FF4560'],
          labels: [
            'Sunday',
            'Monday',
            'Tuesday',
            'Wednesday',
            'Thursday',
            'Friday',
            'Saturday',
          ],
          plotOptions: {
            radar: {
              size: 140,
            },
          },
          markers: {
            size: 4,
            colors: ['#fff'],
            strokeColor: ['#FF4560'],
            strokeWidth: 2,
          },
          tooltip: {
            y: {
              formatter: function(val) {
                return val
              },
            },
          },
          yaxis: {
            tickAmount: 7,
            labels: {
              formatter: function(val, i) {
                if (i % 2 === 0) {
                  return val
                } else {
                  return ''
                }
              },
            },
          },
        },
      },
      multipleSeriesChart: {
        series: [
          {
            name: 'Series 1',
            data: [80, 50, 30, 40, 100, 20],
          },
          {
            name: 'Series 2',
            data: [20, 30, 40, 80, 20, 80],
          },
          {
            name: 'Series 3',
            data: [44, 76, 78, 13, 43, 10],
          },
        ],
        chartOptions: {
          chart: {
            dropShadow: {
              enabled: true,
              blur: 1,
              left: 1,
              top: 1,
            },
          },
          colors: ['#727cf5', '#02a8b5', '#fd7e14'],
          stroke: {
            width: 0,
          },
          fill: {
            opacity: 0.4,
          },
          markers: {
            size: 0,
          },
          labels: ['2011', '2012', '2013', '2014', '2015', '2016'],
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
            <h4 class="header-title mb-3">Radar with Polygon-fill</h4>
            <!-- Radar with Polygon-fill -->
            <apexchart
              height="380"
              type="radar"
              class="apex-charts"
              :series="polygonRadarChart.series"
              :options="polygonRadarChart.chartOptions"
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
            <h4 class="header-title mb-3">Radar – Multiple Series</h4>
            <!-- Radar – Multiple Series -->
            <apexchart
              type="radar"
              height="350"
              :options="multipleSeriesChart.chartOptions"
              :series="multipleSeriesChart.series"
            />
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