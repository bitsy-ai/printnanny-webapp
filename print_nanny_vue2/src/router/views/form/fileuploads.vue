<script>
import vue2Dropzone from 'vue2-dropzone'

import appConfig from '@src/app.config'
import Layout from '@layouts/main'
import PageHeader from '@components/page-header'

/**
 * File Uploads component
 */
export default {
  page: {
    title: 'File Uploads',
    meta: [{ name: 'description', content: appConfig.description }],
  },
  components: { vueDropzone: vue2Dropzone, Layout, PageHeader },
  data() {
    return {
      title: 'File Uploads',
      items: [
        {
          text: 'Hyper',
          href: '/',
        },
        {
          text: 'Forms',
          href: '/',
        },
        {
          text: 'File Uploads',
          active: true,
        },
      ],
      dropzoneOptions: {
        url: 'https://httpbin.org/post',
        previewTemplate: this.template(),
        previewsContainer: '.dropzone-previews',
      },
    }
  },
  methods: {
    template: function() {
      return `
      <div class="card mt-1 mb-0 shadow-none border">
          <div class="p-2">
              <div class="row align-items-center">
                  <div class="col-auto">
                      <img data-dz-thumbnail-bg src="#" class="avatar-sm rounded bg-light" alt="">
                  </div>
                  <div class="col pl-0">
                      <a href="javascript:void(0);" class="text-muted font-weight-bold" data-dz-name></a>
                      <p class="mb-0" data-dz-size></p>
                  </div>
                  <div class="col-auto">
                      <!-- Button -->
                      <a href="" class="btn btn-link btn-lg text-muted" data-dz-remove>
                          <i class="dripicons-cross"></i>
                      </a>
                  </div>
              </div>
          </div>
      </div>
      `
    },
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
            <h4 class="header-title m-t-0">Dropzone File Upload</h4>
            <p
              class="text-muted font-14"
            >DropzoneJS is an open source library that provides drag’n’drop file uploads with image previews.</p>
            <!-- file upload -->
            <vue-dropzone
              id="customdropzone"
              ref="myVueDropzone"
              class="dropzone"
              :use-custom-slot="true"
              :include-styling="false"
              :options="dropzoneOptions"
            >
              <div class="dropzone-custom-content">
                <i class="h1 text-muted dripicons-cloud-upload"></i>
                <h3>Drop files here or click to upload.</h3>
                <span class="text-muted font-13">
                  (This is just a demo dropzone. Selected files are
                  <strong>not</strong> actually uploaded.)
                </span>
              </div>
            </vue-dropzone>
            <div id="file-previews" class="dropzone-previews mt-3"></div>
            <div class="text-center mt-4">
              <button type="button" class="btn btn-primary">Send Files</button>
            </div>
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

