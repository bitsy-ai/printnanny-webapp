<script>
import barChart from './bar-chart'

export default {
  components: { barChart },
}
</script>
<template>
  <!-- Chart-->
  <div class="card">
    <div class="card-body">
      <h4 class="header-title mb-3">Orders & Revenue</h4>
      <div class="chartjs-chart">
        <barChart :height="260" />
      </div>
    </div>
  </div>
  <!-- End Chart-->
</template>