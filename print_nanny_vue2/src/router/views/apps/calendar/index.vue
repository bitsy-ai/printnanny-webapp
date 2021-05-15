<script>
import FullCalendar from '@fullcalendar/vue'
import dayGridPlugin from '@fullcalendar/daygrid'
import timeGridPlugin from '@fullcalendar/timegrid'
import interactionPlugin from '@fullcalendar/interaction'
import bootstrapPlugin from '@fullcalendar/bootstrap'
import listPlugin from '@fullcalendar/list'
import { required } from 'vuelidate/lib/validators'

import appConfig from '@src/app.config'
import Layout from '@layouts/main'
import PageHeader from '@components/page-header'

import { calendarEvents, categories } from './data-calendar'

/**
 * Calendar component
 */
export default {
  page: {
    title: 'Calendar',
    meta: [{ name: 'description', content: appConfig.description }],
  },
  components: { FullCalendar, Layout, PageHeader },
  data() {
    return {
      title: 'Calendar',
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
          text: 'Calendar',
          active: true,
        },
      ],
      calendarWeekends: true,
      calendarPlugins: [
        dayGridPlugin,
        timeGridPlugin,
        interactionPlugin,
        bootstrapPlugin,
        listPlugin,
      ],
      themeSystem: 'bootstrap',
      calendarEvents: calendarEvents,
      showModal: false,
      eventModal: false,
      categories: categories,
      submitted: false,
      submit: false,
      newEventData: {},
      edit: {},
      deleteId: {},
      event: {
        title: '',
        category: '',
      },
      editevent: {
        editTitle: '',
      },
    }
  },
  validations: {
    event: {
      title: { required },
      category: { required },
    },
  },
  methods: {
    /**
     * Modal form submit
     */
    handleSubmit(e) {
      this.submitted = true

      // stop here if form is invalid
      this.$v.$touch()
      if (this.$v.$invalid) {
        return
      } else {
        const title = this.event.title
        const category = this.event.category

        this.calendarEvents = this.calendarEvents.concat({
          id: this.calendarEvents.length + 1,
          title,
          start: this.newEventData.date,
          end: this.newEventData.date,
          classNames: [category],
        })

        this.showModal = false
        this.newEventData = {}
      }
      this.submitted = false
      this.event = {}
    },

    /**
     * Hide the modal
     */
    hideModal(e) {
      this.submitted = false
      this.showModal = false
      this.event = {}
    },
    /**
     * Edit event modal submit
     */
    editSubmit(e) {
      this.submit = true
      const editTitle = this.editevent.editTitle
      this.edit.setProp('title', editTitle)
      this.eventModal = false
    },

    /**
     * Delete event
     */
    deleteEvent() {
      var deleteId = this.edit.id
      this.calendarEvents = this.calendarEvents.filter(
        (x) => '' + x.id !== '' + deleteId
      )

      this.eventModal = false
    },
    /**
     * Modal open for add event
     */
    dateClicked(info) {
      this.newEventData = info
      this.showModal = true
    },
    /**
     * Modal open for edit event
     */
    editEvent(info) {
      this.edit = info.event
      this.editevent.editTitle = this.edit.title
      this.eventModal = true
    },

    closeModal() {
      this.eventModal = false
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
    <div class="row">
      <div class="col-12">
        <div class="card">
          <div class="card-body">
            <div class="app-calendar">
              <!-- calendar -->
              <FullCalendar
                ref="fullCalendar"
                default-view="dayGridMonth"
                :header="{
									left: 'prev,next today',
									center: 'title',
									right: 'dayGridMonth,timeGridWeek,timeGridDay,listWeek',
								}"
                :button-text="{
									today: 'Today',
									month: 'Month',
									week: 'Week',
									day: 'Day',
									list: 'List',
									prev: 'Prev',
									next: 'Next',
								}"
                :bootstrap-font-awesome="false"
                :editable="true"
                :droppable="true"
                :plugins="calendarPlugins"
                :events="calendarEvents"
                :weekends="calendarWeekends"
                :theme-system="themeSystem"
                @dateClick="dateClicked"
                @eventClick="editEvent"
              />
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Add new event modal -->
    <b-modal
      v-model="showModal"
      title="Add New Event"
      header-class="pr-4 pl-4 border-bottom-0"
      title-class="text-black font-18"
      body-class="pt-3 pr-4 pl-4"
      hide-footer
    >
      <form @submit.prevent="handleSubmit">
        <div class="row">
          <div class="col-12">
            <div class="form-group">
              <label for="name">Event Name</label>
              <input
                id="name"
                v-model="event.title"
                type="text"
                class="form-control"
                placeholder="Insert Event name"
                :class="{ 'is-invalid': submitted && $v.event.title.$error }"
              />
              <div
                v-if="submitted && !$v.event.title.required"
                class="invalid-feedback"
              >This value is required.</div>
            </div>
          </div>
          <div class="col-12">
            <div class="form-group">
              <label class="control-label">Category</label>
              <select
                v-model="event.category"
                class="form-control"
                name="category"
                :class="{ 'is-invalid': submitted && $v.event.category.errors }"
              >
                <option
                  v-for="option in categories"
                  :key="option.backgroundColor"
                  :value="`${option.value }`"
                >{{ option.name }}</option>
              </select>
              <div
                v-if="submitted && 
                !$v.event.category.required"
                class="invalid-feedback"
              >This value is required.</div>
            </div>
          </div>
        </div>

        <div class="text-right pt-2 pb-2">
          <b-button
            variant="light"
            @click="hideModal"
          >Close</b-button>
          <b-button
            type="submit"
            variant="success"
            class="ml-1"
          >Create event</b-button>
        </div>
      </form>
    </b-modal>

    <!-- Edit Modal -->
    <b-modal
      v-model="eventModal"
      title="Edit Event"
      header-class="pr-4 pl-4 border-bottom-0"
      title-class="text-black font-18"
      hide-footer
      body-class="pt-3 pr-4 pl-4"
    >
      <form @submit.prevent="editSubmit">
        <label>Change event name</label>
        <div class="input-group m-b-15">
          <input
            v-model="editevent.editTitle"
            class="form-control"
            type="text"
          />
          <span class="input-group-append">
            <button
              type="submit"
              class="btn btn-success btn-md"
            >
              <i class="fa fa-check"></i> Save
            </button>
          </span>
        </div>
        <div class="text-right py-3">
          <b-button
            variant="light"
            @click="closeModal"
          >Close</b-button>
          <b-button
            class="ml-1"
            variant="danger"
            @click="deleteEvent"
          >Delete</b-button>
        </div>
      </form>
    </b-modal>
  </Layout>
</template>
