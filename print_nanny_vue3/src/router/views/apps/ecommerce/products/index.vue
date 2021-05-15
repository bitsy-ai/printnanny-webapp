<script>
import Vuetable from 'vuetable-2/src/components/Vuetable'
import VuetablePagination from 'vuetable-2/src/components/VuetablePagination'
import VuetablePaginationInfo from 'vuetable-2/src/components/VuetablePaginationInfo'
import _ from 'lodash'

import appConfig from '@src/app.config'
import Layout from '@layouts/main'
import PageHeader from '@components/page-header'

import { productData } from './data'

/**
 * Products component
 */
export default {
  page: {
    title: 'Products',
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
      productData: productData,
      title: 'Products',
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
          text: 'Products',
          active: true,
        },
      ],
      data: [],
      perPage: 5,
      fields: [
        { name: '__slot:name', title: 'Product', sortField: 'name' },
        { name: 'category', sortField: 'category' },
        { name: 'price', sortField: 'price' },
        { name: 'date', sortField: 'date' },
        { name: 'quantity', sortField: 'quantity' },
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
    this.data = this.productData
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
    onPaginationData(productData) {
      this.$refs.pagination.setPaginationData(productData)
      this.$refs.paginationInfo.setPaginationData(productData)
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
                <a href="javascript: void(0);" class="btn btn-danger mb-2">
                  <i class="mdi mdi-plus-circle mr-2"></i> Add Products
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
                class="table table-centered datatables"
                @vuetable:pagination-data="onPaginationData"
              >
                <template slot="status" slot-scope="props">
                  <span
                    class="badge"
                    :class="{
                      'badge-success': props.rowData.status === 'Active',
                      'badge-danger': props.rowData.status === 'Deactive' }"
                  >{{ props.rowData.status }}</span>
                </template>
                <template slot="name" slot-scope="prop">
                  <img :src="`${prop.rowData.product}`" class="rounded mr-3" height="48" />
                  <p class="m-0 d-inline-block align-middle font-16">
                    <router-link
                      tag="a"
                      to="/apps/ecommerce/products-detail"
                      class="text-body"
                    >{{prop.rowData.name}}</router-link>

                    <br />
                    <span class="text-warning mdi mdi-star"></span>
                    <span class="text-warning mdi mdi-star"></span>
                    <span class="text-warning mdi mdi-star"></span>
                    <span class="text-warning mdi mdi-star"></span>
                    <span class="text-warning mdi mdi-star"></span>
                  </p>
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