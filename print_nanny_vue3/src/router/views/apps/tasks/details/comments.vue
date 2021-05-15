<template>
  <div class="card">
    <div class="card-header">
      <h4 class="my-1">Comments (51)</h4>
    </div>
    <div class="card-body">
      <b-media>
        <template v-slot:aside>
          <img
            class="mr-2 rounded-circle"
            src="@assets/images/users/avatar-3.jpg"
            alt="Generic placeholder image"
            height="32"
          />
        </template>
        <h5 class="mt-0">
          Jeremy Tomlinson
          <small class="text-muted float-right">5 hours ago</small>
        </h5>Nice work, makes me think of The Money Pit.
        <br />
        <a href="javascript: void(0);" class="text-muted font-13 d-inline-block mt-2">
          <i class="mdi mdi-reply"></i> Reply
        </a>

        <b-media class="mt-3">
          <template v-slot:aside>
            <a class="pr-2" href="#">
              <img
                src="@assets/images/users/avatar-4.jpg"
                class="rounded-circle"
                alt="Generic placeholder image"
                height="32"
              />
            </a>
          </template>
          <h5 class="mt-0">
            Thelma Fridley
            <small class="text-muted float-right">3 hours ago</small>
          </h5>i'm in the middle of a timelapse animation myself! (Very different though.) Awesome stuff.
          <br />
          <a href="javascript: void(0);" class="text-muted font-13 d-inline-block mt-2">
            <i class="mdi mdi-reply"></i> Reply
          </a>
        </b-media>
      </b-media>

      <b-media class="mt-3">
        <template v-slot:aside>
          <img
            class="mr-2 rounded-circle"
            src="@assets/images/users/avatar-5.jpg"
            alt="Generic placeholder image"
            height="32"
          />
        </template>
        <h5 class="mt-0">
          Kevin Martinez
          <small class="text-muted float-right">1 day ago</small>
        </h5>It would be very nice to have.
        <br />
        <a href="javascript: void(0);" class="text-muted font-13 d-inline-block mt-2">
          <i class="mdi mdi-reply"></i> Reply
        </a>
      </b-media>

      <div class="text-center mt-2">
        <a href="javascript:void(0);" class="text-danger">
          <i class="mdi mdi-spin mdi-loading mr-1"></i> Load more
        </a>
      </div>

      <div class="border rounded mt-4">
        <form action="#" class="comment-area-box">
          <textarea
            rows="3"
            class="form-control border-0 resize-none"
            placeholder="Your comment..."
          ></textarea>
          <div class="p-2 bg-light d-flex justify-content-between align-items-center">
            <div>
              <a href="#" class="btn btn-sm px-1 btn-light">
                <i class="mdi mdi-upload"></i>
              </a>
              <a href="#" class="btn btn-sm px-1 btn-light">
                <i class="mdi mdi-at"></i>
              </a>
            </div>
            <button type="submit" class="btn btn-sm btn-success">
              <i class="uil uil-message mr-1"></i>Submit
            </button>
          </div>
        </form>
      </div>
      <!-- end .border-->
    </div>
    <!-- end card-body-->
  </div>
  <!-- end card-->
</template>