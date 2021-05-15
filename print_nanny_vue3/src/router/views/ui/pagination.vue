<script>
import appConfig from '@src/app.config'
import Layout from '@layouts/main'
import PageHeader from '@components/page-header'

/**
 * Pagination component
 */
export default {
  page: {
    title: 'Pagination',
    meta: [{ name: 'description', content: appConfig.description }],
  },
  components: { Layout, PageHeader },
  data() {
    return {
      title: 'Pagination',
      items: [
        {
          text: 'Hyper',
          href: '/',
        },
        {
          text: 'Base UI',
          href: '/',
        },
        {
          text: 'Pagination',
          active: true,
        },
      ],
      roundedPage: 2,
    }
  },
}
</script>

<template>
  <Layout>
    <PageHeader :title="title" :items="items" />
    <div class="row">
      <div class="col-xl-6">
        <div class="card">
          <div class="card-body">
            <h4 class="header-title">Default Pagination</h4>
            <p
              class="text-muted font-14 mb-3"
            >Simple pagination inspired by Rdio, great for apps and search results.</p>
            <b-pagination :v-model="2" :total-rows="5" :per-page="1" aria-controls="my-table"></b-pagination>
          </div>
          <!-- end card-body -->
        </div>
        <!-- end card -->
        <div class="card">
          <div class="card-body">
            <h4 class="header-title">Alignment</h4>
            <p
              class="text-muted font-14 mb-3"
            >Change the alignment of pagination components with flexbox utilities.</p>
            <b-pagination :total-rows="3" :per-page="1" align="center"></b-pagination>
            <div class="mt-3">
              <b-pagination :total-rows="3" :per-page="1" align="end"></b-pagination>
            </div>
          </div>
          <!-- end card-body -->
        </div>
        <!-- end card -->
      </div>
      <!-- end col -->

      <div class="col-xl-6">
        <div class="card">
          <div class="card-body">
            <h4 class="header-title">Rounded Pagination</h4>
            <p class="text-muted font-14 mb-3">
              Add
              <code>.pagination-rounded</code> for rounded pagination.
            </p>
            <b-pagination
              v-model="roundedPage"
              pills
              :total-rows="5"
              :per-page="1"
              class="pagination-rounded"
            ></b-pagination>
          </div>
          <!-- end card-body -->
        </div>
        <!-- end card -->
        <div class="card">
          <div class="card-body">
            <h4 class="header-title">Sizing</h4>
            <p class="text-muted font-14 mb-3">
              Add size
              <code>lg</code> or
              <code>sm</code> for additional sizes.
            </p>
            <b-pagination :total-rows="3" :per-page="1" size="lg"></b-pagination>
            <b-pagination :total-rows="3" :per-page="1" size="sm"></b-pagination>
          </div>
          <!-- end card-body -->
        </div>
        <!-- end card -->
      </div>
      <!-- end col -->
    </div>
    <!-- end row -->
  </Layout>
</template>