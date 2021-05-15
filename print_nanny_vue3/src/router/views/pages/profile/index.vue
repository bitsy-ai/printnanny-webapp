<script>
import appConfig from '@src/app.config'
import Layout from '@layouts/main'
import PageHeader from '@components/page-header'

import Profile from '@components/widgets/profile'
import Message from '@components/widgets/message'

import Orders from './orders'
import Seller from './seller'
import Stats from './stats'
import Products from './products'

/**
 * Profile component
 */
export default {
  page: {
    title: 'Profile',
    meta: [{ name: 'description', content: appConfig.description }],
  },
  components: {
    Layout,
    PageHeader,
    Profile,
    Message,
    Orders,
    Seller,
    Stats,
    Products,
  },
  data() {
    return {
      title: 'Profile',
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
          text: 'Profile',
          active: true,
        },
      ],
      messages: [
        {
          image: require('@assets/images/users/avatar-2.jpg'),
          name: 'Tomaslau',
          message: "I've finished it! See you so...",
        },
        {
          image: require('@assets/images/users/avatar-3.jpg'),
          name: 'Stillnotdavid',
          message: 'This theme is awesome!',
        },
        {
          image: require('@assets/images/users/avatar-4.jpg'),
          name: 'Kurafire',
          message: 'Nice to meet you',
        },
        {
          image: require('@assets/images/users/avatar-5.jpg'),
          name: 'Shahedk',
          message: "Hey! there I'm available...",
        },
        {
          image: require('@assets/images/users/avatar-6.jpg'),
          name: 'Adhamdannaway',
          message: 'This theme is awesome!',
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
      <div class="col-sm-12">
        <div class="card bg-primary">
          <div class="card-body profile-user-box">
            <div class="row">
              <div class="col-sm-8">
                <Profile />
              </div>
              <!-- end col-->

              <div class="col-sm-4">
                <div class="text-center mt-sm-0 mt-3 text-sm-right">
                  <button type="button" class="btn btn-light">
                    <i class="mdi mdi-account-edit mr-1"></i> Edit Profile
                  </button>
                </div>
              </div>
              <!-- end col-->
            </div>
            <!-- end row -->
          </div>
          <!-- end card-body/ profile-user-box-->
        </div>
      </div>
    </div>
    <div class="row">
      <div class="col-lg-4">
        <Seller />
        <!-- Toll free number box-->
        <div class="card text-white bg-info overflow-hidden">
          <div class="card-body">
            <div class="toll-free-box text-center">
              <h4>
                <i class="mdi mdi-deskphone"></i> Toll Free : 1-234-567-8901
              </h4>
            </div>
          </div>
          <!-- end card-body-->
        </div>
        <Message :messages="messages" />
      </div>
      <div class="col-lg-8">
        <Orders />
        <Stats />
        <Products />
      </div>
    </div>
  </Layout>
</template>