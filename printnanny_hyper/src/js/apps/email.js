/**
 * Theme: Hyper - Responsive Bootstrap 5 Admin Dashboard
 * Author: Coderthemes
 * Module/App: E-Mail
 */

import 'simplemde/dist/simplemde.min.css';
import SimpleMDE from 'simplemde';

class Email {

  constructor() {

  }

  initSimpleMDE = function () {
    new SimpleMDE({
      element: document.getElementById('simplemde1'),
      spellChecker: false,
      placeholder: 'Write something..',
      tabSize: 2,
      status: false,
      autosave: {
        enabled: false
      }
    });
  }

  init() {
    // Email Checked

    document.querySelectorAll("input").forEach(function (element){
      element.addEventListener('change',function (event){
        if(element.checked){
          element.parentElement.parentElement.parentElement.parentElement.classList.add('mail-selected');
        }else{
          element.parentElement.parentElement.parentElement.parentElement.classList.remove('mail-selected');

        }
      })
    });

    // $('input:checkbox').change(function(){
    //   if($(this).is(":checked")) {
    //     $(this).parent().parent().parent().parent().addClass("mail-selected");
    //   } else {
    //     $(this).parent().parent().parent().parent().removeClass("mail-selected");
    //   }
    // });

    this.initSimpleMDE();


  }


}

// init the dashboard
new Email().init();
