<script>
export default {
  data() {
    return {
      activities: [
        {
          image: require('@assets/images/users/avatar-2.jpg'),
          name: 'Soren Drouin',
          date: '18 Jan 2019 11:28 pm',
          text: 'Completed "Design new idea"...',
          project: 'Hyper Mockup',
        },
        {
          image: require('@assets/images/users/avatar-6.jpg'),
          name: 'Anne Simard',
          date: '18 Jan 2019 11:09 pm',
          text: 'Assigned task "Poster illustation design"...',
          project: 'Hyper Mockup',
        },
        {
          image: require('@assets/images/users/avatar-3.jpg'),
          name: 'Nicolas Chartier',
          date: '15 Jan 2019 09:29 pm',
          text: 'Completed "Drinking bottle graphics"...',
          project: 'Web UI Design',
        },
        {
          image: require('@assets/images/users/avatar-4.jpg'),
          name: 'Gano Cloutier',
          date: '10 Jan 2019 08:36 pm',
          text: 'Completed "Design new idea"...',
          project: 'UBold Admin',
        },
        {
          image: require('@assets/images/users/avatar-5.jpg'),
          name: 'Francis Achin',
          date: '08 Jan 2019 12:28 pm',
          text: 'Assigned task "Hyper app design"...',
          project: 'Website Mockup',
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
      <h4 class="header-title mb-3">Recent Activities</h4>

      <div class="table-responsive mb-0">
        <table class="table table-centered table-nowrap table-hover">
          <tbody>
            <tr v-for="activity of activities" :key="activity.name">
              <td>
                <div class="media">
                  <img
                    class="mr-2 rounded-circle"
                    :src="`${activity.image}`"
                    width="40"
                    alt="Generic placeholder image"
                  />
                  <div class="media-body">
                    <h5 class="mt-0 mb-1">
                      {{ activity.name }}
                      <small class="font-weight-normal ml-3">{{ activity.date }}</small>
                    </h5>
                    <span class="font-13">{{ activity.text }}</span>
                  </div>
                </div>
              </td>
              <td>
                <span class="text-muted font-13">Project</span>
                <br />
                <p class="mb-0">{{ activity.project }}</p>
              </td>
              <td class="table-action" style="width: 50px;">
                <b-dropdown toggle-class="arrow-none card-drop p-0" variant="black" right>
                  <template v-slot:button-content>
                    <i class="mdi mdi-dots-horizontal"></i>
                  </template>
                  <!-- item-->
                  <a href="javascript:void(0);" class="dropdown-item">Settings</a>
                  <!-- item-->
                  <a href="javascript:void(0);" class="dropdown-item">Action</a>
                </b-dropdown>
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