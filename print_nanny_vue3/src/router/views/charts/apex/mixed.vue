<script>
import appConfig from '@src/app.config'
import Layout from '@layouts/main'
import PageHeader from '@components/page-header'

/**
 * Mixed Charts component
 */
export default {
  page: {
    title: 'Mixed Charts',
    meta: [{ name: 'description', content: appConfig.description }],
  },
  components: { Layout, PageHeader },
  data() {
    return {
      title: 'Mixed Charts',
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
          text: 'Mixed Charts',
          active: true,
        },
      ],
      multipleYaxiesChart: {
        series: [
          {
            name: 'Income',
            type: 'column',
            data: [1.4, 2, 2.5, 1.5, 2.5, 2.8, 3.8, 4.6],
          },
          {
            name: 'Cashflow',
            type: 'column',
            data: [1.1, 3, 3.1, 4, 4.1, 4.9, 6.5, 8.5],
          },
          {
            name: 'Revenue',
            type: 'line',
            data: [20, 29, 37, 36, 44, 45, 50, 58],
          },
        ],
        chartOptions: {
          chart: {
            stacked: false,
            toolbar: {
              show: false,
            },
          },
          dataLabels: {
            enabled: false,
          },
          stroke: {
            width: [0, 0, 3],
          },
          colors: ['#727cf5', '#39afd1', '#fa5c7c'],
          xaxis: {
            categories: [2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016],
          },
          yaxis: [
            {
              axisTicks: {
                show: true,
              },
              axisBorder: {
                show: true,
                color: '#727cf5',
              },
              labels: {
                style: {
                  color: '#39afd1',
                },
              },
              title: {
                text: 'Income (thousand crores)',
              },
            },
            {
              axisTicks: {
                show: true,
              },
              axisBorder: {
                show: true,
                color: '#727cf5',
              },
              labels: {
                style: {
                  color: '#39afd1',
                },
                offsetX: 10,
              },
              title: {
                text: 'Operating Cashflow (thousand crores)',
              },
            },
            {
              opposite: true,
              axisTicks: {
                show: true,
              },
              axisBorder: {
                show: true,
                color: '#fa5c7c',
              },
              labels: {
                style: {
                  color: '#fa5c7c',
                },
              },
              title: {
                text: 'Revenue (thousand crores)',
              },
            },
          ],
          tooltip: {
            followCursor: true,
            y: {
              formatter: function(y) {
                if (typeof y !== 'undefined') {
                  return y + ' thousand crores'
                }
                return y
              },
            },
          },
          grid: {
            borderColor: '#f1f3fa',
          },
          legend: {
            offsetY: -10,
          },
          responsive: [
            {
              breakpoint: 600,
              options: {
                yaxis: {
                  show: false,
                },
                legend: {
                  show: false,
                },
              },
            },
          ],
        },
      },
      lineColumnAreaChart: {
        series: [
          {
            name: 'Team A',
            type: 'column',
            data: [23, 11, 22, 27, 13, 22, 37, 21, 44, 22, 30],
          },
          {
            name: 'Team B',
            type: 'area',
            data: [44, 55, 41, 67, 22, 43, 21, 41, 56, 27, 43],
          },
          {
            name: 'Team C',
            type: 'line',
            data: [30, 25, 36, 30, 45, 35, 64, 52, 59, 36, 39],
          },
        ],
        chartOptions: {
          chart: {
            stacked: false,
            toolbar: {
              show: false,
            },
          },
          stroke: {
            width: [0, 2, 4],
            curve: 'smooth',
          },
          plotOptions: {
            bar: {
              columnWidth: '50%',
            },
          },
          colors: ['#727cf5', '#39afd1', '#fa5c7c'],
          fill: {
            opacity: [0.85, 0.25, 1],
            gradient: {
              inverseColors: false,
              shade: 'light',
              type: 'vertical',
              opacityFrom: 0.85,
              opacityTo: 0.55,
              stops: [0, 100, 100, 100],
            },
          },
          labels: [
            '01/01/2003',
            '02/01/2003',
            '03/01/2003',
            '04/01/2003',
            '05/01/2003',
            '06/01/2003',
            '07/01/2003',
            '08/01/2003',
            '09/01/2003',
            '10/01/2003',
            '11/01/2003',
          ],
          markers: {
            size: 0,
          },
          legend: {
            offsetY: -10,
          },
          xaxis: {
            type: 'datetime',
          },
          yaxis: {
            title: {
              text: 'Points',
            },
          },
          tooltip: {
            shared: true,
            intersect: false,
            y: {
              formatter: function(y) {
                if (typeof y !== 'undefined') {
                  return y.toFixed(0) + ' points'
                }
                return y
              },
            },
          },
          grid: {
            borderColor: '#f1f3fa',
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
            <h4 class="header-title">Multiple Y-Axis Chart</h4>
            <!-- Multiple Y-Axis Chart -->
            <apexchart
              height="380"
              type="line"
              class="apex-charts"
              :series="multipleYaxiesChart.series"
              :options="multipleYaxiesChart.chartOptions"
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
            <h4 class="header-title">Line, Column & Area Chart</h4>
            <!-- Line, Column & Area Chart -->
            <apexchart
              height="380"
              type="line"
              class="apex-charts"
              :series="lineColumnAreaChart.series"
              :options="lineColumnAreaChart.chartOptions"
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