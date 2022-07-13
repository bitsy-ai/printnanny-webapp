/**
 * Theme: Hyper - Responsive Bootstrap 5 Admin Dashboard
 * Author: Coderthemes
 * Module/App: Chat
 */
import Quill from 'quill/dist/quill';
import 'quill/dist/quill.bubble.css';
import 'quill/dist/quill.snow.css';
import 'quill/dist/quill.core.css';


import 'simplemde/dist/simplemde.min.css';
import SimpleMDE from 'simplemde';

class EditorsForm {
  constructor() {

  }

  init() {

    if(document.getElementById('bubble-editor')) {
      new Quill('#bubble-editor', {
        theme: 'bubble'
      });
    }
    if(document.getElementById('snow-editor')) {
      new Quill('#snow-editor', {
        theme: 'snow',
        modules: {
          'toolbar': [[{ 'font': [] }, { 'size': [] }], ['bold', 'italic', 'underline', 'strike'], [{ 'color': [] }, { 'background': [] }], [{ 'script': 'super' }, { 'script': 'sub' }], [{ 'header': [false, 1, 2, 3, 4, 5, 6] }, 'blockquote', 'code-block'], [{ 'list': 'ordered' }, { 'list': 'bullet' }, { 'indent': '-1' }, { 'indent': '+1' }], ['direction', { 'align': [] }], ['link', 'image', 'video'], ['clean']]
        },
      });
    }
    if(document.getElementById('simplemde1')) {
      new SimpleMDE({
        element: document.getElementById('simplemde1'),
        spellChecker: false,
        placeholder: 'Write something..',
        tabSize: 2,
        status: ["autosave", "lines", "words", "cursor"],
        autosave: {
          enabled: true,
          uniqueId: "MyUniqueID",
        }
      });
    }



  }
}

// init the dashboard
new EditorsForm().init();
