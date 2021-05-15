<script>
import appConfig from '@src/app.config'
import Layout from '@layouts/main'
import PageHeader from '@components/page-header'

/**
 * Carousel component
 */
export default {
  page: {
    title: 'Carousel',
    meta: [{ name: 'description', content: appConfig.description }],
  },
  components: { Layout, PageHeader },
  data() {
    return {
      title: 'Carousel',
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
          text: 'Carousel',
          active: true,
        },
      ],
      slide: 0,
    }
  },
}
</script>

<template>
  <Layout>
    <PageHeader :title="title" :items="items" />
    <div class="row">
      <div class="col-lg-6">
        <div class="card">
          <div class="card-body">
            <h4 class="header-title">Slides only</h4>
            <p class="text-muted font-14">
              Here’s a carousel with slides only.
              Note the presence of the
              <code>.d-block</code>
              and
              <code>.img-fluid</code> on carousel images
              to prevent browser default image alignment.
            </p>
            <b-carousel id="carousel-fade" style="text-shadow: 0px 0px 2px #000">
              <b-carousel-slide :img-src="require('@assets/images/small/small-1.jpg')"></b-carousel-slide>
              <b-carousel-slide :img-src="require('@assets/images/small/small-2.jpg')"></b-carousel-slide>
              <b-carousel-slide :img-src="require('@assets/images/small/small-3.jpg')"></b-carousel-slide>
            </b-carousel>
          </div>
          <!-- end card-body -->
        </div>
        <!-- end card -->
      </div>
      <!-- end col -->
      <div class="col-lg-6">
        <div class="card">
          <div class="card-body">
            <h4 class="header-title">With controls</h4>
            <p class="text-muted font-14">Adding in the previous and next controls:</p>
            <b-carousel style="text-shadow: 0px 0px 2px #000" controls>
              <b-carousel-slide :img-src="require('@assets/images/small/small-3.jpg')"></b-carousel-slide>
              <b-carousel-slide :img-src="require('@assets/images/small/small-2.jpg')"></b-carousel-slide>
              <b-carousel-slide :img-src="require('@assets/images/small/small-1.jpg')"></b-carousel-slide>
            </b-carousel>
          </div>
          <!-- end card-body -->
        </div>
        <!-- end card -->
      </div>
      <!-- end col -->
    </div>
    <!-- end row -->

    <div class="row">
      <div class="col-lg-6">
        <div class="card">
          <div class="card-body">
            <h4 class="header-title">With indicators</h4>
            <p class="text-muted font-14">
              You can also add the indicators to the
              carousel, alongside the controls, too.
            </p>
            <b-carousel style="text-shadow: 0px 0px 2px #000" controls indicators>
              <b-carousel-slide :img-src="require('@assets/images/small/small-3.jpg')"></b-carousel-slide>
              <b-carousel-slide :img-src="require('@assets/images/small/small-2.jpg')"></b-carousel-slide>
              <b-carousel-slide :img-src="require('@assets/images/small/small-1.jpg')"></b-carousel-slide>
            </b-carousel>
          </div>
          <!-- end card-body -->
        </div>
        <!-- end card -->
      </div>
      <!-- end col -->
      <div class="col-lg-6">
        <div class="card">
          <div class="card-body">
            <h4 class="header-title">With captions</h4>
            <p class="text-muted font-14">
              Add captions to your slides easily with the
              <code>.carousel-caption</code> element within any
              <code>.carousel-item</code>.
            </p>
            <b-carousel
              id="carousel-1"
              v-model="slide"
              :interval="4000"
              controls
              indicators
              style="text-shadow: 1px 1px 2px #333;"
            >
              <!-- Text slides with image -->
              <b-carousel-slide :img-src="require('@assets/images/small/small-1.jpg')">
                <h3 class="text-white">First slide label</h3>
                <p>Nulla vitae elit libero, a pharetra augue mollis interdum.</p>
              </b-carousel-slide>

              <!-- Slides with custom text -->
              <b-carousel-slide :img-src="require('@assets/images/small/small-3.jpg')">
                <h3 class="text-white">Second slide label</h3>
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
              </b-carousel-slide>

              <!-- Slides with image only -->
              <b-carousel-slide :img-src="require('@assets/images/small/small-2.jpg')">
                <h3 class="text-white">Third slide label</h3>
                <p>Praesent commodo cursus magna, vel scelerisque nisl consectetur.</p>
              </b-carousel-slide>
            </b-carousel>
          </div>
          <!-- end card-body -->
        </div>
        <!-- end card -->
      </div>
      <!-- end col -->
    </div>
    <!-- end row -->
    <div class="row">
      <div class="col-lg-6">
        <div class="card">
          <div class="card-body">
            <h4 class="header-title">Crossfade</h4>
            <p class="text-muted font-14">
              Add
              <code>fade</code> to your carousel to animate slides with a fade transition instead of a slide.
            </p>
            <b-carousel style="text-shadow: 0px 0px 2px #000" controls fade>
              <b-carousel-slide :img-src="require('@assets/images/small/small-1.jpg')"></b-carousel-slide>
              <b-carousel-slide :img-src="require('@assets/images/small/small-2.jpg')"></b-carousel-slide>
              <b-carousel-slide :img-src="require('@assets/images/small/small-3.jpg')"></b-carousel-slide>
            </b-carousel>
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