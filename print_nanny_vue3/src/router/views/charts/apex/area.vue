<script>
import appConfig from '@src/app.config'
import Layout from '@layouts/main'
import PageHeader from '@components/page-header'

/**
 * Chart series data
 */
var generateDayWiseTimeSeries = function(baseval, count, yrange) {
  var i = 0
  var series = []
  while (i < count) {
    var x = baseval
    var y =
      Math.floor(Math.random() * (yrange.max - yrange.min + 1)) + yrange.min

    series.push([x, y])
    baseval += 86400000
    i++
  }
  return series
}

/**
 * Area Charts component
 */
export default {
  page: {
    title: 'Area Charts',
    meta: [{ name: 'description', content: appConfig.description }],
  },
  components: { Layout, PageHeader },
  data() {
    return {
      title: 'Area Charts',
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
          text: 'Area Charts',
          active: true,
        },
      ],
      stackedAreaChart: {
        series: [
          {
            name: 'South',
            data: generateDayWiseTimeSeries(
              new Date('11 Feb 2017 GMT').getTime(),
              20,
              {
                min: 10,
                max: 60,
              }
            ),
          },
          {
            name: 'North',
            data: generateDayWiseTimeSeries(
              new Date('11 Feb 2017 GMT').getTime(),
              20,
              {
                min: 10,
                max: 20,
              }
            ),
          },
          {
            name: 'Central',
            data: generateDayWiseTimeSeries(
              new Date('11 Feb 2017 GMT').getTime(),
              20,
              {
                min: 10,
                max: 15,
              }
            ),
          },
        ],
        chartOptions: {
          chart: {
            stacked: true,
            events: {
              selection: function(chart, e) {
                console.log(new Date(e.xaxis.min))
              },
            },
          },
          dataLabels: {
            enabled: false,
          },
          colors: ['#727cf5', '#0acf97', '#e3eaef'],
          stroke: {
            width: 2,
            curve: 'smooth',
          },
          fill: {
            type: 'gradient',
            gradient: {
              opacityFrom: 0.6,
              opacityTo: 0.8,
            },
          },
          legend: {
            position: 'top',
            horizontalAlign: 'left',
          },
          xaxis: {
            type: 'datetime',
          },
        },
      },
      areaChartNullvalues: {
        series: [
          {
            name: 'Network',
            data: [
              {
                x: 'Dec 23 2017',
                y: null,
              },
              {
                x: 'Dec 24 2017',
                y: 44,
              },
              {
                x: 'Dec 25 2017',
                y: 31,
              },
              {
                x: 'Dec 26 2017',
                y: 38,
              },
              {
                x: 'Dec 27 2017',
                y: null,
              },
              {
                x: 'Dec 28 2017',
                y: 32,
              },
              {
                x: 'Dec 29 2017',
                y: 55,
              },
              {
                x: 'Dec 30 2017',
                y: 51,
              },
              {
                x: 'Dec 31 2017',
                y: 67,
              },
              {
                x: 'Jan 01 2018',
                y: 22,
              },
              {
                x: 'Jan 02 2018',
                y: 34,
              },
              {
                x: 'Jan 03 2018',
                y: null,
              },
              {
                x: 'Jan 04 2018',
                y: null,
              },
              {
                x: 'Jan 05 2018',
                y: 11,
              },
              {
                x: 'Jan 06 2018',
                y: 4,
              },
              {
                x: 'Jan 07 2018',
                y: 15,
              },
              {
                x: 'Jan 08 2018',
                y: null,
              },
              {
                x: 'Jan 09 2018',
                y: 9,
              },
              {
                x: 'Jan 10 2018',
                y: 34,
              },
              {
                x: 'Jan 11 2018',
                y: null,
              },
              {
                x: 'Jan 12 2018',
                y: null,
              },
              {
                x: 'Jan 13 2018',
                y: 13,
              },
              {
                x: 'Jan 14 2018',
                y: null,
              },
            ],
          },
        ],
        chartOptions: {
          chart: {
            animations: {
              enabled: false,
            },
            zoom: {
              enabled: false,
            },
          },
          dataLabels: {
            enabled: false,
          },
          stroke: {
            curve: 'straight',
          },
          fill: {
            opacity: 0.8,
            gradient: {
              enabled: false,
            },
            pattern: {
              enabled: true,
              style: ['verticalLines', 'horizontalLines'],
              width: 5,
              depth: 6,
            },
          },
          markers: {
            size: 5,
            hover: {
              size: 9,
            },
          },
          colors: ['#6c757d'],

          title: {
            text: 'Network Monitoring',
          },
          tooltip: {
            intersect: true,
            shared: false,
          },
          theme: {
            palette: 'palette1',
          },
          xaxis: {
            type: 'datetime',
          },
          yaxis: {
            title: {
              text: 'Bytes Received',
            },
          },
          grid: {
            row: {
              colors: ['transparent', 'transparent'], // takes an array which will be repeated on columns
              opacity: 0.2,
            },
            borderColor: '#f1f3fa',
          },
          responsive: [
            {
              breakpoint: 600,
              options: {
                chart: {
                  toolbar: {
                    show: false,
                  },
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
            <h4 class="header-title mb-4">Stacked Area</h4>
            <!-- Stacked Area chart -->
            <apexchart
              height="422"
              type="area"
              class="apex-charts"
              :series="stackedAreaChart.series"
              :options="stackedAreaChart.chartOptions"
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
            <h4 class="header-title mb-4">Area chart with null value</h4>
            <!-- Area chart with null value -->
            <apexchart
              height="422"
              type="area"
              class="apex-charts"
              :series="areaChartNullvalues.series"
              :options="areaChartNullvalues.chartOptions"
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