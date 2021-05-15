<script>
import appConfig from '@src/app.config'
import Layout from '@layouts/main'
import PageHeader from '@components/page-header'

import Description from './description'
import Comments from './comments'
import Attachment from './attachment'

/**
 * Task Detail component
 */
export default {
  page: {
    title: 'Task Detail',
    meta: [{ name: 'description', content: appConfig.description }],
  },
  components: { Layout, PageHeader, Description, Comments, Attachment },
  data() {
    return {
      title: 'Task Detail',
      items: [
        {
          text: 'Hyper',
          href: '/',
        },
        {
          text: 'Tasks',
          href: '/',
        },
        {
          text: 'Task Detail',
          active: true,
        },
      ],
    }
  },
}
</script>

<template>
  <Layout>
    <PageHeader :title="title" :items="items" />
    <div class="row">
      <div class="col-xl-8 col-lg-7">
        <!-- project card -->
        <Description />
        <Comments />
      </div>
      <!-- end col -->

      <div class="col-xl-4 col-lg-5">
        <Attachment />
      </div>
      <!-- end col -->
    </div>
    <!-- end row -->
  </Layout>
</template>