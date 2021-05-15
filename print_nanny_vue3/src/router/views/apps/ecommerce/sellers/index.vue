<script>
import Vuetable from 'vuetable-2/src/components/Vuetable'
import VuetablePagination from 'vuetable-2/src/components/VuetablePagination'
import VuetablePaginationInfo from 'vuetable-2/src/components/VuetablePaginationInfo'
import _ from 'lodash'

import appConfig from '@src/app.config'
import Layout from '@layouts/main'
import PageHeader from '@components/page-header'

import { sellersData } from './data'

/**
 * Sellers component
 */
export default {
  page: {
    title: 'Sellers',
    meta: [{ name: 'description', content: appConfig.description }],
  },
  components: {
    Vuetable,
    VuetablePagination,
    VuetablePaginationInfo,
    Layout,
    PageHeader,
  },
  data() {
    return {
      sellersData: sellersData,
      title: 'Sellers',
      items: [
        {
          text: 'Hyper',
          href: '/',
        },
        {
          text: 'eCommerce',
          href: '/',
        },
        {
          text: 'Sellers',
          active: true,
        },
      ],
      data: [],
      perPage: 10,
      fields: [
        { name: '__slot:name', title: 'Seller', sortField: 'name' },
        { name: 'storename', title: 'Store Name', sortField: 'storename' },
        { name: 'products', sortField: 'products' },
        { name: 'balance', title: 'Wallet Balance', sortField: 'balance' },
        { name: 'date', title: 'Create Date', sortField: 'date' },
        { name: '__slot:revenue', title: 'Revenue' },
        { name: '__slot:actions', title: 'Action' },
      ],
      css: {
        pagination: {
          activeClass: 'btn-primary text-white',
          pageClass: 'btn btn-rounded',
          linkClass: 'btn',
          icons: {
            prev: '',
            next: '',
          },
        },
      },
      series: [
        {
          data: sellersData.series,
        },
      ],
      chartOptions: {
        chart: {
          sparkline: {
            enabled: true,
          },
        },
        stroke: {
          width: 2,
          curve: 'smooth',
        },
        markers: {
          size: 0,
        },
        colors: ['#727cf5'],
        tooltip: {
          fixed: {
            enabled: false,
          },
          x: {
            show: false,
          },
          y: {
            title: {
              formatter: function(seriesName) {
                return ''
              },
            },
          },
          marker: {
            show: false,
          },
        },
      },
    }
  },
  watch: {
    data(newVal, oldVal) {
      this.$refs.vuetable.refresh()
    },
  },
  mounted() {
    this.data = this.sellersData
  },
  methods: {
    /**
     * Pagination page change
     */
    onChangePage(page) {
      this.$refs.vuetable.changePage(page)
    },
    /**
     * Pagination info and pagination show
     */
    onPaginationData(sellersData) {
      this.$refs.pagination.setPaginationData(sellersData)
      this.$refs.paginationInfo.setPaginationData(sellersData)
    },

    /**
     * Manage data sorting and show pagination
     */
    dataManager(sortOrder, pagination) {
      if (this.data.length < 1) return
      let local = this.data

      // sortOrder can be empty, so we have to check for that as well
      if (sortOrder.length > 0) {
        local = _.orderBy(local, sortOrder[0].sortField, sortOrder[0].direction)
      }
      pagination = this.$refs.vuetable.makePagination(
        local.length,
        this.perPage
      )
      let from = pagination.from - 1
      let to = from + this.perPage

      return {
        pagination: pagination,
        data: _.slice(local, from, to),
      }
    },
  },
}
</script>

<template>
  <Layout>
    <PageHeader :title="title" :items="items" />
    <div class="row">
      <div class="col-12">
        <div class="card">
          <div class="card-body">
            <div class="row mb-2">
              <div class="col-sm-4">
                <a href="javascript:void(0);" class="btn btn-danger mb-2">
                  <i class="mdi mdi-plus-circle mr-2"></i> Add Sellers
                </a>
              </div>
              <div class="col-sm-8">
                <div class="text-sm-right">
                  <button type="button" class="btn btn-success mb-2 mr-1">
                    <i class="mdi mdi-settings"></i>
                  </button>
                  <button type="button" class="btn btn-light mb-2 mr-1">Import</button>
                  <button type="button" class="btn btn-light mb-2">Export</button>
                </div>
              </div>
              <!-- end col-->
            </div>
            <!-- Table -->
            <div class="table-responsive">
              <vuetable
                ref="vuetable"
                :per-page="perPage"
                :fields="fields"
                :api-mode="false"
                :data-manager="dataManager"
                pagination-path="pagination"
                class="table table-centered datatables table-hover"
                @vuetable:pagination-data="onPaginationData"
              >
                <template slot="name" slot-scope="prop" class="table-user">
                  <img
                    :src="`${prop.rowData.image}`"
                    alt="table-user"
                    class="mr-2 rounded-circle"
                    height="30px"
                  />
                  <a
                    href="javascript:void(0);"
                    class="text-body font-weight-semibold"
                  >{{prop.rowData.name}}</a>
                </template>
                <template slot="revenue" slot-scope="prop">
                  <apexchart
                    height="35"
                    width="80"
                    type="line"
                    class="spark-chart"
                    :series="prop.rowData.series"
                    :options="chartOptions"
                  ></apexchart>
                </template>
                <template slot="actions">
                  <div class="table-button-container">
                    <a href="javascript:void(0);" class="action-icon">
                      <i class="mdi mdi-square-edit-outline"></i>
                    </a>
                    <a href="javascript:void(0);" class="action-icon">
                      <i class="mdi mdi-delete"></i>
                    </a>
                  </div>
                </template>
              </vuetable>
            </div>
            <!-- end table -->

            <!-- pagination -->
            <div class="row">
              <div class="col-sm-12 col-md-5">
                <vuetable-pagination-info ref="paginationInfo" class="font-weight-semibold"></vuetable-pagination-info>
              </div>
              <div class="col-sm-12 col-md-7">
                <!-- pagination -->
                <vuetable-pagination
                  ref="pagination"
                  :css="css.pagination"
                  class="pagination pagination-rounded justify-content-end"
                  @vuetable-pagination:change-page="onChangePage"
                ></vuetable-pagination>
                <!-- end pagination -->
              </div>
            </div>
            <!-- end pagination -->
          </div>
        </div>
      </div>
    </div>
  </Layout>
</template>