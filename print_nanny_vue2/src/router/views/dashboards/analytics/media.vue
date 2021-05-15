<script>
export default {
  data() {
    return {
      mediaData: [
        {
          network: 'Facebook',
          visits: 2250,
          progressValue: 65,
        },
        {
          network: 'Instagram',
          visits: 1501,
          progressValue: 45,
        },
        {
          network: 'Twitter',
          visits: 750,
          progressValue: 30,
        },
        {
          network: 'LinkedIn',
          visits: 540,
          progressValue: 25,
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
      <h4 class="header-title mt-1">Social Media Traffic</h4>

      <b-table-simple responsive centered class="table-sm mb-0 font-14">
        <b-thead thread-variant="light">
          <b-tr>
            <b-th>Network</b-th>
            <b-th>Visits</b-th>
            <b-th style="width: 40%;"></b-th>
          </b-tr>
        </b-thead>
        <b-tbody>
          <b-tr v-for="media of mediaData" :key="media.name">
            <b-td>{{ media.network }}</b-td>
            <b-td>{{ media.visits }}</b-td>
            <b-td>
              <b-progress height="3px" class="mt-2" :value="media.progressValue"></b-progress>
            </b-td>
          </b-tr>
        </b-tbody>
      </b-table-simple>
      <!-- end table -->
    </div>
    <!-- end card-body-->
  </div>
  <!-- end card-->
</template>