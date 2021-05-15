<script>
import appConfig from '@src/app.config'
import Layout from '@layouts/main'
import PageHeader from '@components/page-header'

/**
 * Basic Tables component
 */
export default {
  page: {
    title: 'Basic Tables',
    meta: [{ name: 'description', content: appConfig.description }],
  },
  components: { Layout, PageHeader },
  data() {
    return {
      title: 'Basic Tables',
      items: [
        {
          text: 'Hyper',
          href: '/',
        },
        {
          text: 'Tables',
          href: '/',
        },
        {
          text: 'Basic Tables',
          active: true,
        },
      ],
      checked: true,
      checked1: true,
      checked2: true,
      checked3: true,
      checked4: true,
      checked5: true,
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
            <h4 class="header-title">Basic example</h4>
            <p class="text-muted font-14">
              For basic styling—light padding and only horizontal dividers—add the base class
              <code>.table</code> to any
              <code>&lt;table&gt;</code>.
            </p>
            <b-table-simple responsive class="mb-0">
              <b-thead>
                <b-tr>
                  <b-th>Name</b-th>
                  <b-th>Phone Number</b-th>
                  <b-th>Date of Birth</b-th>
                  <b-th>Active?</b-th>
                </b-tr>
              </b-thead>
              <b-tbody>
                <b-tr>
                  <b-td>Risa D. Pearson</b-td>
                  <b-td>336-508-2157</b-td>
                  <b-td>July 24, 1950</b-td>
                  <b-td>
                    <b-form-checkbox name="check-button" switch></b-form-checkbox>
                  </b-td>
                </b-tr>
                <b-tr>
                  <b-td>Ann C. Thompson</b-td>
                  <b-td>646-473-2057</b-td>
                  <b-td>January 25, 1959</b-td>
                  <b-td>
                    <b-form-checkbox name="check-button" switch></b-form-checkbox>
                  </b-td>
                </b-tr>
                <b-tr>
                  <b-td>Paul J. Friend</b-td>
                  <b-td>281-308-0793</b-td>
                  <b-td>September 1, 1939</b-td>
                  <b-td>
                    <b-form-checkbox v-model="checked" name="check-button" switch></b-form-checkbox>
                  </b-td>
                </b-tr>
                <b-tr>
                  <b-td>Linda G. Smith</b-td>
                  <b-td>606-253-1207</b-td>
                  <b-td>May 3, 1962</b-td>
                  <b-td>
                    <b-form-checkbox name="check-button" switch></b-form-checkbox>
                  </b-td>
                </b-tr>
              </b-tbody>
            </b-table-simple>
            <!-- end table-responsive-->
          </div>
        </div>
      </div>
      <!-- end col -->

      <div class="col-xl-6">
        <div class="card">
          <div class="card-body">
            <h4 class="header-title">Inverse table</h4>
            <p class="text-muted font-14">
              You can also invert the colors—with light text on dark backgrounds—with
              <code>dark</code>.
            </p>
            <b-table-simple responsive dark class="mb-0">
              <b-thead>
                <b-tr>
                  <b-th>Name</b-th>
                  <b-th>Phone Number</b-th>
                  <b-th>Date of Birth</b-th>
                  <b-th>Active?</b-th>
                </b-tr>
              </b-thead>
              <b-tbody>
                <b-tr>
                  <b-td>Risa D. Pearson</b-td>
                  <b-td>336-508-2157</b-td>
                  <b-td>July 24, 1950</b-td>
                  <b-td>
                    <b-form-checkbox name="check-button" switch></b-form-checkbox>
                  </b-td>
                </b-tr>
                <b-tr>
                  <b-td>Ann C. Thompson</b-td>
                  <b-td>646-473-2057</b-td>
                  <b-td>January 25, 1959</b-td>
                  <b-td>
                    <b-form-checkbox v-model="checked1" name="check-button" switch></b-form-checkbox>
                  </b-td>
                </b-tr>
                <b-tr>
                  <b-td>Paul J. Friend</b-td>
                  <b-td>281-308-0793</b-td>
                  <b-td>September 1, 1939</b-td>
                  <b-td>
                    <b-form-checkbox name="check-button" switch></b-form-checkbox>
                  </b-td>
                </b-tr>
                <b-tr>
                  <b-td>Linda G. Smith</b-td>
                  <b-td>606-253-1207</b-td>
                  <b-td>May 3, 1962</b-td>
                  <b-td>
                    <b-form-checkbox name="check-button" switch></b-form-checkbox>
                  </b-td>
                </b-tr>
              </b-tbody>
            </b-table-simple>
          </div>
        </div>
      </div>
      <!-- end col -->
    </div>
    <!-- end row -->

    <div class="row">
      <div class="col-xl-6">
        <div class="card">
          <div class="card-body">
            <h4 class="header-title">Striped rows</h4>
            <p class="text-muted font-14">
              Use
              <code>striped</code> to add zebra-striping to any table row
              within the
              <code>&lt;tbody&gt;</code>.
            </p>
            <b-table-simple responsive striped class="mb-0">
              <b-thead>
                <b-tr>
                  <b-th>User</b-th>
                  <b-th>Account No.</b-th>
                  <b-th>Balance</b-th>
                  <b-th>Action</b-th>
                </b-tr>
              </b-thead>
              <b-tbody>
                <b-tr>
                  <b-td class="table-user">
                    <img
                      src="@assets/images/users/avatar-2.jpg"
                      alt="table-user"
                      class="mr-2 rounded-circle"
                    />
                    Risa D. Pearson
                  </b-td>
                  <b-td>AC336 508 2157</b-td>
                  <b-td>July 24, 1950</b-td>
                  <b-td class="table-action">
                    <a href="javascript: void(0);" class="action-icon">
                      <i class="mdi mdi-pencil"></i>
                    </a>
                    <a href="javascript: void(0);" class="action-icon">
                      <i class="mdi mdi-delete"></i>
                    </a>
                  </b-td>
                </b-tr>
                <b-tr>
                  <b-td class="table-user">
                    <img
                      src="@assets/images/users/avatar-3.jpg"
                      alt="table-user"
                      class="mr-2 rounded-circle"
                    />
                    Ann C. Thompson
                  </b-td>
                  <b-td>SB646 473 2057</b-td>
                  <b-td>January 25, 1959</b-td>
                  <b-td class="table-action">
                    <a href="javascript: void(0);" class="action-icon">
                      <i class="mdi mdi-pencil"></i>
                    </a>
                    <a href="javascript: void(0);" class="action-icon">
                      <i class="mdi mdi-delete"></i>
                    </a>
                  </b-td>
                </b-tr>
                <b-tr>
                  <b-td class="table-user">
                    <img
                      src="@assets/images/users/avatar-4.jpg"
                      alt="table-user"
                      class="mr-2 rounded-circle"
                    />
                    Paul J. Friend
                  </b-td>
                  <b-td>DL281 308 0793</b-td>
                  <b-td>September 1, 1939</b-td>
                  <b-td class="table-action">
                    <a href="javascript: void(0);" class="action-icon">
                      <i class="mdi mdi-pencil"></i>
                    </a>
                    <a href="javascript: void(0);" class="action-icon">
                      <i class="mdi mdi-delete"></i>
                    </a>
                  </b-td>
                </b-tr>
                <b-tr>
                  <b-td class="table-user">
                    <img
                      src="@assets/images/users/avatar-5.jpg"
                      alt="table-user"
                      class="mr-2 rounded-circle"
                    />
                    Sean C. Nguyen
                  </b-td>
                  <b-td>CA269 714 6825</b-td>
                  <b-td>February 5, 1994</b-td>
                  <b-td class="table-action">
                    <a href="javascript: void(0);" class="action-icon">
                      <i class="mdi mdi-pencil"></i>
                    </a>
                    <a href="javascript: void(0);" class="action-icon">
                      <i class="mdi mdi-delete"></i>
                    </a>
                  </b-td>
                </b-tr>
              </b-tbody>
            </b-table-simple>
          </div>
        </div>
      </div>
      <!-- end col -->
      <div class="col-xl-6">
        <div class="card">
          <div class="card-body">
            <h4 class="header-title">Bordered table</h4>
            <p class="text-muted font-14">
              Add
              <code>bordered</code> for borders on all sides of the table and cells.
            </p>
            <b-table-simple responsive bordered class="mb-0">
              <b-thead>
                <b-tr>
                  <b-th>User</b-th>
                  <b-th>Account No.</b-th>
                  <b-th>Balance</b-th>
                  <b-th>Action</b-th>
                </b-tr>
              </b-thead>
              <b-tbody>
                <b-tr>
                  <b-td class="table-user">
                    <img
                      src="@assets/images/users/avatar-6.jpg"
                      alt="table-user"
                      class="mr-2 rounded-circle"
                    />
                    Risa D. Pearson
                  </b-td>
                  <b-td>AC336 508 2157</b-td>
                  <b-td>July 24, 1950</b-td>
                  <b-td class="table-action">
                    <a href="javascript: void(0);" class="action-icon">
                      <i class="mdi mdi-pencil"></i>
                    </a>
                    <a href="javascript: void(0);" class="action-icon">
                      <i class="mdi mdi-delete"></i>
                    </a>
                  </b-td>
                </b-tr>
                <b-tr>
                  <b-td class="table-user">
                    <img
                      src="@assets/images/users/avatar-7.jpg"
                      alt="table-user"
                      class="mr-2 rounded-circle"
                    />
                    Ann C. Thompson
                  </b-td>
                  <b-td>SB646 473 2057</b-td>
                  <b-td>January 25, 1959</b-td>
                  <b-td class="table-action">
                    <a href="javascript: void(0);" class="action-icon">
                      <i class="mdi mdi-pencil"></i>
                    </a>
                    <a href="javascript: void(0);" class="action-icon">
                      <i class="mdi mdi-delete"></i>
                    </a>
                  </b-td>
                </b-tr>
                <b-tr>
                  <b-td class="table-user">
                    <img
                      src="@assets/images/users/avatar-8.jpg"
                      alt="table-user"
                      class="mr-2 rounded-circle"
                    />
                    Paul J. Friend
                  </b-td>
                  <b-td>DL281 308 0793</b-td>
                  <b-td>September 1, 1939</b-td>
                  <b-td class="table-action">
                    <a href="javascript: void(0);" class="action-icon">
                      <i class="mdi mdi-pencil"></i>
                    </a>
                    <a href="javascript: void(0);" class="action-icon">
                      <i class="mdi mdi-delete"></i>
                    </a>
                  </b-td>
                </b-tr>
                <b-tr>
                  <b-td class="table-user">
                    <img
                      src="@assets/images/users/avatar-9.jpg"
                      alt="table-user"
                      class="mr-2 rounded-circle"
                    />
                    Sean C. Nguyen
                  </b-td>
                  <b-td>CA269 714 6825</b-td>
                  <b-td>February 5, 1994</b-td>
                  <b-td class="table-action">
                    <a href="javascript: void(0);" class="action-icon">
                      <i class="mdi mdi-pencil"></i>
                    </a>
                    <a href="javascript: void(0);" class="action-icon">
                      <i class="mdi mdi-delete"></i>
                    </a>
                  </b-td>
                </b-tr>
              </b-tbody>
            </b-table-simple>
          </div>
        </div>
      </div>
      <!-- end col -->
    </div>
    <!-- end row -->
    
    <div class="row">
      <div class="col-xl-6">
        <div class="card">
          <div class="card-body">
            <h4 class="header-title">Hoverable rows</h4>
            <p class="text-muted font-14">
              Add
              <code>hover</code> to enable a hover state on table rows within a
              <code>&lt;b-tbody&gt;</code>.
            </p>
            <b-table-simple responsive hover class="mb-0">
              <b-thead>
                <b-tr>
                  <b-th>Product</b-th>
                  <b-th>Price</b-th>
                  <b-th>Quantity</b-th>
                  <b-th>Amount</b-th>
                </b-tr>
              </b-thead>
              <b-tbody>
                <b-tr>
                  <b-td>ASOS Ridley High Waist</b-td>
                  <b-td>$79.49</b-td>
                  <b-td>
                    <span class="badge badge-primary">82 Pcs</span>
                  </b-td>
                  <b-td>$6,518.18</b-td>
                </b-tr>
                <b-tr>
                  <b-td>Marco Lightweight Shirt</b-td>
                  <b-td>$128.50</b-td>
                  <b-td>
                    <span class="badge badge-primary">37 Pcs</span>
                  </b-td>
                  <b-td>$4,754.50</b-td>
                </b-tr>
                <b-tr>
                  <b-td>Half Sleeve Shirt</b-td>
                  <b-td>$39.99</b-td>
                  <b-td>
                    <span class="badge badge-primary">64 Pcs</span>
                  </b-td>
                  <b-td>$2,559.36</b-td>
                </b-tr>
                <b-tr>
                  <b-td>Lightweight Jacket</b-td>
                  <b-td>$20.00</b-td>
                  <b-td>
                    <span class="badge badge-primary">184 Pcs</span>
                  </b-td>
                  <b-td>$3,680.00</b-td>
                </b-tr>
              </b-tbody>
            </b-table-simple>
          </div>
        </div>
      </div>
      <div class="col-xl-6">
        <div class="card">
          <div class="card-body">
            <h4 class="header-title">Small table</h4>
            <p class="text-muted font-14">
              Add
              <code>small</code> to make tables more compact by cutting cell padding in half.
            </p>
            <b-table-simple responsive small class="mb-0">
              <b-thead>
                <b-tr>
                  <b-th>Product</b-th>
                  <b-th>Price</b-th>
                  <b-th>Quantity</b-th>
                  <b-th>Amount</b-th>
                </b-tr>
              </b-thead>
              <b-tbody>
                <b-tr>
                  <b-td>ASOS Ridley High Waist</b-td>
                  <b-td>$79.49</b-td>
                  <b-td>
                    <span class="badge badge-primary">82 Pcs</span>
                  </b-td>
                  <b-td>$6,518.18</b-td>
                </b-tr>
                <b-tr>
                  <b-td>Marco Lightweight Shirt</b-td>
                  <b-td>$128.50</b-td>
                  <b-td>
                    <span class="badge badge-primary">37 Pcs</span>
                  </b-td>
                  <b-td>$4,754.50</b-td>
                </b-tr>
                <b-tr>
                  <b-td>Half Sleeve Shirt</b-td>
                  <b-td>$39.99</b-td>
                  <b-td>
                    <span class="badge badge-primary">64 Pcs</span>
                  </b-td>
                  <b-td>$2,559.36</b-td>
                </b-tr>
                <b-tr>
                  <b-td>Lightweight Jacket</b-td>
                  <b-td>$20.00</b-td>
                  <b-td>
                    <span class="badge badge-primary">184 Pcs</span>
                  </b-td>
                  <b-td>$3,680.00</b-td>
                </b-tr>
                <b-tr>
                  <b-td>Marco Shoes</b-td>
                  <b-td>$28.49</b-td>
                  <b-td>
                    <span class="badge badge-primary">69 Pcs</span>
                  </b-td>
                  <b-td>$1,965.81</b-td>
                </b-tr>
                <b-tr>
                  <b-td>ASOS Ridley High Waist</b-td>
                  <b-td>$79.49</b-td>
                  <b-td>
                    <span class="badge badge-primary">82 Pcs</span>
                  </b-td>
                  <b-td>$6,518.18</b-td>
                </b-tr>
              </b-tbody>
            </b-table-simple>
          </div>
        </div>
      </div>
    </div>
    <!-- end row -->

    <div class="row">
      <div class="col-xl-6">
        <div class="card">
          <div class="card-body">
            <h4 class="header-title">Table head options</h4>
            <p class="text-muted font-14">
              Use one of two modifier classes to make
              <code>&lt;b-thead&gt;</code>s appear light or dark gray.
            </p>
            <b-table-simple responsive class="mb-0">
              <b-thead head-variant="dark">
                <b-tr>
                  <b-th>Product</b-th>
                  <b-th>Courier</b-th>
                  <b-th>Process</b-th>
                  <b-th>Status</b-th>
                </b-tr>
              </b-thead>
              <b-tbody>
                <b-tr>
                  <b-td>ASOS Ridley High Waist</b-td>
                  <b-td>FedEx</b-td>
                  <b-td>
                    <b-progress :value="100" variant="success" height="5px" class="mt-1"></b-progress>
                  </b-td>
                  <b-td>
                    <i class="mdi mdi-circle text-success"></i> Delivered
                  </b-td>
                </b-tr>
                <b-tr>
                  <b-td>Marco Lightweight Shirt</b-td>
                  <b-td>DHL</b-td>
                  <b-td>
                    <b-progress :value="50" variant="warning" height="5px" class="mt-1"></b-progress>
                  </b-td>
                  <b-td>
                    <i class="mdi mdi-circle text-warning"></i> Shipped
                  </b-td>
                </b-tr>
                <b-tr>
                  <b-td>Half Sleeve Shirt</b-td>
                  <b-td>Bright</b-td>
                  <b-td>
                    <b-progress :value="25" variant="info" height="5px" class="mt-1"></b-progress>
                  </b-td>
                  <b-td>
                    <i class="mdi mdi-circle text-info"></i> Order Received
                  </b-td>
                </b-tr>
                <b-tr>
                  <b-td>Lightweight Jacket</b-td>
                  <b-td>FedEx</b-td>
                  <b-td>
                    <b-progress :value="100" variant="success" height="5px" class="mt-1"></b-progress>
                  </b-td>
                  <b-td>
                    <i class="mdi mdi-circle text-success"></i> Delivered
                  </b-td>
                </b-tr>
              </b-tbody>
            </b-table-simple>
          </div>
        </div>
      </div>
      <!-- end col -->
      <div class="col-xl-6">
        <div class="card">
          <div class="card-body">
            <h4 class="header-title">Contextual with background color</h4>
            <p
              class="text-muted font-14"
            >Use contextual classes to color table rows or individual cells.</p>
            <b-table-simple responsive class="mb-0">
              <b-thead>
                <b-tr>
                  <b-th>Product</b-th>
                  <b-th>Courier</b-th>
                  <b-th>Process</b-th>
                  <b-th>Status</b-th>
                </b-tr>
              </b-thead>
              <b-tbody>
                <b-tr variant="success">
                  <b-td>ASOS Ridley High Waist</b-td>
                  <b-td>FedEx</b-td>
                  <b-td>
                    <b-progress :value="100" variant="success" height="5px" class="mt-1"></b-progress>
                  </b-td>
                  <b-td>
                    <i class="mdi mdi-circle text-success"></i> Delivered
                  </b-td>
                </b-tr>
                <b-tr>
                  <b-td>Marco Lightweight Shirt</b-td>
                  <b-td>DHL</b-td>
                  <b-td>
                    <b-progress :value="50" variant="warning" height="5px" class="mt-1"></b-progress>
                  </b-td>
                  <b-td>
                    <i class="mdi mdi-circle text-warning"></i> Shipped
                  </b-td>
                </b-tr>
                <b-tr variant="danger">
                  <b-td>Half Sleeve Shirt</b-td>
                  <b-td>Bright</b-td>
                  <b-td>
                    <b-progress :value="25" variant="info" height="5px" class="mt-1"></b-progress>
                  </b-td>
                  <b-td>
                    <i class="mdi mdi-circle text-info"></i> Order Received
                  </b-td>
                </b-tr>
                <b-tr>
                  <b-td>Lightweight Jacket</b-td>
                  <b-td>FedEx</b-td>
                  <b-td>
                    <b-progress :value="100" variant="success" height="5px" class="mt-1"></b-progress>
                  </b-td>
                  <b-td>
                    <i class="mdi mdi-circle text-success"></i> Delivered
                  </b-td>
                </b-tr>
              </b-tbody>
            </b-table-simple>
          </div>
        </div>
      </div>
      <!-- end col -->
    </div>
    <!-- end row -->

    <div class="row">
      <div class="col-12">
        <div class="card">
          <div class="card-body">
            <h4 class="header-title">Always responsive</h4>
            <p class="text-muted font-14">
              Across every breakpoint, use
              <code>responsive</code> for horizontally scrolling tables. Use
              <code>responsive{-sm|-md|-lg|-xl}</code> as needed to create responsive tables up to a particular breakpoint. From that breakpoint and up, the table will behave
              normally and not scroll horizontally.
            </p>
            <b-table-simple responsive class="mb-0">
              <b-thead>
                <b-tr>
                  <b-th scope="col">#</b-th>
                  <b-th scope="col">Heading</b-th>
                  <b-th scope="col">Heading</b-th>
                  <b-th scope="col">Heading</b-th>
                  <b-th scope="col">Heading</b-th>
                  <b-th scope="col">Heading</b-th>
                  <b-th scope="col">Heading</b-th>
                  <b-th scope="col">Heading</b-th>
                  <b-th scope="col">Heading</b-th>
                  <b-th scope="col">Heading</b-th>
                </b-tr>
              </b-thead>
              <b-tbody>
                <b-tr>
                  <b-th scope="row">1</b-th>
                  <b-td>Cell</b-td>
                  <b-td>Cell</b-td>
                  <b-td>Cell</b-td>
                  <b-td>Cell</b-td>
                  <b-td>Cell</b-td>
                  <b-td>Cell</b-td>
                  <b-td>Cell</b-td>
                  <b-td>Cell</b-td>
                  <b-td>Cell</b-td>
                </b-tr>
                <b-tr>
                  <b-th scope="row">2</b-th>
                  <b-td>Cell</b-td>
                  <b-td>Cell</b-td>
                  <b-td>Cell</b-td>
                  <b-td>Cell</b-td>
                  <b-td>Cell</b-td>
                  <b-td>Cell</b-td>
                  <b-td>Cell</b-td>
                  <b-td>Cell</b-td>
                  <b-td>Cell</b-td>
                </b-tr>
                <b-tr>
                  <b-th scope="row">3</b-th>
                  <b-td>Cell</b-td>
                  <b-td>Cell</b-td>
                  <b-td>Cell</b-td>
                  <b-td>Cell</b-td>
                  <b-td>Cell</b-td>
                  <b-td>Cell</b-td>
                  <b-td>Cell</b-td>
                  <b-td>Cell</b-td>
                  <b-td>Cell</b-td>
                </b-tr>
              </b-tbody>
            </b-table-simple>
          </div>
        </div>
      </div>
      <!-- end col -->
    </div>
    <!-- end row -->

    <div class="row">
      <div class="col-xl-6">
        <div class="card">
          <div class="card-body">
            <h4 class="header-title">Basic Borderless Example</h4>
            <p class="text-muted font-14">
              Add
              <code>borderless</code> for a table without borders.
            </p>
            <b-table-simple responsive borderless class="mb-0">
              <b-thead>
                <b-tr>
                  <b-th>Name</b-th>
                  <b-th>Phone Number</b-th>
                  <b-th>Date of Birth</b-th>
                  <b-th>Active?</b-th>
                </b-tr>
              </b-thead>
              <b-tbody>
                <b-tr>
                  <b-td>Risa D. Pearson</b-td>
                  <b-td>336-508-2157</b-td>
                  <b-td>July 24, 1950</b-td>
                  <b-td>
                    <b-form-checkbox v-model="checked2" name="check-button" switch></b-form-checkbox>
                  </b-td>
                </b-tr>
                <b-tr>
                  <b-td>Ann C. Thompson</b-td>
                  <b-td>646-473-2057</b-td>
                  <b-td>January 25, 1959</b-td>
                  <b-td>
                    <b-form-checkbox v-model="checked3" name="check-button" switch></b-form-checkbox>
                  </b-td>
                </b-tr>
                <b-tr>
                  <b-td>Paul J. Friend</b-td>
                  <b-td>281-308-0793</b-td>
                  <b-td>September 1, 1939</b-td>
                  <b-td>
                    <b-form-checkbox name="check-button" switch></b-form-checkbox>
                  </b-td>
                </b-tr>
                <b-tr>
                  <b-td>Linda G. Smith</b-td>
                  <b-td>606-253-1207</b-td>
                  <b-td>May 3, 1962</b-td>
                  <b-td>
                    <b-form-checkbox name="check-button" switch></b-form-checkbox>
                  </b-td>
                </b-tr>
              </b-tbody>
            </b-table-simple>
          </div>
        </div>
      </div>
      <!-- end col -->
      <div class="col-xl-6">
        <div class="card">
          <div class="card-body">
            <h4 class="header-title">Inverse Borderless table</h4>
            <p class="text-muted font-14">
              Add
              <code>borderless</code> for a table without borders.
            </p>
            <b-table-simple responsive borderless dark class="mb-0">
              <b-thead>
                <b-tr>
                  <b-th>Name</b-th>
                  <b-th>Phone Number</b-th>
                  <b-th>Date of Birth</b-th>
                  <b-th>Active?</b-th>
                </b-tr>
              </b-thead>
              <b-tbody>
                <b-tr>
                  <b-td>Risa D. Pearson</b-td>
                  <b-td>336-508-2157</b-td>
                  <b-td>July 24, 1950</b-td>
                  <b-td>
                    <b-form-checkbox name="check-button" switch></b-form-checkbox>
                  </b-td>
                </b-tr>
                <b-tr>
                  <b-td>Ann C. Thompson</b-td>
                  <b-td>646-473-2057</b-td>
                  <b-td>January 25, 1959</b-td>
                  <b-td>
                    <b-form-checkbox v-model="checked4" name="check-button" switch></b-form-checkbox>
                  </b-td>
                </b-tr>
                <b-tr>
                  <b-td>Paul J. Friend</b-td>
                  <b-td>281-308-0793</b-td>
                  <b-td>September 1, 1939</b-td>
                  <b-td>
                    <b-form-checkbox name="check-button" switch></b-form-checkbox>
                  </b-td>
                </b-tr>
                <b-tr>
                  <b-td>Linda G. Smith</b-td>
                  <b-td>606-253-1207</b-td>
                  <b-td>May 3, 1962</b-td>
                  <b-td>
                    <b-form-checkbox v-model="checked5" name="check-button" switch></b-form-checkbox>
                  </b-td>
                </b-tr>
              </b-tbody>
            </b-table-simple>
          </div>
        </div>
      </div>
      <!-- end col -->
    </div>
    <!-- end row -->
  </Layout>
</template>