<script>
import { Bar } from 'vue-chartjs'

export default {
  extends: Bar,
  mounted() {
    this.renderChart(
      {
        labels: [
          'Jan',
          'Feb',
          'Mar',
          'Apr',
          'May',
          'Jun',
          'Jul',
          'Aug',
          'Sep',
          'Oct',
          'Nov',
          'Dec',
        ],
        datasets: [
          {
            barPercentage: 0.7,
            categoryPercentage: 0.5,
            label: 'Orders',
            backgroundColor: '#727cf5',
            borderColor: '#727cf5',
            hoverBackgroundColor: '#727cf5',
            hoverBorderColor: '#727cf5',
            data: [65, 59, 80, 81, 56, 89, 40, 32, 65, 59, 80, 81],
          },
          {
            barPercentage: 0.7,
            categoryPercentage: 0.5,
            label: 'Revenue',
            backgroundColor: '#e3eaef',
            borderColor: '#e3eaef',
            hoverBackgroundColor: '#e3eaef',
            hoverBorderColor: '#e3eaef',
            data: [89, 40, 32, 65, 59, 80, 81, 56, 89, 40, 65, 59],
          },
        ],
      },
      {
        responsive: true,
        maintainAspectRatio: false,
        legend: {
          display: false,
        },
        scales: {
          yAxes: [
            {
              gridLines: {
                display: false,
                color: 'rgba(0,0,0,0.05)',
              },
              stacked: false,
              ticks: {
                stepSize: 20,
              },
            },
          ],
          xAxes: [
            {
              stacked: false,
              gridLines: {
                color: 'rgba(0,0,0,0.01)',
              },
            },
          ],
        },
      }
    )
  },
}
</script>