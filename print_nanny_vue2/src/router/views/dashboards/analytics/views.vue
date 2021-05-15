<script>
function getRandomData(number) {
  var graphData = []
  for (var idx = 0; idx < number; idx++) {
    graphData.push(Math.floor(Math.random() * Math.floor(90)) + 30)
  }
  return graphData
}
export default {
  data() {
    return {
      series: [
        {
          name: 'Views',
          data: getRandomData(10),
        },
      ],
      chartOptions: {
        chart: {
          stacked: true,
          toolbar: {
            show: false,
          },
        },
        plotOptions: {
          bar: {
            horizontal: false,
            endingShape: 'rounded',
            columnWidth: '22%',
            dataLabels: {
              position: 'top', // top, center, bottom
            },
          },
        },
        dataLabels: {
          enabled: true,
          offsetY: -24,
          style: {
            fontSize: '12px',
            colors: ['#98a6ad'],
          },
        },
        zoom: {
          enabled: false,
        },
        legend: {
          show: false,
        },
        colors: ['#0acf97'],
        xaxis: {
          labels: {
            show: false,
          },
          axisTicks: {
            show: false,
          },
          axisBorder: {
            show: false,
          },
        },
        yaxis: {
          labels: {
            show: false,
          },
        },
        fill: {
          type: 'gradient',
          gradient: {
            inverseColors: !0,
            shade: 'light',
            type: 'horizontal',
            shadeIntensity: 0.25,
            gradientToColors: void 0,
            opacityFrom: 1,
            opacityTo: 1,
            stops: [0, 100, 100, 100],
          },
        },
        tooltip: {
          y: {
            formatter: function(val) {
              return val
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
          <!-- item-->
          <a href="javascript:void(0);" class="dropdown-item">Refresh Report</a>
          <!-- item-->
          <a href="javascript:void(0);" class="dropdown-item">Export Report</a>
        </b-dropdown>
      </div>
      <h4 class="header-title">Views Per Minute</h4>

      <apexchart
        height="150"
        type="bar"
        class="apex-charts mt-2"
        :series="series"
        :options="chartOptions"
      ></apexchart>

      <div class="table-responsive mt-3 mb-0">
        <table class="table table-sm mb-0 font-13">
          <thead>
            <tr>
              <th>Page</th>
              <th>Views</th>
              <th>Bounce Rate</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>
                <a href="javascript:void(0);" class="text-muted">/hyper/dashboard-analytics</a>
              </td>
              <td>25</td>
              <td>87.5%</td>
            </tr>
            <tr>
              <td>
                <a href="javascript:void(0);" class="text-muted">/hyper/dashboard-crm</a>
              </td>
              <td>15</td>
              <td>21.48%</td>
            </tr>
            <tr>
              <td>
                <a href="javascript:void(0);" class="text-muted">/ubold/dashboard</a>
              </td>
              <td>10</td>
              <td>63.59%</td>
            </tr>
            <tr>
              <td>
                <a href="javascript:void(0);" class="text-muted">/minton/home</a>
              </td>
              <td>7</td>
              <td>56.12%</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <!-- end card-body-->
  </div>
  <!-- end card-->
</template>