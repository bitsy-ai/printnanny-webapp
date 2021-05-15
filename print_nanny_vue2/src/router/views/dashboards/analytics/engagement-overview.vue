<script>
export default {
  data() {
    return {
      engagementData: [
        {
          duration: '0-30',
          sessions: 2250,
          views: 4250,
        },
        {
          duration: '31-60',
          sessions: 1501,
          views: 2050,
        },
        {
          duration: '61-120',
          sessions: 750,
          views: 1600,
        },
        {
          duration: '121-240',
          sessions: 540,
          views: 1040,
        },
      ],
    }
  },
}
</script>

<template>
  <div class="card">
    <div class="card-body">
      <a href class="p-0 float-right mb-3">
        Export
        <i class="mdi mdi-download ml-1"></i>
      </a>
      <h4 class="header-title mt-1">Engagement Overview</h4>

      <b-table-simple responsive centered class="table-sm mb-0 font-14">
        <b-thead thread-variant="light">
          <b-tr>
            <b-th>Duration (Secs)</b-th>
            <b-th style="width: 30%;">Sessions</b-th>
            <b-th style="width: 30%;">Views</b-th>
          </b-tr>
        </b-thead>
        <b-tbody>
          <b-tr v-for="data of engagementData" :key="data.duration">
            <b-td>{{data.duration}}</b-td>
            <b-td>{{data.sessions}}</b-td>
            <b-td>{{data.views}}</b-td>
          </b-tr>
        </b-tbody>
      </b-table-simple>
      <!-- end table -->
    </div>
    <!-- end card-body-->
  </div>
  <!-- end card-->
</template>