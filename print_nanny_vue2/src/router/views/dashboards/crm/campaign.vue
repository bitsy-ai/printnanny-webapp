<script>
export default {
  data() {
    return {
      series: [86, 36, 50],
      chartOptions: {
        labels: ['Total Sent', 'Reached', 'Opened'],
        colors: ['#ffbc00', '#727cf5', '#0acf97'],
        plotOptions: {
          radialBar: {
            track: {
              margin: 8,
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
          <a href="javascript:void(0);" class="dropdown-item">Today</a>
          <!-- item-->
          <a href="javascript:void(0);" class="dropdown-item">Yesterday</a>
          <!-- item-->
          <a href="javascript:void(0);" class="dropdown-item">Last Week</a>
          <!-- item-->
          <a href="javascript:void(0);" class="dropdown-item">Last Month</a>
        </b-dropdown>
      </div>
      <h4 class="header-title mb-1">Campaigns</h4>
      <apexchart type="radialBar" height="339" :series="series" :options="chartOptions"></apexchart>

      <div class="row text-center mt-2">
        <div class="col-md-4">
          <i class="mdi mdi-send widget-icon rounded-circle bg-light-lighten text-muted"></i>
          <h3 class="font-weight-normal mt-3">
            <span>6,510</span>
          </h3>
          <p class="text-muted mb-0 mb-2">
            <i class="mdi mdi-checkbox-blank-circle text-warning"></i> Total Sent
          </p>
        </div>
        <div class="col-md-4">
          <i class="mdi mdi-flag-variant widget-icon rounded-circle bg-light-lighten text-muted"></i>
          <h3 class="font-weight-normal mt-3">
            <span>3,487</span>
          </h3>
          <p class="text-muted mb-0 mb-2">
            <i class="mdi mdi-checkbox-blank-circle text-primary"></i> Reached
          </p>
        </div>
        <div class="col-md-4">
          <i class="mdi mdi-email-open widget-icon rounded-circle bg-light-lighten text-muted"></i>
          <h3 class="font-weight-normal mt-3">
            <span>1,568</span>
          </h3>
          <p class="text-muted mb-0 mb-2">
            <i class="mdi mdi-checkbox-blank-circle text-success"></i> Opened
          </p>
        </div>
      </div>
      <!-- end row-->
    </div>
    <!-- end card-body -->
  </div>
  <!-- end card -->
</template>