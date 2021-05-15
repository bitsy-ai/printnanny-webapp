<script>

/**
 * Profile-widget component
 * 1. User may specify the text color of widget while using in another component. Ex. black, white etc. 
 */
export default {
  props: {
    textColor: {
      type: String,
      default: 'white',
    },
  },
}
</script>

<template>
  <div class="media">
    <span class="float-left m-2 mr-4">
      <img
        src="@assets/images/users/avatar-2.jpg"
        style="height: 100px;"
        alt
        class="rounded-circle img-thumbnail"
      />
    </span>
    <div class="media-body">
      <h4 :class="`mt-1 mb-1 text-${textColor}`">Michael Franklin</h4>
      <p :class="`font-13 text-${textColor}-50`">Authorised Brand Seller</p>

      <ul :class="`mb-0 list-inline text-${textColor}`">
        <li class="list-inline-item mr-3">
          <h5 class="mb-1">$ 25,184</h5>
          <p :class="`mb-0 font-13 text-${textColor}`">Total Revenue</p>
        </li>
        <li class="list-inline-item">
          <h5 class="mb-1">5482</h5>
          <p :class="`mb-0 font-13 text-${textColor}`">Number of Orders</p>
        </li>
      </ul>
    </div>
    <!-- end media-body-->
  </div>
  <!-- end media -->
</template>