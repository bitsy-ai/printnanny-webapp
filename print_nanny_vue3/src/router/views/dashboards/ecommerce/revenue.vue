<script>
export default {
  data() {
    return {
      series: [
        {
          name: 'Current Week',
          data: [10, 20, 15, 25, 20, 30, 20],
        },
        {
          name: 'Previous Week',
          data: [0, 15, 10, 30, 15, 35, 25],
        },
      ],
      chartOptions: {
        chart: {
          dropShadow: {
            enabled: true,
            opacity: 0.2,
            blur: 7,
            left: -7,
            top: 7,
          },
          toolbar: {
            show: false,
          },
          parentHeightOffset: 0,
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
          curve: 'smooth',
          width: 4,
        },
        colors: ['#727cf5', '#0acf97'],
        zoom: {
          enabled: false,
        },
        legend: {
          show: false,
        },
        xaxis: {
          type: 'string',
          categories: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
          tooltip: {
            enabled: false,
          },
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
      },
    }
  },
}
</script>

<template>
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
    <h4 class="header-title mb-3">Revenue</h4>
    <div class="chart-content-bg">
      <div class="row text-center">
        <div class="col-md-6">
          <p class="text-muted mb-0 mt-3">Current Week</p>
          <h2 class="font-weight-normal mb-3">
            <small class="mdi mdi-checkbox-blank-circle text-primary align-middle mr-1"></small>
            <span>$58,254</span>
          </h2>
        </div>
        <div class="col-md-6">
          <p class="text-muted mb-0 mt-3">Previous Week</p>
          <h2 class="font-weight-normal mb-3">
            <small class="mdi mdi-checkbox-blank-circle text-success align-middle mr-1"></small>
            <span>$69,524</span>
          </h2>
        </div>
      </div>
    </div>
    <div class="dash-item-overlay d-none d-md-block">
      <h5>Today's Earning: $2,562.30</h5>
      <p class="text-muted font-13 mb-3 mt-2">
        Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui.
        Etiam rhoncus...
      </p>
      <a href="javascript: void(0);" class="btn btn-outline-primary">
        View Statements
        <i class="mdi mdi-arrow-right ml-2"></i>
      </a>
    </div>
    <apexchart
      height="317"
      type="line"
      class="apex-charts mt-3"
      :series="series"
      :options="chartOptions"
    ></apexchart>
  </div>
  <!-- end card-body -->
</template>