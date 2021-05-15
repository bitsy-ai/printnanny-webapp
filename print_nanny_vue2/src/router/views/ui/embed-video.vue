<script>
import appConfig from '@src/app.config'
import Layout from '@layouts/main'
import PageHeader from '@components/page-header'

/**
 * Embed Video component
 */
export default {
  page: {
    title: 'Embed Video',
    meta: [{ name: 'description', content: appConfig.description }],
  },
  components: { Layout, PageHeader },
  data() {
    return {
      title: 'Embed Video',
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
          text: 'Embed Video',
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
            <h4 class="header-title">Responsive embed video 21:9</h4>
            <p class="text-muted font-14">
              Use class
              <code>.embed-responsive-21by9</code>
            </p>
            <!-- 21:9 aspect ratio -->
            <b-embed
              type="iframe"
              aspect="21by9"
              class="embed-responsive-item"
              src="https://www.youtube.com/embed/PrUxWZiQfy4?autohide=0&showinfo=0&controls=0"
              allowfullscreen
            ></b-embed>
          </div>
        </div>
        <div class="card">
          <div class="card-body">
            <h4 class="header-title">Responsive embed video 1:1</h4>
            <p class="text-muted font-14">
              Use class
              <code>.embed-responsive-1by1</code>
            </p>
            <b-embed
              type="iframe"
              aspect="1by1"
              class="embed-responsive-item"
              src="https://www.youtube.com/embed/PrUxWZiQfy4?autohide=0&showinfo=0&controls=0"
              allowfullscreen
            ></b-embed>
          </div>
        </div>
      </div>

      <div class="col-xl-6">
        <div class="card">
          <div class="card-body">
            <h4 class="header-title">Responsive embed video 16:9</h4>
            <p class="text-muted font-14">
              Use class
              <code>.embed-responsive-16by9</code>
            </p>
            <!-- 16:9 aspect ratio -->
            <b-embed
              type="iframe"
              aspect="16by9"
              class="embed-responsive-item"
              src="https://www.youtube.com/embed/PrUxWZiQfy4?autohide=0&showinfo=0&controls=0"
              allowfullscreen
            ></b-embed>
          </div>
        </div>
        <div class="card">
          <div class="card-body">
            <h4 class="header-title">Responsive embed video 4:3</h4>
            <p class="text-muted font-14">
              Use class
              <code>.embed-responsive-4by3</code>
            </p>
            <!-- 4:3 aspect ratio -->
            <b-embed
              type="iframe"
              aspect="4by3"
              class="embed-responsive-item"
              src="https://www.youtube.com/embed/PrUxWZiQfy4?autohide=0&showinfo=0&controls=0"
              allowfullscreen
            ></b-embed>
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