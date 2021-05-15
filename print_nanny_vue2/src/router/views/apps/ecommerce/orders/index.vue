<script>
import appConfig from '@src/app.config'
import Layout from '@layouts/main'
import PageHeader from '@components/page-header'

import { orderData } from './data'

/**
 * Orders component
 */
export default {
  page: {
    title: 'Orders',
    meta: [{ name: 'description', content: appConfig.description }],
  },
  components: { Layout, PageHeader },
  data() {
    return {
      orderData: orderData,
      title: 'Orders',
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
          text: 'Orders',
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
      <div class="col-12">
        <div class="card">
          <div class="card-body">
            <div class="row mb-2">
              <div class="col-lg-8">
                <form class="form-inline">
                  <div class="form-group mb-2">
                    <label for="inputPassword2" class="sr-only">Search</label>
                    <input
                      id="inputPassword2"
                      type="search"
                      class="form-control"
                      placeholder="Search..."
                    />
                  </div>
                  <div class="form-group mx-sm-3 mb-2">
                    <label for="status-select" class="mr-2">Status</label>
                    <select id="status-select" class="custom-select">
                      <option selected>Choose...</option>
                      <option value="1">Paid</option>
                      <option value="2">Awaiting Authorization</option>
                      <option value="3">Payment failed</option>
                      <option value="4">Cash On Delivery</option>
                      <option value="5">Fulfilled</option>
                      <option value="6">Unfulfilled</option>
                    </select>
                  </div>
                </form>
              </div>
              <div class="col-lg-4">
                <div class="text-lg-right">
                  <button type="button" class="btn btn-danger mb-2 mr-2">
                    <i class="mdi mdi-basket mr-1"></i> Add New Order
                  </button>
                  <button type="button" class="btn btn-light mb-2">Export</button>
                </div>
              </div>
              <!-- end col-->
            </div>

            <div class="table-responsive">
              <table class="table table-centered mb-0">
                <thead class="thead-light">
                  <tr>
                    <th style="width: 20px;">
                      <div class="custom-control custom-checkbox">
                        <input id="customCheck" type="checkbox" class="custom-control-input" />
                        <label class="custom-control-label" for="customCheck">&nbsp;</label>
                      </div>
                    </th>
                    <th>Order ID</th>
                    <th>Date</th>
                    <th>Payment Status</th>
                    <th>Total</th>
                    <th>Payment Method</th>
                    <th>Order Status</th>
                    <th style="width: 125px;">Action</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="(order, index) of orderData" :key="order.id">
                    <td>
                      <div class="custom-control custom-checkbox">
                        <input
                          :id="`customCheck${index}`"
                          type="checkbox"
                          class="custom-control-input"
                        />
                        <label class="custom-control-label" :for="`customCheck${index}`">&nbsp;</label>
                      </div>
                    </td>
                    <td>
                      <router-link
                        tag="a"
                        to="/apps/ecommerce/order-detail"
                        class="text-body font-weight-bold"
                      >{{order.id}}</router-link>
                    </td>
                    <td>
                      {{order.date}}
                      <small class="text-muted">{{order.time}}</small>
                    </td>
                    <td>
                      <h5>
                        <span
                          class="badge badge-success-lighten"
                          :class="{ 'badge-warning-lighten': order.status === 'Awaiting Authorization',
                          'badge-danger-lighten': order.status === 'Payment Failed' }"
                        >
                          <i
                            class="mdi"
                            :class="{ 'mdi-coin': order.status === 'Paid', 
                              'mdi-timer-sand': order.status === 'Awaiting Authorization',
                            'mdi-cancel': order.status === 'Payment Failed' }"
                          ></i>
                          {{order.status}}
                        </span>
                      </h5>
                    </td>
                    <td>{{order.total}}</td>
                    <td>{{order.payment}}</td>
                    <td>
                      <h5>
                        <span
                          class="badge badge-info-lighten"
                          :class="{ 'badge-warning-lighten': order.orderStatus === 'Processing',
                          'badge-danger-lighten': order.orderStatus === 'Cancelled' }"
                        >{{order.orderStatus}}</span>
                      </h5>
                    </td>
                    <td>
                      <a href="javascript:void(0);" class="action-icon">
                        <i class="mdi mdi-eye"></i>
                      </a>
                      <a href="javascript:void(0);" class="action-icon">
                        <i class="mdi mdi-square-edit-outline"></i>
                      </a>
                      <a href="javascript:void(0);" class="action-icon">
                        <i class="mdi mdi-delete"></i>
                      </a>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
    </div>
  </Layout>
</template>