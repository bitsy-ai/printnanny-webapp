<script>
import ToDoList from '@components/widgets/todo-list'

export default {
  components: {
    ToDoList,
  },
  data() {
    return {
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
    }
  },
}
</script>

<template>
  <!-- Todo -->
  <ToDoList
    :items="todoItems"
    todo-window-height="133px"
  />
</template>