<script>
import appConfig from '@src/app.config'
import Layout from '@layouts/main'
import PageHeader from '@components/page-header'

/**
 * Tabs component
 */
export default {
  page: {
    title: 'Tabs',
    meta: [{ name: 'description', content: appConfig.description }],
  },
  components: { Layout, PageHeader },
  data() {
    return {
      title: 'Tabs',
      items: [
        {
          text: 'Hyper',
          href: '/',
        },
        {
          text: 'Base UI',
          href: '/',
        },
        {
          text: 'Tabs',
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
      <div class="col-xl-6">
        <div class="card">
          <div class="card-body">
            <h4 class="header-title">Default Tabs</h4>
            <p class="text-muted font-14 mb-3">Simple widget of tabbable panes of local content.</p>
            <b-tabs content-class="mt-3">
              <b-tab>
                <template v-slot:title>
                  <span class="d-inline-block d-sm-none">
                    <i class="mdi mdi-home-variant d-md-none d-block"></i>
                  </span>
                  <span class="d-none d-sm-inline-block">Home</span>
                </template>
                <p>Food truck quinoa dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim.</p>
                <p
                  class="mb-0"
                >Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt.Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim.</p>
              </b-tab>
              <b-tab active>
                <template v-slot:title>
                  <span class="d-inline-block d-sm-none">
                    <i class="mdi mdi-account-circle d-md-none d-block"></i>
                  </span>
                  <span class="d-none d-sm-inline-block">Profile</span>
                </template>
                <p>Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt.Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim.</p>
                <p
                  class="mb-0"
                >Food truck quinoa dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim.</p>
              </b-tab>
              <b-tab>
                <template v-slot:title>
                  <span class="d-inline-block d-sm-none">
                    <i class="mdi mdi-settings-outline d-md-none d-block"></i>
                  </span>
                  <span class="d-none d-sm-inline-block">Settings</span>
                </template>
                <p>Food truck quinoa dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim.</p>
                <p
                  class="mb-0"
                >Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt.Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim.</p>
              </b-tab>
            </b-tabs>
          </div>
          <!-- end card-body -->
        </div>
        <!-- end card -->
      </div>
      <!-- end col -->
      <div class="col-xl-6">
        <div class="card">
          <div class="card-body">
            <h4 class="header-title">Tabs Justified</h4>
            <p class="text-muted font-14 mb-3">
              Using
              <code>justified</code>, you can force your
              <code>tab menu items</code> to use the full available width.
            </p>
            <b-tabs justified pills content-class="mt-3" nav-class="bg-nav-pills">
              <b-tab title-link-class="rounded-0">
                <template v-slot:title>
                  <span class="d-inline-block d-sm-none">
                    <i class="mdi mdi-home-variant d-md-none d-block"></i>
                  </span>
                  <span class="d-none d-sm-inline-block">Home</span>
                </template>
                <p>Food truck quinoa dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim.</p>
                <p
                  class="mb-0"
                >Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt.Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim.</p>
              </b-tab>
              <b-tab title-link-class="rounded-0" active>
                <template v-slot:title>
                  <i class="mdi mdi-account-circle d-md-none d-block"></i>
                  <span class="d-none d-md-block">Profile</span>
                </template>
                <p>Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt.Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim.</p>
                <p
                  class="mb-0"
                >Food truck quinoa dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim.</p>
              </b-tab>
              <b-tab title-link-class="rounded-0">
                <template v-slot:title>
                  <i class="mdi mdi-settings-outline d-md-none d-block"></i>
                  <span class="d-none d-md-block">Settings</span>
                </template>
                <p>Food truck quinoa dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim.</p>
                <p
                  class="mb-0"
                >Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt.Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim.</p>
              </b-tab>
            </b-tabs>
          </div>
          <!-- end card-body -->
        </div>
        <!-- end card -->
      </div>
      <!-- end col -->
    </div>
    <!--end row-->

    <div class="row">
      <div class="col-xl-6">
        <div class="card">
          <div class="card-body">
            <h4 class="header-title">Tabs Vertical Left</h4>
            <p class="text-muted font-14 mb-3">
              You can stack your navigation by changing the flex item direction with the
              <code>.flex-column</code> utility.
            </p>
            <b-tabs
              pills
              vertical
              nav-class="bg-white p-0"
              nav-wrapper-class="col-sm-3"
              content-class="pt-0 px-2"
            >
              <b-tab active title-item-class="mb-2">
                <template v-slot:title>
                  <span class="d-inline-block d-sm-none">
                    <i class="mdi mdi-home-variant d-md-none d-block"></i>
                  </span>
                  <span class="d-none d-sm-inline-block">Home</span>
                </template>
                <b-card-text>
                  <p>Cillum ad ut irure tempor velit nostrud occaecat ullamco aliqua anim Leggings sint. Veniam sint duis incididunt do esse magna mollit excepteur laborum qui. Id id reprehenderit sit est eu aliqua occaecat quis et velit excepteur laborum mollit dolore eiusmod. Ipsum dolor in occaecat commodo et voluptate minim reprehenderit mollit pariatur. Deserunt non laborum enim et cillum eu deserunt excepteur ea incididunt minim occaecat.</p>
                </b-card-text>
              </b-tab>
              <b-tab title-item-class="mb-2">
                <template v-slot:title>
                  <span class="d-inline-block d-sm-none">
                    <i class="mdi mdi-account-circle d-md-none d-block"></i>
                  </span>
                  <span class="d-none d-sm-inline-block">Profile</span>
                </template>
                <b-card-text>
                  <p>Culpa dolor voluptate do laboris laboris irure reprehenderit id incididunt duis pariatur mollit aute magna pariatur consectetur. Eu veniam duis non ut dolor deserunt commodo et minim in quis laboris ipsum velit id veniam. Quis ut consectetur adipisicing officia excepteur non sit. Ut et elit aliquip labore Leggings enim eu. Ullamco mollit occaecat dolore ipsum id officia mollit qui esse anim eiusmod do sint minim consectetur qui.</p>
                </b-card-text>
              </b-tab>
              <b-tab title-item-class="mb-2">
                <template v-slot:title>
                  <span class="d-inline-block d-sm-none">
                    <i class="mdi mdi-settings-outline d-md-none d-block"></i>
                  </span>
                  <span class="d-none d-sm-inline-block">Settings</span>
                </template>
                <b-card-text>
                  <p>Food truck quinoa dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Cillum ad ut irure tempor velit nostrud occaecat ullamco aliqua anim Leggings sint. Veniam sint duis incididunt do esse magna mollit excepteur laborum qui.</p>
                </b-card-text>
              </b-tab>
            </b-tabs>
          </div>
          <!-- end card-body -->
        </div>
        <!-- end card -->
      </div>
      <!-- end col -->

      <div class="col-xl-6">
        <div class="card">
          <div class="card-body">
            <h4 class="header-title">Tabs Vertical Right</h4>
            <p class="text-muted font-14 mb-3">
              You can stack your navigation by changing the flex item direction with the
              <code>.flex-column</code> utility.
            </p>
            <b-tabs
              pills
              vertical
              end
              nav-class="bg-white p-0"
              active-tab-class="pt-1"
              nav-wrapper-class="col-sm-3"
              content-class="pt-0 px-2"
            >
              <b-tab active title-item-class="mb-2">
                <template v-slot:title>
                  <span class="d-inline-block d-sm-none">
                    <i class="mdi mdi-home-variant d-md-none d-block"></i>
                  </span>
                  <span class="d-none d-sm-inline-block">Home</span>
                </template>
                <b-card-text>
                  <p>Cillum ad ut irure tempor velit nostrud occaecat ullamco aliqua anim Leggings sint. Veniam sint duis incididunt do esse magna mollit excepteur laborum qui. Id id reprehenderit sit est eu aliqua occaecat quis et velit excepteur laborum mollit dolore eiusmod. Ipsum dolor in occaecat commodo et voluptate minim reprehenderit mollit pariatur. Deserunt non laborum enim et cillum eu deserunt excepteur ea incididunt minim occaecat.</p>
                </b-card-text>
              </b-tab>
              <b-tab title-item-class="mb-2">
                <template v-slot:title>
                  <span class="d-inline-block d-sm-none">
                    <i class="mdi mdi-account-circle d-md-none d-block"></i>
                  </span>
                  <span class="d-none d-sm-inline-block">Profile</span>
                </template>
                <b-card-text>
                  <p>Culpa dolor voluptate do laboris laboris irure reprehenderit id incididunt duis pariatur mollit aute magna pariatur consectetur. Eu veniam duis non ut dolor deserunt commodo et minim in quis laboris ipsum velit id veniam. Quis ut consectetur adipisicing officia excepteur non sit. Ut et elit aliquip labore Leggings enim eu. Ullamco mollit occaecat dolore ipsum id officia mollit qui esse anim eiusmod do sint minim consectetur qui.</p>
                </b-card-text>
              </b-tab>
              <b-tab title-item-class="mb-2">
                <template v-slot:title>
                  <span class="d-inline-block d-sm-none">
                    <i class="mdi mdi-settings-outline d-md-none d-block"></i>
                  </span>
                  <span class="d-none d-sm-inline-block">Settings</span>
                </template>
                <b-card-text>
                  <p>Food truck quinoa dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Cillum ad ut irure tempor velit nostrud occaecat ullamco aliqua anim Leggings sint. Veniam sint duis incididunt do esse magna mollit excepteur laborum qui.</p>
                </b-card-text>
              </b-tab>
            </b-tabs>
          </div>
          <!-- end card-body -->
        </div>
        <!-- end card -->
      </div>
      <!-- end col -->
    </div>
    <!--end row-->

    <div class="row">
      <div class="col-xl-6">
        <div class="card">
          <div class="card-body">
            <h4 class="header-title">Tabs Bordered</h4>
            <p class="text-muted font-14 mb-3">
              The navigation item can have a simple bottom border as well. Just specify the class
              <code>.nav-bordered</code>.
            </p>
            <b-tabs nav-class="nav-tabs nav-bordered" content-class="mt-3">
              <b-tab>
                <template v-slot:title>
                  <span class="d-inline-block d-sm-none">
                    <i class="mdi mdi-home-variant d-md-none d-block"></i>
                  </span>
                  <span class="d-none d-sm-inline-block">Home</span>
                </template>
                <p>Leggings occaecat dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim.</p>
                <p
                  class="mb-0"
                >Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt.Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim.</p>
              </b-tab>
              <b-tab active>
                <template v-slot:title>
                  <span class="d-inline-block d-sm-none">
                    <i class="mdi mdi-account-circle d-md-none d-block"></i>
                  </span>
                  <span class="d-none d-sm-inline-block">Profile</span>
                </template>
                <p>Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt.Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim.</p>
                <p
                  class="mb-0"
                >Leggings occaecat dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim.</p>
              </b-tab>
              <b-tab>
                <template v-slot:title>
                  <span class="d-inline-block d-sm-none">
                    <i class="mdi mdi-settings-outline d-md-none d-block"></i>
                  </span>
                  <span class="d-none d-sm-inline-block">Settings</span>
                </template>
                <p>Food truck quinoa dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim.</p>
                <p
                  class="mb-0"
                >Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt.Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim.</p>
              </b-tab>
            </b-tabs>
          </div>
          <!-- end card-body -->
        </div>
        <!-- end card -->
      </div>
      <!-- end col -->

      <div class="col-xl-6">
        <div class="card">
          <div class="card-body">
            <h4 class="header-title">Tabs Bordered Justified</h4>
            <p class="text-muted font-14 mb-3">
              The navigation item can have a simple bottom border as well. Just specify the class
              <code>.nav-bordered</code>.
            </p>
            <b-tabs justified nav-class="nav-tabs nav-bordered" content-class="mt-3">
              <b-tab>
                <template v-slot:title>
                  <span class="d-inline-block d-sm-none">
                    <i class="mdi mdi-home-variant d-md-none d-block"></i>
                  </span>
                  <span class="d-none d-sm-inline-block">Home</span>
                </template>
                <p>Leggings occaecat dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim.</p>
                <p
                  class="mb-0"
                >Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt.Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim.</p>
              </b-tab>
              <b-tab active>
                <template v-slot:title>
                  <span class="d-inline-block d-sm-none">
                    <i class="mdi mdi-account-circle d-md-none d-block"></i>
                  </span>
                  <span class="d-none d-sm-inline-block">Profile</span>
                </template>
                <p>Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt.Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim.</p>
                <p
                  class="mb-0"
                >Leggings occaecat dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim.</p>
              </b-tab>
              <b-tab>
                <template v-slot:title>
                  <span class="d-inline-block d-sm-none">
                    <i class="mdi mdi-settings-outline d-md-none d-block"></i>
                  </span>
                  <span class="d-none d-sm-inline-block">Settings</span>
                </template>
                <p>Food truck quinoa dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim.</p>
                <p
                  class="mb-0"
                >Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt.Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim.</p>
              </b-tab>
            </b-tabs>
          </div>
          <!-- end card-body -->
        </div>
        <!-- end card -->
      </div>
      <!-- end col -->
    </div>
    <!--end row-->
  </Layout>
</template>