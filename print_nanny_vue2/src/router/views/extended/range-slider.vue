<script>
import VueSlideBar from 'vue-slide-bar'

import appConfig from '@src/app.config'
import Layout from '@layouts/main'
import PageHeader from '@components/page-header'

/**
 * Range Slider component
 */
export default {
  page: {
    title: 'Range Slider',
    meta: [{ name: 'description', content: appConfig.description }],
  },
  components: { VueSlideBar, Layout, PageHeader },
  data() {
    return {
      title: 'Range Slider',
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
          text: 'Range Slider',
          active: true,
        },
      ],
      simpleValue: 10,
      sliderCustomzie: 300,
      sliderWithLabel: {
        value: 45,
        data: [15, 30, 45, 60, 75, 90, 120],
        range: [
          {
            label: '15 mins',
          },
          {
            label: '30 mins',
            isHide: true,
          },
          {
            label: '45 mins',
          },
          {
            label: '1 hr',
            isHide: true,
          },
          {
            label: '1 hr 15 mins',
          },
          {
            label: '1 hr 30 mins',
            isHide: true,
          },
          {
            label: '2 hrs',
          },
        ],
        rangeValue: {},
      },
      customData: {
        value: 3,
        data: [1, 2, 3, 4, 5, 6, 7],
        range: [
          {
            label: 'Sunday',
          },
          {
            label: 'Monday',
          },
          {
            label: 'Tuesday',
          },
          {
            label: 'Wednesday',
          },
          {
            label: 'Thursday',
          },
          {
            label: 'Friday',
          },
          {
            label: 'Saturday',
          },
        ],
      },
      loader: null,
      loadingValue: 0,
      customStyle: 800,
      lineHeight: 10,
    }
  },
  methods: {
    /**
     * Range and label slider set range
     */
    callbackRange(val) {
      this.sliderWithLabel.rangeValue = val
    },
    /**
     * Loading slider
     */
    startLoad() {
      this.loader = setInterval(() => {
        this.loadingValue++
        if (this.loadingValue === 100) {
          clearInterval(this.loader)
        }
      }, 100)
    },
  },
}
</script>

<template>
  <Layout>
    <PageHeader :title="title" :items="items" />
    <div class="row">
      <div class="col-md-6">
        <div class="card">
          <div class="card-body">
            <h4 class="header-title">Default</h4>
            <p class="text-muted font-14">Start without params</p>
            <vue-slide-bar v-model="simpleValue" />
          </div>
          <!-- end card-body -->
        </div>
        <!-- end card -->
      </div>
      <!-- end col -->
      <div class="col-md-6">
        <div class="card">
          <div class="card-body">
            <h4 class="header-title">Min-Max</h4>
            <p class="text-muted font-14">Set min value, max value and start point</p>
            <vue-slide-bar v-model="sliderCustomzie" :min="100" :max="500" />
          </div>
          <!-- end card-body -->
        </div>
        <!-- end card -->
      </div>
      <!-- end col -->
    </div>
    <!-- end row -->

    <div class="row">
      <div class="col-md-6">
        <div class="card">
          <div class="card-body">
            <h4 class="header-title">Range and Label</h4>
            <p class="text-muted font-14">Set range, data</p>
            <div class="px-3">
              <vue-slide-bar
                v-model="sliderWithLabel.value"
                :data="sliderWithLabel.data"
                :range="sliderWithLabel.range"
                @callbackRange="callbackRange"
              />
            </div>
          </div>
          <!-- end card-body -->
        </div>
        <!-- end card -->
      </div>
      <!-- end col -->
      <div class="col-md-6">
        <div class="card">
          <div class="card-body">
            <h4 class="header-title">Loading</h4>
            <p class="text-muted font-14">Set start</p>
            <vue-slide-bar v-model="loadingValue" :show-tooltip="true" :is-disabled="true" />
            <br />
            <b-button size="sm" variant="light" @click="startLoad">Start</b-button>
          </div>
          <!-- end card-body -->
        </div>
        <!-- end card -->
      </div>
      <!-- end col -->
    </div>
    <!-- end row -->

    <div class="row">
      <div class="col-md-6">
        <div class="card">
          <div class="card-body">
            <h4 class="header-title">Custom Style</h4>
            <p class="text-muted font-14">Set line-heigth</p>
            <vue-slide-bar v-model="customStyle" :min="100" :max="1000" :line-height="lineHeight" />
          </div>
          <!-- end card-body -->
        </div>
        <!-- end card -->
      </div>
      <!-- end col -->
      <div class="col-md-6">
        <div class="card">
          <div class="card-body pb-0">
            <h4 class="header-title">Custom Data</h4>
            <p class="text-muted font-14">Set label</p>
            <div class="px-3">
              <vue-slide-bar :data="customData.data" :range="customData.range" />
            </div>
          </div>
          <!-- end card-body -->
        </div>
        <!-- end card -->
      </div>
      <!-- end col -->
    </div>
    <!-- end row -->
  </Layout>
</template>