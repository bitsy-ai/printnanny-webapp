<script>
import appConfig from '@src/app.config'
import Layout from '@layouts/main'
import PageHeader from '@components/page-header'

/**
 * Avatars component
 */
export default {
  page: {
    title: 'Avatars',
    meta: [{ name: 'description', content: appConfig.description }],
  },
  components: { Layout, PageHeader },
  data() {
    return {
      title: 'Avatars',
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
          text: 'Avatars',
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
      <div class="col-xl-6">
        <div class="card">
          <div class="card-body">
            <h4 class="header-title">Sizing - Images</h4>
            <p class="text-muted font-14 mb-3">
              Create and group avatars of different sizes and shapes with the css classes.
              Using Bootstrap's naming convention, you can control size of avatar including standard avatar, or scale it up to different sizes.
            </p>
            <div class="row">
              <div class="col-md-3">
                <b-img
                  :src="require('@assets/images/users/avatar-2.jpg')"
                  fluid
                  rounded
                  class="avatar-xs"
                  alt="image"
                ></b-img>

                <p>
                  <code>.avatar-xs</code>
                </p>
                <b-img
                  :src="require('@assets/images/users/avatar-3.jpg')"
                  fluid
                  rounded
                  class="avatar-sm mt-2"
                  alt="image"
                ></b-img>

                <p class="mb-2 mb-sm-0">
                  <code>.avatar-sm</code>
                </p>
              </div>
              <div class="col-md-3">
                <b-img
                  :src="require('@assets/images/users/avatar-4.jpg')"
                  fluid
                  rounded
                  class="avatar-md"
                  alt="image"
                ></b-img>

                <p>
                  <code>.avatar-md</code>
                </p>
              </div>

              <div class="col-md-3">
                <b-img
                  :src="require('@assets/images/users/avatar-5.jpg')"
                  fluid
                  rounded
                  class="avatar-lg"
                  alt="image"
                ></b-img>
                <p>
                  <code>.avatar-lg</code>
                </p>
              </div>

              <div class="col-md-3">
                <b-img
                  :src="require('@assets/images/users/avatar-6.jpg')"
                  fluid
                  rounded
                  class="avatar-xl"
                  alt="image"
                ></b-img>

                <p class="mb-0">
                  <code>.avatar-xl</code>
                </p>
              </div>
            </div>
            <!-- end row-->
          </div>
          <!-- end card-body -->
        </div>
        <!-- end card -->
      </div>
      <!-- end col-->
      <div class="col-xl-6">
        <div class="card">
          <div class="card-body">
            <h4 class="header-title">Rounded Circle</h4>
            <p class="text-muted font-14 mb-3">
              Using an additional class
              <code>rounded='circle'</code> in
              <code>&lt;img&gt;</code> element creates the rounded avatar.
            </p>
            <div class="row">
              <div class="col-md-4">
                <b-img
                  :src="require('@assets/images/users/avatar-7.jpg')"
                  fluid
                  rounded="circle"
                  class="avatar-md"
                  alt="image"
                ></b-img>
                <p class="mt-1">
                  <code>.avatar-md .rounded-circle</code>
                </p>
              </div>

              <div class="col-md-4">
                <b-img
                  :src="require('@assets/images/users/avatar-8.jpg')"
                  fluid
                  rounded="circle"
                  class="avatar-lg"
                  alt="image"
                ></b-img>
                <p>
                  <code>.avatar-lg .rounded-circle</code>
                </p>
              </div>

              <div class="col-md-4">
                <b-img
                  :src="require('@assets/images/users/avatar-9.jpg')"
                  fluid
                  rounded="circle"
                  class="avatar-xl"
                  alt="image"
                ></b-img>
                <p class="mb-0">
                  <code>.avatar-xl .rounded-circle</code>
                </p>
              </div>
            </div>
            <!-- end row-->
          </div>
          <!-- end card-body -->
        </div>
        <!-- end card -->
      </div>
      <!-- end col-->
    </div>
    <!-- end row -->

    <div class="row">
      <div class="col-12">
        <div class="card">
          <div class="card-body">
            <h4 class="header-title">Images shapes</h4>
            <p class="text-muted font-14 mb-3">Avatars with different sizes and shapes.</p>

            <div class="row">
              <div class="col-sm-2">
                <b-img
                  :src="require('@assets/images/small/small-2.jpg')"
                  fluid
                  rounded
                  alt="image"
                  width="200"
                ></b-img>

                <p class="mb-0">
                  <code>.rounded</code>
                </p>
              </div>

              <div class="col-sm-2 text-center">
                <b-img
                  :src="require('@assets/images/users/avatar-6.jpg')"
                  fluid
                  rounded
                  alt="image"
                  width="120"
                ></b-img>
                <p class="mb-0">
                  <code>.rounded</code>
                </p>
              </div>

              <div class="col-sm-2 text-center">
                <b-img
                  :src="require('@assets/images/users/avatar-7.jpg')"
                  fluid
                  rounded="circle"
                  alt="image"
                  width="120"
                ></b-img>
                <p class="mb-0">
                  <code>.rounded-circle</code>
                </p>
              </div>

              <div class="col-sm-2">
                <b-img
                  :src="require('@assets/images/small/small-3.jpg')"
                  fluid
                  thumbnail
                  alt="image"
                  width="200"
                ></b-img>
                <p class="mb-0">
                  <code>.img-thumbnail</code>
                </p>
              </div>
              <div class="col-sm-2">
                <b-img
                  :src="require('@assets/images/users/avatar-8.jpg')"
                  fluid
                  thumbnail
                  rounded="circle"
                  alt="image"
                  width="120"
                ></b-img>
                <p class="mb-0">
                  <code>.rounded-circle .img-thumbnail</code>
                </p>
              </div>
            </div>
            <!-- end row-->
          </div>
          <!-- end card-body -->
        </div>
        <!-- end card -->
      </div>
      <!-- end col-->
    </div>
    <!-- end row -->
  </Layout>
</template>