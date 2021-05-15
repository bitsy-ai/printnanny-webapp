<script>
import { Doughnut } from 'vue-chartjs'

export default {
  extends: Doughnut,
  mounted() {
    this.renderChart(
      {
        labels: ['Direct', 'Affilliate', 'Sponsored', 'E-mail'],
        datasets: [
          {
            data: [300, 135, 48, 154],
            backgroundColor: ['#727cf5', '#fa5c7c', '#0acf97', '#ebeff2'],
            borderColor: 'transparent',
            borderWidth: '3',
          },
        ],
      },
      {
        maintainAspectRatio: true,
        cutoutPercentage: 60,
        legend: {
          display: false,
        },
        height: 200,
      }
    )
  },
}
</script>