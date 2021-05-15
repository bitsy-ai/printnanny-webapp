<script>
import appConfig from '@src/app.config'
import Layout from '@layouts/main'
import PageHeader from '@components/page-header'

/**
 * RadialBar Charts component
 */
export default {
  page: {
    title: 'RadialBar Charts',
    meta: [{ name: 'description', content: appConfig.description }],
  },
  components: { Layout, PageHeader },
  data() {
    return {
      title: 'RadialBar Charts',
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
          text: 'RadialBar Charts',
          active: true,
        },
      ],
      customAngleChart: {
        series: [76, 67, 61, 90],
        chartOptions: {
          plotOptions: {
            radialBar: {
              offsetY: -30,
              startAngle: 0,
              endAngle: 270,
              hollow: {
                margin: 5,
                size: '30%',
                background: 'transparent',
                image: undefined,
              },
              dataLabels: {
                name: {
                  show: false,
                },
                value: {
                  show: false,
                },
              },
            },
          },
          colors: ['#0acf97', '#727cf5', '#fa5c7c', '#ffbc00'],
          labels: ['Vimeo', 'Messenger', 'Facebook', 'LinkedIn'],
          legend: {
            show: true,
            floating: true,
            fontSize: '13px',
            position: 'left',
            offsetX: 10,
            offsetY: 10,
            labels: {
              useSeriesColors: true,
            },
            markers: {
              size: 0,
            },
            formatter: function(seriesName, opts) {
              return (
                seriesName + ':  ' + opts.w.globals.series[opts.seriesIndex]
              )
            },
            itemMargin: {
              horizontal: 1,
            },
          },
          responsive: [
            {
              breakpoint: 480,
              options: {
                legend: {
                  show: false,
                },
              },
            },
          ],
        },
      },
      circularGuageChart: {
        series: [67],
        chartOptions: {
          plotOptions: {
            radialBar: {
              startAngle: -135,
              endAngle: 135,
              dataLabels: {
                name: {
                  fontSize: '16px',
                  color: undefined,
                  offsetY: 120,
                },
                value: {
                  offsetY: 76,
                  fontSize: '22px',
                  color: undefined,
                  formatter: function(val) {
                    return val + '%'
                  },
                },
              },
            },
          },
          fill: {
            gradient: {
              enabled: true,
              shade: 'dark',
              shadeIntensity: 0.15,
              inverseColors: false,
              opacityFrom: 1,
              opacityTo: 1,
              stops: [0, 50, 65, 91],
            },
          },
          colors: ['#727cf5'],
          stroke: {
            dashArray: 4,
          },
          labels: ['Median Ratio'],
          responsive: [
            {
              breakpoint: 380,
              options: {
                chart: {
                  height: 280,
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
            <h4 class="header-title mb-4">Circle Chart - Custom Angle</h4>
            <div class="text-center">
              <!-- Circle Chart -->
              <apexchart
                height="380"
                type="radialBar"
                class="apex-charts"
                :series="customAngleChart.series"
                :options="customAngleChart.chartOptions"
              ></apexchart>
            </div>
          </div>
          <!-- end card body-->
        </div>
        <!-- end card -->
      </div>
      <!-- end col-->

      <div class="col-xl-6">
        <div class="card">
          <div class="card-body">
            <h4 class="header-title mb-4">Stroked Circular Guage</h4>
            <!-- Stroked Circular Guage -->
            <apexchart
              height="380"
              type="radialBar"
              class="apex-charts"
              :series="circularGuageChart.series"
              :options="circularGuageChart.chartOptions"
            ></apexchart>
          </div>
          <!-- end card body-->
        </div>
        <!-- end card -->
      </div>
      <!-- end col-->
    </div>
  </Layout>
</template>