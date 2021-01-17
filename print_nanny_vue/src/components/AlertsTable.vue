<script>
import { mapActions, mapState } from 'vuex'

import {
  ALERTS_MODULE,
  FETCH_ALERTS,
  ALERTS,
  PAGINATION
} from '@/store/alerts'

console.log('ALERTS_MODULE', ALERTS_MODULE)
console.log('FETCH_ALERTS', FETCH_ALERTS)
console.log('ALERTS', ALERTS)
console.log('PAGINATION', PAGINATION)

export default {
  data: () => ({
    filter: '',
    fields: ['alert_type', 'alert_subtype', 'icon', 'title', 'time'],
    sortBy: '',
    sortDesc: true
  }),
  methods: {
    ...mapActions(ALERTS_MODULE, {
      fetchAlerts: FETCH_ALERTS
    })
  },
  computed: {
    ...mapState(ALERTS_MODULE, {
      alerts: ALERTS,
      pagination: PAGINATION
    })
  },
  created () {
    this.fetchAlerts()
  }
}

// :per-page="alerts.pageSize"
// :current-page="alertsTable.page"
</script>

<template>
  <div class="container">
    <b-row class="mb-3">
      <b-col md="3">
        <b-form-input v-model="filter" type="search" id="filterInput" placeholder="Type to Search"></b-form-input>
      </b-col>
    </b-row>
    <b-row>
      <b-col>
        <b-table
          id="alerts-table"
          striped
          hover
          outlined
          :fields="fields"
          :items="alerts"
          :filter="filter"
          :current-page="pagination.currentPage"
          :perPage="pagination.pageSize"
          :sortBy="sortBy"
          :sortDesc="sortDesc"
        >
        </b-table>
      </b-col>
    </b-row>
    <b-row>
      <b-col>

        <b-pagination-nav :number-of-pages="pagination.totalPages" use-router>

        </b-pagination-nav>
      </b-col>
    </b-row>
  </div>
 </template>
