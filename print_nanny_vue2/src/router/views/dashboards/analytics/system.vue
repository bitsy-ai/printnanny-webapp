<script>
export default {
  data() {
    return {
      chartOptions: {
        labels: ['Windows', 'Macintosh', 'Linux', 'Android'],
        colors: ['#727cf5', '#0acf97', '#fa5c7c', '#ffbc00'],
        plotOptions: {
          radialBar: {
            dataLabels: {
              name: {
                fontSize: '22px',
              },
              value: {
                fontSize: '16px',
              },
              total: {
                show: true,
                label: 'OS',
                formatter: function(w) {
                  // By default this function returns the average of all series. The below is just an example to show the use of custom formatter function
                  return 8541
                },
              },
            },
          },
        },
      },
      series: [44, 55, 67, 83],
    }
  },
}
</script>

<template>
  <div class="card">
    <div class="card-body">
      <div class="dropdown float-right">
        <a
          href="#"
          class="dropdown-toggle arrow-none card-drop p-0"
          data-toggle="dropdown"
          aria-expanded="false"
        >
          <i class="mdi mdi-dots-vertical"></i>
        </a>
        <div class="dropdown-menu dropdown-menu-right">
          <a href="javascript:void(0);" class="dropdown-item">Refresh Report</a>
          <a href="javascript:void(0);" class="dropdown-item">Export Report</a>
        </div>
      </div>
      <h4 class="header-title">Sessions by Operating System</h4>

      <!-- <div id="sessions-os" class="apex-charts mt-3" data-colors="#727cf5,#0acf97,#fa5c7c,#ffbc00"></div> -->
      <apexchart
        height="304"
        type="radialBar"
        class="apex-charts mt-3"
        :series="series"
        :options="chartOptions"
      ></apexchart>

      <div class="row text-center mt-2">
        <div class="col-6">
          <h4 class="font-weight-normal">
            <span>6,510</span>
          </h4>
          <p class="text-muted mb-0">Online System</p>
        </div>
        <div class="col-6">
          <h4 class="font-weight-normal">
            <span>2,031</span>
          </h4>
          <p class="text-muted mb-0">Offline System</p>
        </div>
      </div>
    </div>
    <!-- end card-body-->
  </div>
  <!-- end card-->
</template>