<script>
import appConfig from '@src/app.config'
import Layout from '@layouts/main'
import PageHeader from '@components/page-header'

/**
 * Progress component
 */
export default {
  page: {
    title: 'Progress',
    meta: [{ name: 'description', content: appConfig.description }],
  },
  components: { Layout, PageHeader },
  data() {
    return {
      title: 'Progress',
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
          text: 'Progress',
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
            <h4 class="header-title">Examples</h4>
            <p
              class="text-muted font-14"
            >A progress bar can be used to show a user how far along he/she is in a process.</p>
            <b-progress :value="0"></b-progress>
            <b-progress :value="25" class="mt-2"></b-progress>
            <b-progress :value="50" class="mt-2"></b-progress>
            <b-progress :value="75" class="mt-2"></b-progress>
            <b-progress :value="100" class="mt-2"></b-progress>
          </div>
          <!-- end card-body -->
        </div>
        <!-- end card-->
        <div class="card">
          <div class="card-body">
            <h4 class="header-title">Height</h4>
            <p
              class="text-muted font-14"
            >The height of the progress bar can be controlled with the height prop.</p>
            <b-progress :value="25" :max="100" class="mb-2" variant="danger" height="1px"></b-progress>
            <b-progress :value="25" :max="100" class="mb-2" variant="primary" height="3px"></b-progress>
            <b-progress :value="25" :max="100" class="mb-2" variant="success" height="5px"></b-progress>
            <b-progress :value="50" :max="100" class="mb-2" variant="info" height="8px"></b-progress>
            <b-progress :value="75" :max="100" class="mb-2" variant="warning" height="12px"></b-progress>
            <b-progress :value="38" :max="100" variant="success" height="15px"></b-progress>
          </div>
          <!-- end card-body -->
        </div>
        <!-- end card-->
        <div class="card">
          <div class="card-body">
            <h4 class="header-title">Multiple bars</h4>
            <p
              class="text-muted font-14"
            >Include multiple progress bars in a progress component if you need.</p>

            <b-progress class="mt-2" :max="100">
              <b-progress-bar :value="45 * (3 / 10)" variant="primary"></b-progress-bar>
              <b-progress-bar :value="45 * (6.6 / 10)" variant="success"></b-progress-bar>
              <b-progress-bar :value="45 * (4.8 / 10)" variant="info"></b-progress-bar>
            </b-progress>
          </div>
          <!-- end card-body -->
        </div>
        <!-- end card-->
        <div class="card">
          <div class="card-body">
            <h4 class="header-title">Animated stripes</h4>
            <p class="text-muted font-14">
              The striped gradient can also be animated. Add
              <code>animated</code> to
              <code>progress-bar</code> to animate the stripes right to left via CSS3 animations.
            </p>
            <b-progress :value="75" animated></b-progress>
          </div>
          <!-- end card-body -->
        </div>
        <!-- end card-->
      </div>
      <!-- end col -->

      <div class="col-xl-6">
        <div class="card">
          <div class="card-body">
            <h4 class="header-title">Labels</h4>
            <p class="text-muted font-14">
              Add labels to your progress bars by placing text within the
              <code>progress-bar</code>.
            </p>
            <b-progress :value="25" show-progress class="mt-3"></b-progress>
          </div>
          <!-- end card-body -->
        </div>
        <!-- end card-->
        <div class="card">
          <div class="card-body">
            <h4 class="header-title">Backgrounds</h4>
            <p
              class="text-muted font-14"
            >Use background utility classes to change the appearance of individual progress bars.</p>
            <b-progress :value="25" variant="success"></b-progress>
            <b-progress :value="50" variant="info" class="mt-2"></b-progress>
            <b-progress :value="75" variant="warning" class="mt-2"></b-progress>
            <b-progress :value="100" variant="danger" class="mt-2"></b-progress>
            <b-progress :value="65" variant="dark" class="mt-2"></b-progress>
            <b-progress :value="50" variant="secondary" class="mt-2"></b-progress>
          </div>
          <!-- end card-body -->
        </div>
        <!-- end card-->
        <div class="card">
          <div class="card-body">
            <h4 class="header-title">Striped</h4>
            <p class="text-muted font-14">
              Add
              <code>animated</code> to any
              <code>progress-bar</code> to apply a stripe via CSS gradient over the progress bar’s background color.
            </p>
            <b-progress :value="10" :max="100" class="mb-2" variant="primary" animated></b-progress>
            <b-progress :value="25" :max="100" class="mb-2" variant="success" animated></b-progress>
            <b-progress :value="50" :max="100" class="mb-2" variant="info" animated></b-progress>
            <b-progress :value="75" :max="100" class="mb-2" variant="warning" animated></b-progress>
            <b-progress :value="100" :max="100" class="mb-2" variant="danger" animated></b-progress>
            <b-progress :value="75" :max="100" variant="primary" animated></b-progress>
          </div>
          <!-- end card-body -->
        </div>
        <!-- end card-->
      </div>
      <!-- end col -->
    </div>
    <!-- end row -->
  </Layout>
</template>