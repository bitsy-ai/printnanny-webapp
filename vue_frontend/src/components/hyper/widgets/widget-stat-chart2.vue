<script>
/**
 * A stat show case widget to show progress through chart visulization
 * 1. Title specify the bigger text of widget    
 * 2. Widget 'number' property specify the value of title.
 * 3. Widget chart color specify using the 'chartColor' input property.
 * 4. Widget chart series data specify using the 'chartData' input property.
 * 5. Using 'chartType' property user specify the chart type such as line, bar.   
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
      default: '#734CEA',
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
          width: 4,
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
  <div class="card widget-flat">
    <div class="card-body">
      <div class="float-right">
        <button type="button" class="btn btn-sm btn-light">View</button>
      </div>
      <h6 class="text-muted text-uppercase mt-0" title="Revenue">{{title}}</h6>
      <h3 class="mb-4 mt-2">{{number}}</h3>
      <apexchart
        :type="`${chartType}`"
        height="100"
        class="apex-charts mb-3"
        :series="series"
        :options="chartOptions"
      ></apexchart>
      <div class="row text-center">
        <div class="col-6">
          <h6 class="text-truncate d-block">Last Month</h6>
          <p class="font-18 mb-0">358</p>
        </div>
        <div class="col-6">
          <h6 class="text-truncate d-block">Current Month</h6>
          <p class="font-18 mb-0">194</p>
        </div>
      </div>
    </div>
    <!-- end card-body -->
  </div>
  <!-- end card -->
</template>