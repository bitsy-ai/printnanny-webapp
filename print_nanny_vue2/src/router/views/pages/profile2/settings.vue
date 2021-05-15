<template>
  <form class="mt-3">
    <h5 class="mb-4 text-uppercase">
      <i class="mdi mdi-account-circle mr-1"></i> Personal Info
    </h5>
    <div class="row">
      <div class="col-md-6">
        <div class="form-group">
          <label for="firstname">First Name</label>
          <input id="firstname" type="text" class="form-control" placeholder="Enter first name" />
        </div>
      </div>
      <div class="col-md-6">
        <div class="form-group">
          <label for="lastname">Last Name</label>
          <input id="lastname" type="text" class="form-control" placeholder="Enter last name" />
        </div>
      </div>
      <!-- end col -->
    </div>
    <!-- end row -->

    <div class="row">
      <div class="col-12">
        <div class="form-group">
          <label for="userbio">Bio</label>
          <textarea id="userbio" class="form-control" rows="4" placeholder="Write something..."></textarea>
        </div>
      </div>
      <!-- end col -->
    </div>
    <!-- end row -->

    <div class="row">
      <div class="col-md-6">
        <div class="form-group">
          <label for="useremail">Email Address</label>
          <input id="useremail" type="email" class="form-control" placeholder="Enter email" />
          <span class="form-text text-muted">
            <small>
              If you want to change email please
              <a href="javascript: void(0);">click</a> here.
            </small>
          </span>
        </div>
      </div>
      <div class="col-md-6">
        <div class="form-group">
          <label for="userpassword">Password</label>
          <input
            id="userpassword"
            type="password"
            class="form-control"
            placeholder="Enter password"
          />
          <span class="form-text text-muted">
            <small>
              If you want to change password please
              <a href="javascript: void(0);">click</a> here.
            </small>
          </span>
        </div>
      </div>
      <!-- end col -->
    </div>
    <!-- end row -->

    <h5 class="mb-3 text-uppercase bg-light p-2">
      <i class="mdi mdi-office-building mr-1"></i> Company Info
    </h5>
    <div class="row">
      <div class="col-md-6">
        <div class="form-group">
          <label for="companyname">Company Name</label>
          <input id="companyname" type="text" class="form-control" placeholder="Enter company name" />
        </div>
      </div>
      <div class="col-md-6">
        <div class="form-group">
          <label for="cwebsite">Website</label>
          <input id="cwebsite" type="text" class="form-control" placeholder="Enter website url" />
        </div>
      </div>
      <!-- end col -->
    </div>
    <!-- end row -->

    <h5 class="mb-3 text-uppercase bg-light p-2">
      <i class="mdi mdi-earth mr-1"></i> Social
    </h5>
    <div class="row">
      <div class="col-md-6">
        <div class="form-group">
          <label for="social-fb">Facebook</label>
          <div class="input-group">
            <div class="input-group-prepend">
              <span class="input-group-text">
                <i class="mdi mdi-facebook"></i>
              </span>
            </div>
            <input id="social-fb" type="text" class="form-control" placeholder="Url" />
          </div>
        </div>
      </div>
      <div class="col-md-6">
        <div class="form-group">
          <label for="social-tw">Twitter</label>
          <div class="input-group">
            <div class="input-group-prepend">
              <span class="input-group-text">
                <i class="mdi mdi-twitter"></i>
              </span>
            </div>
            <input id="social-tw" type="text" class="form-control" placeholder="Username" />
          </div>
        </div>
      </div>
      <!-- end col -->
    </div>
    <!-- end row -->

    <div class="row">
      <div class="col-md-6">
        <div class="form-group">
          <label for="social-insta">Instagram</label>
          <div class="input-group">
            <div class="input-group-prepend">
              <span class="input-group-text">
                <i class="mdi mdi-instagram"></i>
              </span>
            </div>
            <input id="social-insta" type="text" class="form-control" placeholder="Url" />
          </div>
        </div>
      </div>
      <div class="col-md-6">
        <div class="form-group">
          <label for="social-lin">Linkedin</label>
          <div class="input-group">
            <div class="input-group-prepend">
              <span class="input-group-text">
                <i class="mdi mdi-linkedin"></i>
              </span>
            </div>
            <input id="social-lin" type="text" class="form-control" placeholder="Url" />
          </div>
        </div>
      </div>
      <!-- end col -->
    </div>
    <!-- end row -->

    <div class="row">
      <div class="col-md-6">
        <div class="form-group">
          <label for="social-sky">Skype</label>
          <div class="input-group">
            <div class="input-group-prepend">
              <span class="input-group-text">
                <i class="mdi mdi-skype"></i>
              </span>
            </div>
            <input id="social-sky" type="text" class="form-control" placeholder="@username" />
          </div>
        </div>
      </div>
      <div class="col-md-6">
        <div class="form-group">
          <label for="social-gh">Github</label>
          <div class="input-group">
            <div class="input-group-prepend">
              <span class="input-group-text">
                <i class="mdi mdi-github-circle"></i>
              </span>
            </div>
            <input id="social-gh" type="text" class="form-control" placeholder="Username" />
          </div>
        </div>
      </div>
      <!-- end col -->
    </div>
    <!-- end row -->

    <div class="text-right">
      <button type="submit" class="btn btn-success mt-2">
        <i class="mdi mdi-content-save"></i> Save
      </button>
    </div>
  </form>
</template>