<script>
import Layout from '@layouts/main'

export default {
  page: {
    title: 'Loading page...',
    meta: [{ name: 'description', content: 'Loading page...' }],
  },
  name: 'Loading',
  components: { Layout },
}
</script>

<template>
  <Layout>
    <!-- Pre-loader -->
    <div class="preloader">
      <div id="status">
        <b-spinner style="width: 3rem; height: 3rem;" label="Large Spinner" variant="primary"></b-spinner>
      </div>
    </div>
    <!-- End Preloader -->
  </Layout>
</template>
