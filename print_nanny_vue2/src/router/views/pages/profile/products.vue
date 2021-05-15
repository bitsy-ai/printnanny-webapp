<script>
export default {}
</script>

<template>
  <div class="card">
    <div class="card-body">
      <h4 class="header-title mb-3">My Products</h4>
      <b-table-simple class="table-centered mb-0" hover responsive>
        <b-thead>
          <b-tr>
            <b-th>Product</b-th>
            <b-th>Price</b-th>
            <b-th>Stock</b-th>
            <b-th>Amount</b-th>
          </b-tr>
        </b-thead>
        <b-tbody>
          <b-tr>
            <b-td>ASOS Ridley High Waist</b-td>
            <b-td>$79.49</b-td>
            <b-td>
              <span class="badge badge-primary">82 Pcs</span>
            </b-td>
            <b-td>$6,518.18</b-td>
          </b-tr>
          <b-tr>
            <b-td>Marco Lightweight Shirt</b-td>
            <b-td>$128.50</b-td>
            <b-td>
              <span class="badge badge-primary">37 Pcs</span>
            </b-td>
            <b-td>$4,754.50</b-td>
          </b-tr>
          <b-tr>
            <b-td>Half Sleeve Shirt</b-td>
            <b-td>$39.99</b-td>
            <b-td>
              <span class="badge badge-primary">64 Pcs</span>
            </b-td>
            <b-td>$2,559.36</b-td>
          </b-tr>
          <b-tr>
            <b-td>Lightweight Jacket</b-td>
            <b-td>$20.00</b-td>
            <b-td>
              <span class="badge badge-primary">184 Pcs</span>
            </b-td>
            <b-td>$3,680.00</b-td>
          </b-tr>
          <b-tr>
            <b-td>Marco Shoes</b-td>
            <b-td>$28.49</b-td>
            <b-td>
              <span class="badge badge-primary">69 Pcs</span>
            </b-td>
            <b-td>$1,965.81</b-td>
          </b-tr>
        </b-tbody>
      </b-table-simple>
      <!-- end table responsive-->
    </div>
    <!-- end col-->
  </div>
</template>