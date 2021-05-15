<script>
import appConfig from '@src/app.config'
import Layout from '@layouts/main'
import PageHeader from '@components/page-header'

import ChatUser from './chat-user'
import ChatArea from './chat-area'
import ChatProfile from './chat-profile'

/**
 * Chat Component
 */
export default {
  page: {
    title: 'Chat',
    meta: [{ name: 'description', content: appConfig.description }],
  },
  components: {
    Layout,
    PageHeader,
    ChatUser,
    ChatArea,
    ChatProfile,
  },
  data() {
    return {
      title: 'Chat',
      items: [
        {
          text: 'Hyper',
          href: '/',
        },
        {
          text: 'Chat',
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
      <!-- start chat users-->
      <div class="col-xl-3 col-lg-6 order-lg-1 order-xl-1">
        <ChatUser />
      </div>
      <div class="col-xl-6 col-lg-12 order-lg-2 order-xl-1">
        <ChatArea />
      </div>
      <div class="col-xl-3 col-lg-6 order-lg-1 order-xl-2">
        <ChatProfile />
      </div>
    </div>
  </Layout>
</template>