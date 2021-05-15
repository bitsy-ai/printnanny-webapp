<script>
import { tasks } from './data'

export default {
  data() {
    return {
      tasks: tasks,
      todayTasks: tasks.filter((t) => t.id === 'today'),
      upcomingTask: tasks.filter((t) => t.id === 'upcoming'),
      otherTask: tasks.filter((t) => t.id === 'other'),
    }
  },
}
</script>

<template>
  <div class="row mt-2">
    <div class="col">
      <a
        v-b-toggle.todayTasks
        class="text-dark"
        href="javascript: void(0);"
        aria-controls="todayTasks"
      >
        <h5 class="m-0 pb-2">
          <i class="uil uil-angle-down font-18"></i>Today
          <span class="text-muted font-size-14">(10)</span>
        </h5>
      </a>
      <b-collapse id="todayTasks" visible>
        <div class="card mb-0">
          <div class="card-body pt-2 pb-2">
            <div
              v-for="(task, index) of todayTasks"
              :key="index"
              class="row justify-content-sm-between mt-2"
            >
              <div class="col-sm-6 mb-2 mb-sm-0">
                <div class="custom-control custom-checkbox">
                  <input :id="`task-${index}`" type="checkbox" class="custom-control-input" />
                  <label class="custom-control-label" :for="`task-${index}`">{{ task.name }}</label>
                </div>
                <!-- end checkbox -->
              </div>
              <!-- end col -->
              <div class="col-sm-6">
                <div class="d-flex justify-content-between">
                  <div>
                    <img :src="`${task.user}`" alt="image" class="avatar-xs rounded-circle" />
                  </div>
                  <div>
                    <ul class="list-inline font-13 text-right">
                      <li class="list-inline-item">
                        <i class="uil uil-schedule font-16 mr-1"></i>
                        {{task.time}}
                      </li>
                      <li class="list-inline-item ml-1">
                        <i class="uil uil-align-alt font-16 mr-1"></i>
                        {{task.task}}
                      </li>
                      <li class="list-inline-item ml-1">
                        <i class="uil uil-comment-message font-16 mr-1"></i>
                        {{ task.message }}
                      </li>
                      <li class="list-inline-item ml-1">
                        <span
                          class="badge p-1"
                          :class="{ 'badge-danger-lighten': `${task.status}` === 'High',
                                            'badge-info-lighten': `${task.status}` === 'Medium',
                                            'badge-success-lighten': `${task.status}` === 'Low' }"
                        >{{ task.status }}</span>
                      </li>
                    </ul>
                  </div>
                </div>
                <!-- end .d-flex-->
              </div>
              <!-- end col -->
            </div>
          </div>
          <!-- end card-body -->
        </div>
        <!-- end card -->
      </b-collapse>
      <!-- end collapse-->

      <div class="mt-4">
        <a
          v-b-toggle.upcomingTask
          class="text-dark"
          href="javascript: void(0);"
          aria-controls="upcomingTask"
        >
          <h5 class="mb-0 pb-2">
            <i class="uil uil-angle-down font-18"></i>Upcoming
            <span class="text-muted">(5)</span>
          </h5>
        </a>
        <b-collapse id="upcomingTask" visible>
          <div class="card mb-0">
            <div class="card-body pt-2 pb-2">
              <div
                v-for="(task, index) of upcomingTask"
                :key="index"
                class="row justify-content-sm-between mt-2"
              >
                <div class="col-sm-6 mb-2 mb-sm-0">
                  <div class="custom-control custom-checkbox">
                    <input
                      :id="`task-upcoming-${index}`"
                      type="checkbox"
                      class="custom-control-input"
                    />
                    <label
                      class="custom-control-label"
                      :for="`task-upcoming-${index}`"
                    >{{ task.name }}</label>
                  </div>
                  <!-- end checkbox -->
                </div>
                <!-- end col -->
                <div class="col-sm-6">
                  <div class="d-flex justify-content-between">
                    <div>
                      <img :src="`${task.user}`" alt="image" class="avatar-xs rounded-circle" />
                    </div>
                    <div>
                      <ul class="list-inline font-13 text-sm-right">
                        <li class="list-inline-item">
                          <i class="uil uil-schedule font-16 mr-1"></i>
                          {{task.time}}
                        </li>
                        <li class="list-inline-item ml-1">
                          <i class="uil uil-align-alt font-16 mr-1"></i>
                          {{task.task}}
                        </li>
                        <li class="list-inline-item ml-1">
                          <i class="uil uil-comment-message font-16 mr-1"></i>
                          {{ task.message }}
                        </li>
                        <li class="list-inline-item ml-2">
                          <span
                            class="badge p-1"
                            :class="{ 'badge-danger-lighten': `${task.status}` === 'High',
                                            'badge-info-lighten': `${task.status}` === 'Medium',
                                            'badge-success-lighten': `${task.status}` === 'Low' }"
                          >{{ task.status }}</span>
                        </li>
                      </ul>
                    </div>
                  </div>
                  <!-- end .d-flex-->
                </div>
                <!-- end col -->
              </div>
              <!-- end row -->
            </div>
            <!-- end card-body-->
          </div>
          <!-- end card -->
        </b-collapse>
        <!-- end collapse-->
      </div>

      <div class="mt-4">
        <a
          v-b-toggle.otherTask
          class="text-dark"
          href="javascript: void(0);"
          aria-controls="otherTask"
        >
          <h5 class="m-0 pb-2">
            <i class="uil uil-angle-down font-18"></i>Other
            <span class="text-muted">(3)</span>
          </h5>
        </a>
        <b-collapse id="otherTask" visible>
          <div class="card mb-0">
            <div class="card-body pt-2 pb-2">
              <div
                v-for="(task, index) of otherTask"
                :key="index"
                class="row justify-content-sm-between mt-2"
              >
                <div class="col-sm-6 mb-2 mb-sm-0">
                  <div class="custom-control custom-checkbox">
                    <input :id="`task-other-${index}`" type="checkbox" class="custom-control-input" />
                    <label class="custom-control-label" :for="`task-other-${index}`">{{ task.name }}</label>
                  </div>
                  <!-- end checkbox -->
                </div>
                <!-- end col -->
                <div class="col-sm-6">
                  <div class="d-flex justify-content-between">
                    <div>
                      <img :src="`${task.user}`" alt="image" class="avatar-xs rounded-circle" />
                    </div>
                    <div class="mt-3 mt-sm-0">
                      <ul class="list-inline font-13 text-sm-right">
                        <li class="list-inline-item">
                          <i class="uil uil-schedule font-16 mr-1"></i>
                          {{task.time}}
                        </li>
                        <li class="list-inline-item ml-1">
                          <i class="uil uil-align-alt font-16 mr-1"></i>
                          {{task.task}}
                        </li>
                        <li class="list-inline-item ml-1">
                          <i class="uil uil-comment-message font-16 mr-1"></i>
                          {{ task.message }}
                        </li>
                        <li class="list-inline-item ml-2">
                          <span
                            class="badge p-1"
                            :class="{ 'badge-danger-lighten': `${task.status}` === 'High',
                                            'badge-info-lighten': `${task.status}` === 'Medium',
                                            'badge-success-lighten': `${task.status}` === 'Low' }"
                          >{{ task.status }}</span>
                        </li>
                      </ul>
                    </div>
                  </div>
                  <!-- end .d-flex-->
                </div>
                <!-- end col -->
              </div>
              <!-- end row-->
            </div>
            <!-- end card-body -->
          </div>
          <!-- end card -->
        </b-collapse>
        <!-- end collapse-->
      </div>
    </div>
    <!-- end col -->
  </div>
</template>