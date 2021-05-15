<script>
import appConfig from '@src/app.config'
import Layout from '@layouts/main'
import PageHeader from '@components/page-header'

import UserCard from './user-card'
import Messages from './messages'
import About from './about'
import Timeline from './timeline'
import Settings from './settings'

/**
 * Profile 2 component
 */
export default {
  page: {
    title: 'Profile 2',
    meta: [{ name: 'description', content: appConfig.description }],
  },
  components: {
    Layout,
    PageHeader,
    UserCard,
    Messages,
    About,
    Timeline,
    Settings,
  },
  data() {
    return {
      title: 'Profile 2',
      items: [
        {
          text: 'Hyper',
          href: '/',
        },
        {
          text: 'Pages',
          href: '/',
        },
        {
          text: 'Profile 2',
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
      <div class="col-xl-4 col-lg-5">
        <UserCard />
        <Messages />
      </div>
      <!-- end col -->
      <div class="col-lg-8 col-xl-8">
        <div class="card">
          <div class="card-body">
            <b-tabs content-class="mt-1" pills justified nav-class="bg-nav-pills">
              <b-tab title="About" title-link-class="rounded-0">
                <About />
              </b-tab>
              <b-tab active title="Timeline" title-link-class="rounded-0">
                <Timeline />
              </b-tab>
              <b-tab title="Settings" title-link-class="rounded-0">
                <Settings />
              </b-tab>
            </b-tabs>
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