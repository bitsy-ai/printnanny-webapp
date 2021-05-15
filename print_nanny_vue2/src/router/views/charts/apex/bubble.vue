<script>
import appConfig from '@src/app.config'
import Layout from '@layouts/main'
import PageHeader from '@components/page-header'

function generateData(baseval, count, yrange) {
  var i = 0
  var series = []
  while (i < count) {
    var x = Math.floor(Math.random() * (750 - 1 + 1)) + 1
    var y =
      Math.floor(Math.random() * (yrange.max - yrange.min + 1)) + yrange.min
    var z = Math.floor(Math.random() * (75 - 15 + 1)) + 15

    series.push([x, y, z])
    baseval += 86400000
    i++
  }
  return series
}

function generateData1(baseval1, count, yrange) {
  var i = 0
  var series = []
  while (i < count) {
    // var x =Math.floor(Math.random() * (750 - 1 + 1)) + 1;
    var y =
      Math.floor(Math.random() * (yrange.max - yrange.min + 1)) + yrange.min
    var z = Math.floor(Math.random() * (75 - 15 + 1)) + 15

    series.push([baseval1, y, z])
    baseval1 += 86400000
    i++
  }
  return series
}

/**
 * Bubble Charts component
 */
export default {
  page: {
    title: 'Bubble Charts',
    meta: [{ name: 'description', content: appConfig.description }],
  },
  components: { Layout, PageHeader },
  data() {
    return {
      title: 'Bubble Charts',
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
          text: 'Bubble Charts',
          active: true,
        },
      ],
      simpleBubbleChart: {
        series: [
          {
            name: 'Bubble1',
            data: generateData(new Date('11 Feb 2017 GMT').getTime(), 20, {
              min: 10,
              max: 60,
            }),
          },
          {
            name: 'Bubble2',
            data: generateData(new Date('11 Feb 2017 GMT').getTime(), 20, {
              min: 10,
              max: 60,
            }),
          },
          {
            name: 'Bubble3',
            data: generateData(new Date('11 Feb 2017 GMT').getTime(), 20, {
              min: 10,
              max: 60,
            }),
          },
        ],
        chartOptions: {
          chart: {
            toolbar: {
              show: false,
            },
          },
          dataLabels: {
            enabled: false,
          },
          fill: {
            opacity: 0.8,
            gradient: {
              enabled: false,
            },
          },
          title: {
            text: 'Simple Bubble Chart',
          },
          colors: ['#727cf5', '#ffbc00', '#fa5c7c'],
          xaxis: {
            tickAmount: 12,
            type: 'category',
          },
          grid: {
            borderColor: '#f1f3fa',
          },
          legend: {
            offsetY: -10,
          },
          yaxis: {
            max: 70,
          },
        },
      },
      DBubbleChart: {
        series: [
          {
            name: 'Product 1',
            data: generateData1(new Date('11 Feb 2017 GMT').getTime(), 20, {
              min: 10,
              max: 60,
            }),
          },
          {
            name: 'Product 2',
            data: generateData1(new Date('11 Feb 2017 GMT').getTime(), 20, {
              min: 10,
              max: 60,
            }),
          },
          {
            name: 'Product 3',
            data: generateData1(new Date('11 Feb 2017 GMT').getTime(), 20, {
              min: 10,
              max: 60,
            }),
          },
          {
            name: 'Product 4',
            data: generateData1(new Date('11 Feb 2017 GMT').getTime(), 20, {
              min: 10,
              max: 60,
            }),
          },
        ],
        chartOptions: {
          chart: {
            toolbar: {
              show: false,
            },
          },
          dataLabels: {
            enabled: false,
          },
          colors: ['#727cf5', '#0acf97', '#fa5c7c', '#39afd1'],
          fill: {
            type: 'gradient',
          },
          xaxis: {
            tickAmount: 12,
            type: 'datetime',

            labels: {
              rotate: 0,
            },
          },
          yaxis: {
            max: 70,
          },
          legend: {
            offsetY: -10,
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
            <h4 class="header-title">Simple Bubble Chart</h4>
            <!-- Bubble chart -->
            <apexchart
              height="380"
              type="bubble"
              class="apex-charts"
              :series="simpleBubbleChart.series"
              :options="simpleBubbleChart.chartOptions"
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
            <h4 class="header-title">3D Bubble Chart</h4>
            <!-- 3D bubble chart -->
            <apexchart
              height="380"
              type="bubble"
              class="apex-charts"
              :series="DBubbleChart.series"
              :options="DBubbleChart.chartOptions"
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