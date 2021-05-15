<script>
export default {
  data() {
    return {
      leadsData: [
        {
          image: require('@assets/images/users/avatar-2.jpg'),
          name: 'Risa Pearson',
          email: 'richard.john@mail.com',
          status: 'Cold lead',
        },
        {
          image: require('@assets/images/users/avatar-3.jpg'),
          name: 'Margaret D. Evans',
          email: 'margaret.evans@rhyta.com',
          status: 'Lost lead',
        },
        {
          image: require('@assets/images/users/avatar-4.jpg'),
          name: 'Bryan J. Luellen',
          email: 'bryuellen@dayrep.com',
          status: 'Won lead',
        },
        {
          image: require('@assets/images/users/avatar-5.jpg'),
          name: 'Kathryn S. Collier',
          email: 'collier@jourrapide.com',
          status: 'Cold lead',
        },
        {
          image: require('@assets/images/users/avatar-1.jpg'),
          name: 'Timothy Kauper',
          email: 'thykauper@rhyta.com',
          status: 'Cold lead',
        },
        {
          image: require('@assets/images/users/avatar-6.jpg'),
          name: 'Zara Raws',
          email: 'austin@dayrep.com',
          status: 'Won lead',
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
      <h4 class="header-title mb-4">Recent Leads</h4>

      <div v-for="leads of leadsData" :key="leads.name" class="media mt-3">
        <img
          class="mr-3 rounded-circle"
          :src="`${leads.image}`"
          width="40"
          alt="Generic placeholder image"
        />
        <div class="media-body">
          <span
            class="badge float-right"
            :class="{ 'badge-success-lighten': `${leads.status}` === 'Won lead',
            'badge-danger-lighten': `${leads.status}` === 'Lost lead',
            'badge-warning-lighten': `${leads.status}` === 'Cold lead' }"
          >{{ leads.status }}</span>
          <h5 class="mt-0 mb-1">{{ leads.name }}</h5>
          <span class="font-13">{{ leads.email }}</span>
        </div>
      </div>
      <!-- end media -->
    </div>
    <!-- end card-body -->
  </div>
  <!-- end card-->
</template>