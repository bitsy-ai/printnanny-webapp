<script>
import flatPickr from 'vue-flatpickr-component'

export default {
  components: {
    flatPickr,
  },
  data() {
    return {
      inlinepicker: +new Date(),
      inline: {
        inline: true,
        shorthandCurrentMonth: true,
      },
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
      <h4 class="header-title mb-3">Your Calendar</h4>

      <div class="row calendar-widget calendar-widget-inline">
        <div class="col-md-6">
          <flat-pickr v-model="inlinepicker" :config="inline"></flat-pickr>
        </div>
        <!-- end col-->
        <div class="col-md-6">
          <ul class="list-unstyled">
            <li class="mb-4">
              <p class="text-muted mb-1 font-13">
                <i class="mdi mdi-calendar"></i> 7:30 AM - 10:00 AM
              </p>
              <h5>Meeting with BD Team</h5>
            </li>
            <li class="mb-4">
              <p class="text-muted mb-1 font-13">
                <i class="mdi mdi-calendar"></i> 10:30 AM - 11:45 AM
              </p>
              <h5>Design Review - Hyper Admin</h5>
            </li>
            <li class="mb-4">
              <p class="text-muted mb-1 font-13">
                <i class="mdi mdi-calendar"></i> 12:15 PM - 02:00 PM
              </p>
              <h5>Setup Github Repository</h5>
            </li>
            <li>
              <p class="text-muted mb-1 font-13">
                <i class="mdi mdi-calendar"></i> 5:30 PM - 07:00 PM
              </p>
              <h5>Meeting with Design Studio</h5>
            </li>
          </ul>
        </div>
        <!-- end col -->
      </div>
      <!-- end row -->
    </div>
    <!-- end card body-->
  </div>
  <!-- end card -->
</template>