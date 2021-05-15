<script>
import { required } from 'vuelidate/lib/validators'
import simplebar from 'simplebar-vue'

/**
 * Todo component
 * 1. User specifies the title of window using the 'title' input property.
 * 2. Window height set using the 'todoWindowHeight' input property. Height would count in pixel.
 * 3. Todolist array specify the id, todo, done task.
 *    id - specify the unique id of todo
 *    todo - specify the name
 *    done - Specify the todo done or not using checkbox checked value. Checkbox checked specify the done todo.
 */
export default {
  components: { simplebar },
  props: {
    title: {
      type: String,
      default: 'Todo',
    },
    todoWindowHeight: {
      type: String,
      default: '404',
    },
    items: {
      type: Array,
      default: function() {
        return []
      },
    },
  },
  data() {
    return {
      todoItems: [...this.items],
      newTodoItem: {
        task: '',
      },
      isSubmitted: false,
    }
  },
  validations: {
    newTodoItem: {
      task: { required },
    },
  },
  computed: {
    /**
     * return completed todo
     */
    completedTodo() {
      return this.todoItems.filter((t) => t.isCompleted === false)
    },
  },
  methods: {
    /**
     * Todo form submit
     */
    saveTodo() {
      this.isSubmitted = true
      this.$v.$touch()
      if (this.$v.$invalid) {
        return
      } else {
        var id = this.todoItems.length
        const task = this.newTodoItem.task
        // Value Push in Todo
        this.todoItems.push({
          id: id + 1,
          task,
          isCompleted: false,
        })
      }
      this.isSubmitted = false
      this.newTodoItem = {}
    },

    /**
     * Check box value change
     */
    togleStatus(index) {
      this.todoItems[index].isCompleted = !this.todoItems[index].isCompleted
    },

    /**
     * Hide Selected todo
     */
    archiveTodo() {
      // eslint-disable-next-line no-return-assign
      return (this.todoItems = this.todoItems.filter(
        (x) => x.isCompleted === false
      ))
    },
  },
}
</script>

<template>
  <div class="card">
    <div class="card-body">
      <b-dropdown
        variant="white"
        class="float-right"
        toggle-class="arrow-none card-drop p-0"
        right
      >
        <template v-slot:button-content>
          <i class="mdi mdi-dots-vertical"></i>
        </template>
        <!-- item-->
        <a
          href="javascript:void(0);"
          class="dropdown-item"
        >Settings</a>
        <!-- item-->
        <a
          href="javascript:void(0);"
          class="dropdown-item"
        >Action</a>
      </b-dropdown>
      <h4 class="mb-3 header-title">{{ title }}</h4>
      <div class="todoapp">
        <div class="row align-items-center">
          <div class="col-sm-6">
            <h5 id="todo-message">
              <span id="todo-remaining">{{completedTodo.length}}</span> of
              <span id="todo-total">{{todoItems.length}}</span> remaining
            </h5>
          </div>
          <div class="col-sm-6">
            <a
              href="javascript: void(0);"
              class="float-right btn btn-light btn-sm"
              @click="archiveTodo"
            >Archive</a>
          </div>
        </div>
        <simplebar :style="`max-height:${todoWindowHeight}`">
          <div>
            <ul
              id="todo-list"
              class="list-group list-group-flush todo-list"
            >
              <li
                v-for="(todo, index) in todoItems"
                :key="index"
                class="list-group-item border-0 pl-0"
              >
                <div class="custom-control custom-checkbox">
                  <input
                    :id="`${todo.id}`"
                    :checked="`${todo.isCompleted ? true : ''}`"
                    type="checkbox"
                    class="custom-control-input"
                    @change="togleStatus(index)"
                  />
                  <label
                    :for="`${todo.id}`"
                    class="custom-control-label"
                  >{{todo.task}}</label>
                </div>
              </li>
            </ul>
          </div>
        </simplebar>
        <form @submit.prevent="saveTodo">
          <div class="row mt-1">
            <div class="col-lg-10">
              <input
                v-model="newTodoItem.task"
                type="text"
                class="form-control"
                placeholder="Add new todo"
                name="todo"
                :class="{ 'is-invalid': isSubmitted && $v.newTodoItem.task.$error }"
              />
              <div
                v-if="isSubmitted && !$v.newTodoItem.task.required"
                class="invalid-feedback"
              >This value is required.</div>
            </div>
            <div class="col-lg-2">
              <button
                type="submit"
                class="btn btn-primary width-sm"
              >Add</button>
            </div>
          </div>
          <!-- end row -->
        </form>
        <!-- end form -->
      </div>
    </div>
    <!-- end card-body -->
  </div>
  <!-- end card -->
</template>