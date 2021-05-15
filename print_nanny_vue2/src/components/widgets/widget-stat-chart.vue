<script>
/**
 * A stat show case widget to show progress through chart visulization
 * 1. widget text specify the which data represents in widget.
 * 2. widget 'number' property specify the value of title such as progress or sales etc., that depends on title.
 * 3. Widget chart color specify using the 'chartColor' input property.
 * 4. widget trend specify using the 'subtext' input property. Trend value consider on title.
 * 5. Widget chart series data specify using the 'chartData' input property.
 * 6. Using 'chartType' property user specify the chart type such as line, bar.
 */
export default {
  props: {
    title: {
      type: String,
      default: '',
    },
    number: {
      type: String,
      default: '',
    },
    chartColor: {
      type: String,
      default: '#727cf5',
    },
    subtext: {
      type: String,
      default: '',
    },
    chartData: {
      type: Array,
      required: true,
    },
    chartType: {
      type: String,
      default: 'bar',
    },
  },
  data() {
    return {
      chartOptions: {
        chart: {
          sparkline: {
            enabled: true,
          },
        },
        grid: {
          padding: {
            top: 10,
          },
        },
        plotOptions: {
          bar: {
            columnWidth: '60%',
          },
        },
        xaxis: {
          crosshairs: {
            width: 1,
          },
        },
        tooltip: {
          fixed: {
            enabled: false,
          },
          x: {
            show: false,
          },
          y: {
            title: {
              formatter: (seriesName) => {
                return ''
              },
            },
          },
          marker: {
            show: false,
          },
        },
        stroke: {
          width: 2,
          curve: 'smooth',
        },
        colors: [this.chartColor],
      },
      series: [
        {
          data: this.chartData,
        },
      ],
    }
  },
}
</script>
<template>
  <div class="row align-items-center">
    <div class="col-6">
      <h5 class="text-muted font-weight-normal mt-0 text-truncate" title="Campaign Sent">{{ title }}</h5>
      <h3 class="my-2 py-1">{{ number }}</h3>
      <p class="mb-0 text-muted">
        <span class="text-success mr-2">
          <i class="mdi mdi-arrow-up-bold"></i>
          {{ subtext }}
        </span>
      </p>
    </div>
    <!-- end col -->
    <div class="col-6">
      <div class="text-right">
        <apexchart :type="`${chartType}`" height="60" :series="series" :options="chartOptions"></apexchart>
      </div>
    </div>
    <!-- end col -->
  </div>
  <!-- end row -->
</template>