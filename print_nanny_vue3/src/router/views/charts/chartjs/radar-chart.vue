<script>
import { Radar } from 'vue-chartjs'

export default {
  extends: Radar,
  mounted() {
    this.renderChart(
      {
        labels: [
          'Eating',
          'Drinking',
          'Sleeping',
          'Designing',
          'Coding',
          'Cycling',
          'Running',
        ],
        datasets: [
          {
            label: 'Desktops',
            backgroundColor: 'rgba(57, 175, 209, 0.2)',
            borderColor: '#39afd1',
            pointBackgroundColor: '#39afd1',
            pointBorderColor: '#fff',
            pointHoverBackgroundColor: '#fff',
            pointHoverBorderColor: '#3bafda',
            data: [65, 59, 90, 81, 56, 55, 40],
          },
          {
            label: 'Tablets',
            backgroundColor: 'rgba(161, 127, 224, 0.2)',
            borderColor: '#a17fe0',
            pointBackgroundColor: '#a17fe0',
            pointBorderColor: '#fff',
            pointHoverBackgroundColor: '#fff',
            pointHoverBorderColor: '#f672a7',
            data: [28, 48, 40, 19, 96, 27, 100],
          },
        ],
      },
      {
        maintainAspectRatio: true,
        legend: {
          position: 'top',
        },
      }
    )
  },
}
</script>