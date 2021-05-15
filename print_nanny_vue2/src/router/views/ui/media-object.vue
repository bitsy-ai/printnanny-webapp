<script>
import appConfig from '@src/app.config'
import Layout from '@layouts/main'
import PageHeader from '@components/page-header'

/**
 * Media Object component
 */
export default {
  page: {
    title: 'Media Object',
    meta: [{ name: 'description', content: appConfig.description }],
  },
  components: { Layout, PageHeader },
  data() {
    return {
      title: 'Media Object',
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
          text: 'Media Object',
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
            <h4 class="header-title">Default media object</h4>
            <p
              class="text-muted font-14 mb-3"
            >The default media displays a media object (images, video, audio) to the left or right of a content block.</p>
            <b-media class="mb-3">
              <template v-slot:aside>
                <b-img
                  :src="require('@assets/images/users/avatar-10.jpg')"
                  height="64"
                  rounded="circle"
                  alt="image"
                ></b-img>
              </template>
              <h5 class="mt-0">Media heading</h5>
              <p class="mb-0">
                Cras sit amet nibh libero, in gravida nulla. Nulla vel metus scelerisque ante sollicitudin.
                Cras purus odio, vestibulum in vulputate at, tempus viverra turpis. Fusce condimentum nunc
                ac nisi vulputate fringilla. Donec lacinia congue felis in faucibus.
              </p>
            </b-media>
            <b-media class="mb-3">
              <template v-slot:aside>
                <div class="avatar-md">
                  <span
                    class="avatar-title bg-success-lighten text-success font-20 rounded-circle"
                  >MD</span>
                </div>
              </template>
              <h5 class="mt-0">Media heading</h5>
              <p class="mb-0">
                Cras sit amet nibh libero, in gravida nulla. Nulla vel metus scelerisque ante sollicitudin.
                Cras purus odio, vestibulum in vulputate at, tempus viverra turpis. Fusce condimentum nunc
                ac nisi vulputate fringilla. Donec lacinia congue felis in faucibus.
              </p>
              <b-media class="mt-3">
                <template v-slot:aside>
                  <b-img
                    :src="require('@assets/images/users/avatar-3.jpg')"
                    height="64"
                    rounded="circle"
                    alt="image"
                  ></b-img>
                </template>

                <h5 class="mt-0">Media heading</h5>Cras sit amet nibh libero, in gravida nulla. Nulla vel metus scelerisque ante sollicitudin.
                Cras purus odio, vestibulum in vulputate at, tempus viverra turpis. Fusce condimentum nunc
                ac nisi vulputate fringilla. Donec lacinia congue felis in faucibus.
              </b-media>
            </b-media>
            <b-media right-align vertical-align="center">
              <template v-slot:aside>
                <b-img
                  :src="require('@assets/images/users/avatar-4.jpg')"
                  height="64"
                  rounded="circle"
                  alt="image"
                ></b-img>
              </template>
              <h5 class="mt-0 mb-1">Media object</h5>
              <p class="mb-0">
                Cras sit amet nibh libero, in gravida nulla. Nulla vel metus scelerisque ante sollicitudin.
                Cras purus odio, vestibulum in vulputate at, tempus viverra turpis. Fusce condimentum nunc ac
                nisi vulputate fringilla. Donec lacinia congue felis in faucibus.
              </p>
            </b-media>
          </div>
          <!-- end card-body -->
        </div>
        <!-- end card -->
      </div>
      <!-- end col -->

      <div class="col-xl-6">
        <div class="card">
          <div class="card-body">
            <h4 class="header-title">Media Alignment</h4>
            <p class="text-muted font-14 mb-3">
              Media in a media object can be aligned with flexbox utilities to the top (default), center, or end of your
              <code>media</code> content.
            </p>
            <ul class="list-unstyled">
              <b-media tag="li" vertical-align="top">
                <template v-slot:aside>
                  <b-img
                    :src="require('@assets/images/users/avatar-5.jpg')"
                    height="64"
                    rounded
                    alt="image"
                  ></b-img>
                </template>
                <h5 class="mt-0">Top-aligned media</h5>
                <p
                  class="mb-1"
                >Cras sit amet nibh libero, in gravida nulla. Nulla vel metus scelerisque ante sollicitudin. Cras purus odio, vestibulum in vulputate at, tempus viverra turpis. Fusce condimentum nunc ac nisi vulputate fringilla. Donec lacinia congue felis in faucibus.</p>
                <p
                  class="mb-0"
                >Donec sed odio dui. Nullam quis risus eget urna mollis ornare vel eu leo. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.</p>
              </b-media>

              <b-media tag="li" class="my-3" vertical-align="center">
                <template v-slot:aside>
                  <div class="avatar-md">
                    <span
                      class="avatar-title bg-danger-lighten text-danger font-20 rounded-circle"
                    >CA</span>
                  </div>
                </template>

                <h5 class="mt-0">Center-aligned media</h5>
                <p
                  class="mb-1"
                >Cras sit amet nibh libero, in gravida nulla. Nulla vel metus scelerisque ante sollicitudin. Cras purus odio, vestibulum in vulputate at, tempus viverra turpis. Fusce condimentum nunc ac nisi vulputate fringilla. Donec lacinia congue felis in faucibus.</p>
                <p
                  class="mb-0"
                >Donec sed odio dui. Nullam quis risus eget urna mollis ornare vel eu leo. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.</p>
              </b-media>

              <b-media tag="li" vertical-align="end">
                <template v-slot:aside>
                  <b-img
                    :src="require('@assets/images/users/avatar-7.jpg')"
                    height="64"
                    rounded
                    alt="image"
                  ></b-img>
                </template>

                <h5 class="mt-0">Bottom-aligned media</h5>
                <p
                  class="mb-1"
                >Cras sit amet nibh libero, in gravida nulla. Nulla vel metus scelerisque ante sollicitudin. Cras purus odio, vestibulum in vulputate at, tempus viverra turpis. Fusce condimentum nunc ac nisi vulputate fringilla. Donec lacinia congue felis in faucibus.</p>
                <p
                  class="mb-0"
                >Donec sed odio dui. Nullam quis risus eget urna mollis ornare vel eu leo. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.</p>
              </b-media>
            </ul>
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