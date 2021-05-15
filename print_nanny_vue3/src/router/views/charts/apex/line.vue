<script>
import appConfig from '@src/app.config'
import Layout from '@layouts/main'
import PageHeader from '@components/page-header'

/**
 * Line Charts component
 */
export default {
  page: {
    title: 'Line Charts',
    meta: [{ name: 'description', content: appConfig.description }],
  },
  components: { Layout, PageHeader },
  data() {
    return {
      title: 'Line Charts',
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
          text: 'Line Charts',
          active: true,
        },
      ],
      datalabelsChart: {
        series: [
          {
            name: 'High - 2018',
            data: [28, 29, 33, 36, 32, 32, 33],
          },
          {
            name: 'Low - 2018',
            data: [12, 11, 14, 18, 17, 13, 13],
          },
        ],
        chartOptions: {
          chart: {
            zoom: {
              enabled: false,
            },
            toolbar: {
              show: false,
            },
          },
          colors: ['#6c757d', '#727cf5'],
          dataLabels: {
            enabled: true,
          },
          stroke: {
            width: [3, 3],
            curve: 'smooth',
          },
          title: {
            text: 'Average High & Low Temperature',
            align: 'left',
          },
          grid: {
            row: {
              colors: ['transparent', 'transparent'], // takes an array which will be repeated on columns
              opacity: 0.2,
            },
            borderColor: '#f1f3fa',
          },
          markers: {
            style: 'inverted',
            size: 6,
          },
          xaxis: {
            categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul'],
            title: {
              text: 'Month',
            },
          },
          yaxis: {
            title: {
              text: 'Temperature',
            },
            min: 5,
            max: 40,
          },
          legend: {
            position: 'top',
            horizontalAlign: 'right',
            floating: true,
            offsetY: -25,
            offsetX: -5,
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
                legend: {
                  show: false,
                },
              },
            },
          ],
        },
      },
      dashedlineChart: {
        series: [
          {
            name: 'Session Duration',
            data: [45, 52, 38, 24, 33, 26, 21, 20, 6, 8, 15, 10],
          },
          {
            name: 'Page Views',
            data: [35, 41, 62, 42, 13, 18, 29, 37, 36, 51, 32, 35],
          },
          {
            name: 'Total Visits',
            data: [87, 57, 74, 99, 75, 38, 62, 47, 82, 56, 45, 47],
          },
        ],
        chartOptions: {
          chart: {
            height: 380,
            type: 'line',
            zoom: {
              enabled: false,
            },
          },
          dataLabels: {
            enabled: false,
          },
          stroke: {
            width: [3, 5, 3],
            curve: 'straight',
            dashArray: [0, 8, 5],
          },
          markers: {
            size: 0,
            style: 'hollow', // full, hollow, inverted
          },
          xaxis: {
            categories: [
              '01 Jan',
              '02 Jan',
              '03 Jan',
              '04 Jan',
              '05 Jan',
              '06 Jan',
              '07 Jan',
              '08 Jan',
              '09 Jan',
              '10 Jan',
              '11 Jan',
              '12 Jan',
            ],
          },
          colors: ['#6c757d', '#0acf97', '#39afd1'],
          tooltip: {
            y: {
              title: {
                formatter: function(val) {
                  if (val === 'Session Duration') return val + ' (mins)'
                  else if (val === 'Page Views') return val + ' per session'
                  return val
                },
              },
            },
          },
          grid: {
            borderColor: '#f1f3fa',
          },
          legend: {
            offsetY: -10,
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
            <h4 class="header-title mb-4">Line with Data Labels</h4>
            <!-- Line with Data Labels -->
            <apexchart
              height="380"
              type="line"
              class="apex-charts"
              :series="datalabelsChart.series"
              :options="datalabelsChart.chartOptions"
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
            <h4 class="header-title mb-4">Dashes line chart</h4>
            <!-- Dashes line chart -->
            <apexchart
              height="380"
              type="line"
              class="apex-charts"
              :series="dashedlineChart.series"
              :options="dashedlineChart.chartOptions"
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