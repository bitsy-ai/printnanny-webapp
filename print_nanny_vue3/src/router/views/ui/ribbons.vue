<script>
import appConfig from '@src/app.config'
import Layout from '@layouts/main'
import PageHeader from '@components/page-header'

/**
 * Ribbons component
 */
export default {
  page: {
    title: 'Ribbons',
    meta: [{ name: 'description', content: appConfig.description }],
  },
  components: { Layout, PageHeader },
  data() {
    return {
      title: 'Ribbons',
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
          text: 'Ribbons',
          active: true,
        },
      ],
      ribbonsData: [
        {
          title: 'Primary Header',
          color: 'primary',
          icon: 'mdi mdi-access-point',
          textalign: 'left',
          titlealign: 'right',
        },
        {
          title: 'Success Header',
          color: 'success',
          icon: 'mdi mdi-access-point',
          textalign: 'right',
          titlealign: 'left',
        },
        {
          title: 'Info Header',
          color: 'info',
          icon: 'mdi mdi-access-point',
          textalign: 'right',
          titlealign: 'left',
        },
        {
          title: 'Warning Header',
          color: 'warning',
          icon: 'mdi mdi-access-point',
          textalign: 'left',
          titlealign: 'right',
        },
        {
          title: 'Danger Header',
          color: 'danger',
          icon: 'mdi mdi-access-point',
          textalign: 'right',
          titlealign: 'left',
        },
        {
          title: 'Dark Header',
          color: 'dark',
          icon: 'mdi mdi-access-point',
          textalign: 'right',
          titlealign: 'left',
          shape: true,
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
      <div v-for="ribbon in ribbonsData" :key="ribbon.title" class="col-lg-4">
        <div class="card">
          <div class="card-body ribbon-box">
            <div :class="`ribbon ribbon-${ribbon.color} float-${ribbon.textalign}`">
              <i :class="`${ribbon.icon} mr-1`"></i>
              {{ribbon.color | titlecase}}
            </div>
            <h5 :class="`text-${ribbon.color} float-${ribbon.titlealign} mt-0`">{{ ribbon.title }}</h5>
            <div class="ribbon-content">
              <p class="mb-0">
                Quisque nec turpis at urna dictum luctus. Suspendisse convallis dignissim eros at
                volutpat. In egestas
                mattis dui. Aliquam mattis dictum aliquet. Nulla sapien mauris, eleifend et sem ac, commodo
                dapibus odio.
              </p>
            </div>
          </div>
          <!-- end card-body -->
        </div>
        <!-- end card -->
      </div>
      <!-- end col -->
    </div>
    <!-- end row -->

    <div class="row">
      <div v-for="ribbon in ribbonsData" :key="ribbon.title" class="col-lg-4">
        <div class="card">
          <div class="card-body ribbon-box">
            <div :class="`ribbon-two ribbon-two-${ribbon.color}`">
              <span>{{ribbon.color | titlecase}}</span>
            </div>
            <p class="mb-0">
              Quisque nec turpis at urna dictum luctus. Suspendisse convallis dignissim eros at
              volutpat. In egestas mattis dui. Aliquam mattis dictum aliquet. Nulla sapien mauris, eleifend et sem
              ac, commodo dapibus odio. Vivamus pretium nec odio cursus elementum. Suspendisse molestie
              ullamcorper ornare.
            </p>
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