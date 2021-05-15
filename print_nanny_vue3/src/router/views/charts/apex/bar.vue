<script>
import appConfig from '@src/app.config'
import Layout from '@layouts/main'
import PageHeader from '@components/page-header'

/**
 * Bar Charts component
 */
export default {
  page: {
    title: 'Bar Charts',
    meta: [{ name: 'description', content: appConfig.description }],
  },
  components: { Layout, PageHeader },
  data() {
    return {
      title: 'Bar Charts',
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
          text: 'Bar Charts',
          active: true,
        },
      ],
      basicBarChart: {
        series: [
          {
            data: [400, 430, 448, 470, 540, 580, 690, 1100, 1200, 1380],
          },
        ],
        chartOptions: {
          chart: {
            toolbar: {
              show: false,
            },
          },
          plotOptions: {
            bar: {
              horizontal: true,
            },
          },
          colors: ['#39afd1'],
          dataLabels: {
            enabled: false,
          },
          xaxis: {
            categories: [
              'South Korea',
              'Canada',
              'United Kingdom',
              'Netherlands',
              'Italy',
              'France',
              'Japan',
              'United States',
              'China',
              'Germany',
            ],
          },
          states: {
            hover: {
              filter: 'none',
            },
          },
          grid: {
            borderColor: '#f1f3fa',
          },
        },
      },
      nagativeValuesChart: {
        series: [
          {
            name: 'Males',
            data: [
              0.4,
              0.65,
              0.76,
              0.88,
              1.5,
              2.1,
              2.9,
              3.8,
              3.9,
              4.2,
              4,
              4.3,
              4.1,
              4.2,
              4.5,
              3.9,
              3.5,
              3,
            ],
          },
          {
            name: 'Females',
            data: [
              -0.8,
              -1.05,
              -1.06,
              -1.18,
              -1.4,
              -2.2,
              -2.85,
              -3.7,
              -3.96,
              -4.22,
              -4.3,
              -4.4,
              -4.1,
              -4,
              -4.1,
              -3.4,
              -3.1,
              -2.8,
            ],
          },
        ],
        chartOptions: {
          chart: {
            stacked: true,
          },
          colors: ['#fa5c7c', '#0acf97'],
          plotOptions: {
            bar: {
              horizontal: true,
              barHeight: '80%',
            },
          },
          dataLabels: {
            enabled: false,
          },
          stroke: {
            width: 1,
            colors: ['#fff'],
          },
          grid: {
            xaxis: {
              showLines: false,
            },
          },
          yaxis: {
            min: -5,
            max: 5,
            title: {
              // text: 'Age',
            },
          },
          tooltip: {
            shared: false,
            x: {
              formatter: function(val) {
                return val
              },
            },
            y: {
              formatter: function(val) {
                return Math.abs(val) + '%'
              },
            },
          },
          xaxis: {
            categories: [
              '85+',
              '80-84',
              '75-79',
              '70-74',
              '65-69',
              '60-64',
              '55-59',
              '50-54',
              '45-49',
              '40-44',
              '35-39',
              '30-34',
              '25-29',
              '20-24',
              '15-19',
              '10-14',
              '5-9',
              '0-4',
            ],
            title: {
              text: 'Percent',
            },
            labels: {
              formatter: function(val) {
                return Math.abs(Math.round(val)) + '%'
              },
            },
          },
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
            <h4 class="header-title">Basic Bar Chart</h4>
            <!-- Basic bar chart -->
            <apexchart
              height="380"
              type="bar"
              class="apex-charts"
              :series="basicBarChart.series"
              :options="basicBarChart.chartOptions"
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
            <h4 class="header-title">Bar with Negative Values</h4>
            <!-- Nagative value chart -->
            <apexchart
              height="380"
              type="bar"
              class="apex-charts"
              :series="nagativeValuesChart.series"
              :options="nagativeValuesChart.chartOptions"
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