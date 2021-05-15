<script>
import Vuetable from 'vuetable-2/src/components/Vuetable'
import VuetablePagination from 'vuetable-2/src/components/VuetablePagination'
import VuetablePaginationInfo from 'vuetable-2/src/components/VuetablePaginationInfo'
import _ from 'lodash'

import appConfig from '@src/app.config'
import Layout from '@layouts/main'
import PageHeader from '@components/page-header'

import { customersData } from './data'

/**
 * Customers component
 */
export default {
  page: {
    title: 'Customers',
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
      customersData: customersData,
      title: 'Customers',
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
          text: 'Customers',
          active: true,
        },
      ],
      data: [],
      perPage: 10,
      fields: [
        { name: '__slot:name', title: 'Customer', sortField: 'name' },
        { name: 'phone', sortField: 'phone' },
        { name: 'email', sortField: 'email' },
        { name: 'location', sortField: 'location' },
        { name: 'date', title: 'Create Date', sortField: 'date' },
        { name: '__slot:status', title: 'Status', sortField: 'status' },
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
    }
  },
  watch: {
    data(newVal, oldVal) {
      this.$refs.vuetable.refresh()
    },
  },
  mounted() {
    this.data = this.customersData
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
    onPaginationData(customersData) {
      this.$refs.pagination.setPaginationData(customersData)
      this.$refs.paginationInfo.setPaginationData(customersData)
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
                  <i class="mdi mdi-plus-circle mr-2"></i> Add Customers
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
                class="table table-centered datatables table-striped"
                @vuetable:pagination-data="onPaginationData"
              >
                <template slot="status" slot-scope="props">
                  <span
                    class="badge"
                    :class="{
                      'badge-success-lighten': props.rowData.status === 'Active',
                      'badge-danger-lighten': props.rowData.status === 'Blocked' }"
                  >{{ props.rowData.status }}</span>
                </template>
                <template slot="name" slot-scope="prop">
                  <img :src="`${prop.rowData.image}`" class="mr-2 rounded-circle" height="30" />
                  <a
                    href="javascript:void(0);"
                    class="text-body font-weight-semibold"
                  >{{ prop.rowData.name }}</a>
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
                <vuetable-pagination
                  ref="pagination"
                  :css="css.pagination"
                  class="pagination pagination-rounded justify-content-end"
                  @vuetable-pagination:change-page="onChangePage"
                ></vuetable-pagination>
              </div>
            </div>
            <!-- end pagination -->
          </div>
        </div>
      </div>
    </div>
  </Layout>
</template>