<script>
import { Doughnut } from 'vue-chartjs'

export default {
  extends: Doughnut,
  mounted() {
    this.renderChart(
      {
        labels: ['Completed', 'In-progress', 'Behind'],
        datasets: [
          {
            data: [64, 26, 10],
            backgroundColor: ['#0acf97', '#727cf5', '#fa5c7c'],
            borderColor: 'transparent',
            borderWidth: '3',
          },
        ],
      },
      {
        maintainAspectRatio: true,
        cutoutPercentage: 80,
        legend: {
          display: false,
        },
      }
    )
  },
}
</script>