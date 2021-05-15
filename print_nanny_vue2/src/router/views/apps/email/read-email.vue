<script>
import VueSimplemde from 'vue-simplemde'

import appConfig from '@src/app.config'
import Layout from '@layouts/main'
import PageHeader from '@components/page-header'

import Toolbar from './toolbar'

/**
 * Email Read component
 */
export default {
  page: {
    title: 'Email Read',
    meta: [{ name: 'description', content: appConfig.description }],
  },
  components: { VueSimplemde, Layout, PageHeader, Toolbar },
  data() {
    return {
      title: 'Email Read',
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
          text: 'Email Read',
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
    }
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
            <!-- End Left sidebar -->

            <div class="page-aside-right">
              <Toolbar />
              <div class="mt-3">
                <h5 class="font-18">Your elite author Graphic Optimization reward is ready!</h5>

                <hr />

                <div class="media mb-3 mt-1">
                  <img
                    class="d-flex mr-2 rounded-circle"
                    src="@assets/images/users/avatar-2.jpg"
                    alt="placeholder image"
                    height="32"
                  />
                  <div class="media-body">
                    <small class="float-right">Dec 14, 2017, 5:17 AM</small>
                    <h6 class="m-0 font-14">Steven Smith</h6>
                    <small class="text-muted">From: jonathan@domain.com</small>
                  </div>
                </div>

                <p>Hi Coderthemes!</p>
                <p>Clicking ‘Order Service’ on the right-hand side of the above page will present you with an order page. This service has the following Briefing Guidelines that will need to be filled before placing your order:</p>
                <ol>
                  <li>Your design preferences (Color, style, shapes, Fonts, others)</li>
                  <li>Tell me, why is your item different?</li>
                  <li>Do you want to bring up a specific feature of your item? If yes, please tell me</li>
                  <li>Do you have any preference or specific thing you would like to change or improve on your item page?</li>
                  <li>Do you want to include your item's or your provider's logo on the page? if yes, please send it to me in vector format (Ai or EPS)</li>
                  <li>Please provide me with the copy or text to display</li>
                </ol>

                <p>Filling in this form with the above information will ensure that they will be able to start work quickly.</p>
                <p>You can complete your order by putting your coupon code into the Promotional code box and clicking ‘Apply Coupon’.</p>
                <p>
                  <b>Best,</b>
                  <br />Graphic Studio
                </p>
                <hr />

                <h5 class="mb-3">Attachments</h5>

                <div class="row">
                  <div class="col-xl-4">
                    <div class="card mb-1 shadow-none border">
                      <div class="p-2">
                        <div class="row align-items-center">
                          <div class="col-auto">
                            <div class="avatar-sm">
                              <span
                                class="avatar-title bg-primary-lighten text-primary rounded"
                              >.ZIP</span>
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
                  </div>
                  <!-- end col -->
                  <div class="col-xl-4">
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
                            <a
                              href="javascript:void(0);"
                              class="text-muted font-weight-bold"
                            >Dashboard-design.jpg</a>
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
                  </div>
                  <!-- end col -->
                  <div class="col-xl-4">
                    <div class="card mb-0 shadow-none border">
                      <div class="p-2">
                        <div class="row align-items-center">
                          <div class="col-auto">
                            <div class="avatar-sm">
                              <span class="avatar-title bg-secondary rounded">.MP4</span>
                            </div>
                          </div>
                          <div class="col pl-0">
                            <a
                              href="javascript:void(0);"
                              class="text-muted font-weight-bold"
                            >Admin-bug-report.mp4</a>
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
                  <!-- end col -->
                </div>
                <!-- end row-->

                <div class="mt-5">
                  <a href class="btn btn-secondary mr-2">
                    <i class="mdi mdi-reply mr-1"></i> Reply
                  </a>
                  <a href class="btn btn-light">
                    Forward
                    <i class="mdi mdi-forward ml-1"></i>
                  </a>
                </div>
              </div>
              <!-- end .mt-4 -->
            </div>
            <!-- end inbox-rightbar-->
          </div>

          <div class="clearfix"></div>
        </div>
        <!-- end card-box -->
      </div>
      <!-- end Col -->
    </div>
    <!-- End row -->

    <!-- compose modal -->
    <b-modal
      v-model="showModal"
      title="New Message"
      title-tag="h4"
      header-class="modal-colored-header bg-primary"
      hide-footer
    >
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
    </b-modal>
    <!-- end modal -->
  </Layout>
</template>