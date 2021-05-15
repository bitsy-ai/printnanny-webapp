<script>
import appConfig from '@src/app.config'
import Layout from '@layouts/main'
import PageHeader from '@components/page-header'

import Profile from '@components/widgets/profile'
import Stat from '@components/widgets/widget-stat'
import StatIcon from '@components/widgets/widget-stat-icon'
import StatChart from '@components/widgets/widget-stat-chart'
import Chat from '@components/widgets/chat'
import ToDoList from '@components/widgets/todo-list'
import Message from '@components/widgets/message'
import RecentActivity from '@components/widgets/recent-activity'
import Transactions from '@components/widgets/transactions'
import StatChart2 from '@components/widgets/widget-stat-chart2'

/**
 * Widgets component
 */
export default {
  page: {
    title: 'Widgets',
    meta: [{ name: 'description', content: appConfig.description }],
  },
  components: {
    Layout,
    PageHeader,
    Profile,
    Stat,
    StatIcon,
    StatChart,
    Chat,
    ToDoList,
    Message,
    RecentActivity,
    Transactions,
    StatChart2,
  },
  data() {
    return {
      title: 'Widgets',
      items: [
        {
          text: 'Hyper',
          href: '/',
        },
        {
          text: 'Widgets',
          active: true,
        },
      ],
      statdata: [
        {
          title: '$424,652',
          subtitle: 'Sales',
          chartColor: '#3688fc',
          chartData: [
            47,
            45,
            54,
            38,
            56,
            24,
            65,
            31,
            37,
            39,
            62,
            51,
            35,
            41,
            35,
            27,
            93,
            53,
            61,
            27,
            54,
            43,
            19,
            46,
          ],
          chartType: 'area',
        },
        {
          title: '$135,965',
          subtitle: 'Profits',
          chartColor: '#0acf97',
          chartData: [
            47,
            45,
            54,
            38,
            56,
            24,
            65,
            31,
            37,
            39,
            62,
            51,
            35,
            41,
            35,
            27,
            93,
            53,
            61,
            27,
            54,
            43,
            19,
            46,
          ],
          chartType: 'bar',
        },
      ],
      staticon: [
        {
          icon: 'mdi-currency-btc',
          number: '$6,254',
          title: 'Revenue',
          color: 'danger',
          subtext: '7.00%',
        },
        {
          icon: 'mdi-pulse widget-icon',
          number: '+ 30.56%',
          title: 'Growth',
          color: 'success',
          subtext: '4.87%',
        },
        {
          icon: 'mdi-account-multiple',
          number: '36,254',
          title: 'Customers',
          color: 'success',
          subtext: '5.27%',
        },
        {
          icon: 'mdi-currency-usd',
          number: '$10,245',
          title: 'Revenue',
          color: 'danger',
          subtext: '1.08%',
        },
      ],
      statchart: [
        {
          title: 'Campaign Sent',
          number: '9,184',
          subtext: '3.27%',
          chartData: [25, 66, 41, 89, 63, 25, 44, 12, 36, 9, 54],
          chartColor: '#727cf5',
          chartType: 'bar',
        },
        {
          title: 'New Leads',
          number: '3,254',
          subtext: '5.38%',
          chartData: [25, 66, 41, 89, 63, 25, 44, 12, 36, 9, 54],
          chartColor: '#727cf5',
          chartType: 'line',
        },
        {
          title: 'Deals',
          number: '861',
          subtext: '4.87%',
          chartData: [12, 14, 2, 47, 42, 15, 47, 75, 65, 19, 14],
          chartColor: '#727cf5',
          chartType: 'bar',
        },
        {
          title: 'Booked Revenue',
          number: '$253k',
          subtext: '11.7%',
          chartData: [47, 45, 74, 14, 56, 74, 14, 11, 7, 39, 82],
          chartColor: '#727cf5',
          chartType: 'bar',
        },
      ],
      chatMessages: [
        {
          id: 1,
          image: require('@assets/images/users/avatar-5.jpg'),
          name: 'Geneva',
          message: 'Hello!',
          time: '10:00',
        },
        {
          id: 2,
          image: require('@assets/images/users/avatar-1.jpg'),
          name: 'Dominic',
          message: 'Hi, How are you? What about our next meeting?',
          time: '10:01',
        },
        {
          id: 3,
          image: require('@assets/images/users/avatar-5.jpg'),
          name: 'Geneva',
          message: 'Yeah everything is fine',
          time: '10:01',
        },
        {
          id: 4,
          image: require('@assets/images/users/avatar-1.jpg'),
          name: 'Dominic',
          message: "Wow that's great",
          time: '10:02',
        },
        {
          id: 5,
          image: require('@assets/images/users/avatar-5.jpg'),
          name: 'Geneva',
          message: 'Yup!',
          time: '10:03',
        },
      ],
      todoItems: [
        {
          id: 1,
          task: 'Build an angular app',
          isCompleted: true,
        },
        {
          id: 2,
          task: 'Create new version 3.0',
          isCompleted: false,
        },
        {
          id: 3,
          task: 'Hehe!! This is looks cool!',
          isCompleted: false,
        },
        {
          id: 4,
          task: 'Testing??',
          isCompleted: true,
        },
        {
          id: 5,
          task: 'Creating component page',
          isCompleted: true,
        },
        {
          id: 6,
          task: 'Build a js based app',
          isCompleted: true,
        },
        {
          id: 7,
          task: 'Design One page theme',
          isCompleted: false,
        },
        {
          id: 8,
          task: "That's Brilliant",
          isCompleted: true,
        },
      ],
      messages: [
        {
          image: require('@assets/images/users/avatar-2.jpg'),
          name: 'Tomaslau',
          message: "I've finished it! See you so...",
        },
        {
          image: require('@assets/images/users/avatar-3.jpg'),
          name: 'Stillnotdavid',
          message: 'This theme is awesome!',
        },
        {
          image: require('@assets/images/users/avatar-4.jpg'),
          name: 'Kurafire',
          message: 'Nice to meet you',
        },
        {
          image: require('@assets/images/users/avatar-5.jpg'),
          name: 'Shahedk',
          message: "Hey! there I'm available...",
        },
        {
          image: require('@assets/images/users/avatar-6.jpg'),
          name: 'Adhamdannaway',
          message: 'This theme is awesome!',
        },
      ],
      activityData: [
        {
          id: 1,
          icon: 'mdi-upload',
          title: 'You sold an item',
          text: 'Paul Burgess just purchased “Hyper - Admin Dashboard”!',
          subtext: '5 minutes ago',
          color: 'info',
        },
        {
          id: 2,
          icon: 'mdi-airplane',
          title: 'Product on the Bootstrap Market',
          text: 'Dave Gamache added',
          subtext: '30 minutes ago',
          boldText: 'Admin Dashboard',
          color: 'primary',
        },
        {
          id: 3,
          icon: 'mdi-microphone',
          title: 'Robert Delaney',
          text: 'Send you message',
          boldText: '"Are you there?"',
          subtext: '2 hours ago',
          color: 'info',
        },
        {
          id: 4,
          icon: 'mdi-airplane',
          title: 'Audrey Tobey',
          text: 'Uploaded a photo',
          subtext: '14 hours ago',
          boldText: '"Error.jpg"',
          color: 'primary',
        },
      ],
      transactions: [
        {
          title: 'Purchased Hyper Admin Template',
          icon: 'mdi-arrow-collapse-up',
          date: 'Today',
          amount: '-$489.30',
          color: 'danger',
        },
        {
          title: 'Payment received Bootstrap Marketplace',
          icon: 'mdi-arrow-collapse-down',
          date: 'Yesterday',
          amount: '+$1578.54',
          color: 'success',
        },
        {
          title: 'Freelance work - Shane',
          icon: 'mdi-arrow-collapse-down',
          date: '16 Sep 2018',
          amount: '+$247.5',
          color: 'success',
        },
        {
          title: 'Hire new developer for work',
          icon: 'mdi-arrow-collapse-up',
          date: '09 Sep 2018',
          amount: '-$185.14',
          color: 'danger',
        },
        {
          title: 'Money received from paypal',
          icon: 'mdi-arrow-collapse-down',
          date: '28 Aug 2018',
          amount: '+$684.45',
          color: 'success',
        },
        {
          title: 'Zairo landing purchased',
          icon: 'mdi-arrow-collapse-up',
          date: '17 Aug 2018',
          amount: '-$21.00',
          color: 'danger',
        },
        {
          title: 'Interest received',
          icon: 'mdi-arrow-collapse-down',
          date: '09 Sep 2018',
          amount: '+$784.55',
          color: 'success',
        },
      ],
      chartData: [
        {
          title: 'Sales Summary',
          number: '259',
          chartColor: '#734CEA',
          chartData: [25, 66, 41, 59, 25, 44, 12, 36, 9, 21],
          chartType: 'line',
        },
        {
          title: 'Revenue',
          number: '$6,254',
          chartColor: '#34bfa3',
          chartData: [12, 14, 2, 47, 32, 44, 14, 55, 41, 69],
          chartType: 'bar',
        },
        {
          title: 'Active Users',
          number: '324',
          chartColor: '#f4516c',
          chartData: [47, 45, 74, 32, 56, 31, 44, 33, 45, 19],
          chartType: 'line',
        },
        {
          title: 'Expense Summary',
          number: '$4,745.2',
          chartColor: '#00c5dc',
          chartData: [15, 75, 47, 65, 14, 32, 19, 54, 44, 61],
          chartType: 'bar',
        },
      ],
      chatWindowHeight: '340px',
      todoWindowHeight: '315px',
      activityWindowHeight: '330px',
      textColor: 'black',
    }
  },
}
</script>

<template>
  <Layout>
    <PageHeader
      :title="title"
      :items="items"
    />
    <div class="row">
      <div class="col-lg-4">
        <div class="card">
          <div class="card-body">
            <Profile :text-color="textColor" />
          </div>
          <!-- end card-body-->
        </div>
      </div>
      <div
        v-for="data of statdata"
        :key="data.chartType"
        class="col-lg-4"
      >
        <Stat
          :title="data.title"
          :subtitle="data.subtitle"
          :chart-color="data.chartColor"
          :chart-data="data.chartData"
          :chart-type="data.chartType"
        />
      </div>
      <!-- end col -->
    </div>
    <!-- end row -->

    <div class="row">
      <div
        v-for="stat of staticon"
        :key="stat.icon"
        class="col-xl-3 col-lg-6"
      >
        <StatIcon
          :icon="stat.icon"
          :title="stat.title"
          :number="stat.number"
          :subtext="stat.subtext"
          :color="stat.color"
        />
      </div>
      <!-- end col -->
    </div>
    <!-- end row -->

    <div class="row">
      <div
        v-for="chart of statchart"
        :key="chart.text"
        class="col-xl-3 col-lg-6"
      >
        <div class="card">
          <div class="card-body">
            <StatChart
              :title="chart.title"
              :number="chart.number"
              :chart-data="chart.chartData"
              :chart-color="chart.chartColor"
              :chart-type="chart.chartType"
              :subtext="chart.subtext"
            />
          </div>
        </div>
      </div>
      <!-- end col -->
    </div>
    <!-- end row -->

    <div class="row">
      <div class="col-lg-4">
        <!-- chat -->
        <Chat
          :chat-messages="chatMessages"
          :chat-window-height="chatWindowHeight"
        />
      </div>
      <!-- end col -->
      <div class="col-lg-4">
        <div class="card cta-box bg-danger text-white">
          <div class="card-body">
            <div class="media align-items-center">
              <div class="media-body">
                <h2 class="mt-0">
                  <i class="mdi mdi-bullhorn-outline"></i>
                </h2>
                <h3 class="m-0 font-weight-normal cta-box-title">
                  Enhance your
                  <b>Campaign</b> for better outreach
                  <i class="mdi mdi-arrow-right-bold-outline"></i>
                </h3>
              </div>
              <img
                class="ml-3"
                src="@assets/images/email-campaign.svg"
                width="120"
                alt="Generic placeholder image"
              />
            </div>
          </div>
          <!-- end card-body -->
        </div>
        <!-- end card-->

        <div class="card cta-box bg-primary text-white">
          <div class="card-body">
            <div class="text-center">
              <h3 class="m-0 font-weight-normal cta-box-title">
                Enhance your
                <b>Campaign</b> for better outreach
              </h3>

              <img
                class="my-3"
                src="@assets/images/report.svg"
                width="180"
                alt="Generic placeholder image"
              />

              <br />

              <a
                href="javascript:void(0);"
                class="btn btn-sm btn-light btn-rounded"
              >
                Know More
                <i class="mdi mdi-arrow-right"></i>
              </a>
            </div>
          </div>
          <!-- end card-body -->
        </div>
        <!-- end card-->
      </div>
      <div class="col-lg-4">
        <!-- Todo -->
        <ToDoList
          :items="todoItems"
          :todo-window-height="todoWindowHeight"
        />
      </div>
    </div>
    <!-- end row -->

    <div class="row">
      <div class="col-lg-4">
        <!-- Messages -->
        <Message :messages="messages" />
      </div>
      <div class="col-lg-4">
        <!-- Recent-activity -->
        <RecentActivity
          :activity-data="activityData"
          :activity-window-height="activityWindowHeight"
        />
      </div>
      <div class="col-lg-4">
        <!-- Transactions -->
        <Transactions :transactions="transactions" />
      </div>
    </div>
    <!-- end row -->

    <div class="row">
      <div
        v-for="item of chartData"
        :key="item.text"
        class="col-lg-6 col-xl-3"
      >
        <StatChart2
          :title="item.title"
          :number="item.number"
          :chart-color="item.chartColor"
          :chart-data="item.chartData"
          :chart-type="item.chartType"
        />
      </div>
      <!-- end col -->
    </div>
    <!-- end row -->

    <div class="row">
      <div class="col-lg-4">
        <div class="card text-white bg-info overflow-hidden">
          <div class="card-body">
            <div class="toll-free-box text-center">
              <h4>
                <i class="mdi mdi-deskphone"></i> Toll Free : 1-234-567-8901
              </h4>
            </div>
          </div>
          <!-- end card-body-->
        </div>
        <!-- end card -->
      </div>
      <!-- end col-->

      <div class="col-lg-4">
        <div class="card text-white bg-danger overflow-hidden">
          <div class="card-body">
            <div class="toll-free-box text-center">
              <h4>
                <i class="mdi mdi-headset"></i> Need help ? Just contact us
              </h4>
            </div>
          </div>
          <!-- end card-body-->
        </div>
        <!-- end card -->
      </div>
      <!-- end col-->

      <div class="col-lg-4">
        <div class="card bg-success text-white">
          <div class="card-body">
            <div class="text-center">
              <h4>
                <i class="mdi mdi-deskphone"></i> Toll Free : 1-234-567-8901
              </h4>
            </div>
          </div>
          <!-- end card-body-->
        </div>
        <!-- end card -->
      </div>
      <!-- end col-->
    </div>
    <!-- end row -->
  </Layout>
</template>