<script>
export default {
  data() {
    return {
      series: [
        {
          name: 'Actual',
          data: [65, 59, 80, 81, 56, 89, 40, 32, 65, 59, 80, 81],
        },
        {
          name: 'Projection',
          data: [89, 40, 32, 65, 59, 80, 81, 56, 89, 40, 65, 59],
        },
      ],
      chartOptions: {
        chart: {
          parentHeightOffset: 0,
          stacked: true,
          toolbar: {
            show: false,
          },
        },
        plotOptions: {
          bar: {
            horizontal: false,
            columnWidth: '20%',
          },
        },
        grid: {
          padding: {
            left: 0,
            right: 0,
          },
        },
        dataLabels: {
          enabled: false,
        },
        stroke: {
          show: true,
          width: 2,
          colors: ['transparent'],
        },
        zoom: {
          enabled: false,
        },
        legend: {
          show: false,
        },
        colors: ['#727cf5', '#e3eaef'],
        xaxis: {
          categories: [
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
          axisBorder: {
            show: false,
          },
        },
        yaxis: {
          labels: {
            formatter: function(val) {
              return val + 'k'
            },
            offsetX: -15,
          },
        },
        fill: {
          opacity: 1,
        },
        tooltip: {
          y: {
            formatter: function(val) {
              return '$' + val + 'k'
            },
          },
        },
      },
    }
  },
}
</script>

<template>
  <div class="card">
    <div class="card-body">
      <div class="dropdown float-right">
        <b-dropdown toggle-class="arrow-none card-drop p-0" variant="black" right>
          <template v-slot:button-content>
            <i class="mdi mdi-dots-vertical"></i>
          </template>
          <a href="javascript:void(0);" class="dropdown-item">Sales Report</a>
          <!-- item-->
          <a href="javascript:void(0);" class="dropdown-item">Export Report</a>
          <!-- item-->
          <a href="javascript:void(0);" class="dropdown-item">Profit</a>
          <!-- item-->
          <a href="javascript:void(0);" class="dropdown-item">Action</a>
        </b-dropdown>
      </div>
      <h4 class="header-title mb-3">Projections Vs Actuals</h4>
      <apexchart height="255" type="bar" :series="series" :options="chartOptions"></apexchart>
    </div>
    <!-- end card-body -->
  </div>
  <!-- end card -->
</template>
