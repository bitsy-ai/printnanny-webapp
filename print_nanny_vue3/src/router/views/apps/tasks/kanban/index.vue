<script>
import Vue from 'vue'
import moment from 'moment'
import draggable from 'vuedraggable'
import DatePicker from 'vue2-datepicker'
import { required } from 'vuelidate/lib/validators'

import appConfig from '@src/app.config'
import Layout from '@layouts/main'

import { todoData, progressData, reviewData, doneData } from './data'

Vue.prototype.moment = moment

export default {
  page: {
    title: 'Kanban board',
    meta: [{ name: 'description', content: appConfig.description }],
  },
  components: { DatePicker, draggable, Layout },
  data() {
    return {
      todoData: todoData,
      progressData: progressData,
      reviewData: reviewData,
      doneData: doneData,
      showModal: false,
      defaultdate: '',
      form: {
        project: '',
        title: '',
        priority: '',
        assign: '',
        date: '',
      },
      submitted: false,
    }
  },
  validations: {
    form: {
      project: { required },
      title: { required },
      priority: { required },
      assign: { required },
      date: { required },
    },
  },
  methods: {
    /**
     * Task modal form submit
     */
    taskformsubmit(e) {
      this.submitted = true
      this.$v.$touch()
      if (this.$v.$invalid) {
        return
      } else {
        const project = this.form.project
        const title = this.form.title
        const priority = this.form.priority
        const assign = this.form.assign
        const date = this.form.date
        this.todoData.push({
          image: require('@assets/images/users/avatar-1.jpg'),
          project,
          title,
          priority,
          assign,
          date,
        })
        this.showModal = false
      }
      this.submitted = false
      this.form = {}
    },

    /**
     * Hide modal on close
     */
    hideModal(e) {
      this.submitted = false
      this.showModal = false
      this.form = {}
    },
  },
}
</script>

<template>
  <Layout>
    <!-- start page title -->
    <div class="row">
      <div class="col-12">
        <div class="page-title-box">
          <div class="page-title-right">
            <ol class="breadcrumb m-0">
              <li class="breadcrumb-item">
                <a href="javascript: void(0);">Hyper</a>
              </li>
              <li class="breadcrumb-item">
                <a href="javascript: void(0);">Tasks</a>
              </li>
              <li class="breadcrumb-item active">Kanban Board</li>
            </ol>
          </div>
          <h4 class="page-title">
            Kanban Board
            <a
              class="btn btn-success btn-sm ml-3"
              href="javascript: void(0);"
              @click="showModal = true"
            >Add New</a>
          </h4>
        </div>
      </div>
    </div>
    <!-- end page title -->

    <div class="row">
      <div class="col-12">
        <div class="board">
          <!-- Toda task -->
          <div class="tasks">
            <h5 class="mt-0 task-header">TODO (3)</h5>

            <div id="task-list-one" class="task-list-items">
              <draggable class="list-group" group="tasks" :list="todoData">
                <!-- Task Item -->
                <div v-for="todo of todoData" :key="todo.id" class="card mb-0">
                  <div class="card-body p-3">
                    <small
                      class="float-right text-muted"
                    >{{moment(new Date(todo.date)).format('DD-MMM-YYYY')}}</small>
                    <span
                      class="badge"
                      :class="{ 'badge-success': todo.priority === 'Low',
                    'badge-secondary': todo.priority === 'Medium', 
                    'badge-danger': todo.priority === 'High' }"
                    >{{todo.priority}}</span>

                    <h5 class="mt-2 mb-2">
                      <a href="#" class="text-secondary">{{todo.title}}</a>
                    </h5>

                    <p class="mb-0">
                      <span class="pr-2 text-nowrap mb-2 d-inline-block">
                        <i class="mdi mdi-briefcase-outline text-muted"></i>
                        {{todo.project}}
                      </span>
                      <span class="text-nowrap mb-2 d-inline-block">
                        <i class="mdi mdi-comment-multiple-outline text-muted"></i>
                        <b> {{todo.comments}}</b> Comments
                      </span>
                    </p>

                    <b-dropdown
                      right
                      variant="white"
                      class="float-right"
                      toggle-class="text-muted arrow-none p-0"
                    >
                      <template slot="button-content">
                        <i class="mdi mdi-dots-vertical font-18"></i>
                      </template>
                      <b-dropdown-item href="javascript: void(0);">
                        <i class="mdi mdi-pencil mr-1"></i>Edit
                      </b-dropdown-item>
                      <b-dropdown-item href="javascript: void(0);">
                        <i class="mdi mdi-delete mr-1"></i>Delete
                      </b-dropdown-item>
                      <b-dropdown-item href="javascript: void(0);">
                        <i class="mdi mdi-plus-circle-outline mr-1"></i>Add People
                      </b-dropdown-item>
                      <b-dropdown-item href="javascript: void(0);">
                        <i class="mdi mdi-exit-to-app mr-1"></i>Leave
                      </b-dropdown-item>
                    </b-dropdown>

                    <p class="mb-0">
                      <img
                        :src="`${todo.image}`"
                        alt="user-img"
                        class="avatar-xs rounded-circle mr-1"
                      />
                      <span class="align-middle">{{todo.assign}}</span>
                    </p>
                  </div>
                  <!-- end card-body -->
                </div>
                <!-- Task Item End -->
              </draggable>
            </div>
          </div>

          <!-- progress task -->
          <div class="tasks">
            <h5 class="mt-0 task-header">In Progress (2)</h5>

            <div id="task-list-one" class="task-list-items">
              <draggable class="list-group" group="tasks" :list="progressData">
                <!-- Task Item -->
                <div v-for="progress of progressData" :key="progress.id" class="card mb-0">
                  <div class="card-body p-3">
                    <small class="float-right text-muted">{{progress.date}}</small>
                    <span
                      class="badge"
                      :class="{ 'badge-success': progress.priority === 'Low',
                    'badge-secondary': progress.priority === 'Medium',
                    'badge-danger': progress.priority === 'High' }"
                    >{{progress.priority}}</span>

                    <h5 class="mt-2 mb-2">
                      <a href="#" class="text-secondary">{{progress.title}}</a>
                    </h5>

                    <p class="mb-0">
                      <span class="pr-2 text-nowrap mb-2 d-inline-block">
                        <i class="mdi mdi-briefcase-outline text-muted"></i>
                        {{progress.project}}
                      </span>
                      <span class="text-nowrap mb-2 d-inline-block">
                        <i class="mdi mdi-comment-multiple-outline text-muted"></i>
                        <b> {{progress.comments}}</b> Comments
                      </span>
                    </p>

                    <b-dropdown
                      right
                      variant="white"
                      class="float-right"
                      toggle-class="text-muted arrow-none p-0"
                    >
                      <template slot="button-content">
                        <i class="mdi mdi-dots-vertical font-18"></i>
                      </template>
                      <b-dropdown-item href="javascript: void(0);">
                        <i class="mdi mdi-pencil mr-1"></i>Edit
                      </b-dropdown-item>
                      <b-dropdown-item href="javascript: void(0);">
                        <i class="mdi mdi-delete mr-1"></i>Delete
                      </b-dropdown-item>
                      <b-dropdown-item href="javascript: void(0);">
                        <i class="mdi mdi-plus-circle-outline mr-1"></i>Add People
                      </b-dropdown-item>
                      <b-dropdown-item href="javascript: void(0);">
                        <i class="mdi mdi-exit-to-app mr-1"></i>Leave
                      </b-dropdown-item>
                    </b-dropdown>

                    <p class="mb-0">
                      <img
                        :src="`${progress.image}`"
                        alt="user-img"
                        class="avatar-xs rounded-circle mr-1"
                      />
                      <span class="align-middle">{{progress.assign}}</span>
                    </p>
                  </div>
                  <!-- end card-body -->
                </div>
                <!-- Task Item End -->
              </draggable>
            </div>
          </div>

          <!-- Review task -->
          <div class="tasks">
            <h5 class="mt-0 task-header">Review (4)</h5>

            <div id="task-list-one" class="task-list-items">
              <draggable class="list-group" group="tasks" :list="reviewData">
                <!-- Task Item -->
                <div v-for="review of reviewData" :key="review.id" class="card mb-0">
                  <div class="card-body p-3">
                    <small class="float-right text-muted">{{review.date}}</small>
                    <span
                      class="badge"
                      :class="{ 'badge-danger': review.priority === 'High',
                    'badge-secondary': review.priority === 'Medium',
                    'badge-success': review.priority === 'Low' }"
                    >{{review.priority}}</span>

                    <h5 class="mt-2 mb-2">
                      <a href="#" class="text-secondary">{{review.title}}</a>
                    </h5>

                    <p class="mb-0">
                      <span class="pr-2 text-nowrap mb-2 d-inline-block">
                        <i class="mdi mdi-briefcase-outline text-muted"></i>
                        {{review.project}}
                      </span>
                      <span class="text-nowrap mb-2 d-inline-block">
                        <i class="mdi mdi-comment-multiple-outline text-muted"></i>
                        <b> {{review.comments}}</b> Comments
                      </span>
                    </p>

                    <b-dropdown
                      right
                      variant="white"
                      class="float-right"
                      toggle-class="text-muted arrow-none p-0"
                    >
                      <template slot="button-content">
                        <i class="mdi mdi-dots-vertical font-18"></i>
                      </template>
                      <b-dropdown-item href="javascript: void(0);">
                        <i class="mdi mdi-pencil mr-1"></i>Edit
                      </b-dropdown-item>
                      <b-dropdown-item href="javascript: void(0);">
                        <i class="mdi mdi-delete mr-1"></i>Delete
                      </b-dropdown-item>
                      <b-dropdown-item href="javascript: void(0);">
                        <i class="mdi mdi-plus-circle-outline mr-1"></i>Add People
                      </b-dropdown-item>
                      <b-dropdown-item href="javascript: void(0);">
                        <i class="mdi mdi-exit-to-app mr-1"></i>Leave
                      </b-dropdown-item>
                    </b-dropdown>

                    <p class="mb-0">
                      <img
                        :src="`${review.image}`"
                        alt="user-img"
                        class="avatar-xs rounded-circle mr-1"
                      />
                      <span class="align-middle">{{review.assign}}</span>
                    </p>
                  </div>
                  <!-- end card-body -->
                </div>
                <!-- Task Item End -->
              </draggable>
            </div>
          </div>

          <!-- Done task -->
          <div class="tasks">
            <h5 class="mt-0 task-header">Done (1)</h5>

            <div id="task-list-one" class="task-list-items">
              <draggable class="list-group" group="tasks" :list="doneData">
                <!-- Task Item -->
                <div v-for="donetask of doneData" :key="donetask.id" class="card mb-0">
                  <div class="card-body p-3">
                    <small class="float-right text-muted">{{donetask.date}}</small>
                    <span
                      class="badge"
                      :class="{ 'badge-danger': donetask.priority === 'High',
                    'badge-secondary': donetask.priority === 'Medium',
                    'badge-success': donetask.priority === 'Low' }"
                    >{{donetask.priority}}</span>

                    <h5 class="mt-2 mb-2">
                      <a href="#" class="text-secondary">{{donetask.title}}</a>
                    </h5>

                    <p class="mb-0">
                      <span class="pr-2 text-nowrap mb-2 d-inline-block">
                        <i class="mdi mdi-briefcase-outline text-muted"></i>
                        {{donetask.project}}
                      </span>
                      <span class="text-nowrap mb-2 d-inline-block">
                        <i class="mdi mdi-comment-multiple-outline text-muted"></i>
                        <b> {{donetask.comments}}</b> Comments
                      </span>
                    </p>

                    <b-dropdown
                      right
                      variant="white"
                      class="float-right"
                      toggle-class="text-muted arrow-none p-0"
                    >
                      <template slot="button-content">
                        <i class="mdi mdi-dots-vertical font-18"></i>
                      </template>
                      <b-dropdown-item href="javascript: void(0);">
                        <i class="mdi mdi-pencil mr-1"></i>Edit
                      </b-dropdown-item>
                      <b-dropdown-item href="javascript: void(0);">
                        <i class="mdi mdi-delete mr-1"></i>Delete
                      </b-dropdown-item>
                      <b-dropdown-item href="javascript: void(0);">
                        <i class="mdi mdi-plus-circle-outline mr-1"></i>Add People
                      </b-dropdown-item>
                      <b-dropdown-item href="javascript: void(0);">
                        <i class="mdi mdi-exit-to-app mr-1"></i>Leave
                      </b-dropdown-item>
                    </b-dropdown>

                    <p class="mb-0">
                      <img
                        :src="`${donetask.image}`"
                        alt="user-img"
                        class="avatar-xs rounded-circle mr-1"
                      />
                      <span class="align-middle">{{donetask.assign}}</span>
                    </p>
                  </div>
                  <!-- end card-body -->
                </div>
                <!-- Task Item End -->
              </draggable>
            </div>
          </div>
        </div>
      </div>
      <!-- end col -->
    </div>
    <!-- end row -->

    <!-- New task add modal -->
    <b-modal
      id="modal-1"
      v-model="showModal"
      centered
      size="lg"
      title="Create New Task"
      title-tag="h4"
      title-class="modal-title"
      hide-footer
    >
      <form class="p-2" @submit.prevent="taskformsubmit">
        <div class="form-group">
          <label>Project</label>
          <select
            v-model="form.project"
            class="form-control"
            :class="{ 'is-invalid': submitted && $v.form.project.$error }"
          >
            <option>Select</option>
            <option>Hyper</option>
            <option>CRM</option>
            <option>iOS</option>
          </select>
          <div
            v-if="submitted && !$v.form.project.required"
            class="invalid-feedback"
          >project is required</div>
        </div>

        <div class="row">
          <div class="col-md-8">
            <div class="form-group">
              <label for="task-title">Title</label>
              <input
                id="task-title"
                v-model="form.title"
                type="text"
                class="form-control"
                placeholder="Enter title"
                :class="{ 'is-invalid': submitted && $v.form.title.$error }"
              />
              <div
                v-if="submitted && !$v.form.title.required"
                class="invalid-feedback"
              >Title is required</div>
            </div>
          </div>

          <div class="col-md-4">
            <div class="form-group">
              <label for="task-priority2">Priority</label>
              <select
                id="task-priority2"
                v-model="form.priority"
                class="form-control"
                :class="{ 'is-invalid': submitted && $v.form.priority.$error }"
              >
                <option>Low</option>
                <option>Medium</option>
                <option>High</option>
              </select>
              <div
                v-if="submitted && !$v.form.priority.required"
                class="invalid-feedback"
              >Title is required</div>
            </div>
          </div>
        </div>

        <div class="form-group">
          <label for="task-description">Description</label>
          <textarea id="task-description" class="form-control" rows="3"></textarea>
        </div>

        <div class="row">
          <div class="col-md-6">
            <div class="form-group">
              <label for="task-title">Assign To</label>
              <select
                id="task-priority"
                v-model="form.assign"
                class="form-control"
                :class="{ 'is-invalid': submitted && $v.form.assign.$error }"
              >
                <option>Coderthemes</option>
                <option>Robert Carlile</option>
                <option>Louis Allen</option>
                <option>Sean White</option>
                <option>Riley Steele</option>
                <option>Zak Turnbull</option>
              </select>
              <div
                v-if="submitted && !$v.form.assign.required"
                class="invalid-feedback"
              >Assign is required</div>
            </div>
          </div>

          <div class="col-md-6">
            <div class="form-group">
              <label for="task-priority">Due Date</label>
              <date-picker
                v-model="form.date"
                :first-day-of-week="1"
                lang="en"
                confirm
                :class="{ 'is-invalid': submitted && $v.form.date.$error }"
              ></date-picker>
              <div
                v-if="submitted && !$v.form.date.required"
                class="invalid-feedback"
              >Date is required</div>
            </div>
          </div>
        </div>

        <div class="text-right">
          <b-button variant="light" @click="hideModal">Cancel</b-button>
          <b-button type="submit" variant="primary" class="ml-1">Create</b-button>
        </div>
      </form>
    </b-modal>
    <!-- end Modal  -->
  </Layout>
</template>
