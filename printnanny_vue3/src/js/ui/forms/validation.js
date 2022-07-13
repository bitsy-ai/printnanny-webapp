/**
 * Theme: Hyper - Responsive Bootstrap 5 Admin Dashboard
 * Author: Coderthemes
 * Module/App: Chat
 */

class Validation {
  constructor() {

  }

  init() {

    document.querySelectorAll(".needs-validation").forEach(function (element){
      element.addEventListener('submit',function (event){
        element.classList.add('was-validated');
        if(element.checkValidity()===false){
          event.preventDefault();
          event.stopPropagation();
          return false;
        }
        return true;
      });

    });




  }
}

// init the dashboard
new Validation().init();
