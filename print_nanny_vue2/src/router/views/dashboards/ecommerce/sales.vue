<script>
export default {
  data() {
    return {
      series: [44, 55, 41, 17],
      chartOptions: {
        legend: {
          show: false,
        },
        stroke: {
          colors: ['transparent'],
        },
        labels: ['Direct', 'Affilliate', 'Sponsored', 'E-mail'],
        responsive: [
          {
            breakpoint: 480,
            options: {
              chart: {
                width: 200,
              },
              legend: {
                position: 'bottom',
              },
            },
          },
        ],
        colors: ['#727cf5', '#0acf97', '#fa5c7c', '#ffbc00'],
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
          <a href="javascript:void(0);" class="dropdown-item">Sales Report</a>
          <!-- item-->
          <a href="javascript:void(0);" class="dropdown-item">Export Report</a>
          <!-- item-->
          <a href="javascript:void(0);" class="dropdown-item">Profit</a>
          <!-- item-->
          <a href="javascript:void(0);" class="dropdown-item">Action</a>
        </b-dropdown>
      </div>
      <h4 class="header-title">Total Sales</h4>

      <apexchart
        height="290"
        type="donut"
        class="apex-charts mb-4 mt-4"
        :series="series"
        :options="chartOptions"
      ></apexchart>

      <div class="chart-widget-list">
        <p>
          <i class="mdi mdi-square text-primary"></i> Direct
          <span class="float-right">$300.56</span>
        </p>
        <p>
          <i class="mdi mdi-square text-danger"></i> Affilliate
          <span class="float-right">$135.18</span>
        </p>
        <p>
          <i class="mdi mdi-square text-success"></i> Sponsored
          <span class="float-right">$48.96</span>
        </p>
        <p class="mb-0">
          <i class="mdi mdi-square text-warning"></i> E-mail
          <span class="float-right">$154.02</span>
        </p>
      </div>
    </div>
    <!-- end card-body-->
  </div>
  <!-- end card-->
</template>