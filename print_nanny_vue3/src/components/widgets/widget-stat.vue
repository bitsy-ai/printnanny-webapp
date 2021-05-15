<script>
/**
 * A stat show case widget to show progress through chart visulization
 * 1. Title specify the value of subtitle. EX. The sales is subtitle and the value is $424,652.    
 * 2. Widget chart represent for which data, that specify in subtitle. Ex. Sales subtitle specify the chart data is as of the sales of product.
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
    subtitle: {
      type: String,
      default: '',
    },
    chartColor: {
      type: String,
      default: '#3688fc',
    },
    chartData: {
      type: Array,
      required: true,
    },
    chartType: {
      type: String,
      default: 'line',
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
        xaxis: {
          crosshairs: {
            width: 1,
          },
        },
        stroke: {
          width: 1,
          curve: 'straight',
        },
        fill: {
          opacity: 0.5,
        },
        title: {
          text: this.title,
          offsetX: 20,
          offsetY: 20,
          style: {
            fontSize: '24px',
          },
        },
        subtitle: {
          text: this.subtitle,
          offsetX: 20,
          offsetY: 55,
          style: {
            fontSize: '14px',
          },
        },
        colors: [this.chartColor],
      },
      series: [
        {
          name: this.subtitle,
          data: this.chartData,
        },
      ],
    }
  },
}
</script>

<template>
  <div class="card">
    <div class="card-body p-0">
      <apexchart
        :type="`${chartType}`"
        height="172"
        class="apex-charts"
        :series="series"
        :options="chartOptions"
      ></apexchart>
    </div>
    <!-- end card-body -->
  </div>
  <!-- end card -->
</template>