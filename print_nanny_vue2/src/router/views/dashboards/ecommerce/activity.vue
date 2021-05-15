<script>
import RecentActivity from '@components/widgets/recent-activity'

export default {
  components: { RecentActivity },
  data() {
    return {
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
        {
          id: 5,
          icon: 'mdi-upload',
          title: 'You sold an item',
          text: 'Paul Burgess just purchased “Hyper - Admin Dashboard”!',
          subtext: '16 hours ago',
          color: 'info',
        },
        {
          id: 6,
          icon: 'mdi-airplane',
          title: 'Product on the Bootstrap Market',
          text: 'Dave Gamache added',
          subtext: '22 hours ago',
          boldText: 'Admin Dashboard',
          color: 'primary',
        },
        {
          id: 7,
          icon: 'mdi-microphone',
          title: 'Robert Delaney',
          text: 'Send you message',
          subtext: '30 minutes ago',
          boldText: '"Are you there?"',
          color: 'info',
        },
      ],
      activityWindowHeight: '430px',
    }
  },
}
</script>

<template>
  <RecentActivity :activity-data="activityData" :activity-window-height="activityWindowHeight" />
</template>