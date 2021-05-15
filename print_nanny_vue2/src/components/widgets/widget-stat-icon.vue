<script>
/**
 * A simple widget with icon
 * 1. Widget icon name specify using the 'icon' input property
 * 2. Widget title specify the widget data are belongs to title.
 * 3. widget 'number' property specify the value of title such as progress or sales etc., that depends on title.
 * 4. widget trend color specify using the 'color' input property.
 * 5. widget trend specify using the 'subtext' input property. Trend value consider on title.
 */
export default {
  props: {
    icon: {
      type: String,
      default: '',
    },
    title: {
      type: String,
      default: '',
    },
    number: {
      type: String,
      default: '',
    },
    color: {
      type: String,
      default: 'success',
    },
    subtext: {
      type: String,
      default: '',
    },
  },
}
</script>

<template>
  <div class="card widget-flat">
    <div class="card-body">
      <div class="float-right">
        <i :class="`mdi ${icon} widget-icon`"></i>
      </div>
      <h5 class="text-muted font-weight-normal mt-0" title="Number of Customers">{{ title }}</h5>
      <h3 class="mt-3 mb-3">{{ number }}</h3>
      <p class="mb-0 text-muted">
        <span :class="`text-${color} mr-2`">
          <i
            :class=" { 'mdi mdi-arrow-down-bold': `${color}` === 'danger' ,
          'mdi mdi-arrow-up-bold': `${color}` === 'success' }"
          ></i>
          {{subtext}}
        </span>
        <span class="text-nowrap">Since last month</span>
      </p>
    </div>
    <!-- end card-body-->
  </div>
  <!-- end card -->
</template>