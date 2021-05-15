<script>
import DatePicker from 'vue2-datepicker'

import appConfig from '@src/app.config'
import Layout from '@layouts/main'

import Stats from './stats'
import Projection from './projection'
import Revenue from './revenue'
import Sales from './sales'
import Activity from './activity'
import Products from './products'

/**
 * Dashboard-1 Component
 */
export default {
  page: {
    title: 'Dashboard',
    meta: [{ name: 'description', content: appConfig.description }],
  },
  components: {
    DatePicker,
    Layout,
    Stats,
    Projection,
    Revenue,
    Sales,
    Activity,
    Products,
  },
  data() {
    return {
      state: {
        date: new Date(),
      },
    }
  },
}
</script>

<template>
  <Layout>
    <!-- start page title -->
    <div class="row">
      <div class="col-12">
        <div class="page-title-box">
          <div class="page-title-right">
            <form class="form-inline">
              <div class="form-group">
                <div class="input-group">
                  <date-picker
                    id="dash-daterange"
                    v-model="state.date"
                    :first-day-of-week="1"
                    lang="en"
                    format="MM/DD/YYYY"
                  ></date-picker>
                </div>
              </div>
              <a href="javascript: void(0);" class="btn btn-primary ml-2">
                <i class="mdi mdi-autorenew"></i>
              </a>
              <a href="javascript: void(0);" class="btn btn-primary ml-1">
                <i class="mdi mdi-filter-variant"></i>
              </a>
            </form>
          </div>
          <h4 class="page-title">Dashboard</h4>
        </div>
      </div>
    </div>
    <!-- end page title -->

    <div class="row">
      <div class="col-xl-5 col-lg-6">
        <Stats />
      </div>
      <div class="col-xl-7 col-lg-6">
        <Projection />
      </div>
      <!-- end col -->
    </div>

    <div class="row">
      <div class="col-xl-9">
        <div class="card">
          <Revenue />
        </div>
      </div>
      <div class="col-xl-3">
        <Sales />
      </div>
    </div>
    <div class="row">
      <div class="col-xl-3">
        <Activity />
      </div>
      <div class="col">
        <Products />
      </div>
    </div>
  </Layout>
</template>
