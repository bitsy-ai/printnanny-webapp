<script>
import appConfig from '@src/app.config'
import Layout from '@layouts/main'
import PageHeader from '@components/page-header'

/**
 * Social-feed component
 */
export default {
  page: {
    title: 'Social',
    meta: [{ name: 'description', content: appConfig.description }],
  },
  components: { Layout, PageHeader },
  data() {
    return {
      title: 'Social',
      items: [
        {
          text: 'Hyper',
          href: '/',
        },
        {
          text: 'Social',
          href: '/',
        },
        {
          text: 'Feed',
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
      <div class="col-xl-3 col-lg-6 order-lg-1 order-xl-1">
        <!-- start profile info -->
        <div class="card">
          <div class="card-body">
            <b-dropdown
              class="float-right"
              variant="black"
              right
              toggle-class="arrow-none card-drop p-0"
            >
              <template v-slot:button-content>
                <i class="mdi mdi-dots-horizontal"></i>
              </template>
              <!-- item-->
              <a href="javascript:void(0);" class="dropdown-item">Edit Profile</a>
              <!-- item-->
              <a href="javascript:void(0);" class="dropdown-item">Settings</a>
            </b-dropdown>
            <b-media>
              <template v-slot:aside>
                <img
                  class="d-flex align-self-start rounded mr-2"
                  src="@assets/images/users/avatar-5.jpg"
                  alt="Dominic Keller"
                  height="48"
                />
              </template>
              <h5 class="mt-1 mb-0">Dominic Keller</h5>
              <p class="mb-1 mt-1 text-muted">California, USA</p>
            </b-media>

            <div class="list-group list-group-flush mt-2">
              <a
                href="javascript:void(0);"
                class="list-group-item list-group-item-action text-primary border-0"
              >
                <i class="uil uil-images mr-1"></i> News Feed
              </a>
              <a href="javascript:void(0);" class="list-group-item list-group-item-action border-0">
                <i class="uil uil-comment-alt-message mr-1"></i> Messages
              </a>
              <a href="javascript:void(0);" class="list-group-item list-group-item-action border-0">
                <i class="uil uil-calendar-alt mr-1"></i> Events
              </a>
              <a href="javascript:void(0);" class="list-group-item list-group-item-action border-0">
                <i class="uil uil-users-alt mr-1"></i> Groups
              </a>
              <a href="javascript:void(0);" class="list-group-item list-group-item-action border-0">
                <i class="uil uil-copy mr-1"></i> Pages
              </a>
            </div>
          </div>
        </div>
        <!-- end profile info -->

        <!-- event info -->
        <div class="card">
          <div class="card-body p-2">
            <div class="list-group list-group-flush my-2">
              <a href="javascript:void(0);" class="list-group-item list-group-item-action border-0">
                <i class="uil uil-calendar-alt mr-1"></i> 3 events this week
              </a>
              <a href="javascript:void(0);" class="list-group-item list-group-item-action border-0">
                <i class="uil uil-calender mr-1"></i> Eva's birthday today
              </a>
              <a href="javascript:void(0);" class="list-group-item list-group-item-action border-0">
                <i class="uil uil-bookmark mr-1"></i> Jenny's wedding tomorrow
              </a>
            </div>
          </div>
        </div>
        <!-- end event info -->

        <!-- news -->
        <div class="card">
          <div class="card-body">
            <b-dropdown
              class="float-right"
              toggle-class="arrow-none card-drop p-0"
              right
              variant="black"
            >
              <template v-slot:button-content>
                <i class="mdi mdi-dots-horizontal"></i>
              </template>

              <!-- item-->
              <a href="javascript:void(0);" class="dropdown-item">Today</a>
              <!-- item-->
              <a href="javascript:void(0);" class="dropdown-item">Yesterday</a>
              <!-- item-->
              <a href="javascript:void(0);" class="dropdown-item">Last Week</a>
              <!-- item-->
              <a href="javascript:void(0);" class="dropdown-item">Last Month</a>
            </b-dropdown>

            <h4 class="header-title mb-1">Trending</h4>
            <b-media class="mt-3">
              <template v-slot:aside>
                <i class="uil uil-arrow-growth mr-2 font-18 text-primary"></i>
              </template>
              <a class="mt-1 font-14" href="javascript:void(0);">
                <strong>Golden Globes:</strong>
                <span class="text-muted">The 27 Best moments from the Golden Globe Awards</span>
              </a>
            </b-media>

            <b-media class="mt-3">
              <template v-slot:aside>
                <i class="uil uil-arrow-growth mr-2 font-18 text-primary"></i>
              </template>
              <a class="mt-1 font-14" href="javascript:void(0);">
                <strong>World Cricket:</strong>
                <span class="text-muted">India has won ICC T20 World Cup Yesterday</span>
              </a>
            </b-media>

            <b-media class="mt-3">
              <template v-slot:aside>
                <i class="uil uil-arrow-growth mr-2 font-18 text-primary"></i>
              </template>
              <a class="mt-1 font-14" href="javascript:void(0);">
                <strong>Antartica:</strong>
                <span
                  class="text-muted"
                >Metling of Totten Glacier could cause high risk to areas near by sea</span>
              </a>
            </b-media>
          </div>
          <!-- end card-body-->
        </div>
        <!-- end card-->
      </div>
      <!-- end col -->

      <div class="col-xl-6 col-lg-12 order-lg-2 order-xl-1">
        <!-- new post -->
        <div class="card">
          <div class="card-body p-0">
            <b-tabs nav-class="nav-tabs nav-bordered" content-class="p-3">
              <b-tab title-link-class="px-3 py-2">
                <template v-slot:title>
                  <i class="mdi mdi-pencil-box-multiple font-18 d-md-none d-block"></i>
                  <span class="d-none d-sm-inline-block">Create Post</span>
                </template>
                <div class="border rounded">
                  <form action="#" class="comment-area-box">
                    <textarea
                      rows="4"
                      class="form-control border-0 resize-none"
                      placeholder="Write something...."
                    ></textarea>
                    <div class="p-2 bg-light d-flex justify-content-between align-items-center">
                      <div>
                        <a href="#" class="btn btn-sm px-2 font-16 btn-light">
                          <i class="uil uil-scenery"></i>
                        </a>
                        <a href="#" class="btn btn-sm px-2 font-16 btn-light">
                          <i class="uil uil-location"></i>
                        </a>
                        <a href="#" class="btn btn-sm px-2 font-16 btn-light">
                          <i class="uil uil-paperclip"></i>
                        </a>
                      </div>
                      <button type="submit" class="btn btn-sm btn-success">
                        <i class="uil uil-message mr-1"></i>Post
                      </button>
                    </div>
                  </form>
                </div>
              </b-tab>
              <b-tab title-link-class="px-3 py-2">
                <template v-slot:title>
                  <i class="mdi mdi-image font-18 d-md-none d-block"></i>
                  <span class="d-none d-md-block">Photos/Videos</span>
                </template>
                <div class="border rounded">
                  <form action="#" class="comment-area-box">
                    <textarea
                      rows="4"
                      class="form-control border-0 resize-none"
                      placeholder="Write something...."
                    ></textarea>
                    <div class="p-2 bg-light d-flex justify-content-between align-items-center">
                      <div>
                        <a href="#" class="btn btn-sm px-2 font-16 btn-light">
                          <i class="uil uil-scenery"></i>
                        </a>
                        <a href="#" class="btn btn-sm px-2 font-16 btn-light">
                          <i class="uil uil-location"></i>
                        </a>
                        <a href="#" class="btn btn-sm px-2 font-16 btn-light">
                          <i class="uil uil-paperclip"></i>
                        </a>
                      </div>
                      <button type="submit" class="btn btn-sm btn-success">
                        <i class="uil uil-message mr-1"></i>Post
                      </button>
                    </div>
                  </form>
                </div>
              </b-tab>
              <b-tab title-link-class="px-3 py-2">
                <template v-slot:title>
                  <i class="mdi mdi-book-open-variant font-18 d-md-none d-block"></i>
                  <span class="d-none d-md-block">Story</span>
                </template>
                <div class="border rounded">
                  <form action="#" class="comment-area-box">
                    <textarea
                      rows="4"
                      class="form-control border-0 resize-none"
                      placeholder="Write something...."
                    ></textarea>
                    <div class="p-2 bg-light d-flex justify-content-between align-items-center">
                      <div>
                        <a href="#" class="btn btn-sm px-2 font-16 btn-light">
                          <i class="uil uil-scenery"></i>
                        </a>
                        <a href="#" class="btn btn-sm px-2 font-16 btn-light">
                          <i class="uil uil-location"></i>
                        </a>
                        <a href="#" class="btn btn-sm px-2 font-16 btn-light">
                          <i class="uil uil-paperclip"></i>
                        </a>
                      </div>
                      <button type="submit" class="btn btn-sm btn-success">
                        <i class="uil uil-message mr-1"></i>Post
                      </button>
                    </div>
                  </form>
                </div>
              </b-tab>
            </b-tabs>
            <!-- end tabs -->
          </div>
          <!-- end card-body -->
        </div>
        <!-- end new post -->

        <!-- start news feeds -->
        <div class="card">
          <div class="card-body pb-1">
            <b-media>
              <template v-slot:aside>
                <img
                  class="mr-2 rounded"
                  src="@assets/images/users/avatar-3.jpg"
                  alt="Generic placeholder image"
                  height="32"
                />
              </template>

              <b-dropdown
                class="float-right text-muted"
                variant="black"
                right
                toggle-class="arrow-none card-drop p-0"
              >
                <template v-slot:button-content>
                  <i class="mdi mdi-dots-horizontal"></i>
                </template>
                <!-- item-->
                <a href="javascript:void(0);" class="dropdown-item">Edit</a>
                <!-- item-->
                <a href="javascript:void(0);" class="dropdown-item">Delete</a>
              </b-dropdown>
              <h5 class="m-0">Jeremy Tomlinson</h5>
              <p class="text-muted">
                <small>
                  about 2 minuts ago
                  <span class="mx-1">⚬</span>
                  <span>Public</span>
                </small>
              </p>
            </b-media>

            <hr class="m-0" />

            <div class="font-16 text-center text-dark my-3">
              <i class="mdi mdi-format-quote-open font-20"></i> Leave one wolf alive and the sheep are never safe. When people ask you
              what happened here, tell them the North remembers. Tell them winter came for
              House Frey.
            </div>

            <hr class="m-0" />

            <div class="my-1">
              <a href="javascript: void(0);" class="btn btn-sm btn-link text-muted pl-0">
                <i class="mdi mdi-heart text-danger"></i> 2k Likes
              </a>
              <a href="javascript: void(0);" class="btn btn-sm btn-link text-muted">
                <i class="uil uil-comments-alt"></i> 200 Comments
              </a>
              <a href="javascript: void(0);" class="btn btn-sm btn-link text-muted">
                <i class="uil uil-share-alt"></i> Share
              </a>
            </div>

            <hr class="m-0" />

            <div class="mt-3">
              <b-media>
                <template v-slot:aside>
                  <img
                    class="mr-2 rounded"
                    src="@assets/images/users/avatar-9.jpg"
                    alt="Generic placeholder image"
                    height="32"
                  />
                </template>
                <h5 class="m-0">Sansa Stark</h5>
                <p class="text-muted mb-0">
                  <small>2 mins ago</small>
                </p>

                <p class="my-1">
                  This is awesome! Proud of sis :) Waiting for you to
                  come back to winterfall
                </p>

                <div>
                  <a href="javascript: void(0);" class="btn btn-sm btn-link text-muted p-0">
                    <i class="uil uil-heart mr-1"></i> Like
                  </a>
                  <a href="javascript: void(0);" class="btn btn-sm btn-link text-muted p-0 pl-2">
                    <i class="uil uil-comments-alt mr-1"></i> Reply
                  </a>
                </div>
                <b-media class="mt-3">
                  <template v-slot:aside>
                    <img
                      class="mr-2 rounded"
                      src="@assets/images/users/avatar-8.jpg"
                      alt="Generic placeholder image"
                      height="32"
                    />
                  </template>
                  <h5 class="m-0">Cersei Lannister</h5>
                  <p class="text-muted mb-0">
                    <small>1 min ago</small>
                  </p>

                  <p class="my-1">I swear! She won't be able to reach to winterfall</p>
                </b-media>
                <!-- end media-->
              </b-media>
              <!-- end media-->

              <hr />
              <b-media class="mb-2">
                <template v-slot:aside>
                  <img
                    src="@assets/images/users/avatar-1.jpg"
                    height="32"
                    class="align-self-start rounded mr-2"
                    alt="Arya Stark"
                  />
                </template>
                <input
                  type="text"
                  class="form-control border-0 form-control-sm"
                  placeholder="Write a comment"
                />
                <!-- end medi-body -->
              </b-media>
              <!-- end media-->
            </div>
          </div>
          <!-- end card-body -->
        </div>
        <!-- end card -->

        <div class="card">
          <div class="card-body pb-1">
            <b-media>
              <template v-slot:aside>
                <img
                  class="mr-2 rounded"
                  src="@assets/images/users/avatar-5.jpg"
                  alt="Generic placeholder image"
                  height="32"
                />
              </template>

              <b-dropdown
                class="float-right text-muted"
                variant="black"
                right
                toggle-class="arrow-none card-drop p-0"
              >
                <template v-slot:button-content>
                  <i class="mdi mdi-dots-horizontal"></i>
                </template>
                <!-- item-->
                <a href="javascript:void(0);" class="dropdown-item">Edit</a>
                <!-- item-->
                <a href="javascript:void(0);" class="dropdown-item">Delete</a>
              </b-dropdown>
              <h5 class="m-0">Jon Snow</h5>
              <p class="text-muted">
                <small>
                  20 min ago
                  <span class="mx-1">⚬</span>
                  <span>Public</span>
                </small>
              </p>
            </b-media>
            <!-- end media -->

            <hr class="m-0" />

            <div class="my-3">
              <p>"Feeling awesome at the wall!"</p>
              <div class="row">
                <div class="col-sm-8">
                  <img
                    src="@assets/images/small/small-4.jpg"
                    alt="post-img"
                    class="rounded mr-1 mb-3 mb-sm-0 img-fluid"
                  />
                </div>
                <div class="col">
                  <img
                    src="@assets/images/small/small-2.jpg"
                    alt="post-img"
                    class="rounded mr-1 img-fluid mb-3"
                  />
                  <img
                    src="@assets/images/small/small-3.jpg"
                    alt="post-img"
                    class="rounded mr-1 img-fluid"
                  />
                </div>
              </div>
            </div>

            <div class="mt-1 mb-1">
              <a href="javascript: void(0);" class="btn btn-sm btn-link text-muted pl-0">
                <i class="mdi mdi-heart text-danger"></i> 1.2k Likes
              </a>
              <a href="javascript: void(0);" class="btn btn-sm btn-link text-muted">
                <i class="uil uil-comments-alt"></i> 148 Comments
              </a>
              <a href="javascript: void(0);" class="btn btn-sm btn-link text-muted">
                <i class="uil uil-share-alt"></i> Share
              </a>
            </div>
            <hr class="m-0" />

            <div class="mt-3">
              <b-media>
                <template v-slot:aside>
                  <img
                    class="mr-2 rounded"
                    src="@assets/images/users/avatar-9.jpg"
                    alt="Generic placeholder image"
                    height="32"
                  />
                </template>
                <h5 class="m-0">Sansa Stark</h5>
                <p class="text-muted mb-0">
                  <small>2 mins ago</small>
                </p>

                <p class="my-1">
                  This is awesome! Proud of sis :) Waiting for you to
                  come back to winterfall
                </p>

                <div>
                  <a href="javascript: void(0);" class="btn btn-sm btn-link text-muted p-0">
                    <i class="uil uil-heart mr-1"></i> Like
                  </a>
                  <a href="javascript: void(0);" class="btn btn-sm btn-link text-muted p-0 pl-2">
                    <i class="uil uil-comments-alt mr-1"></i> Reply
                  </a>
                </div>
              </b-media>
              <!-- end media-->

              <hr />
              <b-media class="mb-2">
                <template v-slot:aside>
                  <img
                    src="@assets/images/users/avatar-1.jpg"
                    height="32"
                    class="align-self-start rounded mr-2"
                    alt="Arya Stark"
                  />
                </template>
                <input
                  type="text"
                  class="form-control border-0 form-control-sm"
                  placeholder="Write a comment"
                />
              </b-media>
              <!-- end media-->
            </div>
          </div>
          <!-- end card-body -->
        </div>
        <!-- end card -->
        <!-- end news feeds -->

        <!-- loader -->
        <div class="text-center mb-3">
          <a href="javascript:void(0);" class="text-danger">
            <i class="mdi mdi-spin mdi-loading mr-1 font-16"></i> Load more
          </a>
        </div>
        <!-- end loader -->
      </div>

      <div class="col-xl-3 col-lg-6 order-lg-1 order-xl-2">
        <!-- video -->
        <div class="card">
          <div class="card-body">
            <b-dropdown
              class="float-right"
              variant="black"
              right
              toggle-class="arrow-none card-drop p-0"
            >
              <template v-slot:button-content>
                <i class="mdi mdi-dots-horizontal"></i>
              </template>
              <!-- item-->
              <a href="javascript:void(0);" class="dropdown-item">Today</a>
              <!-- item-->
              <a href="javascript:void(0);" class="dropdown-item">Yesterday</a>
              <!-- item-->
              <a href="javascript:void(0);" class="dropdown-item">Last Week</a>
              <!-- item-->
              <a href="javascript:void(0);" class="dropdown-item">Last Month</a>
            </b-dropdown>

            <h4 class="header-title mb-1">Featured Video For You</h4>

            <div class="mt-3">
              <div class="embed-responsive embed-responsive-16by9">
                <iframe
                  class="embed-responsive-item"
                  src="https://www.youtube.com/embed/9_eqq0HlN9g?autohide=0&showinfo=0&controls=0"
                ></iframe>
              </div>
            </div>
          </div>
          <!-- end card-body -->
        </div>
        <!-- end video -->

        <!-- video -->
        <div class="card">
          <div class="card-body pb-0">
            <b-dropdown
              class="float-right"
              variant="black"
              right
              toggle-class="arrow-none card-drop p-0"
            >
              <template v-slot:button-content>
                <i class="mdi mdi-dots-horizontal"></i>
              </template>
              <!-- item-->
              <a href="javascript:void(0);" class="dropdown-item">View All</a>
            </b-dropdown>
            <h4 class="header-title mb-3">People you may know</h4>

            <div class="inbox-widget">
              <div class="inbox-item">
                <div class="inbox-item-img">
                  <img src="@assets/images/users/avatar-2.jpg" class="rounded-circle" alt />
                </div>
                <p class="inbox-item-author">Robb Stark</p>
                <p class="inbox-item-text">The first king in the North</p>
                <p class="inbox-item-date">
                  <button type="button" class="btn btn-sm btn-outline-primary px-1 py-0">
                    <i class="uil uil-user-plus font-16"></i>
                  </button>
                </p>
              </div>
              <div class="inbox-item">
                <div class="inbox-item-img">
                  <img src="@assets/images/users/avatar-3.jpg" class="rounded-circle" alt />
                </div>
                <p class="inbox-item-author">Stillnot David</p>
                <p class="inbox-item-text">Lady of winterfall</p>
                <p class="inbox-item-date">
                  <button type="button" class="btn btn-sm btn-outline-primary px-1 py-0">
                    <i class="uil uil-user-plus font-16"></i>
                  </button>
                </p>
              </div>
              <div class="inbox-item">
                <div class="inbox-item-img">
                  <img src="@assets/images/users/avatar-4.jpg" class="rounded-circle" alt />
                </div>
                <p class="inbox-item-author">Cersei Lannister</p>
                <p class="inbox-item-text">Queen of the Seven Kingdoms</p>
                <p class="inbox-item-date">
                  <button type="button" class="btn btn-sm btn-outline-primary px-1 py-0">
                    <i class="uil uil-user-plus font-16"></i>
                  </button>
                </p>
              </div>

              <div class="inbox-item">
                <div class="inbox-item-img">
                  <img src="@assets/images/users/avatar-5.jpg" class="rounded-circle" alt />
                </div>
                <p class="inbox-item-author">Daenerys Targaryen</p>
                <p class="inbox-item-text">Hey! there I'm available...</p>
                <p class="inbox-item-date">
                  <button type="button" class="btn btn-sm btn-outline-primary px-1 py-0">
                    <i class="uil uil-user-plus font-16"></i>
                  </button>
                </p>
              </div>
              <div class="inbox-item">
                <div class="inbox-item-img">
                  <img src="@assets/images/users/avatar-6.jpg" class="rounded-circle" alt />
                </div>
                <p class="inbox-item-author">Adhamd Annaway</p>
                <p class="inbox-item-text">Queen Daenerys</p>
                <p class="inbox-item-date">
                  <button type="button" class="btn btn-sm btn-outline-primary px-1 py-0">
                    <i class="uil uil-user-plus font-16"></i>
                  </button>
                </p>
              </div>
            </div>
            <!-- end inbox-widget -->

            <div class="mt-2 mb-3 text-center">
              <a href>
                View More
                <i class="uil uil-arrow-right ml-1"></i>
              </a>
            </div>
          </div>
          <!-- end card-body -->
        </div>
        <!-- end video -->
      </div>
      <!-- end col -->
    </div>
    <!--end row -->
  </Layout>
</template>