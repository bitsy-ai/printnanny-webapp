<script>
export default {
  data() {
    return {
      series: [
        {
          name: 'Sessions',
          data: [10, 20, 5, 15, 10, 20, 15, 25, 20, 30, 25, 40, 30, 50, 35],
        },
      ],
      chartOptions: {
        chart: {
          toolbar: {
            show: false,
          },
        },
        dataLabels: {
          enabled: false,
        },
        stroke: {
          curve: 'smooth',
          width: 4,
        },
        zoom: {
          enabled: false,
        },
        legend: {
          show: false,
        },
        colors: ['#0acf97'],
        xaxis: {
          type: 'string',
          tooltip: {
            enabled: false,
          },
          axisBorder: {
            show: false,
          },
          labels: {},
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
          type: 'gradient',
          gradient: {
            type: 'vertical',
            shadeIntensity: 1,
            inverseColors: false,
            opacityFrom: 0.45,
            opacityTo: 0.05,
            stops: [45, 100],
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
      <b-alert
        variant="warning"
        class="mb-3"
        show
        dismissible
      >Property HY1xx is not receiving hits. Either your site is not receiving any sessions or it is not tagged correctly.</b-alert>

      <ul class="nav float-right d-none d-lg-flex">
        <li class="nav-item">
          <a class="nav-link text-muted" href="#">Today</a>
        </li>
        <li class="nav-item">
          <a class="nav-link text-muted" href="#">7d</a>
        </li>
        <li class="nav-item">
          <a class="nav-link active" href="#">15d</a>
        </li>
        <li class="nav-item">
          <a class="nav-link text-muted" href="#">1m</a>
        </li>
        <li class="nav-item">
          <a class="nav-link text-muted" href="#">1y</a>
        </li>
      </ul>
      <h4 class="header-title mb-3">Sessions Overview</h4>

      <apexchart
        height="309"
        type="area"
        class="apex-charts mt-3"
        :series="series"
        :options="chartOptions"
      ></apexchart>
    </div>
    <!-- end card-body-->
  </div>
</template>