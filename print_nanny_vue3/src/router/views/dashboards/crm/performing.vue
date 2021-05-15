<script>
export default {
  data() {
    return {
      performingData: [
        {
          name: 'Jeremy Young',
          leads: 187,
          deals: 154,
          tasks: 49,
        },
        {
          name: 'Thomas Krueger',
          leads: 235,
          deals: 127,
          tasks: 83,
        },
        {
          name: 'Pete Burdine',
          leads: 365,
          deals: 148,
          tasks: 62,
        },
        {
          name: 'Mary Nelson',
          leads: 735,
          deals: 159,
          tasks: 283,
        },
        {
          name: 'Kevin Grove',
          leads: 458,
          deals: 126,
          tasks: 73,
        },
      ],
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
          <a href="javascript:void(0);" class="dropdown-item">Settings</a>
          <!-- item-->
          <a href="javascript:void(0);" class="dropdown-item">Action</a>
        </b-dropdown>
      </div>
      <h4 class="header-title mb-3">Top Performing</h4>

      <div class="table-responsive mb-0">
        <table class="table table-striped table-sm table-nowrap table-centered mb-0">
          <thead>
            <tr>
              <th>User</th>
              <th>Leads</th>
              <th>Deals</th>
              <th>Tasks</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="data of performingData" :key="data.name">
              <td>
                <h5 class="font-15 mb-1 font-weight-normal">{{ data.name }}</h5>
                <span class="text-muted font-13">Senior Sales Executive</span>
              </td>
              <td>{{ data.leads }}</td>
              <td>{{ data.deals }}</td>
              <td>{{ data.tasks }}</td>
              <td class="table-action">
                <a href="javascript: void(0);" class="action-icon">
                  <i class="mdi mdi-eye"></i>
                </a>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
      <!-- end table-responsive-->
    </div>
    <!-- end card-body-->
  </div>
  <!-- end card-->
</template>