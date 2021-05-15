<script>
import VueSimplemde from 'vue-simplemde'

import appConfig from '@src/app.config'
import Layout from '@layouts/main'
import PageHeader from '@components/page-header'

import { emailData } from './data'

import Toolbar from '../toolbar'

/**
 * Inbox Component
 */
export default {
  page: {
    title: 'Inbox',
    meta: [{ name: 'description', content: appConfig.description }],
  },
  components: {
    VueSimplemde,
    Layout,
    PageHeader,
    Toolbar,
  },
  data() {
    return {
      emailData: emailData,
      title: 'Inbox',
      items: [
        {
          text: 'Hyper',
          href: '/',
        },
        {
          text: 'Email',
          href: '/',
        },
        {
          text: 'Inbox',
          active: true,
        },
      ],
      showModal: false,
      content: '',
      configs: {
        spellChecker: false,
        placeholder: 'Write something..',
        tabSize: 2,
        status: false,
        autosave: {
          enabled: false,
        },
      },
      // page number
      currentPage: 1,
      // default page size
      perPage: 15,

      // start and end index
      startIndex: 1,
      endIndex: 15,
    }
  },
  computed: {
    rows() {
      return this.emailData.length
    },
  },
  created() {
    this.startIndex = 0
    this.endIndex = this.perPage

    this.paginatedEmailData = this.emailData.slice(
      this.startIndex,
      this.endIndex
    )
  },
  methods: {
    /**
     * page change
     */
    onPageChange() {
      this.startIndex = (this.currentPage - 1) * this.perPage
      this.endIndex = (this.currentPage - 1) * this.perPage + this.perPage

      this.paginatedEmailData = this.emailData.slice(
        this.startIndex,
        this.endIndex
      )
    },
  },
}
</script>

<template>
  <Layout>
    <PageHeader :title="title" :items="items" />
    <div class="row">
      <!-- Right Sidebar -->
      <div class="col-12">
        <div class="card">
          <div class="card-body">
            <!-- Left sidebar -->
            <div class="page-aside-left">
              <button
                type="button"
                class="btn btn-danger btn-block"
                @click="showModal = true"
              >Compose</button>

              <div class="email-menu-list mt-3">
                <a href="javascript: void(0);" class="text-danger font-weight-bold">
                  <i class="dripicons-inbox mr-2"></i>Inbox
                  <span class="badge badge-danger-lighten float-right ml-2">7</span>
                </a>
                <a href="javascript: void(0);">
                  <i class="dripicons-star mr-2"></i>Starred
                </a>
                <a href="javascript: void(0);">
                  <i class="dripicons-clock mr-2"></i>Snoozed
                </a>
                <a href="javascript: void(0);">
                  <i class="dripicons-document mr-2"></i>Draft
                  <span class="badge badge-info-lighten float-right ml-2">32</span>
                </a>
                <a href="javascript: void(0);">
                  <i class="dripicons-exit mr-2"></i>Sent Mail
                </a>
                <a href="javascript: void(0);">
                  <i class="dripicons-trash mr-2"></i>Trash
                </a>
                <a href="javascript: void(0);">
                  <i class="dripicons-tag mr-2"></i>Important
                </a>
                <a href="javascript: void(0);">
                  <i class="dripicons-warning mr-2"></i>Spam
                </a>
              </div>

              <div class="mt-4">
                <h6 class="text-uppercase">Labels</h6>
                <div class="email-menu-list labels-list mt-2">
                  <a href="javascript: void(0);">
                    <i class="mdi mdi-circle font-13 text-info mr-2"></i>Updates
                  </a>
                  <a href="javascript: void(0);">
                    <i class="mdi mdi-circle font-13 text-warning mr-2"></i>Friends
                  </a>
                  <a href="javascript: void(0);">
                    <i class="mdi mdi-circle font-13 text-success mr-2"></i>Family
                  </a>
                  <a href="javascript: void(0);">
                    <i class="mdi mdi-circle font-13 text-primary mr-2"></i>Social
                  </a>
                  <a href="javascript: void(0);">
                    <i class="mdi mdi-circle font-13 text-danger mr-2"></i>Important
                  </a>
                  <a href="javascript: void(0);">
                    <i class="mdi mdi-circle font-13 text-secondary mr-2"></i>Promotions
                  </a>
                </div>
              </div>

              <div class="mt-5">
                <h4>
                  <span class="badge badge-pill p-1 px-2 badge-secondary-lighten">FREE</span>
                </h4>
                <h6 class="text-uppercase mt-3">Storage</h6>
                <b-progress height="5px" class="my-2" :value="46" variant="success"></b-progress>

                <p class="text-muted font-13 mb-0">7.02 GB (46%) of 15 GB used</p>
              </div>
            </div>
            <!-- end Left sidebar -->

            <div class="page-aside-right">
              <Toolbar />
              <div class="mt-3">
                <ul class="email-list">
                  <li
                    v-for="(email,index) in paginatedEmailData"
                    :key="index"
                    :class="{ 'unread': `${email.unread}` === 'true' }"
                  >
                    <div class="email-sender-info">
                      <div class="checkbox-wrapper-mail">
                        <div class="custom-control custom-checkbox">
                          <input :id="`mail${index}`" type="checkbox" class="custom-control-input" />
                          <label class="custom-control-label" :for="`mail${index}`"></label>
                        </div>
                      </div>
                      <span :class="`star-toggle mdi mdi-star-outline text-${email.text}`"></span>
                      <a href="javascript: void(0);" class="email-title">{{email.title}}</a>
                    </div>
                    <div class="email-content">
                      <a href="javascript: void(0);" class="email-subject">{{email.subject}}</a>
                      <div class="email-date">{{email.date}}</div>
                    </div>
                    <div class="email-action-icons">
                      <ul class="list-inline">
                        <li class="list-inline-item">
                          <a href="javascript: void(0);">
                            <i class="mdi mdi-archive email-action-icons-item"></i>
                          </a>
                        </li>
                        <li class="list-inline-item">
                          <a href="javascript: void(0);">
                            <i class="mdi mdi-delete email-action-icons-item"></i>
                          </a>
                        </li>
                        <li class="list-inline-item">
                          <a href="javascript: void(0);">
                            <i class="mdi mdi-email-open email-action-icons-item"></i>
                          </a>
                        </li>
                        <li class="list-inline-item">
                          <a href="javascript: void(0);">
                            <i class="mdi mdi-clock email-action-icons-item"></i>
                          </a>
                        </li>
                      </ul>
                    </div>
                  </li>
                </ul>
                <div class="row justify-content-md-between align-items-md-center">
                  <div class="col-xl-7">Showing {{startIndex}} - {{endIndex}} of {{rows}}</div>
                  <!-- end col-->
                  <div class="col-xl-5">
                    <!-- pagination -->
                    <div class="text-md-right float-md-right mt-2 pagination-rounded">
                      <b-pagination
                        v-model="currentPage"
                        :total-rows="rows"
                        :per-page="perPage"
                        @input="onPageChange"
                      ></b-pagination>
                    </div>
                    <!-- end pagination -->
                  </div>
                  <!-- end col-->
                </div>
              </div>
            </div>
            <!-- end inbox-rightbar-->
          </div>
        </div>
        <!-- end card -->
      </div>
      <!-- end col -->
    </div>
    <!-- end row -->

    <!-- Compose modal -->
    <b-modal
      v-model="showModal"
      title="New Message"
      title-tag="h4"
      header-class="modal-colored-header bg-primary"
      hide-footer
    >
      <div>
        <form class="p-1">
          <div class="form-group mb-2">
            <label for="msgto">To</label>
            <input id="msgto" type="text" class="form-control" placeholder="example@email.com" />
          </div>
          <div class="form-group mb-2">
            <label for="mailsubject">Subject</label>
            <input id="mailsubject" type="text" class="form-control" placeholder="your subject" />
          </div>
          <div class="form-group write-mdg-box mb-3">
            <label>Message</label>
            <vue-simplemde v-model="content" :configs="configs" />
          </div>

          <button type="button" class="btn btn-primary" @click="showModal = false">
            <i class="mdi mdi-send mr-1"></i> Send Message
          </button>
          <button type="button" class="btn btn-light ml-1" @click="showModal = false">Cancel</button>
        </form>
      </div>
    </b-modal>
    <!-- end modal -->
  </Layout>
</template>