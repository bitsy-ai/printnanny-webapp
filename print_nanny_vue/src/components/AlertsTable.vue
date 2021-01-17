<script>
import { mapActions, mapState } from 'vuex'

import {
  ALERTS_TABLE_MODULE,
  FETCH_ALERTS,
  ALERTS,
  PAGINATION
} from '@/store/alerts'

export default {
  props: {
    page: String
  },
  data: () => ({
    filter: '',
    fields: ['status', 'event_type', 'title', 'description', 'time'],
    sortBy: 'time',
    sortDesc: true
  }),
  methods: {
    ...mapActions(ALERTS_TABLE_MODULE, {
      fetchAlerts: FETCH_ALERTS
    })
  },
  computed: {
    ...mapState(ALERTS_TABLE_MODULE, {
      alerts: ALERTS,
      pagination: PAGINATION
    })
  },
  created () {
    console.log(this.page)
    this.fetchAlerts({ page: this.page })
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
          :items="alerts.results"
          primary-key="id"
          :filter="filter"
          :current-page="pagination.currentPage"
          :perPage="pagination.pageSize"
          :sortBy="sortBy"
          :sortDesc="sortDesc"
        >
        <template #cell(status)="data">
          <span :class="`badge badge-${data.item.color}`"><strong>{{ data.item.alert_subtype}}</strong></span>
        </template>

        <template #cell(event_type)="data">
          {{ data.item.alert_type }}
        </template>

        </b-table>
      </b-col>
    </b-row>
    <b-row>
      <b-col>

        <b-pagination-nav
        :link-gen="pagination.linkGen"
        :number-of-pages="pagination.totalPages"
        use-router>

        </b-pagination-nav>
      </b-col>
    </b-row>
  </div>
 </template>
