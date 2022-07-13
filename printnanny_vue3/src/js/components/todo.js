/**
 * Theme: Hyper - Responsive Bootstrap 5 Admin Dashboard
 * Author: Coderthemes
 * Module/App: CRMDashboard
 */

import 'simplebar/dist/simplebar';

class Todo {

  constructor() {

    this.body = document.body;
    this.todoContainer = document.getElementById('todo-container');
    this.todoMessage = document.getElementById('todo-message');
    this.todoRemaining = document.getElementById("todo-remaining");
    this.todoTotal = document.getElementById("todo-total");
    this.archiveBtn = document.getElementById('btn-archive');
    this.todoList = document.getElementById('todo-list');
    this.todoDonechk = '.todo-done';
    this.todoForm = document.getElementById('todo-form');
    this.todoInput = document.getElementById('todo-input-text');
    this.todoBtn = document.getElementById('todo-btn-submit');

    this.todoData = [
      {
        'id': '1',
        'text': 'Design One page theme',
        'done': false
      },
      {
        'id': '2',
        'text': 'Build a js based app',
        'done': true
      },
      {
        'id': '3',
        'text': 'Creating component page',
        'done': true
      },
      {
        'id': '4',
        'text': 'Testing??',
        'done': true
      },
      {
        'id': '5',
        'text': 'Hehe!! This looks cool!',
        'done': false
      },
      {
        'id': '6',
        'text': 'Create new version 3.0',
        'done': false
      },
      {
        'id': '7',
        'text': 'Build an angular app',
        'done': true
      }];

    this.todoCompletedData = [];
    this.todoUnCompletedData = [];
  }

  archives() {
    this.todoUnCompletedData = [];
    for (let count = 0; count < this.todoData.length; count++) {
      const todoItem = this.todoData[count];
      if (todoItem.done === true) {
        this.todoCompletedData.push(todoItem);
      } else {
        this.todoUnCompletedData.push(todoItem);
      }
    }
    this.todoData = [];
    this.todoData = [].concat(this.todoUnCompletedData);
    this.generate();
  }

  addTodo(todoText) {
    this.todoData.push({ 'id': this.todoData.length, 'text': todoText, 'done': false });
    this.generate();
  }


  init() {

    const self = this;


    document.addEventListener('change', function (e) {

      if (e.target.checked) {
        self.markTodo(e.target.id, true);
      } else {
        self.markTodo(e.target.id, false);
      }
      //regenerate list
      self.generate();
    });

    if (this.archiveBtn) {
      this.archiveBtn.addEventListener('click', function (e) {
        e.preventDefault();
        self.archives();
      })
    }

    if (this.todoForm) {
      this.todoForm.addEventListener("submit", function (e) {
        e.preventDefault();
        if (self.todoInput.value === "" || typeof (self.todoInput.value) == 'undefined' || self.todoInput.value == null) {
          self.todoInput.focus();
          return false;
        } else {
          self.addTodo(self.todoInput.value);
          self.todoForm.classList.remove('was-validated');
          self.todoInput.value = "";
          return true;
        }
      });
    }

    window.addEventListener('load', function () {
      self.generate();

    });


  }

  //mark/unmark - you can use ajax to save data on server side
  markTodo = function (todoId, complete) {
    for (let count = 0; count < this.todoData.length; count++) {
      if (this.todoData[count].id == todoId) {
        this.todoData[count].done = complete;
      }
    }
  };

  generate() {
    //clear list
    this.todoList.innerHTML = "";

    let text = "";
    let remaining = 0;
    for (let count = 0; count < this.todoData.length; count++) {

      let todoItem = this.todoData[count];
      if (todoItem.done === true) {
        text += ('<li class="list-group-item border-0 ps-0"><div class="form-check mb-0"><input type="checkbox" class="form-check-input todo-done" id="' + todoItem.id + '" checked><label class="form-check-label" for="' + todoItem.id + '"><s>' + " " + todoItem.text + '</s></label></div></li>');
      } else {
        remaining += 1;
        text += ('<li class="list-group-item border-0 ps-0"><div class="form-check mb-0"><input type="checkbox" class="form-check-input todo-done" id="' + todoItem.id + '"><label class="form-check-label" for="' + todoItem.id + '">' + " " + todoItem.text + '</label></div></li>');
      }
    }

    if (this.todoRemaining)
      this.todoRemaining.innerHTML = remaining.toString();
    if (this.todoTotal)
      this.todoTotal.innerHTML = this.todoData.length.toString();
    this.todoList.innerHTML = (text);


  };
}


export default Todo;
