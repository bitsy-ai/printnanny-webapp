<script>
export default {
  data() {
    return {
      series: [
        {
          name: 'Usage',
          data: [80, 50, 30, 40, 60, 20],
        },
      ],
      chartOptions: {
        chart: {
          toolbar: {
            show: false,
          },
        },
        labels: ['Chrome', 'Firefox', 'Safari', 'Opera', 'Edge', 'Explorer'],
        plotOptions: {
          radar: {
            size: 130,
            polygons: {
              strokeColor: '#e9e9e9',
              fill: {
                colors: ['#f8f8f8', '#fff'],
              },
            },
          },
        },
        colors: ['#727cf5'],
        yaxis: {
          labels: {
            formatter: function(val) {
              return val + '%'
            },
          },
        },
        dataLabels: {
          enabled: true,
        },
        markers: {
          size: 4,
          colors: ['#fff'],
          strokeColor: ['#727cf5'],
          strokeWidth: 2,
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
          <!-- item-->
          <a href="javascript:void(0);" class="dropdown-item">Refresh Report</a>
          <!-- item-->
          <a href="javascript:void(0);" class="dropdown-item">Export Report</a>
        </b-dropdown>
      </div>
      <h4 class="header-title">Sessions by Browser</h4>
      <apexchart
        height="343"
        type="radar"
        class="apex-charts mt-3"
        :series="series"
        :options="chartOptions"
      ></apexchart>
    </div>
    <!-- end card-body-->
  </div>
  <!-- end card-->
</template>