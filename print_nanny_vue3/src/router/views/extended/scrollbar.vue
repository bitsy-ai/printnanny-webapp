<script>
import simplebar from 'simplebar-vue'

import appConfig from '@src/app.config'
import Layout from '@layouts/main'
import PageHeader from '@components/page-header'

/**
 * Scrollbar component
 */
export default {
  page: {
    title: 'Scrollbar',
    meta: [{ name: 'description', content: appConfig.description }],
  },
  components: { simplebar, Layout, PageHeader },
  data() {
    return {
      title: 'Scrollbar',
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
          text: 'Scrollbar',
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
            <h4 class="header-title">Default Scroll</h4>
            <p class="text-muted font-14">
              Just use data attribute
              <code>data-simplebar</code>
              and add
              <code>max-height: **px</code> oh fix height
            </p>

            <simplebar style="max-height: 250px;">
              SimpleBar does only one thing: replace the browser's default scrollbar
              with a custom CSS-styled one without losing performances.
              Unlike some popular plugins, SimpleBar doesn't mimic scroll with
              Javascript, causing janks and strange scrolling behaviours...
              You keep the awesomeness of native scrolling...with a custom scrollbar!
              <p>
                SimpleBar
                <strong>
                  does NOT implement a custom scroll
                  behaviour
                </strong>. It keeps the
                <strong>native</strong>
                <code>overflow: auto</code> scroll and
                <strong>only</strong> replace
                the scrollbar visual appearance.
              </p>
              <h5>Design it as you want</h5>
              <p>
                SimpleBar uses pure CSS to style the scrollbar. You can easily
                customize it as you want! Or even have multiple style on the same
                page...or just keep the default style ("Mac OS" scrollbar style).
              </p>
              <h5>Lightweight and performant</h5>
              <p>
                Only 6kb minified. SimpleBar doesn't use Javascript to handle
                scrolling. You keep the performances/behaviours of the native
                scroll.
              </p>
              <h5>Supported everywhere</h5>
              <p>
                SimpleBar has been tested on the following browsers: Chrome, Firefox,
                Safari, Edge, IE11.
              </p>
            </simplebar>
          </div>
          <!-- end card-body -->
        </div>
        <!-- end card -->
      </div>
      <!-- end col -->
      <div class="col-xl-6">
        <div class="card">
          <div class="card-body">
            <h4 class="header-title">RTL Position</h4>
            <p class="text-muted font-14">
              Just use data attribute
              <code>data-simplebar data-simplebar-direction='rtl'</code>
              and add
              <code>max-height: **px</code> oh fix height
            </p>

            <simplebar data-simplebar data-simplebar-direction="rtl" style="max-height: 250px;">
              SimpleBar does only one thing: replace the browser's default scrollbar
              with a custom CSS-styled one without losing performances.
              Unlike some popular plugins, SimpleBar doesn't mimic scroll with
              Javascript, causing janks and strange scrolling behaviours...
              You keep the awesomeness of native scrolling...with a custom scrollbar!
              <p>
                SimpleBar
                <strong>
                  does NOT implement a custom scroll
                  behaviour
                </strong>. It keeps the
                <strong>native</strong>
                <code>overflow: auto</code> scroll and
                <strong>only</strong> replace
                the scrollbar visual appearance.
              </p>
              <h5>Design it as you want</h5>
              <p>
                SimpleBar uses pure CSS to style the scrollbar. You can easily
                customize it as you want! Or even have multiple style on the same
                page...or just keep the default style ("Mac OS" scrollbar style).
              </p>
              <h5>Lightweight and performant</h5>
              <p>
                Only 6kb minified. SimpleBar doesn't use Javascript to handle
                scrolling. You keep the performances/behaviours of the native
                scroll.
              </p>
              <h5>Supported everywhere</h5>
              <p>
                SimpleBar has been tested on the following browsers: Chrome, Firefox,
                Safari, Edge, IE11.
              </p>
            </simplebar>
          </div>
          <!-- end card-body -->
        </div>
        <!-- end card -->
      </div>
      <!-- end col -->
    </div>
    <!-- end row -->
   
    <div class="row">
      <div class="col-xl-6">
        <div class="card">
          <div class="card-body">
            <h4 class="header-title">Scroll Size</h4>
            <p class="text-muted font-14">
              Just use data attribute
              <code>data-simplebar</code>
              and add
              <code>max-height: **px</code> oh fix height
            </p>
            <simplebar id="data-simplebar-lg" data-simplebar style="max-height: 250px;">
              SimpleBar does only one thing: replace the browser's default scrollbar
              with a custom CSS-styled one without losing performances.
              Unlike some popular plugins, SimpleBar doesn't mimic scroll with
              Javascript, causing janks and strange scrolling behaviours...
              You keep the awesomeness of native scrolling...with a custom scrollbar!
              <p>
                SimpleBar
                <strong>
                  does NOT implement a custom scroll
                  behaviour
                </strong>. It keeps the
                <strong>native</strong>
                <code>overflow: auto</code> scroll and
                <strong>only</strong> replace
                the scrollbar visual appearance.
              </p>
              <h5>Design it as you want</h5>
              <p>
                SimpleBar uses pure CSS to style the scrollbar. You can easily
                customize it as you want! Or even have multiple style on the same
                page...or just keep the default style ("Mac OS" scrollbar style).
              </p>
              <h5>Lightweight and performant</h5>
              <p>
                Only 6kb minified. SimpleBar doesn't use Javascript to handle
                scrolling. You keep the performances/behaviours of the native
                scroll.
              </p>
              <h5>Supported everywhere</h5>
              <p>
                SimpleBar has been tested on the following browsers: Chrome, Firefox,
                Safari, Edge, IE11.
              </p>
            </simplebar>
          </div>
          <!-- end card-body -->
        </div>
        <!-- end card -->
      </div>
      <!-- end col -->
      <div class="col-xl-6">
        <div class="card">
          <div class="card-body">
            <h4 class="header-title">Scroll Color</h4>
            <p class="text-muted font-14">
              Just use data attribute
              <code>data-simplebar data-simplebar-primary</code>
              and add
              <code>max-height: **px</code> oh fix height
            </p>
            <simplebar id="data-simplebar-primary" style="max-height: 250px;">
              SimpleBar does only one thing: replace the browser's default scrollbar
              with a custom CSS-styled one without losing performances.
              Unlike some popular plugins, SimpleBar doesn't mimic scroll with
              Javascript, causing janks and strange scrolling behaviours...
              You keep the awesomeness of native scrolling...with a custom scrollbar!
              <p>
                SimpleBar
                <strong>
                  does NOT implement a custom scroll
                  behaviour
                </strong>. It keeps the
                <strong>native</strong>
                <code>overflow: auto</code> scroll and
                <strong>only</strong> replace
                the scrollbar visual appearance.
              </p>
              <h5>Design it as you want</h5>
              <p>
                SimpleBar uses pure CSS to style the scrollbar. You can easily
                customize it as you want! Or even have multiple style on the same
                page...or just keep the default style ("Mac OS" scrollbar style).
              </p>
              <h5>Lightweight and performant</h5>
              <p>
                Only 6kb minified. SimpleBar doesn't use Javascript to handle
                scrolling. You keep the performances/behaviours of the native
                scroll.
              </p>
              <h5>Supported everywhere</h5>
              <p>
                SimpleBar has been tested on the following browsers: Chrome, Firefox,
                Safari, Edge, IE11.
              </p>
            </simplebar>
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