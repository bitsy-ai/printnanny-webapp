<script>
import StarRating from 'vue-star-rating'

import appConfig from '@src/app.config'
import Layout from '@layouts/main'
import PageHeader from '@components/page-header'

/**
 * Ratings component
 */
export default {
  page: {
    title: 'Ratings',
    meta: [{ name: 'description', content: appConfig.description }],
  },
  components: { StarRating, Layout, PageHeader },
  data() {
    return {
      title: 'Ratings',
      items: [
        {
          text: 'Hyper',
          href: '/',
        },
        {
          text: 'Extended UI',
          href: '/',
        },
        {
          text: 'Ratings',
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
      <div class="col-xl-6">
        <div class="card">
          <div class="card-body">
            <h4 class="header-title mb-2">Default Ratings</h4>
            <star-rating :rating="3" :star-size="23"></star-rating>
          </div>
        </div>
        <div class="card">
          <div class="card-body">
            <h4 class="header-title mb-2">Half Stars</h4>
            <star-rating :increment="0.5" :star-size="23"></star-rating>
          </div>
        </div>
        <div class="card">
          <div class="card-body">
            <h4 class="header-title mb-2">Bordered Stars</h4>
            <star-rating :rating="3" :border-width="2" :star-size="23"></star-rating>
          </div>
        </div>

        <div class="card">
          <div class="card-body">
            <h4 class="header-title mb-2">Vibrant Stars</h4>
            <star-rating inactive-color="#e1bad9" active-color="#cc1166" :star-size="23"></star-rating>
          </div>
        </div>
        <div class="card">
          <div class="card-body">
            <h4 class="header-title mb-2">Fluid Stars</h4>
            <star-rating :increment="0.01" :fixed-points="2" :star-size="23"></star-rating>
          </div>
        </div>
      </div>
      <div class="col-xl-6">
        <div class="card">
          <div class="card-body">
            <h4 class="header-title mb-2">Custom Star Shape</h4>
            <star-rating
              :border-width="5"
              :star-size="23"
              border-color="#d8d8d8"
              :rounded-corners="true"
              :star-points="[23,2, 14,17, 0,19, 10,34, 7,50, 23,43, 38,50, 36,34, 46,19, 31,17]"
            ></star-rating>
          </div>
        </div>
        <div class="card">
          <div class="card-body">
            <h4 class="header-title mb-2">Non rounded start rating</h4>
            <star-rating :rating="4.67" :round-start-rating="false" :star-size="23"></star-rating>
          </div>
        </div>
        <div class="card">
          <div class="card-body">
            <h4 class="header-title mb-2">Readonly and preset value</h4>
            <star-rating :rating="2.5" :read-only="true" :increment="0.01" :star-size="23"></star-rating>
          </div>
        </div>
        <div class="card">
          <div class="card-body">
            <h4 class="header-title mb-2">RTL Support</h4>
            <star-rating :rtl="true" :increment="0.5" :star-size="23"></star-rating>
          </div>
        </div>
      </div>
    </div>
  </Layout>
</template> 
