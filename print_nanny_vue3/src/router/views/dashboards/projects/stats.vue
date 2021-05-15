<script>
export default {
  data() {
    return {
      statData: [
        {
          icon: 'dripicons-briefcase',
          value: '29',
          text: 'Total Projects',
        },
        {
          icon: 'dripicons-checklist',
          value: '715',
          text: 'Total Tasks',
        },
        {
          icon: 'dripicons-user-group',
          value: '31',
          text: 'Members',
        },
        {
          icon: 'dripicons-graph-line',
          value: '93%',
          text: 'Productivity',
        },
      ],
    }
  },
}
</script>

<template>
  <div class="card widget-inline">
    <div class="card-body p-0">
      <div class="row no-gutters">
        <div v-for="data of statData" :key="data.text" class="col-sm-6 col-xl-3">
          <div class="card shadow-none m-0 border-left">
            <div class="card-body text-center">
              <i :class="`${data.icon} text-muted`" style="font-size: 24px;"></i>
              <h3>
                <span>{{ data.value }}</span>
              </h3>
              <p class="text-muted font-15 mb-0">{{ data.text }}</p>
            </div>
          </div>
        </div>
      </div>
      <!-- end row -->
    </div>
    <!-- end card-body -->
  </div>
  <!-- end card-->
</template>