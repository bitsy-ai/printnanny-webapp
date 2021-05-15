<script>
import simplebar from 'simplebar-vue'

/**
 * Recent-activity component
 * 1. User specifies the title of window using the 'title' input property.
 * 2. Window height set using the 'activityWindowHeight' input property. Height would count in pixel.
 * 3. Activitydata array specify the id, icon, title, text, subtext, boldText, color
 *    id - Unique id of activity
 *    icon - Activity icon name
 *    title - Activity name specified in title.
 *    text - Activity description specify in text.
 *    subtext - Activity performed on which time, that specified in subtext.
 *    boldText - From activity description the highlight words of text specified using boldText
 *    color - Activity icon color specify using the color
 */
export default {
  components: {
    simplebar,
  },
  props: {
    title: {
      type: String,
      default: 'Recent Activity',
    },
    activityWindowHeight: {
      type: String,
      default: '424',
    },
    activityData: {
      type: Array,
      default: function() {
        return []
      },
    },
  },
}
</script>

<template>
  <div class="card">
    <div class="card-body">
      <div class="dropdown float-right">
        <b-dropdown toggle-class="arrow-none card-drop p-0" variant="white" right>
          <template v-slot:button-content>
            <i class="mdi mdi-dots-vertical"></i>
          </template>
          <a href="javascript:void(0);" class="dropdown-item">Sales Report</a>
          <!-- item-->
          <a href="javascript:void(0);" class="dropdown-item">Export Report</a>
          <!-- item-->
          <a href="javascript:void(0);" class="dropdown-item">Profit</a>
          <!-- item-->
          <a href="javascript:void(0);" class="dropdown-item">Action</a>
        </b-dropdown>
      </div>
      <h4 class="header-title mb-2">{{ title }}</h4>

      <simplebar :style="`max-height:${activityWindowHeight}`">
        <div class="timeline-alt pb-0">
          <div v-for="activity of activityData" :key="activity.id" class="timeline-item">
            <i
              :class="`mdi ${activity.icon} bg-${activity.color}-lighten text-${activity.color} timeline-icon`"
            ></i>
            <div class="timeline-item-info">
              <a
                href="#"
                :class="`text-${activity.color} font-weight-bold mb-1 d-block`"
              >{{ activity.title }}</a>
              <small>
                {{ activity.text }}
                <span class="font-weight-bold">{{ activity.boldText }}</span>
              </small>
              <p class="mb-0 pb-2">
                <small class="text-muted">{{ activity.subtext }}</small>
              </p>
            </div>
          </div>
        </div>
      </simplebar>
    </div>
    <!-- end card-body -->
  </div>
  <!-- end card -->
</template>