<script>
export default {
  data() {
    return {
      statData: [
        {
          title: 'Orders',
          value: '1,587',
          icon: 'dripicons-basket',
          percentage: '+11%',
          text: 'From previous period',
        },
        {
          title: 'Revenue',
          value: '$46,782',
          icon: 'dripicons-box',
          percentage: '-29%',
          text: 'From previous period',
        },
        {
          title: 'Product Sold',
          value: '1,890',
          icon: 'dripicons-jewel',
          percentage: '+89%',
          text: 'Last year',
        },
      ],
    }
  },
}
</script>

<template>
  <div class="row">
    <div v-for="stat of statData" :key="stat.title" class="col-sm-4">
      <div class="card tilebox-one">
        <div class="card-body">
          <i :class="`${stat.icon} float-right text-muted`"></i>
          <h6 class="text-muted text-uppercase mt-0">{{stat.title}}</h6>
          <h2 class="m-b-20">{{stat.value}}</h2>
          <span class="badge badge-primary" :class="{ 'badge-danger': stat.percentage === '-29%' }">{{stat.percentage}}</span>
          <span class="text-muted"> {{stat.text}}</span>
        </div>
        <!-- end card-body-->
      </div>
      <!--end card-->
    </div>
    <!-- end col -->
  </div>
  <!-- end row -->
</template>