<script>
import appConfig from '@src/app.config'
import Layout from '@layouts/main'

import Panel from './panel'
import Detail from './detail'

export default {
  page: {
    title: 'Tasks List',
    meta: [{ name: 'description', content: appConfig.description }],
  },
  components: { Layout, Panel, Detail },
}
</script>

<template>
  <Layout>
    <div class="row">
      <div class="col-xl-8">
        <!-- start page title -->
        <div class="page-title-box">
          <div class="page-title-right">
            <div class="app-search">
              <form>
                <div class="input-group">
                  <input type="text" class="form-control" placeholder="Search..." />
                  <span class="mdi mdi-magnify"></span>
                  <div class="input-group-append">
                    <b-dropdown variant="secondary" right>
                      <template slot="button-content">
                        <i class="uil uil-sort-amount-down"></i>
                      </template>
                      <b-dropdown-item href="javascript: void(0);">Due Date</b-dropdown-item>
                      <b-dropdown-item href="javascript: void(0);">Added Date</b-dropdown-item>
                      <b-dropdown-item href="javascript: void(0);">Assignee</b-dropdown-item>
                    </b-dropdown>
                  </div>
                </div>
              </form>
            </div>
          </div>
          <h4 class="page-title">
            Tasks
            <a href="#" class="btn btn-success btn-sm ml-3">Add New</a>
          </h4>
        </div>
        <!-- end page title -->
        <Panel />
        <!-- end row -->
      </div>
      <!-- end col -->
      <div class="col-xl-4">
        <Detail />
      </div>
    </div>
    <!-- end row -->
  </Layout>
</template>