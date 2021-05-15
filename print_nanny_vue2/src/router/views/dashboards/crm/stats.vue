<script>
import StatChart from '@components/widgets/widget-stat-chart'

export default {
  components: {
    StatChart,
  },
  data() {
    return {
      chartData: [
        {
          title: 'Campaign Sent',
          number: '9,184',
          chartColor: '#727cf5',
          subtext: '3.27%',
          chartData: [25, 66, 41, 89, 63, 25, 44, 12, 36, 9, 54],
          chartType: 'bar',
        },
        {
          title: 'New Leads',
          number: '3,254',
          chartColor: '#0acf97',
          subtext: '5.38%',
          chartData: [25, 66, 41, 89, 63, 25, 44, 12, 36, 9, 54],
          chartType: 'line',
        },
        {
          title: 'Deals',
          number: '861',
          chartColor: '#727cf5',
          subtext: '4.87%',
          chartData: [12, 14, 2, 47, 42, 15, 47, 75, 65, 19, 14],
          chartType: 'bar',
        },
        {
          title: 'Booked Revenue',
          number: '$253k',
          chartColor: '#0acf97',
          subtext: '11.7%',
          chartData: [47, 45, 74, 14, 56, 74, 14, 11, 7, 39, 82],
          chartType: 'bar',
        },
      ],
    }
  },
}
</script>

<template>
  <div class="row">
    <div v-for="chart of chartData" :key="chart.text" class="col-lg-6 col-xl-3">
      <div class="card">
        <div class="card-body">
          <StatChart
            :title="chart.title"
            :number="chart.number"
            :chart-color="chart.chartColor"
            :chart-data="chart.chartData"
            :chart-type="chart.chartType"
            :subtext="chart.subtext"
          />
        </div>
        <!-- end card-body -->
      </div>
      <!-- end card -->
    </div>
    <!-- end col -->
  </div>
  <!-- end  row -->
</template>