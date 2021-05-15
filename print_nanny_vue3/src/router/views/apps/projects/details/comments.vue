<template>
  <div class="card">
    <div class="card-body">
      <h4 class="mt-0 mb-3">Comments (258)</h4>

      <textarea
        id="example-textarea"
        class="form-control form-control-light mb-2"
        placeholder="Write message"
        rows="3"
      ></textarea>
      <div class="text-right">
        <div class="btn-group mb-2">
          <button type="button" class="btn btn-link btn-sm text-muted font-18">
            <i class="dripicons-paperclip"></i>
          </button>
        </div>
        <div class="btn-group mb-2 ml-2">
          <button type="button" class="btn btn-primary btn-sm">Submit</button>
        </div>
      </div>

      <b-media class="mt-2">
        <template v-slot:aside>
          <img
            class="mr-3 avatar-sm rounded-circle"
            src="@assets/images/users/avatar-3.jpg"
            alt="Generic placeholder image"
          />
        </template>
        <h5 class="mt-0">Jeremy Tomlinson</h5>Cras sit amet nibh libero, in gravida nulla. Nulla vel metus scelerisque ante sollicitudin. Cras purus odio, vestibulum in
        vulputate at, tempus viverra turpis. Fusce condimentum nunc ac nisi vulputate fringilla. Donec lacinia congue felis
        in faucibus.
        <b-media class="mt-3">
          <template v-slot:aside>
            <a class="pr-3" href="#">
              <img
                src="@assets/images/users/avatar-4.jpg"
                class="avatar-sm rounded-circle"
                alt="Generic placeholder image"
              />
            </a>
          </template>
          <h5 class="mt-0">Kathleen Thomas</h5>Cras sit amet nibh libero, in gravida nulla. Nulla vel metus scelerisque ante sollicitudin. Cras purus odio, vestibulum in
          vulputate at, tempus viverra turpis. Fusce condimentum nunc ac nisi vulputate fringilla. Donec lacinia congue
          felis in faucibus.
        </b-media>
      </b-media>

      <div class="text-center mt-2">
        <a href="javascript:void(0);" class="text-danger">Load more</a>
      </div>
    </div>
    <!-- end card-body-->
  </div>
  <!-- end card-->
</template>