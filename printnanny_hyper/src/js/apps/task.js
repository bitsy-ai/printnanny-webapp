/**
 * Theme: Hyper - Responsive Bootstrap 5 Admin Dashboard
 * Author: Coderthemes
 * Module/App: Task
 */

import Quill from 'quill/dist/quill';
import 'quill/dist/quill.bubble.css';
import Dragula from '../components/dragula';
import FileUpload from '../components/file-upload';

class Task {

  constructor() {

  }

  init(){

    if(document.getElementById('bubble-editor')) {
      new Quill('#bubble-editor', {
        theme: 'bubble'
      });
    }

    new Dragula().init();
    new FileUpload().init();

  }

}

// init the dashboard
new Task().init();
