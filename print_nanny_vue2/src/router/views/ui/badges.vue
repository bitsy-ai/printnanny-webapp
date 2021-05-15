<script>
import appConfig from '@src/app.config'
import Layout from '@layouts/main'
import PageHeader from '@components/page-header'

/**
 * Badges component
 */
export default {
  page: {
    title: 'Badges',
    meta: [{ name: 'description', content: appConfig.description }],
  },
  components: { Layout, PageHeader },
  data() {
    return {
      title: 'Badges',
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
          text: 'Badges',
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
            <h4 class="header-title">Default</h4>
            <p class="text-muted font-14 mb-3">
              A simple labeling component. Badges scale to match the size of the immediate parent element by using relative font sizing and
              <code>em</code> units.
            </p>

            <h1>
              h1.Example heading
              <b-badge>New</b-badge>
            </h1>
            <h2>
              h2.Example heading
              <b-badge class="badge-success-lighten">New</b-badge>
            </h2>
            <h3>
              h3.Example heading
              <b-button variant="primary" size="sm">
                Notifications
                <b-badge variant="light">4</b-badge>
              </b-button>
            </h3>
            <h4>
              h4.Example heading
              <b-badge href="#" class="badge-info-lighten">Info Link</b-badge>
            </h4>
            <h5>
              h5.Example heading
              <b-badge class="badge-outline-warning">New</b-badge>
            </h5>
            <h6>
              h6.Example heading
              <b-badge variant="danger">New</b-badge>
            </h6>
          </div>
          <!-- end card-body -->
        </div>
        <!-- end card -->

        <div class="card">
          <div class="card-body">
            <h4 class="header-title">Pill Badges</h4>
            <p class="text-muted font-14 mb-3">
              Use the
              <code>pill</code> modifier class to make badges more rounded.
            </p>

            <b-badge variant="primary" pill>Primary</b-badge>
            <b-badge variant="secondary" pill class="ml-1">Secondary</b-badge>
            <b-badge variant="success" pill class="ml-1">Success</b-badge>
            <b-badge variant="danger" pill class="ml-1">Danger</b-badge>
            <b-badge variant="warning" pill class="ml-1">Warning</b-badge>
            <b-badge variant="info" pill class="ml-1">Info</b-badge>
            <b-badge variant="light" pill class="ml-1">Light</b-badge>
            <b-badge variant="dark" pill class="ml-1">Dark</b-badge>

            <h5 class="mt-4">Lighten Badges</h5>
            <p class="text-muted font-14 mb-3">
              Use the
              <code>.badge-*-lighten</code> modifier class to make badges lighten.
            </p>
            <b-badge pill class="badge-primary-lighten">Primary</b-badge>
            <b-badge pill class="badge-secondary-lighten ml-1">Secondary</b-badge>
            <b-badge pill class="badge-success-lighten ml-1">Success</b-badge>
            <b-badge pill class="badge-danger-lighten ml-1">Danger</b-badge>
            <b-badge pill class="badge-warning-lighten ml-1">Warning</b-badge>
            <b-badge pill class="badge-info-lighten ml-1">Info</b-badge>
            <b-badge pill class="badge-light-lighten ml-1">Light</b-badge>
            <b-badge pill class="badge-dark-lighten ml-1">Dark</b-badge>
          </div>
          <!-- end card-body -->
        </div>
        <!-- end card -->
      </div>
      <!-- end col -->

      <div class="col-xl-6">
        <div class="card">
          <div class="card-body">
            <h4 class="header-title">Contextual variations</h4>
            <p class="text-muted font-14 mb-3">
              Add any of the below mentioned modifier classes to change the appearance of a badge.
              Badge can be more contextual as well.
            </p>
            <b-badge variant="primary">Primary</b-badge>
            <b-badge variant="secondary" class="ml-1">Secondary</b-badge>
            <b-badge variant="success" class="ml-1">Success</b-badge>
            <b-badge variant="danger" class="ml-1">Danger</b-badge>
            <b-badge variant="warning" class="ml-1">Warning</b-badge>
            <b-badge variant="info" class="ml-1">Info</b-badge>
            <b-badge variant="light" class="ml-1">Light</b-badge>
            <b-badge variant="dark" class="ml-1">Dark</b-badge>

            <h5 class="mt-4">Lighten Badges</h5>
            <p class="text-muted font-14 mb-3">
              Using the
              <code>.badge-*-lighten</code> modifier class, you can have more soften variation.
            </p>
            <b-badge variant="primary" class="badge-primary-lighten">Primary</b-badge>
            <b-badge variant="secondary" class="badge-secondary-lighten ml-1">Secondary</b-badge>
            <b-badge variant="success" class="badge-success-lighten ml-1">Success</b-badge>
            <b-badge variant="danger" class="badge-danger-lighten ml-1">Danger</b-badge>
            <b-badge variant="warning" class="badge-warning-lighten ml-1">Warning</b-badge>
            <b-badge variant="info" class="badge-info-lighten ml-1">Info</b-badge>
            <b-badge variant="light" class="badge-light-lighten ml-1">Light</b-badge>
            <b-badge variant="dark" class="badge-dark-lighten ml-1">Dark</b-badge>
          </div>
          <!-- end card-body -->
        </div>
        <!-- end card -->

        <div class="card">
          <div class="card-body">
            <h4 class="header-title">Links Badges</h4>
            <p class="text-muted font-14 mb-3">
              Using the contextual
              <code>.badge-*</code> classes on an
              <code>&lt;a&gt;</code> element quickly provide
              <em>actionable</em> badges with hover and focus states.
            </p>
            <b-badge href="#" variant="primary">Primary</b-badge>
            <b-badge href="#" variant="secondary" class="ml-1">Secondary</b-badge>
            <b-badge href="#" variant="success" class="ml-1">Success</b-badge>
            <b-badge href="#" variant="danger" class="ml-1">Danger</b-badge>
            <b-badge href="#" variant="warning" class="ml-1">Warning</b-badge>
            <b-badge href="#" variant="info" class="ml-1">Info</b-badge>
            <b-badge href="#" variant="light" class="ml-1">Light</b-badge>
            <b-badge href="#" variant="dark" class="ml-1">Dark</b-badge>

            <h5 class="mt-4">Lighten Badges</h5>
            <p class="text-muted font-14 mb-3">
              Use the
              <code>.badge-*-lighten</code> modifier class to make badges lighten.
            </p>
            <b-badge href="#" class="badge-primary-lighten">Primary</b-badge>
            <b-badge href="#" class="badge-secondary-lighten ml-1">Secondary</b-badge>
            <b-badge href="#" class="badge-success-lighten ml-1">Success</b-badge>
            <b-badge href="#" class="badge-danger-lighten ml-1">Danger</b-badge>
            <b-badge href="#" class="badge-warning-lighten ml-1">Warning</b-badge>
            <b-badge href="#" class="badge-info-lighten ml-1">Info</b-badge>
            <b-badge href="#" class="badge-light-lighten ml-1">Light</b-badge>
            <b-badge href="#" class="badge-dark-lighten ml-1">Dark</b-badge>
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