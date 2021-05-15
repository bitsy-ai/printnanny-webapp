<script>
import draggable from 'vuedraggable'

import appConfig from '@src/app.config'
import Layout from '@layouts/main'
import PageHeader from '@components/page-header'

/**
 * Dragula component
 */
export default {
  page: {
    title: 'Dragula',
    meta: [{ name: 'description', content: appConfig.description }],
  },
  components: { draggable, Layout, PageHeader },
  data() {
    return {
      title: 'Dragula',
      items: [
        {
          text: 'Hyper',
          href: '/',
        },
        {
          text: 'Extended UI',
          href: '/',
        },
        {
          text: 'Dragula',
          active: true,
        },
      ],
      colors: [
        {
          variant: 'primary',
        },
        {
          variant: 'secondary',
        },
        {
          variant: 'success',
        },
        {
          variant: 'info',
        },
        {
          variant: 'warning',
        },
        {
          variant: 'danger',
        },
      ],
      itemlist: [
        {
          image: require('@assets/images/users/avatar-1.jpg'),
          name: 'Louis K. Bond',
          text: 'Founder & CEO',
        },
        {
          image: require('@assets/images/users/avatar-2.jpg'),
          name: 'Dennis N. Cloutier',
          text: 'Software Engineer',
        },
        {
          image: require('@assets/images/users/avatar-3.jpg'),
          name: 'Susan J. Sander',
          text: 'Web Designer',
        },
      ],
      itemlist2: [
        {
          image: require('@assets/images/users/avatar-4.jpg'),
          name: 'James M. Short',
          text: 'Web Developer',
        },
        {
          image: require('@assets/images/users/avatar-5.jpg'),
          name: 'Gabriel J. Snyder',
          text: 'Business Analyst',
        },
        {
          image: require('@assets/images/users/avatar-6.jpg'),
          name: 'Louie C. Mason',
          text: 'Human Resources',
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
      <div class="col-12">
        <div class="card">
          <div class="card-body">
            <h4 class="header-title">Simple Drag and Drop Example</h4>
            <p class="text-muted font-14">
              Just specify the data attribute
              <code>data-plugin='dragula'</code> to have drag and drop support in your container.
            </p>
            <draggable :list="colors" class="row">
              <div v-for="color of colors" :key="color.variant" class="col-md-4">
                <div :class="`card mb-0 mt-3 text-white bg-${color.variant}`">
                  <div class="card-body">
                    <blockquote class="card-bodyquote mb-0">
                      <p>
                        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer posuere
                        erat a ante.
                      </p>
                      <footer>
                        Someone famous in
                        <cite title="Source Title">Source Title</cite>
                      </footer>
                    </blockquote>
                  </div>
                  <!-- end card-body-->
                </div>
                <!-- end card-->
              </div>
              <!-- end col-->
            </draggable>
          </div>
        </div>
        <!-- end card -->
      </div>
      <!-- end col -->
    </div>
    <!-- end row -->

    <div class="row">
      <div class="col-12">
        <div class="card">
          <div class="card-body">
            <h4 class="header-title">Move stuff between containers</h4>
            <p class="text-muted font-14 mb-3">
              Just specify the data attribute
              <code>data-plugin='dragula'</code> and
              <code>data-containers='["first-container-id", "second-container-id"]'</code>.
            </p>
            <div class="row">
              <div class="col-md-6">
                <div class="bg-dragula p-2 p-lg-4">
                  <h5 class="mt-0">Part 1</h5>
                  <div id="company-list-left" class="py-2">
                    <draggable class="list-group" group="tasks" :list="itemlist">
                      <div v-for="item of itemlist" :key="item.image" class="card mb-0 mt-2">
                        <div class="card-body">
                          <div class="media">
                            <img
                              :src="`${item.image}`"
                              alt="image"
                              class="mr-3 d-none d-sm-block avatar-sm rounded-circle"
                            />
                            <div class="media-body">
                              <h5 class="mb-1 mt-0">{{item.name}}</h5>
                              <p>{{item.text}}</p>
                              <p class="mb-0 text-muted">
                                <span class="font-italic">
                                  <b>"</b>Disrupt pork belly poutine, asymmetrical tousled succulents selfies. You probably haven't heard of them tattooed master cleanse live-edge keffiyeh.
                                </span>
                              </p>
                            </div>
                            <!-- end media-body -->
                          </div>
                          <!-- end media -->
                        </div>
                        <!-- end card-body -->
                      </div>
                    </draggable>
                  </div>
                </div>
              </div>
              <div class="col-md-6">
                <div class="bg-dragula p-2 p-lg-4">
                  <h5 class="mt-0">Part 2</h5>
                  <div id="company-list-left" class="py-2">
                    <draggable class="list-group" group="tasks" :list="itemlist2">
                      <div v-for="item of itemlist2" :key="item.image" class="card mb-0 mt-2">
                        <div class="card-body">
                          <div class="media">
                            <img
                              :src="`${item.image}`"
                              alt="image"
                              class="mr-3 d-none d-sm-block avatar-sm rounded-circle"
                            />
                            <div class="media-body">
                              <h5 class="mb-1 mt-0">{{item.name}}</h5>
                              <p>{{item.text}}</p>
                              <p class="mb-0 text-muted">
                                <span class="font-italic">
                                  <b>"</b>Disrupt pork belly poutine, asymmetrical tousled succulents selfies. You probably haven't heard of them tattooed master cleanse live-edge keffiyeh.
                                </span>
                              </p>
                            </div>
                            <!-- end media-body -->
                          </div>
                          <!-- end media -->
                        </div>
                        <!-- end card-body -->
                      </div>
                    </draggable>
                  </div>
                </div>
              </div>
              <!-- end col -->
            </div>
            <!-- end row -->
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
