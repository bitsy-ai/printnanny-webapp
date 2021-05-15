<script>
import vue2Dropzone from 'vue2-dropzone'

export default {
  components: { vueDropzone: vue2Dropzone },
  data() {
    return {
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
  <div class="card">
    <div class="card-body">
      <h5 class="card-title mb-3">Attachments</h5>

      <vue-dropzone
        id="customdropzone"
        ref="myVueDropzone"
        class="dropzone"
        :use-custom-slot="true"
        :include-styling="false"
        :options="dropzoneOptions"
      >
        <div class="dropzone-custom-content">
          <i class="h3 text-muted dripicons-cloud-upload"></i>
          <h4>Drop files here or click to upload.</h4>
        </div>
      </vue-dropzone>
      <div id="file-previews" class="dropzone-previews mt-3"></div>

      <div class="card my-1 shadow-none border">
        <div class="p-2">
          <div class="row align-items-center">
            <div class="col-auto">
              <div class="avatar-sm">
                <span class="avatar-title rounded">.ZIP</span>
              </div>
            </div>
            <div class="col pl-0">
              <a
                href="javascript:void(0);"
                class="text-muted font-weight-bold"
              >Hyper-admin-design.zip</a>
              <p class="mb-0">2.3 MB</p>
            </div>
            <div class="col-auto">
              <!-- Button -->
              <a href="javascript:void(0);" class="btn btn-link btn-lg text-muted">
                <i class="dripicons-download"></i>
              </a>
            </div>
          </div>
        </div>
      </div>

      <div class="card mb-1 shadow-none border">
        <div class="p-2">
          <div class="row align-items-center">
            <div class="col-auto">
              <img
                src="@assets/images/projects/project-1.jpg"
                class="avatar-sm rounded"
                alt="file-image"
              />
            </div>
            <div class="col pl-0">
              <a href="javascript:void(0);" class="text-muted font-weight-bold">Dashboard-design.jpg</a>
              <p class="mb-0">3.25 MB</p>
            </div>
            <div class="col-auto">
              <!-- Button -->
              <a href="javascript:void(0);" class="btn btn-link btn-lg text-muted">
                <i class="dripicons-download"></i>
              </a>
            </div>
          </div>
        </div>
      </div>

      <div class="card mb-0 shadow-none border">
        <div class="p-2">
          <div class="row align-items-center">
            <div class="col-auto">
              <div class="avatar-sm">
                <span class="avatar-title bg-secondary rounded">.MP4</span>
              </div>
            </div>
            <div class="col pl-0">
              <a href="javascript:void(0);" class="text-muted font-weight-bold">Admin-bug-report.mp4</a>
              <p class="mb-0">7.05 MB</p>
            </div>
            <div class="col-auto">
              <!-- Button -->
              <a href="javascript:void(0);" class="btn btn-link btn-lg text-muted">
                <i class="dripicons-download"></i>
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>