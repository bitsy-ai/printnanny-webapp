<script>
export default {
  data() {
    return {
      tasksData: [
        {
          name: 'Coffee detail page - Main Page',
          day: 3,
          status: 'In-progress',
          assigned: 'Logan R. Cohn',
          time: '3h 20min',
        },
        {
          name: 'Drinking bottle graphics',
          day: 27,
          status: 'Outdated',
          assigned: 'Jerry F. Powell',
          time: '12h 21min',
        },
        {
          name: 'App design and development',
          day: 7,
          status: 'Completed',
          assigned: 'Scot M. Smith',
          time: '78h 05min',
        },
        {
          name: 'Poster illustation design',
          day: 5,
          status: 'In-progress',
          assigned: 'John P. Ritter',
          time: '26h 58min',
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
          <a href="javascript:void(0);" class="dropdown-item">Weekly Report</a>
          <!-- item-->
          <a href="javascript:void(0);" class="dropdown-item">Monthly Report</a>
          <!-- item-->
          <a href="javascript:void(0);" class="dropdown-item">Action</a>
          <!-- item-->
          <a href="javascript:void(0);" class="dropdown-item">Settings</a>
        </b-dropdown>
      </div>
      <h4 class="header-title mb-3">Tasks</h4>

      <p>
        <b>107</b> Tasks completed out of 195
      </p>

      <div class="table-responsive mb-0">
        <table class="table table-centered table-nowrap table-hover">
          <tbody>
            <tr v-for="task of tasksData" :key="task.name">
              <td>
                <h5 class="font-14 my-1">
                  <a href="javascript:void(0);" class="text-body">{{ task.name }}</a>
                </h5>
                <span class="text-muted font-13">Due in {{task.day}} days</span>
              </td>
              <td>
                <span class="text-muted font-13">Status</span>
                <br />
                <span
                  class="badge"
                  :class=" { 'badge-success-lighten': `${task.status}` === 'Completed',
                  'badge-danger-lighten': `${task.status}` === 'Outdated',
                  'badge-warning-lighten': `${task.status}` === 'In-progress' } "
                >{{ task.status }}</span>
              </td>
              <td>
                <span class="text-muted font-13">Assigned to</span>
                <h5 class="font-14 mt-1 font-weight-normal">{{ task.assigned }}</h5>
              </td>
              <td>
                <span class="text-muted font-13">Total time spend</span>
                <h5 class="font-14 mt-1 font-weight-normal">{{ task.time }}</h5>
              </td>
              <td class="table-action" style="width: 90px;">
                <a href="javascript: void(0);" class="action-icon">
                  <i class="mdi mdi-pencil"></i>
                </a>
                <a href="javascript: void(0);" class="action-icon">
                  <i class="mdi mdi-delete"></i>
                </a>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
      <!-- end table-responsive-->
    </div>
    <!-- end card body-->
  </div>
  <!-- end card -->
</template>