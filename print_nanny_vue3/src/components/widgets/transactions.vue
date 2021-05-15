<script>
import simplebar from 'simplebar-vue'

/**
 * Transactions component
 * 1. User specifies the title of window using the 'title' input property.
 * 2. Window height set using the 'transactionWindowHeight' input property. Height would count in pixel.
 * 3. Transactions array specify - title, icon, date, amount and color.
 *     title - the transaction name specify in title
 *     icon - icon name specify using
 *     date - Transaction which day done specify using date.
 *     amount - transaction amount specify using the
 *     color - Icon and amount color specify using color. Success defines the profit and danger define the loss.
 */
export default {
  components: {
    simplebar,
  },
  props: {
    title: {
      type: String,
      default: 'Transactions',
    },
    transactionWindowHeight: {
      type: String,
      default: '320px',
    },
    transactions: {
      type: Array,
      default: function() {
        return []
      },
    },
  },
}
</script>

<template>
  <div class="card">
    <div class="card-body">
      <div class="dropdown float-right">
        <b-dropdown toggle-class="arrow-none card-drop p-0" variant="white" right>
          <template v-slot:button-content>
            <i class="mdi mdi-dots-vertical"></i>
          </template>
          <!-- item-->
          <a href="javascript:void(0);" class="dropdown-item">Settings</a>
          <!-- item-->
          <a href="javascript:void(0);" class="dropdown-item">Action</a>
        </b-dropdown>
      </div>
      <h4 class="header-title mb-3">{{ title }}</h4>

      <simplebar :style="`max-height:${transactionWindowHeight}`">
        <div v-for="data of transactions" :key="data.title" class="row py-1 align-items-center">
          <div class="col-auto">
            <i :class="`mdi ${data.icon} text-${data.color} font-18`"></i>
          </div>
          <div class="col pl-0">
            <a href="javascript:void(0);" class="text-body">{{data.title}}</a>
            <p class="mb-0 text-muted">
              <small>{{data.date}}</small>
            </p>
          </div>
          <div class="col-auto">
            <span :class="`text-${data.color} font-weight-bold pr-2`">{{data.amount }}</span>
          </div>
        </div>
      </simplebar>
    </div>
    <!-- end card-body -->
  </div>
  <!-- end card -->
</template>