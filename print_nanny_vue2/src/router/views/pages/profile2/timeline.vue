<template>
  <div>
    <div class="border rounded mt-3 mb-3">
      <form action="#" class="comment-area-box">
        <textarea
          rows="3"
          class="form-control border-0 resize-none"
          placeholder="Write something...."
        ></textarea>
        <div class="p-2 bg-light d-flex justify-content-between align-items-center">
          <div>
            <a href="#" class="btn btn-sm px-2 font-16 btn-light">
              <i class="mdi mdi-account-circle"></i>
            </a>
            <a href="#" class="btn btn-sm px-2 font-16 btn-light">
              <i class="mdi mdi-map-marker"></i>
            </a>
            <a href="#" class="btn btn-sm px-2 font-16 btn-light">
              <i class="mdi mdi-camera"></i>
            </a>
            <a href="#" class="btn btn-sm px-2 font-16 btn-light">
              <i class="mdi mdi-emoticon-outline"></i>
            </a>
          </div>
          <button type="submit" class="btn btn-sm btn-dark waves-effect">Post</button>
        </div>
      </form>
    </div>
    <!-- end comment box -->

    <!-- Story Box-->
    <div class="border border-light rounded p-2 mb-3">
      <b-media>
        <template v-slot:aside>
          <img
            class="mr-2 rounded-circle"
            src="@assets/images/users/avatar-3.jpg"
            alt="Generic placeholder image"
            height="32"
          />
        </template>
        <h5 class="m-0">Jeremy Tomlinson</h5>
        <p class="text-muted">
          <small>about 2 minuts ago</small>
        </p>
      </b-media>
      <p>Story based around the idea of time lapse, animation to post soon!</p>

      <img src="@assets/images/small/small-1.jpg" alt="post-img" class="rounded mr-1" height="60" />
      <img src="@assets/images/small/small-2.jpg" alt="post-img" class="rounded mr-1" height="60" />
      <img src="@assets/images/small/small-3.jpg" alt="post-img" class="rounded" height="60" />

      <div class="mt-2">
        <a href="javascript: void(0);" class="btn btn-sm btn-link text-muted">
          <i class="mdi mdi-reply"></i> Reply
        </a>
        <a href="javascript: void(0);" class="btn btn-sm btn-link text-muted">
          <i class="mdi mdi-heart-outline"></i> Like
        </a>
        <a href="javascript: void(0);" class="btn btn-sm btn-link text-muted">
          <i class="mdi mdi-share-variant"></i> Share
        </a>
      </div>
    </div>

    <!-- Story Box-->
    <div class="border border-light rounded p-2 mb-3">
      <b-media>
        <template v-slot:aside>
          <img
            class="mr-2 rounded-circle"
            src="@assets/images/users/avatar-4.jpg"
            alt="Generic placeholder image"
            height="32"
          />
        </template>
        <h5 class="m-0">Thelma Fridley</h5>
        <p class="text-muted">
          <small>about 1 hour ago</small>
        </p>
      </b-media>
      <div class="font-16 text-center font-italic text-dark">
        <i class="mdi mdi-format-quote-open font-20"></i> Cras sit amet nibh libero, in
        gravida nulla. Nulla vel metus scelerisque ante sollicitudin. Cras
        purus odio, vestibulum in vulputate at, tempus viverra turpis. Duis
        sagittis ipsum. Praesent mauris. Fusce nec tellus sed augue semper
        porta. Mauris massa.
      </div>

      <div class="mx-n2 p-2 mt-3 bg-light">
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
            <small class="text-muted">3 hours ago</small>
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
              <small class="text-muted">5 hours ago</small>
            </h5>i'm in the middle of a timelapse animation myself! (Very different though.) Awesome stuff.
          </b-media>
        </b-media>

        <b-media class="mt-2">
          <template v-slot:aside>
            <a class="pr-2" href="#">
              <img
                src="@assets/images/users/avatar-1.jpg"
                class="rounded-circle"
                alt="Generic placeholder image"
                height="32"
              />
            </a>
          </template>
          <input
            id="simpleinput"
            type="text"
            class="form-control border-0 form-control-sm"
            placeholder="Add comment"
          />
        </b-media>
      </div>

      <div class="mt-2">
        <a href="javascript: void(0);" class="btn btn-sm btn-link text-danger">
          <i class="mdi mdi-heart"></i> Like (28)
        </a>
        <a href="javascript: void(0);" class="btn btn-sm btn-link text-muted">
          <i class="mdi mdi-share-variant"></i> Share
        </a>
      </div>
    </div>

    <!-- Story Box-->
    <div class="border border-light p-2 mb-3">
      <b-media>
        <template v-slot:aside>
          <img
            class="mr-2 rounded-circle"
            src="@assets/images/users/avatar-6.jpg"
            alt="Generic placeholder image"
            height="32"
          />
        </template>
        <h5 class="m-0">Martin Williamson</h5>
        <p class="text-muted">
          <small>15 hours ago</small>
        </p>
      </b-media>
      <p>The parallax is a little odd but O.o that house build is awesome!!</p>

      <iframe src="https://player.vimeo.com/video/87993762" height="300" class="img-fluid border-0"></iframe>
    </div>

    <div class="text-center">
      <a href="javascript:void(0);" class="text-danger">
        <i class="mdi mdi-spin mdi-loading mr-1"></i> Load more
      </a>
    </div>
  </div>
</template>