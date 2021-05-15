<script>
export default {
  data() {
    return {
      productsData: [
        {
          name: 'ASOS Ridley High Waist',
          date: '07 April 2018',
          price: '$79.49',
          quantity: 82,
          amount: '$6,518.18',
        },
        {
          name: 'Marco Lightweight Shirt',
          date: '25 March 2018',
          price: '$128.50',
          quantity: 37,
          amount: '$4,754.50',
        },
        {
          name: 'Half Sleeve Shirt',
          date: '17 March 2018',
          price: '$39.99',
          quantity: 64,
          amount: '$2,559.36',
        },
        {
          name: 'Lightweight Jacket',
          date: '05 March 2018',
          price: '$20.00',
          quantity: 184,
          amount: '$3,680.00',
        },
        {
          name: 'Marco Shoes',
          date: '05 March 2018',
          price: '$28.49',
          quantity: 69,
          amount: '$1,965.81',
        },
      ],
    }
  },
}
</script>

<template>
  <div class="card">
    <div class="card-body">
      <div class="float-right">
        <b-dropdown toggle-class="arrow-none card-drop p-0" variant="black" right>
          <template v-slot:button-content>
            <i class="mdi mdi-dots-vertical"></i>
          </template>
          <a href="javascript:void(0);" class="dropdown-item">Sales Report</a>
          <!-- item-->
          <a href="javascript:void(0);" class="dropdown-item">Export Report</a>
          <!-- item-->
          <a href="javascript:void(0);" class="dropdown-item">Profit</a>
          <!-- item-->
          <a href="javascript:void(0);" class="dropdown-item">Action</a>
        </b-dropdown>
      </div>
      <h4 class="header-title mb-2">Top Selling Products</h4>

      <div class="table-responsive mb-0">
        <table class="table table-centered table-nowrap table-hover mb-0 mt-2">
          <tbody>
            <tr v-for="product of productsData" :key="product.name">
              <td>
                <h5 class="font-14 mb-1 font-weight-normal">{{ product.name }}</h5>
                <span class="text-muted font-13">{{ product.date }}</span>
              </td>
              <td>
                <h5 class="font-14 mb-1 font-weight-normal">{{ product.price }}</h5>
                <span class="text-muted font-13">Price</span>
              </td>
              <td>
                <h5 class="font-14 mb-1 font-weight-normal">{{ product.quantity }}</h5>
                <span class="text-muted font-13">Quantity</span>
              </td>
              <td>
                <h5 class="font-14 mb-1 font-weight-normal">{{ product.amount }}</h5>
                <span class="text-muted font-13">Amount</span>
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