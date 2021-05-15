<script>
export default {
  data() {
    return {
      channelData: [
        {
          name: 'Direct',
          visits: 2050,
          progressValue: 65,
          color: 'primary',
        },
        {
          name: 'Organic Search',
          visits: 1405,
          progressValue: 45,
          color: 'info',
        },
        {
          name: 'Refferal',
          visits: 750,
          progressValue: 30,
          color: 'warning',
        },
        {
          name: 'Social',
          visits: 540,
          progressValue: 25,
          color: 'danger',
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
      <h4 class="header-title mt-1">Channels</h4>

      <b-table-simple responsive centered class="table-sm mb-0 font-14">
        <b-thead head-variant="light">
          <b-tr>
            <b-th>Channel</b-th>
            <b-th>Visits</b-th>
            <b-th style="width: 40%;"></b-th>
          </b-tr>
        </b-thead>
        <b-tbody>
          <b-tr v-for="channel of channelData" :key="channel.name">
            <b-td>{{ channel.name }}</b-td>
            <b-td>{{ channel.visits }}</b-td>
            <b-td>
              <b-progress
                height="3px"
                class="mt-2"
                :value="channel.progressValue"
                :variant="channel.color"
              ></b-progress>
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