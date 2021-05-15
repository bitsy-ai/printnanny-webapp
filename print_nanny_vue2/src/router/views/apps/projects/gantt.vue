<script>
import Gantt from 'frappe-gantt'
import simplebar from 'simplebar-vue'

import appConfig from '@src/app.config'
import Layout from '@layouts/main'
import PageHeader from '@components/page-header'

const projects = [
  {
    id: 'proj101',
    name: 'Lunar',
    status: 'On-Track',
    icon: 'uil uil-moonset',
  },
  {
    id: 'proj102',
    name: 'Dark Moon',
    status: 'On-Track',
    icon: 'uil uil-moon-eclipse',
  },
  {
    id: 'proj103',
    name: 'Aurora',
    status: 'Locked',
    icon: 'uil uil-mountains',
  },
  {
    id: 'proj104',
    name: 'Blue Moon',
    status: 'Locked',
    icon: 'uil uil-moon',
  },
  {
    id: 'proj105',
    name: 'Casanova',
    status: 'Delayed',
    icon: 'uil uil-ship',
  },
  {
    id: 'proj106',
    name: 'Darwin',
    status: 'On-Track',
    icon: 'uil uil-subway-alt',
  },
  {
    id: 'proj107',
    name: 'Eagle',
    status: 'Delayed',
    icon: 'uil uil-gold',
  },
]

/**
 * Projects Calendar component
 */
export default {
  page: {
    title: 'Projects Calendar',
    meta: [{ name: 'description', content: appConfig.description }],
  },
  components: { simplebar, Layout, PageHeader },
  data() {
    return {
      title: 'Projects Calendar',
      selectedMode: 'Week',
      modes: ['Quarter Day', 'Half Day', 'Day', 'Week', 'Month'],
      items: [
        {
          text: 'Hyper',
          href: '/',
        },
        {
          text: 'Apps',
          href: '/',
        },
        {
          text: 'Projects Calendar',
          active: true,
        },
      ],
      projects: [...projects],
      tasks: [
        {
          id: '1',
          name: 'Draft the new contract document for sales team',
          start: '2019-07-16',
          end: '2019-07-20',
          progress: 55,
        },
        {
          id: '2',
          name: 'Find out the old contract documents',
          start: '2019-07-19',
          end: '2019-07-21',
          progress: 85,
          dependencies: '1',
        },
        {
          id: '3',
          name:
            'Organize meeting with sales associates to understand need in detail',
          start: '2019-07-21',
          end: '2019-07-22',
          progress: 80,
          dependencies: '2',
        },
        {
          id: '4',
          name: 'iOS App home page',
          start: '2019-07-15',
          end: '2019-07-17',
          progress: 80,
        },
        {
          id: '5',
          name: 'Write a release note',
          start: '2019-07-18',
          end: '2019-07-22',
          progress: 65,
          dependencies: '4',
        },
        {
          id: '6',
          name: 'Setup new sales project',
          start: '2019-07-20',
          end: '2019-07-31',
          progress: 15,
        },
        {
          id: '7',
          name: 'Invite user to a project',
          start: '2019-07-25',
          end: '2019-07-26',
          progress: 99,
          dependencies: '6',
        },
        {
          id: '8',
          name: 'Coordinate with business development',
          start: '2019-07-28',
          end: '2019-07-30',
          progress: 35,
          dependencies: '7',
        },
        {
          id: '9',
          name: 'Kanban board design',
          start: '2019-08-01',
          end: '2019-08-03',
          progress: 25,
          dependencies: '8',
        },
        {
          id: '10',
          name: 'Enable analytics tracking',
          start: '2019-08-05',
          end: '2019-08-07',
          progress: 60,
          dependencies: '9',
        },
      ],
      ganttRef: null,
    }
  },
  mounted() {
    // eslint-disable-next-line camelcase
    this.ganttRef = new Gantt('.gantt-target', this.tasks, {
      custom_popup_html: (task) => {
        // the task object will contain the updated
        // dates and progress value
        // eslint-disable-next-line
        var endDate = task.end
        // eslint-disable-next-line
        var progressCls =
          task.progress >= 60
            ? 'bg-success'
            : task.progress >= 30 && task.progress < 60
            ? 'bg-primary'
            : 'bg-warning'
        return (
          '<div class="popover fade show bs-popover-right gantt-task-details" role="tooltip">' +
          '<div class="arrow"></div><div class="popover-body">' +
          // eslint-disable-next-line no-template-curly-in-string
          `<h5>${task.name}</h5><p class="mb-2">Expected to finish by ${endDate}</p>` +
          '<div class="progress mb-2" style="height: 10px;">' +
          // eslint-disable-next-line no-template-curly-in-string
          `<div class="progress-bar ${progressCls}" role="progressbar" style="width: ${task.progress}%;" aria-valuenow="${task.progress}"` +
          // eslint-disable-next-line no-template-curly-in-string
          ` aria-valuemin="0" aria-valuemax="100">${task.progress}%</div>` +
          '</div></div></div>'
        )
      },
      view_modes: this.modes,
      view_mode: 'Week',
      bar_height: 20,
      padding: 18,
    })
  },
  methods: {
    onModeChange(val) {
      if (this.ganttRef) this.ganttRef.change_view_mode(val)
    },
    onSearch(e) {
      const val = e.target.value
      if (val) {
        this.projects = projects.filter(
          (p) => p.name.toLowerCase().indexOf(val.toLowerCase()) !== -1
        )
      } else this.projects = [...projects]
    },
  },
}
</script>

<template>
  <Layout>
    <PageHeader
      :title="title"
      :items="items"
    />

    <div class="card">
      <div class="card-body">
        <div class="row">
          <!-- start projects-->

          <div class="col-xl-3">
            <div class="pr-xl-3">
              <h5 class="mt-0 mb-3">Projects</h5>

              <!-- start search box -->

              <div class="app-search">
                <form>
                  <div class="form-group position-relative">
                    <input
                      type="text"
                      class="form-control"
                      placeholder="search by name..."
                      @keyup="onSearch"
                    />

                    <span class="mdi mdi-magnify"></span>
                  </div>
                </form>
              </div>

              <!-- end search box -->

              <div class="row">
                <div class="col">
                  <simplebar style="max-height: 535px;">
                    <a
                      v-for="project in projects"
                      :key="project.id"
                      href="javascript:void(0);"
                      class="text-body"
                    >
                      <div class="media mt-2 p-2">
                        <div class="avatar-sm">
                          <span
                            :class="{ 'bg-success-lighten text-success': project.status === 'On-Track', 'bg-warning-lighten text-warning': project.status === 'Locked', 'bg-danger-lighten text-danger': project.status === 'Delayed' }"
                            class="avatar-title rounded-circle"
                          >
                            <i
                              :class="project.icon"
                              class="font-24"
                            ></i>
                          </span>
                        </div>

                        <div class="media-body ml-2">
                          <h5 class="mt-0 mb-0">
                            {{project.name}}
                            <span
                              :class="{ 'badge-success-lighten': project.status === 'On-Track', 'badge-warning-lighten': project.status === 'Locked', 'badge-danger-lighten': project.status === 'Delayed' }"
                              class="badge ml-1"
                            >{{project.status}}</span>
                          </h5>

                          <p class="mt-1 mb-0 text-muted">ID: {{project.id}}</p>
                        </div>
                      </div>
                    </a>

                  </simplebar>
                </div>
              </div>
            </div>
          </div>
          <!-- end projects -->

          <!-- gantt view -->
          <div class="col-xl-9 mt-4 mt-xl-0">
            <div class="pl-xl-3">
              <div class="row">
                <div class="col-auto">
                  <a
                    href="javascript: void(0);"
                    class="btn btn-success btn-sm mb-2"
                  >Add New Task</a>
                </div>
                <div class="col text-sm-right">
                  <div
                    id="modes-filter"
                    class="btn-group btn-group-sm btn-group-toggle mb-2"
                    data-toggle="buttons"
                  >
                    <b-form-group label="">
                      <b-form-radio-group
                        id="mode-selection"
                        v-model="selectedMode"
                        :options="modes"
                        buttons
                        name="radios-btn-default"
                        @change="onModeChange"
                      ></b-form-radio-group>
                    </b-form-group>
                  </div>
                </div>
              </div>
              <div class="row">
                <div class="col mt-3">
                  <div class="gantt-target"></div>
                </div>
              </div>
            </div>
          </div>
          <!-- end gantt view -->
        </div>
      </div>
    </div>
  </Layout>
</template>