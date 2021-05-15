<template>
<body class="authentication-bg">
  <div class="account-pages mt-5 mb-5">
    <div class="container">
      <div class="row justify-content-center">
        <div class="col-lg-5">
          <div class="card">
            <!-- Logo -->
            <div class="card-header pt-4 pb-4 text-center bg-primary">
              <router-link tag="a" to="/">
                <span>
                  <img src="@assets/images/logo.png" alt height="18" />
                </span>
              </router-link>
            </div>

            <div class="card-body p-4">
              <div class="text-center">
                <img src="@assets/images/startman.svg" height="120" alt="File not found Image" />

                <h1 class="text-error mt-4">500</h1>
                <h4 class="text-uppercase text-danger mt-3">Internal Server Error</h4>
                <p class="text-muted mt-3">
                  Why not try refreshing your page? or you can contact
                  <a href class="text-muted">
                    <b>Support</b>
                  </a>
                </p>

                <router-link tag="a" class="btn btn-info mt-3" to="/">
                  <i class="mdi mdi-reply"></i> Return Home
                </router-link>
              </div>
            </div>
            <!-- end card-body-->
          </div>
          <!-- end card-->
        </div>
        <!-- end col -->
      </div>
      <!-- end row -->
    </div>
    <!-- end container -->
  </div>
  <!-- end page -->

  <footer class="footer footer-alt">2018 - 2019 © Hyper - Coderthemes.com</footer>
</body>
</template>