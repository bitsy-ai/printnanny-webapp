<script>
import appConfig from '@src/app.config'
import Layout from '@layouts/main'
import PageHeader from '@components/page-header'

/**
 * series data method
 */
function generateData(count, yrange) {
  var i = 0
  var series = []
  while (i < count) {
    var x = (i + 1).toString()
    var y =
      Math.floor(Math.random() * (yrange.max - yrange.min + 1)) + yrange.min

    series.push({
      x: x,
      y: y,
    })
    i++
  }
  return series
}

/**
 * Heatmap Charts component
 */
export default {
  page: {
    title: 'Heatmap Charts',
    meta: [{ name: 'description', content: appConfig.description }],
  },
  components: { Layout, PageHeader },
  data() {
    return {
      title: 'Heatmap Charts',
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
          text: 'Heatmap Charts',
          active: true,
        },
      ],
      basicHeatmap: {
        series: [
          {
            name: 'Metric1',
            data: generateData(18, {
              min: 0,
              max: 90,
            }),
          },
          {
            name: 'Metric2',
            data: generateData(18, {
              min: 0,
              max: 90,
            }),
          },
          {
            name: 'Metric3',
            data: generateData(18, {
              min: 0,
              max: 90,
            }),
          },
          {
            name: 'Metric4',
            data: generateData(18, {
              min: 0,
              max: 90,
            }),
          },
          {
            name: 'Metric5',
            data: generateData(18, {
              min: 0,
              max: 90,
            }),
          },
          {
            name: 'Metric6',
            data: generateData(18, {
              min: 0,
              max: 90,
            }),
          },
          {
            name: 'Metric7',
            data: generateData(18, {
              min: 0,
              max: 90,
            }),
          },
          {
            name: 'Metric8',
            data: generateData(18, {
              min: 0,
              max: 90,
            }),
          },
          {
            name: 'Metric9',
            data: generateData(18, {
              min: 0,
              max: 90,
            }),
          },
        ],
        chartOptions: {
          dataLabels: {
            enabled: false,
          },
          colors: ['#727cf5'],
          xaxis: {
            type: 'category',
          },
        },
      },
      colorRangeHeatmap: {
        series: [
          {
            name: 'Jan',
            data: generateData(20, {
              min: -30,
              max: 55,
            }),
          },
          {
            name: 'Feb',
            data: generateData(20, {
              min: -30,
              max: 55,
            }),
          },
          {
            name: 'Mar',
            data: generateData(20, {
              min: -30,
              max: 55,
            }),
          },
          {
            name: 'Apr',
            data: generateData(20, {
              min: -30,
              max: 55,
            }),
          },
          {
            name: 'May',
            data: generateData(20, {
              min: -30,
              max: 55,
            }),
          },
          {
            name: 'Jun',
            data: generateData(20, {
              min: -30,
              max: 55,
            }),
          },
          {
            name: 'Jul',
            data: generateData(20, {
              min: -30,
              max: 55,
            }),
          },
          {
            name: 'Aug',
            data: generateData(20, {
              min: -30,
              max: 55,
            }),
          },
          {
            name: 'Sep',
            data: generateData(20, {
              min: -30,
              max: 55,
            }),
          },
        ],
        chartOptions: {
          dataLabels: {
            enabled: false,
          },
          plotOptions: {
            heatmap: {
              shadeIntensity: 0.5,
              colorScale: {
                ranges: [
                  {
                    from: -30,
                    to: 5,
                    name: 'Low',
                    color: '#fa5c7c',
                  },
                  {
                    from: 6,
                    to: 20,
                    name: 'Medium',
                    color: '#ffbc00',
                  },
                  {
                    from: 21,
                    to: 45,
                    name: 'High',
                    color: '#39afd1',
                  },
                  {
                    from: 46,
                    to: 55,
                    name: 'Extreme',
                    color: '#0acf97',
                  },
                ],
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
            <h4 class="header-title">Basic Heatmap - Single Series</h4>
            <!-- Basic Heatmap -->
            <apexchart
              height="380"
              type="heatmap"
              class="apex-charts"
              :series="basicHeatmap.series"
              :options="basicHeatmap.chartOptions"
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
            <h4 class="header-title">Heatmap - Color Range</h4>
            <!-- Heatmap - Color Range -->
            <apexchart
              height="380"
              type="heatmap"
              class="apex-charts"
              :series="colorRangeHeatmap.series"
              :options="colorRangeHeatmap.chartOptions"
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