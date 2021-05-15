<script>
import appConfig from '@src/app.config'
import Layout from '@layouts/main'
import PageHeader from '@components/page-header'

import { projects, projectImage } from './data'

export default {
  page: {
    title: 'Projects',
    meta: [{ name: 'description', content: appConfig.description }],
  },
  components: {
    Layout,
    PageHeader,
  },
  data() {
    return {
      projects: projects,
      projectImage: projectImage,
      title: 'Projects',
      items: [
        {
          text: 'Hyper',
          href: '/',
        },
        {
          text: 'Apps',
          href: '/',
        },
        {
          text: 'Projects',
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
    <div class="row mb-2">
      <div class="col-sm-4">
        <router-link tag="a" to="/apps/projects/create" class="btn btn-danger btn-rounded mb-3">
          <i class="mdi mdi-plus"></i> Create Project
        </router-link>
      </div>
      <div class="col-sm-8">
        <div class="text-sm-right">
          <div class="btn-group mb-3">
            <button type="button" class="btn btn-primary">All</button>
          </div>
          <div class="btn-group mb-3 ml-1">
            <button type="button" class="btn btn-light">Ongoing</button>
            <button type="button" class="btn btn-light">Finished</button>
          </div>
          <div class="btn-group mb-3 ml-2 d-none d-sm-inline-block">
            <button type="button" class="btn btn-secondary">
              <i class="dripicons-view-apps"></i>
            </button>
          </div>
          <div class="btn-group mb-3 d-none d-sm-inline-block">
            <button type="button" class="btn btn-link text-muted">
              <i class="dripicons-checklist"></i>
            </button>
          </div>
        </div>
      </div>
      <!-- end col-->
    </div>
    <div class="row">
      <div v-for="data of projects" :key="data.title" class="col-md-6 col-xl-3">
        <div class="card d-block">
          <div class="card-body">
            <b-dropdown
              class="card-widgets"
              right
              variant="black"
              toggle-tag="a"
              toggle-class="arrow-none p-0"
            >
              <template v-slot:button-content>
                <i class="dripicons-dots-3"></i>
              </template>
              <!-- item-->
              <a href="javascript:void(0);" class="dropdown-item">
                <i class="mdi mdi-pencil mr-1"></i>Edit
              </a>
              <!-- item-->
              <a href="javascript:void(0);" class="dropdown-item">
                <i class="mdi mdi-delete mr-1"></i>Delete
              </a>
              <!-- item-->
              <a href="javascript:void(0);" class="dropdown-item">
                <i class="mdi mdi-email-outline mr-1"></i>Invite
              </a>
              <!-- item-->
              <a href="javascript:void(0);" class="dropdown-item">
                <i class="mdi mdi-exit-to-app mr-1"></i>Leave
              </a>
            </b-dropdown>
            <!-- project title-->
            <h4 class="mt-0">
              <router-link tag="a" to="/apps/projects/details" class="text-title">{{ data.title }}</router-link>
            </h4>
            <div class="badge badge-success mb-3">{{ data.status }}</div>

            <p class="text-muted font-13 mb-3">
              {{ data.description }}
              <a
                href="javascript:void(0);"
                class="font-weight-bold text-muted"
              >view more</a>
            </p>

            <!-- project detail-->
            <p class="mb-1">
              <span class="pr-2 text-nowrap mb-2 d-inline-block">
                <i class="mdi mdi-format-list-bulleted-type text-muted"></i>
                <b>{{data.tasks}}</b> Tasks
              </span>
              <span class="text-nowrap mb-2 d-inline-block">
                <i class="mdi mdi-comment-multiple-outline text-muted"></i>
                <b>{{data.comments}}</b> Comments
              </span>
            </p>
            <div>
              <a
                v-b-tooltip.top
                :title="`${data.name[0]}`"
                href="javascript:void(0);"
                class="d-inline-block"
              >
                <img :src="`${data.images[0]}`" class="rounded-circle avatar-xs" alt="friend" />
              </a>

              <a
                v-b-tooltip.top
                :title="`${data.name[1]}`"
                href="javascript:void(0);"
                class="d-inline-block"
              >
                <img :src="`${data.images[1]}`" class="rounded-circle avatar-xs ml-1" alt="friend" />
              </a>

              <a
                v-if="data.images[2]"
                v-b-tooltip.top
                :title="`${data.name[2]}`"
                href="javascript:void(0);"
                class="d-inline-block"
              >
                <img :src="`${data.images[2]}`" class="rounded-circle avatar-xs ml-1" alt="friend" />
              </a>
              <a
                href="javascript:void(0);"
                class="d-inline-block text-muted font-weight-bold ml-2"
              >{{data.text}}</a>
            </div>
          </div>
          <ul class="list-group list-group-flush">
            <li class="list-group-item p-3">
              <!-- project progress-->
              <p class="mb-2 font-weight-bold">
                Progress
                <span class="float-right">{{data.progressValue}}%</span>
              </p>
              <b-progress :value="data.progressValue" height="5px"></b-progress>
            </li>
          </ul>
        </div>
      </div>
    </div>

    <div class="row">
      <div v-for="data of projectImage" :key="data.title" class="col-md-6 col-xl-3">
        <!-- project card -->
        <div class="card d-block">
          <!-- project-thumbnail -->
          <img class="card-img-top" :src="`${data.product}`" alt="project image cap" />
          <div class="card-img-overlay">
            <div class="badge badge-secondary p-1">{{data.status}}</div>
          </div>

          <div class="card-body position-relative">
            <!-- project title-->
            <h4 class="mt-0">
              <router-link tag="a" to="/apps/projects/details" class="text-title">{{data.title}}</router-link>
            </h4>

            <!-- project detail-->
            <p class="mb-3">
              <span class="pr-2 text-nowrap">
                <i class="mdi mdi-format-list-bulleted-type"></i>
                <b>{{data.tasks}}</b> Tasks
              </span>
              <span class="text-nowrap">
                <i class="mdi mdi-comment-multiple-outline"></i>
                <b>{{data.comments}}</b> Comments
              </span>
            </p>
            <div class="mb-3">
              <a
                v-b-tooltip.top
                :title="`${data.name[0]}`"
                href="javascript:void(0);"
                class="d-inline-block"
              >
                <img :src="`${data.images[0]}`" class="rounded-circle avatar-xs" alt="friend" />
              </a>

              <a
                v-b-tooltip.top
                :title="`${data.name[1]}`"
                href="javascript:void(0);"
                class="d-inline-block"
              >
                <img :src="`${data.images[1]}`" class="rounded-circle avatar-xs ml-1" alt="friend" />
              </a>

              <a
                v-if="data.images[2]"
                v-b-tooltip.top
                :title="`${data.name[2]}`"
                href="javascript:void(0);"
                class="d-inline-block"
              >
                <img :src="`${data.images[2]}`" class="rounded-circle avatar-xs ml-1" alt="friend" />
              </a>
            </div>

            <!-- project progress-->
            <p class="mb-2 font-weight-bold">
              Progress
              <span class="float-right">{{data.progressValue}}%</span>
            </p>
            <b-progress :value="data.progressValue" height="5px"></b-progress>
          </div>
          <!-- end card-body-->
        </div>
        <!-- end card-->
      </div>
      <!-- end col -->
    </div>
  </Layout>
</template>