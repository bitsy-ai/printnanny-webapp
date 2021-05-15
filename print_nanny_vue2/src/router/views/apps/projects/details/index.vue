<script>
import appConfig from '@src/app.config'
import Layout from '@layouts/main'
import PageHeader from '@components/page-header'

import Design from './design'
import Files from './files'
import LineChart from './line-chart'
import Comments from './comments'

export default {
  page: {
    title: 'Project Details',
    meta: [{ name: 'description', content: appConfig.description }],
  },
  components: {
    Layout,
    PageHeader,
    Design,
    Files,
    LineChart,
    Comments,
  },
  data() {
    return {
      title: 'Project Details',
      items: [
        {
          text: 'Hyper',
          href: '/',
        },
        {
          text: 'Projects',
          href: '/',
        },
        {
          text: 'Project Details',
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
      <div class="col-xl-8 col-lg-6">
        <Design />
        <Comments />
      </div>
      <div class="col-lg-6 col-xl-4">
        <div class="card">
          <div class="card-body">
            <h5 class="card-title mb-3">Progress</h5>
            <div class="mt-3 chartjs-chart" style="height: 320px;">
              <LineChart :height="320" />
            </div>
          </div>
        </div>
        <!-- end card-->
        <Files />
      </div>
    </div>
  </Layout>
</template>