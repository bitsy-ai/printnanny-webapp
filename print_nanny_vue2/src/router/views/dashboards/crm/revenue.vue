<script>
export default {
  data() {
    return {
      series: [
        {
          name: 'Total Revenue',
          type: 'area',
          data: [44, 55, 31, 47, 31, 43, 26, 41, 31, 47, 33, 43],
        },
        {
          name: 'Total Pipeline',
          type: 'line',
          data: [55, 69, 45, 61, 43, 54, 37, 52, 44, 61, 43, 56],
        },
      ],
      chartOptions: {
        chart: {
          toolbar: {
            show: false,
          },
        },
        stroke: {
          curve: 'smooth',
          width: 2,
        },
        fill: {
          type: 'solid',
          opacity: [0.35, 1],
        },
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
        markers: {
          size: 0,
        },
        colors: ['#0acf97', '#fa5c7c'],
        yaxis: [
          {
            title: {
              text: 'Revenue (USD)',
            },
            min: 0,
          },
        ],
        tooltip: {
          shared: true,
          intersect: false,
          y: {
            formatter: function(y) {
              if (typeof y !== 'undefined') {
                return y.toFixed(0) + 'k'
              }
              return y
            },
          },
        },
        grid: {
          borderColor: '#f1f3fa',
        },
        legend: {
          fontSize: '14px',
          fontFamily: '14px',
          offsetY: -10,
        },
        responsive: [
          {
            breakpoint: 600,
            options: {
              yaxis: {
                show: false,
              },
              legend: {
                show: false,
              },
            },
          },
        ],
      },
    }
  },
}
</script>

<template>
  <div class="card">
    <div class="card-body">
      <div class="float-right">
        <b-dropdown toggle-class="arrow-none card-drop p-0" variant="black" right>
          <template v-slot:button-content>
            <i class="mdi mdi-dots-vertical"></i>
          </template>
          <a href="javascript:void(0);" class="dropdown-item">Today</a>
          <!-- item-->
          <a href="javascript:void(0);" class="dropdown-item">Yesterday</a>
          <!-- item-->
          <a href="javascript:void(0);" class="dropdown-item">Last Week</a>
          <!-- item-->
          <a href="javascript:void(0);" class="dropdown-item">Last Month</a>
        </b-dropdown>
      </div>

      <h4 class="header-title mb-3">Revenue</h4>

      <div class="chart-content-bg">
        <div class="row text-center">
          <div class="col-md-6">
            <p class="text-muted mb-0 mt-3">Current Month</p>
            <h2 class="font-weight-normal mb-3">
              <span>$42,025</span>
            </h2>
          </div>
          <div class="col-md-6">
            <p class="text-muted mb-0 mt-3">Previous Month</p>
            <h2 class="font-weight-normal mb-3">
              <span>$74,651</span>
            </h2>
          </div>
        </div>
      </div>
      
      <apexchart
        height="321"
        type="line"
        class="apex-charts"
        :series="series"
        :options="chartOptions"
      ></apexchart>
    </div>
    <!-- end card body-->
  </div>
  <!-- end card -->
</template>