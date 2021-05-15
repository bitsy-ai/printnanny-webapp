<script>
import appConfig from '@src/app.config'
import Layout from '@layouts/main'
import PageHeader from '@components/page-header'

/**
 * Alerts component
 */
export default {
  page: {
    title: 'Alerts',
    meta: [{ name: 'description', content: appConfig.description }],
  },
  components: { Layout, PageHeader },
  data() {
    return {
      title: 'Alerts',
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
          text: 'Alerts',
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
            <h4 class="header-title">Default Alert</h4>
            <p class="text-muted font-14 mb-3">
              Provide contextual feedback messages for typical user actions with the handful of available and flexible alert messages.
              Alerts are available for any length of text, as well as an optional dismiss
              button.
            </p>

            <b-alert show variant="primary">
              <strong>Primary -</strong> A simple primary alert—check it out!
            </b-alert>
            <b-alert show variant="secondary">
              <strong>Secondary -</strong> A simple secondary alert—check it out!
            </b-alert>
            <b-alert show variant="success">
              <strong>Success -</strong> A simple success alert—check it out!
            </b-alert>
            <b-alert show variant="danger">
              <strong>Error -</strong> A simple danger alert—check it out!
            </b-alert>
            <b-alert show variant="warning bg-warning text-white border-0">
              <strong>Warning -</strong> A simple warning alert—check it out!
            </b-alert>
            <b-alert show variant="info bg-info text-white border-0">
              <strong>Info -</strong> A simple info alert—check it out!
            </b-alert>
            <b-alert show variant="light bg-light text-dark border-0">
              <strong>Light -</strong> A simple light alert—check it out!
            </b-alert>
            <b-alert show variant="dark bg-dark text-white border-0 mb-0">
              <strong>Dark -</strong> A simple dark alert—check it out!
            </b-alert>
          </div>
          <!-- end card-body-->
        </div>
        <!-- end card-->
      </div>
      <!-- end col-->

      <div class="col-xl-6">
        <div class="card">
          <div class="card-body">
            <h4 class="header-title">Dismissing Alerts</h4>
            <p class="text-muted font-14 mb-3">
              Add a dismiss button and the
              <code>dismissible</code> , which adds
              extra padding to the right of the alert
              and positions the
              <code>close</code> button.
            </p>
            <b-alert show dismissible variant="primary bg-primary text-white border-0">
              <strong>Primary -</strong> A simple primary alert—check it out!
            </b-alert>
            <b-alert show dismissible variant="secondary  bg-secondary text-white border-0">
              <strong>Secondary -</strong> A simple secondary alert—check it out!
            </b-alert>
            <b-alert show dismissible variant="success  bg-success text-white border-0">
              <strong>Success -</strong> A simple success alert—check it out!
            </b-alert>
            <b-alert show dismissible variant="danger  bg-danger text-white border-0">
              <strong>Error -</strong> A simple danger alert—check it out!
            </b-alert>
            <b-alert show dismissible variant="warning">
              <strong>Warning -</strong> A simple warning alert—check it out!
            </b-alert>
            <b-alert show dismissible variant="info">
              <strong>Info -</strong> A simple info alert—check it out!
            </b-alert>
            <b-alert show dismissible variant="light">
              <strong>Light -</strong> A simple light alert—check it out!
            </b-alert>
            <b-alert show dismissible variant="dark">
              <strong>Dark -</strong> A simple dark alert—check it out!
            </b-alert>
          </div>
          <!-- end card-body-->
        </div>
        <!-- end card-->
      </div>
      <!-- end col-->
    </div>
    <!-- end row -->

    <div class="row">
      <div class="col-xl-6">
        <div class="card">
          <div class="card-body">
            <h4 class="header-title">Custom Alerts</h4>
            <p class="text-muted font-14 mb-3">
              Display alert with transparent background and with contextual text color. Use
              classes
              <code>.bg-white</code>, and
              <code>.text-*</code>. E.g.
              <code>
                bg-white
                text-primary
              </code>.
            </p>
            <b-alert show class="bg-white text-primary" variant="primary">
              This is a
              <strong>primary</strong> alert—check it out!
            </b-alert>
            <b-alert show class="bg-white text-secondary" variant="secondary">
              This is a
              <strong>secondary</strong> alert—check it out!
            </b-alert>
            <b-alert show class="bg-white text-success" variant="success">
              This is a
              <strong>success</strong> alert—check it out!
            </b-alert>
            <b-alert show class="bg-white text-info" variant="info">
              This is a
              <strong>info</strong> alert—check it out!
            </b-alert>
            <b-alert show class="bg-white text-warning" variant="warning">
              This is a
              <strong>warning</strong> alert—check it out!
            </b-alert>
            <b-alert show class="bg-white text-danger" variant="danger">
              This is a
              <strong>danger</strong> alert—check it out!
            </b-alert>
            <b-alert show class="bg-white text-light" variant="light">
              This is a
              <strong>light</strong> alert—check it out!
            </b-alert>
            <b-alert show class="bg-white text-dark" variant="dark">
              This is a
              <strong>dark</strong> alert—check it out!
            </b-alert>
          </div>
          <!-- end card-body-->
        </div>
        <!-- end card -->
      </div>
      <!-- end col -->

      <div class="col-xl-6">
        <div class="card">
          <div class="card-body">
            <h4 class="header-title">Link Color</h4>
            <p class="text-muted font-14 mb-3">
              Use the
              <code>.alert-link</code> utility class to quickly provide matching
              colored links within any alert.
            </p>

            <b-alert show variant="primary">
              A simple primary alert with
              <a href="#" class="alert-link">
                an example
                link
              </a>. Give it a click if you like.
            </b-alert>
            <b-alert show variant="secondary">
              A simple secondary alert with
              <a href="#" class="alert-link">
                an example
                link
              </a>. Give it a click if you like.
            </b-alert>
            <b-alert show variant="success">
              A simple success alert with
              <a href="#" class="alert-link">
                an example
                link
              </a>. Give it a click if you like.
            </b-alert>
            <b-alert show variant="danger">
              A simple danger alert with
              <a href="#" class="alert-link">
                an example
                link
              </a>. Give it a click if you like.
            </b-alert>
            <b-alert show variant="warning">
              A simple warning alert with
              <a href="#" class="alert-link">
                an example
                link
              </a>. Give it a click if you like.
            </b-alert>
            <b-alert show variant="info">
              A simple info alert with
              <a href="#" class="alert-link">
                an example
                link
              </a>. Give it a click if you like.
            </b-alert>
            <b-alert show variant="light">
              A simple light alert with
              <a href="#" class="alert-link">
                an example
                link
              </a>. Give it a click if you like.
            </b-alert>
            <b-alert show variant="dark">
              A simple dark alert with
              <a href="#" class="alert-link">
                an example
                link
              </a>. Give it a click if you like.
            </b-alert>
          </div>
          <!-- end card-body-->
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
            <h4 class="header-title">Icons with Alerts</h4>
            <p
              class="text-muted font-14 mb-3"
            >You can also include additional elements like icons, heading, etc along side the actual message.</p>
            <b-alert show variant="success">
              <i class="dripicons-checkmark mr-2"></i>This is a
              <strong>success</strong> alert—check it out!
            </b-alert>
            <b-alert show variant="danger">
              <i class="dripicons-wrong mr-2"></i>This is a
              <strong>danger</strong> alert—check it out!
            </b-alert>
            <b-alert show variant="warning">
              <i class="dripicons-warning mr-2"></i>This is a
              <strong>warning</strong> alert—check it out!
            </b-alert>
            <b-alert show variant="info">
              <i class="dripicons-information mr-2"></i>This is a
              <strong>info</strong>
              alert—check it out!
            </b-alert>
          </div>
          <!-- end card-body-->
        </div>
        <!-- end card -->
      </div>
      <!-- end col -->

      <div class="col-xl-6">
        <div class="card">
          <div class="card-body">
            <h4 class="header-title">Additional content</h4>
            <p class="text-muted font-14 mb-3">
              Alerts can also contain additional HTML elements like headings, paragraphs and
              dividers.
            </p>
            <b-alert show variant="success">
              <h4 class="alert-heading">Well done!</h4>
              <p>
                Aww yeah, you successfully read this important alert message. This example text is going to
                run a bit longer so that you can see how spacing within an alert works with this kind of
                content.
              </p>
              <hr />
              <p
                class="mb-0"
              >Whenever you need to, be sure to use margin utilities to keep things nice and tidy.</p>
            </b-alert>
          </div>
          <!-- end card-body-->
        </div>
        <!-- end card -->
      </div>
      <!-- end col -->
    </div>
    <!-- end row -->
  </Layout>
</template>