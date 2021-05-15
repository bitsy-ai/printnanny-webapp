<script>
import appConfig from '@src/app.config'
import Layout from '@layouts/main'
import PageHeader from '@components/page-header'

/**
 * Accordions component
 */
export default {
  page: {
    title: 'Accordions',
    meta: [{ name: 'description', content: appConfig.description }],
  },
  components: { Layout, PageHeader },
  data() {
    return {
      title: 'Accordions',
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
          text: 'Accordions',
          active: true,
        },
      ],
      text: `
        Anim pariatur cliche reprehenderit, enim eiusmod high life accusamus terry richardson ad squid. 3 wolf moon officia aute, non cupidatat skateboard dolor brunch. Food truck quinoa nesciunt laborum eiusmod. Brunch 3 wolf moon tempor, sunt aliqua put a bird on it squid single-origin coffee nulla assumenda shoreditch et. Nihil anim keffiyeh helvetica, craft beer labore wes anderson cred nesciunt sapiente ea proident. Ad vegan excepteur butcher vice lomo. Leggings occaecat craft beer farm-to-table, raw denim aesthetic synth nesciunt you probably haven't heard of them accusamus labore sustainable VHS.
        `,
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
            <h4 class="header-title">Simple Accordions</h4>
            <p class="text-muted font-14 mb-3">
              Using the card component, you can
              extend the default collapse behavior to create an accordion.
            </p>
            <div role="tablist">
              <b-card no-body class="mb-1">
                <b-card-header header-tag="header" role="tab">
                  <h5 class="py-1">
                    <a
                      v-b-toggle.accordion-1
                      href="javascript: void(0);"
                      class="custom-accordion-title"
                    >Collapsible Group Item #1</a>
                  </h5>
                </b-card-header>
                <b-collapse id="accordion-1" visible accordion="my-accordion" role="tabpanel">
                  <b-card-body>
                    <b-card-text>{{ text }}</b-card-text>
                  </b-card-body>
                </b-collapse>
              </b-card>

              <b-card no-body class="mb-1">
                <b-card-header header-tag="header" role="tab">
                  <h5 class="py-1">
                    <a
                      v-b-toggle.accordion-2
                      href="javascript: void(0);"
                      class="custom-accordion-title"
                    >Collapsible Group Item #2</a>
                  </h5>
                </b-card-header>
                <b-collapse id="accordion-2" accordion="my-accordion" role="tabpanel">
                  <b-card-body>
                    <b-card-text>{{ text }}</b-card-text>
                  </b-card-body>
                </b-collapse>
              </b-card>

              <b-card no-body class="mb-1">
                <b-card-header header-tag="header" role="tab">
                  <h5 class="py-1">
                    <a
                      v-b-toggle.accordion-3
                      href="javascript: void(0);"
                      class="custom-accordion-title"
                    >Collapsible Group Item #3</a>
                  </h5>
                </b-card-header>
                <b-collapse id="accordion-3" accordion="my-accordion" role="tabpanel">
                  <b-card-body>
                    <b-card-text>{{ text }}</b-card-text>
                  </b-card-body>
                </b-collapse>
              </b-card>
            </div>
          </div>
          <!-- end card-body-->
        </div>
        <!-- end card-->
      </div>
      <!-- end col-->
      <div class="col-xl-6">
        <div class="card">
          <div class="card-body">
            <h4 class="header-title">Custom Accordions</h4>
            <p class="text-muted font-14 mb-3">
              You can have custom look and feel for accordion as well. Just use class
              <code>.custom-accordion</code>.
            </p>
            <div role="tablist">
              <b-card no-body class="custom-accordion mb-0 shadow-none">
                <b-card-header header-tag="header" role="tab">
                  <h5 class="py-1 m-0">
                    <a
                      v-b-toggle.custom-accordion1
                      href="javascript: void(0);"
                      class="custom-accordion-title"
                    >Q. Can I use this template for my client?</a>
                  </h5>
                </b-card-header>
                <b-collapse id="custom-accordion1" visible accordion="accordion" role="tabpanel">
                  <b-card-body>
                    <b-card-text>
                      Yup, the marketplace license allows you to use this theme
                      in any end products.
                      For more information on licenses, please refere
                    </b-card-text>
                  </b-card-body>
                </b-collapse>
              </b-card>

              <b-card no-body class="custom-accordion mb-0 shadow-none">
                <b-card-header header-tag="header" role="tab">
                  <h5 class="m-0 py-1">
                    <a
                      v-b-toggle.custom-accordion2
                      href="javascript: void(0);"
                      class="custom-accordion-title"
                    >Q. Can this theme work with Wordpress?</a>
                  </h5>
                </b-card-header>
                <b-collapse id="custom-accordion2" accordion="accordion" role="tabpanel">
                  <b-card-body>
                    <b-card-text>
                      No. This is a HTML template. It won't directly with
                      wordpress, though you can convert this into wordpress
                      compatible theme
                    </b-card-text>
                  </b-card-body>
                </b-collapse>
              </b-card>

              <b-card no-body class="custom-accordion mb-0 shadow-none">
                <b-card-header header-tag="header" role="tab">
                  <h5 class="m-0 py-1">
                    <a
                      v-b-toggle.custom-accordion3
                      href="javascript: void(0);"
                      class="custom-accordion-title"
                    >Q. How do I get help with the theme?</a>
                  </h5>
                </b-card-header>
                <b-collapse id="custom-accordion3" accordion="accordion" role="tabpanel">
                  <b-card-body>
                    <b-card-text>
                      Use our dedicated support email (support@coderthemes.com) to
                      send your issues or feedback. We are here to help anytime
                    </b-card-text>
                  </b-card-body>
                </b-collapse>
              </b-card>

              <b-card no-body class="custom-accordion shadow-none">
                <b-card-header header-tag="header" role="tab">
                  <h5 class="m-0 py-1">
                    <a
                      v-b-toggle.custom-accordion4
                      href="javascript: void(0);"
                      class="custom-accordion-title"
                    >Q. Will you regularly give updates of Hyper ?</a>
                  </h5>
                </b-card-header>
                <b-collapse id="custom-accordion4" accordion="accordion" role="tabpanel">
                  <b-card-body>
                    <b-card-text>Yes, We will update the Hyper regularly. All the future updates would be available without any cost</b-card-text>
                  </b-card-body>
                </b-collapse>
              </b-card>
            </div>
          </div>
          <!-- end card-body-->
        </div>
        <!-- end card-->
      </div>
      <!-- end col-->
    </div>
    <!-- end row-->

    <div class="row">
      <div class="col-xl-6">
        <div class="card">
          <div class="card-body">
            <h4 class="header-title">Collapse</h4>
            <p class="text-muted font-14 mb-3">
              Bootstrap's collapse provides the way to toggle the visibility of any content or element.
              Please read the official
              <a
                href="https://getbootstrap.com/docs/4.3/components/collapse/"
                target="_blank"
              >Bootstrap</a>
              documentation for a full list of options.
            </p>
            <b-button v-b-toggle.collapse class="m-1" variant="primary">Link with href</b-button>

            <!-- Using value -->
            <b-button v-b-toggle="'collapse'" class="m-1" variant="primary">Button with data-target</b-button>

            <!-- Element to collapse -->
            <b-collapse id="collapse" visible class="mt-1">
              <div
                class="card card-body mb-0"
              >Anim pariatur cliche reprehenderit, enim eiusmod high life accusamus terry richardson ad squid. Nihil anim keffiyeh helvetica, craft beer labore wes anderson cred nesciunt sapiente ea proident.</div>
            </b-collapse>
          </div>
          <!-- end card-body -->
        </div>
        <!-- end card -->
      </div>
      <!-- end col -->

      <div class="col-xl-6">
        <div class="card">
          <div class="card-body">
            <h4 class="header-title">Multiple Targets</h4>
            <p class="text-muted font-14 mb-3">
              Multiple
              <code>&lt;button&gt;</code> or
              <code>&lt;a&gt;</code> can show and hide an element if
              they each reference it with their
              <code>href</code> or
              <code>data-target</code> attribute
            </p>
            <p>
              <!-- Using modifiers -->
              <b-button v-b-toggle.collapse-1 class="m-1" variant="primary">Toggle first element</b-button>

              <!-- Using value -->
              <b-button v-b-toggle.collapse-2 class="m-1" variant="primary">Toggle second element</b-button>
              <b-button v-b-toggle.collapse-1.collapse-2 variant="primary">Toggle both elements</b-button>
            </p>
            <!-- Element to collapse -->
            <div class="row">
              <div class="col">
                <b-collapse id="collapse-1">
                  <b-card
                    class="mb-0"
                  >Anim pariatur cliche reprehenderit, enim eiusmod high life accusamus terry richardson ad squid. Nihil anim keffiyeh helvetica, craft beer labore wes anderson cred nesciunt sapiente ea proident.</b-card>
                </b-collapse>
              </div>
              <div class="col">
                <b-collapse id="collapse-2">
                  <b-card
                    class="mb-0"
                  >Anim pariatur cliche reprehenderit, enim eiusmod high life accusamus terry richardson ad squid. Nihil anim keffiyeh helvetica, craft beer labore wes anderson cred nesciunt sapiente ea proident.</b-card>
                </b-collapse>
              </div>
              <!-- end col -->
            </div>
            <!-- end row-->
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
