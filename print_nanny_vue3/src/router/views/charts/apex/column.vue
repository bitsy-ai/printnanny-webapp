<script>
import appConfig from '@src/app.config'
import Layout from '@layouts/main'
import PageHeader from '@components/page-header'

/**
 * Column Charts component
 */
export default {
  page: {
    title: 'Column Charts',
    meta: [{ name: 'description', content: appConfig.description }],
  },
  components: { Layout, PageHeader },
  data() {
    return {
      title: 'Column Charts',
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
          text: 'Column Charts',
          active: true,
        },
      ],
      basicColumnChart: {
        series: [
          {
            name: 'Net Profit',
            data: [44, 55, 57, 56, 61, 58, 63, 60, 66],
          },
          {
            name: 'Revenue',
            data: [76, 85, 101, 98, 87, 105, 91, 114, 94],
          },
          {
            name: 'Free Cash Flow',
            data: [35, 41, 36, 26, 45, 48, 52, 53, 41],
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
              horizontal: false,
              columnWidth: '55%',
              endingShape: 'rounded',
            },
          },
          dataLabels: {
            enabled: false,
          },
          stroke: {
            show: true,
            width: 2,
            colors: ['transparent'],
          },
          colors: ['#727cf5', '#0acf97', '#fa5c7c'],
          xaxis: {
            categories: [
              'Feb',
              'Mar',
              'Apr',
              'May',
              'Jun',
              'Jul',
              'Aug',
              'Sep',
              'Oct',
            ],
          },
          yaxis: {
            title: {
              text: '$ (thousands)',
            },
          },
          fill: {
            opacity: 1,
          },
          tooltip: {
            y: {
              formatter: function(val) {
                return '$ ' + val + ' thousands'
              },
            },
          },
        },
      },
      nagativeValuesChart: {
        series: [
          {
            name: 'Cash Flow',
            data: [
              1.45,
              5.42,
              5.9,
              -0.42,
              -12.6,
              -18.1,
              -18.2,
              -14.16,
              -11.1,
              -6.09,
              0.34,
              3.88,
              13.07,
              5.8,
              2,
              7.37,
              8.1,
              13.57,
              15.75,
              17.1,
              19.8,
              -27.03,
              -54.4,
              -47.2,
              -43.3,
              -18.6,
              -48.6,
              -41.1,
              -39.6,
              -37.6,
              -29.4,
              -21.4,
              -2.4,
            ],
          },
        ],
        chartOptions: {
          chart: {
            toolbar: {
              show: false,
            },
          },
          yaxis: {
            title: {
              text: 'Growth',
            },
            labels: {
              formatter: function(y) {
                return y.toFixed(0) + '%'
              },
            },
          },
          xaxis: {
            // TODO: uncomment below and fix the error
            // type: 'datetime',
            categories: [
              '2011-01-01',
              '2011-02-01',
              '2011-03-01',
              '2011-04-01',
              '2011-05-01',
              '2011-06-01',
              '2011-07-01',
              '2011-08-01',
              '2011-09-01',
              '2011-10-01',
              '2011-11-01',
              '2011-12-01',
              '2012-01-01',
              '2012-02-01',
              '2012-03-01',
              '2012-04-01',
              '2012-05-01',
              '2012-06-01',
              '2012-07-01',
              '2012-08-01',
              '2012-09-01',
              '2012-10-01',
              '2012-11-01',
              '2012-12-01',
              '2013-01-01',
              '2013-02-01',
              '2013-03-01',
              '2013-04-01',
              '2013-05-01',
              '2013-06-01',
              '2013-07-01',
              '2013-08-01',
              '2013-09-01',
            ],
            labels: {
              rotate: -90,
            },
          },
          grid: {
            row: {
              colors: ['transparent', 'transparent'], // takes an array which will be repeated on columns
              opacity: 0.2,
            },
            borderColor: '#f1f3fa',
          },
          colors: ['#727cf5'],
          plotOptions: {
            bar: {
              colors: {
                ranges: [
                  {
                    from: -100,
                    to: -46,
                    color: '#fa5c7c',
                  },
                  {
                    from: -45,
                    to: 0,
                    color: '#ffbc00',
                  },
                ],
              },
              columnWidth: '80%',
            },
          },
          dataLabels: {
            enabled: false,
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
            <h4 class="header-title">Basic Column Chart</h4>
            <!-- Basic column chart -->
            <apexchart
              height="380"
              type="bar"
              class="apex-charts"
              :series="basicColumnChart.series"
              :options="basicColumnChart.chartOptions"
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
            <h4 class="header-title mb-3">Column Chart with Datalabels</h4>
            <!-- column with datalabels chart -->
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