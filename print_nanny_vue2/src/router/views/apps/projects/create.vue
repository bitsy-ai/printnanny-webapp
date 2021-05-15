<script>
import DatePicker from 'vue2-datepicker'
import vue2Dropzone from 'vue2-dropzone'

import appConfig from '@src/app.config'
import Layout from '@layouts/main'
import PageHeader from '@components/page-header'

/**
 * Create Project component
 */
export default {
  page: {
    title: 'Create Project',
    meta: [{ name: 'description', content: appConfig.description }],
  },
  components: { DatePicker, vueDropzone: vue2Dropzone, Layout, PageHeader },
  data() {
    return {
      title: 'Create Project',
      items: [
        {
          text: 'Hyper',
          href: '/',
        },
        {
          text: 'Projects',
          href: '/',
        },
        {
          text: 'Create Project',
          active: true,
        },
      ],
      startDate: '',
      dueDate: '',
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
            <div class="row">
              <div class="col-xl-6">
                <div class="form-group">
                  <label for="projectname">Name</label>
                  <input
                    id="projectname"
                    type="text"
                    class="form-control"
                    placeholder="Enter project name"
                  />
                </div>

                <div class="form-group">
                  <label for="project-overview">Overview</label>
                  <textarea
                    id="project-overview"
                    class="form-control"
                    rows="5"
                    placeholder="Enter some brief about project.."
                  ></textarea>
                </div>

                <!-- Date View -->
                <div class="form-group">
                  <label>Start Date</label>
                  <date-picker
                    v-model="startDate"
                    :first-day-of-week="1"
                    lang="en"
                    format="DD-MMM-YYYY"
                  ></date-picker>
                </div>

                <div class="form-group">
                  <label for="project-budget">Budget</label>
                  <input
                    id="project-budget"
                    type="text"
                    class="form-control"
                    placeholder="Enter project budget"
                  />
                </div>

                <div class="form-group mb-0">
                  <label for="project-overview">Team Members</label>

                  <select class="form-control select2" data-toggle="select2">
                    <option>Select</option>
                    <option value="AZ">Mary Scott</option>
                    <option value="CO">Holly Campbell</option>
                    <option value="ID">Beatrice Mills</option>
                    <option value="MT">Melinda Gills</option>
                    <option value="NE">Linda Garza</option>
                    <option value="NM">Randy Ortez</option>
                    <option value="ND">Lorene Block</option>
                    <option value="UT">Mike Baker</option>
                  </select>

                  <div class="mt-2">
                    <a
                      v-b-tooltip.hover
                      href="javascript:void(0);"
                      title="Mat Helme"
                      class="d-inline-block"
                    >
                      <img
                        src="@assets/images/users/avatar-6.jpg"
                        class="rounded-circle avatar-xs"
                        alt="friend"
                      />
                    </a>

                    <a
                      v-b-tooltip.hover
                      href="javascript:void(0);"
                      title="Michael Zenaty"
                      class="d-inline-block ml-1"
                    >
                      <img
                        src="@assets/images/users/avatar-7.jpg"
                        class="rounded-circle avatar-xs"
                        alt="friend"
                      />
                    </a>

                    <a
                      v-b-tooltip.hover
                      href="javascript:void(0);"
                      title="James Anderson"
                      class="d-inline-block ml-1"
                    >
                      <img
                        src="@assets/images/users/avatar-8.jpg"
                        class="rounded-circle avatar-xs"
                        alt="friend"
                      />
                    </a>

                    <a
                      v-b-tooltip.hover
                      href="javascript:void(0);"
                      title="Lorene Block"
                      class="d-inline-block ml-1"
                    >
                      <img
                        src="@assets/images/users/avatar-4.jpg"
                        class="rounded-circle avatar-xs"
                        alt="friend"
                      />
                    </a>

                    <a
                      v-b-tooltip.hover
                      href="javascript:void(0);"
                      title="Mike Baker"
                      class="d-inline-block ml-1"
                    >
                      <img
                        src="@assets/images/users/avatar-5.jpg"
                        class="rounded-circle avatar-xs"
                        alt="friend"
                      />
                    </a>
                  </div>
                </div>
              </div>
              <!-- end col-->

              <div class="col-xl-6">
                <div class="form-group mt-3 mt-xl-0">
                  <label for="projectname" class="mb-0">Avatar</label>
                  <p class="text-muted font-14">Recommended thumbnail size 800x400 (px).</p>

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
                </div>

                <!-- Date View -->
                <div class="form-group">
                  <label>Due Date</label>
                  <date-picker
                    v-model="dueDate"
                    :first-day-of-week="1"
                    lang="en"
                    format="DD-MMM-YYYY"
                  ></date-picker>
                </div>
              </div>
              <!-- end col-->
            </div>
            <!-- end row -->
          </div>
          <!-- end card-body -->
        </div>
        <!-- end card-->
      </div>
      <!-- end col-->
    </div>
    <!-- end row-->
  </Layout>
</template>