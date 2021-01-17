<script>
import { mapActions } from 'vuex'
import { createInstance } from 'vuex-pagination'
export default {
  components: { },
  data: () => ({
    filter: '',
    currentPage: 1,
    perPage: 25,
    fields: ['alert_type', 'alert_subtype', 'icon', 'title', 'time']
  }),
  computed: {
    alerts: createInstance('alerts', {
      page: 1,
      pageSize: 25,
      args () {
        return {
          query: this.filter
        }
      }
    })
  },
  methods: {
    ...mapActions('alerts', [
      'dismissAll', 'seenAll'

    ])
  }
}
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
          striped
          hover
          outlined
          :fields="fields"
          :per-page="alerts.pageSize"
          :current-page="alerts.page"
          :items="alerts.items"
          :filter="filter"
        >
        </b-table>
      </b-col>
    </b-row>
  </div>
 </template>
