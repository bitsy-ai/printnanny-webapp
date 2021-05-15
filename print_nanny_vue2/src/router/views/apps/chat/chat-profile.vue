<template>
  <div class="card">
    <div class="card-body">
      <div class="dropdown float-right">
        <b-dropdown toggle-class="arrow-none card-drop p-0" variant="white" right>
          <template v-slot:button-content>
            <i class="mdi mdi-dots-horizontal"></i>
          </template>
          <!-- item-->
          <a href="javascript:void(0);" class="dropdown-item">View full</a>
          <!-- item-->
          <a href="javascript:void(0);" class="dropdown-item">Edit Contact Info</a>
          <!-- item-->
          <a href="javascript:void(0);" class="dropdown-item">Remove</a>
        </b-dropdown>
      </div>

      <div class="mt-3 text-center">
        <img
          src="@assets/images/users/avatar-5.jpg"
          alt="shreyu"
          class="img-thumbnail avatar-lg rounded-circle"
        />
        <h4>Shreyu N</h4>
        <button class="btn btn-primary btn-sm mt-1">
          <i class="uil uil-envelope-add mr-1"></i>Send Email
        </button>
        <p class="text-muted mt-2 font-14">
          Last Interacted:
          <strong>Few hours back</strong>
        </p>
      </div>

      <div class="mt-3">
        <hr class />

        <p class="mt-4 mb-1">
          <strong>
            <i class="uil uil-at"></i> Email:
          </strong>
        </p>
        <p>support@coderthemes.com</p>

        <p class="mt-3 mb-1">
          <strong>
            <i class="uil uil-phone"></i> Phone Number:
          </strong>
        </p>
        <p>+1 456 9595 9594</p>

        <p class="mt-3 mb-1">
          <strong>
            <i class="uil uil-location"></i> Location:
          </strong>
        </p>
        <p>California, USA</p>

        <p class="mt-3 mb-1">
          <strong>
            <i class="uil uil-globe"></i> Languages:
          </strong>
        </p>
        <p>English, German, Spanish</p>

        <p class="mt-3 mb-2">
          <strong>
            <i class="uil uil-users-alt"></i> Groups:
          </strong>
        </p>
        <p class="mb-1">
          <span class="badge badge-success-lighten p-1 font-14">Work</span>
          <span class="badge badge-primary-lighten p-1 font-14 ml-1">Friends</span>
        </p>
      </div>
    </div>
    <!-- end card-body -->
  </div>
  <!-- end card-->
</template>